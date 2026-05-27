# Analysis: Mozart Piano Sonata K545 in C major, 1st movement (B1-12 excerpt)

> Source: PIG val piece 017 (`017_Mozart_PSon_K545_C_i_B1-12`)
> Cadence Phase 2 validation result: secondary (texture limit) — see [[concept_cadence_detection]] §7.4
> Status: FIXED 2026-05-27 — long-scale thumb-under rule deployed; K545 RH +4.06pp (BASE 70.02% → Run D 74.08%)

## 1. Excerpt structure

12 bars of K545 mvt1 — the famous opening of "Sonata facile". B1-12 covers:
- m1-4: first theme antecedent (4 bars, ends on HC at m4 — but m4's dominant landing is too short for our HC detection)
- m5-8: consequent — running ascending scale m5-m7 + descending resolution m8 (IAC: V7 in 3rd inversion at m7 → I root at m8, soprano on E not C)
- m9-12: transition / second theme group in dominant key (G major)

## 2. Cadence detection result

- **m7→m8**: detected as **IAC** by `_classify_cadence_pair`. music21 returns:
  - m7 final = [F4, B4, G5] → `V inv=3` (V7 in 3rd inversion, bass=F)
  - m8 final = [C2, E2, E4] → `I inv=0` (root position), soprano=E4 (pc=4) ≠ C tonic → IAC
- **Result**: boundary added at first group of m9 (correct, matches musical phrase structure)
- **Pass 3 fallback m5 boundary**: NOT suppressed in window mode (distance from cadence m9 = 4 bars > suppress_bars=1)
- **Pass 3 fallback m9 boundary**: SUPPRESSED (window mode removes Pass 3 m9 because cadence is at m9)
- **Final phrase_starts under cadence config**: identical to BASE (m1, m5, m9, m11 — m9 just sourced from cadence instead of Pass 3)

## 3. PIG fingering disagreement

K545 RH B1-12 had pre-existing -8.4pp regression with figural+thumb flags ON (Phase 2.3 PIG sweep). Root cause traced to m5 ascending scale:
- PIG 6/6 annotators: 1-2-3-1-2 (thumb-under at D5)
- BASE DP: 1-2-3-4-5 (no thumb-under — already wrong vs PIG, but stable)
- With thumb-reservation ON (TRT): 2-3-4-5-2 (worse — boundary at m5 triggers anti-thumb cost)

## 4. K545 m5 fix: Long-Scale Thumb-Under Rule (2026-05-27)

After Cadence Phase 2 removed the false m5 phrase boundary, DP fingering still
defaulted to `1-2-3-4-5` because `_transition_cost` penalized the thumb-under
transition (C5→D5: pf=3, cf=1) as WRONG_DIRECTION (~11.0 surcharge).

The Long-Scale Thumb-Under Protection rule (see [[../wiki_piano/concept_long_scale_thumb_under]])
detects K545 m5 as a long ascending diatonic scale segment, cancels the
WRONG_DIRECTION penalty on thumb-pass transitions at the standard pivot position
inside the segment, and allows DP to pick `1-2-3-1-2-3-4-5` matching PIG 6/6.

Result: K545 RH BASE 70.02% → Run D (cadence + long_scale): **74.08% (Δ+4.06pp)**.

Both rules are opt-in via `SINGLE_PDF_PHRASE_FLAGS["017_Mozart_PSon_K545_C_i_B1-12"]
= {"cadence": True, "long_scale": True, ...}`.

**v1 deviations from spec** (see [[../wiki_piano/concept_long_scale_thumb_under]] §4):
- Direction guard: only RH ascending + LH descending (2 of 4 cases); RH descending
  thumb-over not yet cancelled
- Position guard: hardcoded `offset % 5 == 2` matches C-major-style pivot; may need
  per-key-signature work to generalise

**v2 update (2026-05-27)**: Position guard refactored from hardcoded `offset % 5 == 2`
to direction-aware modular pattern + uniform end-guard (see
[[../wiki_piano/concept_long_scale_thumb_under]] §4). K545 RH **IMPROVED from
v1 74.08% to v2 77.59% (+3.51pp gain)** — m9's long ascending segment now fires
multiple thumb-unders correctly (v1 only fired once). m5 fingering still
`1-2-3-1-2-3-4-5` matching PIG 6/6. Both v1 deviation notes (direction guard
+ position guard hack) are now RESOLVED.

## 5. HC over-fire concern (why HC was not included in Phase 2)

K545 m1, m2, m4 all have measures ending on a single bass note D (dominant), which music21 classifies as `v` (incomplete minor dominant) or `V`. Including HC detection would add false boundaries at m2, m3, m5 — one per bar in the opening. This is the main reason HC is excluded from Phase 2 scope.

## 6. Cross-refs

- [[concept_cadence_detection]] §7 — Phase 2 algorithm + K283/K545 validation summary
- [[composer_mozart_phrasing]] §7 — K545 status
- [[analysis_mozart_k283_first_mov]] — sister piece, primary success case
- score-claude memory: `project_cadence_phase_2.md`
