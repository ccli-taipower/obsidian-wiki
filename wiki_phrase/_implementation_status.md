# _Implementation Status (non-knowledge meta page)

> **Non-knowledge page.** 此頁面是 project tracking，不是音樂理論知識。
> 與 [[../score-claude/memory/feedback_wiki_knowledge_vs_project_separation]] 一致 — wiki concept/composer/analysis pages 保留純知識；Phase 進度、A/B 結果、commits、TODO 集中在此頁與 score-claude memory.
> Canonical source: [[../score-claude/memory/project_phrase_detection_v1_phase1_phaseB]]（score-claude 端 memory）；本頁為 wiki-internal navigation convenience.

## 1. Current run.py state (as of 2026-05-26)

### 1.1 Implemented detection passes

`program/run.py::_detect_phrase_starts(groups)` has 6+1 passes:

| Pass | Function | Flag | Default |
|---|---|---|---|
| 1 | hard breaks (rest/jump/cadential) | (none, always on) | — |
| 1b | anacrusis (pickup detection) | (always on) | — |
| 2 | period inference from break gaps | (always on) | — |
| 3 | 4/8-bar periodic fallback | (always on) | — |
| **4** | figural boundary | `USE_FIGURAL_BOUNDARY_DETECTION` | False |
| **5** | subject imitation | `USE_SUBJECT_DETECTION` | False |
| **6** | cadence PAC+IAC (Phase 2 — music21 roman) | `USE_CADENCE_DETECTION` | False |
| **7** | texture change | `USE_TEXTURE_DETECTION` | False |

Plus phrase-start cost rule:
- `_running_passage_thumb_reservation_cost()` hooked in `_run_phrase_dp` first-chord init, gated by `USE_THUMB_RESERVATION` (default False).

### 1.2 Per-piece opt-in config

`BACH_INV_PHRASE_FLAGS: dict[int, dict]`:
```python
{
  1: {"figural": True, "thumb": True, "subject": False, "cadence": False},
  2: {"figural": True, "thumb": True, "subject": False, "cadence": False},
  4: {"figural": True, "thumb": True, "subject": False, "cadence": True},  # diagnostic
  5: {"figural": True, "thumb": True, "subject": False, "cadence": False},
}
```

Mvts 3/6/7/8 不啟用：Phase 2.2 A/B 顯示 mvt6 -3.4pp (red-line)、其他 neutral 或 slight negative.

`_process_mvt_book` hook 在 `assign_fingering_v6` 前 temporarily set flags, restore after. 只對 `_BACH_INV_STEM` 書冊生效 (SICILIANO 不受影響).

`SINGLE_PDF_PHRASE_FLAGS: dict[str, dict]` (新增，2026-05-27 Cadence Phase 2; long_scale added 2026-05-27):
```python
{
  "011_Mozart_PSon_K283_G_i_B0-22": {
      "figural": False, "thumb": False, "subject": False,
      "cadence": True, "texture": False, "long_scale": True,
  },  # PIG 011 — verified +1.01pp RH
  "017_Mozart_PSon_K545_C_i_B1-12": {
      "figural": False, "thumb": False, "subject": False,
      "cadence": True, "texture": False, "long_scale": True,
  },  # PIG 017 — long_scale +4.06pp RH (K545 m5 ascending scale fixed)
}
```

Key lookup: `for key, flags in SINGLE_PDF_PHRASE_FLAGS.items(): if key in stem: matched = flags; break` (first match wins, substring match on stem). Hook points: (a) single-PDF main loop in `run.py` (`_apply_phrase_flags(pdf_path.stem)` with try/finally `_restore_phrase_flags`); (b) `compare_pig._run_v6_dp` (takes `mxl_path` + `stem` kwargs, threads through from `compare_piece`).

### 1.3 Module-level context

`_PHRASE_CTX: dict = {"mxl_path": None, "_cache": None, "_cache_key": None}`
由 caller 設定（`_process_mvt_book` 寫 `mvt_path`），讓 cadence detection 可重新解析 music21 score 不用改 `_detect_phrase_starts` signature.

### 1.4 Key tunable constants

| 常數 | 預設 | 對應規則 |
|---|---|---|
| `FIGURAL_MIN_LEN` | 3 | min notes per figure run |
| `FIGURAL_MAX_OCTAVE` | 12 | figure 跨度上限 |
| `FIGURAL_CLOSURE_TOL` | 2 | closure 音歸前 figure |
| `FIGURAL_MAX_STEP_SEMITONES` | 4 | leap 終止 run |
| `RUNNING_PASSAGE_LOOK_AHEAD` | 4 | thumb reservation 看後 N 音 |
| `RUNNING_PASSAGE_MIN_SPAN_SEMITONES` | 5 | span > N → 觸發 |
| `RUNNING_PASSAGE_OUTER_START_PENALTY` | **5.0** | empirically critical |
| `SUBJECT_LEN_NOTES` | 8 | subject template 長度 |
| `SUBJECT_MATCH_TOLERANCE` | 0.8 | interval 一致比例 |
| `SUBJECT_MIN_GAP_GROUPS` | 4 | dedup 寬度 |
| `CADENCE_MIN_GAP_GROUPS` | 3 | dedup |
| `CADENCE_BEAT_TOL` | 0.5 | chord offset 對齊容差 (closest-match within window) |
| `CADENCE_DISABLES_FALLBACK` | **False** | window mode (`True` = drop all Pass 3 fallback when any cadence found; flipped to False after K283 -1.69pp regression) |
| `CADENCE_PC_INCLUSION_BEATS` | 0.5 | retained from earlier DIY-classifier iteration; currently unused by music21-roman path |
| `TEXTURE_WINDOW` | 4 | sliding window |
| `TEXTURE_DENSITY_MIN_DELTA` | 2.0 | density 跳變閾 |
| `TEXTURE_REGISTRAL_MIN_SHIFT` | 7 | 中心 midi shift (半音) |
| `TEXTURE_RANGE_MIN_DELTA` | 5 | range 變化閾 |
| `TEXTURE_SCORE_THRESHOLD` | 1.5 | 投票總分觸發 |
| `TEXTURE_MIN_GAP_GROUPS` | 3 | dedup |
| `USE_LONG_SCALE_THUMB_UNDER` | False | global flag, default OFF; per-piece opt-in (K283 + K545 enabled) |
| `SCALE_MIN_LEN`              | 4     | min notes for a stepwise run to qualify as scale segment |
| `SCALE_MAX_CHROMATIC_RUN`    | 2     | drop segment if ≥3 consecutive half-steps (chromatic exclusion) |

## 2. A/B test results timeline (2026-05-26)

### 2.1 Phase 2.1: mvt4 single piece (figural only)
- Override match: 39.0% → 37.3% (−1.7pp)
- m50 pos2: DP 0 變化（boundary 有插但 DP 局部仍選 thumb）
- **Discovery**: boundary 必要但不充分

### 2.2 Phase 2.2: Bach Inv 1-8 (figural only)
- Aggregate: 37.4% → 37.3% (−0.1pp, essentially neutral)
- High variance: mvt1 +4.0pp, mvt6 −3.4pp
- Per-mvt 結果見 §1.2

### 2.3 Phase 2.3: PIG val 28 (figural + thumb @ 5.0)
- RH GMR: 57.75% → 56.69% (−1.07pp)
- LH GMR: 64.88% → 62.14% (−2.73pp)
- 12 / 28 pieces per-piece regression > 2pp
- → 初判 default OFF

### 2.4 Phase B penalty sweep (figural + thumb, Bach Inv 1-8)
| penalty | aggregate Δ | m50 flip? |
|---|---|---|
| 0.5 | -0.4pp | ❌ |
| 1.5 | -0.4pp | ❌ |
| 3.0 | +0.1pp | ❌ |
| 4.0 | +0.6pp | ❌ |
| **5.0** | **+1.2pp** | **✓** |

→ penalty=5.0 為實測必要值

### 2.5 Subject detection A/B (Bach Inv 1-8)
- subject_only: −0.2pp（neutral）
- all_three (figural+thumb+subject): +1.1pp ≈ figural+thumb 單獨
- → subject 偵測機制正確但 entries 落在曲式大段落點，DP/user 本已對齊

### 2.6 Cadence Phase 1 A/B (Mozart/Beethoven/Chopin/Bach WTC)
- **全部 0 PACs**
- 根因：music21 chordify per-tick fragmentation
- → Phase 1 確認為 placeholder

### 2.7 Texture detection validation
- PIG 034 Beethoven Pathétique LH **m12** 偵測 ✓ (Grave→Allegro 切換)
- Bach mvt4 monophonic: 0 fires ✓ (no texture shift, expected)

### 2.8 下輪 (3) Cost-based 5-piece sample
- pieces: 001, 011, 017, 023, 037
- **0 NEW cost-red-line breaches** under flagged
- Bach Inv 1 cost +63.9 RH / +57.0 LH (vs PIG_min)
- → Phase 2.4 GMR-based 判定 OVERTURNED；cost ≤ PIG_min 全綠

### 2.9 Cadence Phase 2 A/B (2026-05-27)
- K283 (PIG 011): BASE RH 53.27% → Run B (cadence ON) 54.28% (**Δ+1.01pp**); IAC at m10
- K545 (PIG 017): BASE RH 70.02% → Run B 70.02% (Δ+0.00pp); IAC at m8, m5 boundary change made but fingering DP-identical (texture-driven limit documented)
- 26 other PIG val pieces: byte-identical to baseline (isolation verified — 0 non-target drift)
- Aggregate Run B RH: **+0.07pp**
- All 9 `cadence_phase_2` pytest tests: GREEN

### 2.10 Long-Scale Thumb-Under A/B (2026-05-27)
- K545 (PIG 017): BASE RH 70.02% → Run D (cadence + long_scale ON) **74.08%** (**Δ+4.06pp** — primary fix realised)
- K283 (PIG 011): BASE RH 53.27% → Run D 54.28% (Δ+1.01pp — cadence-derived improvement preserved)
- 26 non-target pieces: byte-identical across Runs A/B/C/D ✓ (per-piece flag isolation OK)
- All 21 `test_long_scale_thumb_under.py` pytest tests green
- v1 deployed with 2 spec deviations (direction guard + position guard) — see [[../wiki_piano/concept_long_scale_thumb_under]] §4

## 3. Commit history

### 2026-05-26: Phase 1 (score-claude, 7+1 commits)
| Commit | What |
|---|---|
| `966fae8` | CLAUDE.md wiki_phrase pointer |
| `e942cd4` | Pass 4: figural boundary detection |
| `40f64e1` | thumb-reservation cost rule (Phase B) |
| `7971cfd` | Pass 5: subject imitation detection |
| `0b6d16d` | BACH_INV_PHRASE_FLAGS + per-piece infra (mvt4) |
| `d344183` | Pass 6: cadence PAC (Phase 1 placeholder) |
| `8e0a71e` | Pass 7: texture detection + per-piece expansion mvt1/2/5 |
| `135f956` | cadence lowercase v fix |

obsidian-wiki: 從 `37aef5b` 起到 `045a863`，含 25 page 漸進建構 + cleanup.

### 2026-05-27: Cadence Phase 2 (score-claude, commits `edb434a`–`a84da4e`, 16 commits)
| Commit | What |
|---|---|
| `edb434a` | Spec doc |
| `07efd9a` | Plan doc (12 tasks) |
| `3aaa083` | T1 — `CADENCE_DISABLES_FALLBACK` + `CADENCE_PC_INCLUSION_BEATS` constants |
| `9edc277` | T2 — `_aggregate_measure_chords` helper + K545 unit test |
| `87e06f2` | T2 amendment — expose `final_chord` field (Chord object for music21 roman) |
| `3179d05` | T3 — `_classify_cadence_pair` (music21 roman → PAC/IAC/None) |
| `aa1963e` | T4 — rewrite `_detect_cadence_boundaries` body (PAC+IAC) + K283/K545 integration tests |
| `144bde4` | T5 — `_suppress_fallback_near_cadence` filter + 3 tests |
| `a494c10` | T6 — wire Pass 3 ↔ Pass 6 suppress in `_detect_phrase_starts` |
| `a67c51c` | T7 — `SINGLE_PDF_PHRASE_FLAGS` + `_apply_phrase_flags`/`_restore_phrase_flags` + single-PDF hook |
| `f39a1de` | T8 — `compare_pig._run_v6_dp` wire (mxl_path + stem kwargs + try/finally) |
| `7430a4a` | T9 — `tmp/diag_cadence_p2.py` K283+K545 3-config A/B diagnostic |
| `72efb6a` | T9 fixes — `offset` ↔ `onset_qn` field fallback; `CADENCE_DISABLES_FALLBACK` default True→False (window mode) |
| `976cbb0` | T10 — `tmp/pig28_phrase_ab.py` extended to 3 runs + isolation check (26 non-target byte-identical) |
| `a84da4e` | spec + plan post-pivot reconcile |

obsidian-wiki: 5 pages updated/created in commit `acf3a93`.

### 2026-05-27: Long-Scale Thumb-Under (score-claude, commits `42dacaa`–`1226a52`, 11 commits)
| Commit | What |
|---|---|
| `42dacaa` | T1 — 3 constants (USE_LONG_SCALE_THUMB_UNDER, SCALE_MIN_LEN, SCALE_MAX_CHROMATIC_RUN) |
| `4de8e89` | T2 — _detect_scale_segments + 7 tests |
| `050aaa9` | T3 — _in_scale_segment + 4 tests |
| `17c51fe` | T4 — _is_thumb_pass_at_pivot + _scale_wrong_direction_amount + 10 tests |
| `db5a6cf` | T5 — _apply/restore_phrase_flags 6-tuple |
| `8e8bd74` | T6 — _process_mvt_book inline 6-tuple |
| `5bdc035` | T7 — DP hook wired (note: placed in wrong function, fixed at T9) |
| `7bf6cb4` | T8 — K283 + K545 long_scale=True in SINGLE_PDF_PHRASE_FLAGS |
| `e948958` | T9 fix — move hook to _run_phrase_dp + add direction/position guards |
| `7b9c99c` | T9 diag — tmp/diag_long_scale_k545.py |
| `1226a52` | T10 — PIG 28 harness Run D extension |

## 4. 2026-05-27: Cadence Phase 2 deployment summary

- **Pass 6 upgraded**: Phase 1 placeholder → Phase 2 (music21 roman, PAC+IAC, window mode)
- **New infrastructure**: `SINGLE_PDF_PHRASE_FLAGS` for single-PDF per-piece opt-in (parallel to `BACH_INV_PHRASE_FLAGS`)
- **K283 enabled** (`cadence: True`): verified +1.01pp RH — IAC at m10 added extra boundary
- **K545 enabled** (`cadence: True`): IAC at m8 detected correctly; DP fingering unchanged (texture-driven limit — m5 ascending scale problem requires DP cost rules, not just phrase boundary)
- **Isolation**: 26/26 non-target PIG val pieces byte-identical to baseline
- **Tests**: 9 new `cadence_phase_2` pytest tests, all GREEN
- **HC detection**: explicitly excluded (over-fires on K545 alberti-bass single-note measures)

## 5. Open TODOs / next-session candidates

### Priority A (low effort, high value)
- PIG 28 full cost-based sweep（擴大 5→28）confirm flags 可否 flip default ON
- 如綠 → flip `USE_FIGURAL_BOUNDARY_DETECTION` + `USE_THUMB_RESERVATION` + `USE_TEXTURE_DETECTION` 為 True

### Priority B (moderate effort)
- K545 m5 ascending scale fingering: requires DP cost rule (not boundary fix) — "long-scale protection" or thumb-under promotion; see [[analysis_mozart_k545_first_mov]] §4
- `RUNNING_PASSAGE_OUTER_START_PENALTY` 加進 `_TUNE_SCALARS`（PIG 28 確認後）
- Cadence Phase 2 extension: HC detection (deferred — over-fires on alberti texture); windowed key analysis for mid-piece modulation

### Priority C (per-need)
- `concept_texture_change_detection` Phase 2: dynamic + pedal marking 偵測（需驗證 Audiveris 抽取支援）
- Fioritura / ornament 過濾（Chopin Nocturne case，concept_chopin_lyrical_phrase 已記載）
- Per-piece analysis 擴充：analysis_beethoven_pathetique_first_mov, analysis_chopin_etude_op10_no3, etc.
- analysis_bach_inv_4_d_minor §5 揭露的 `concept_figural_boundary_detection` 已完成、相關連結驗證

### Priority D (experimental)
- Cadence Phase 3: HC/DC detection scope expansion
- Beat-strength filter for PAC (currently PAC accepted on any beat)
- 各 era 的 `concept_modal_cadence_*` 系列（modal final detection）

## 6. Cross-links

- canonical project state: [[../score-claude/memory/project_phrase_detection_v1_phase1_phaseB]]
- foundational principle: [[../score-claude/memory/feedback_phrase_analysis_is_its_own_discipline]]
- separation principle (this page's existence reason): [[../score-claude/memory/feedback_wiki_knowledge_vs_project_separation]]
