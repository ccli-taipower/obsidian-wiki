# Phrase Analysis Wiki Log

## [2026-05-26] init | Wiki created — fugue / counterpoint seed

新建 wiki_phrase/ 作為樂句分段獨立 discipline (parallel to wiki_piano/).
觸發背景：mvt4 m50 RH 樂句邊界漏接，user 指出 phrase analysis 是要獨立學習的軌道，無法用 override 教。詳見 `score-claude/memory/feedback_phrase_analysis_is_its_own_discipline.md`。

**Pages created (4)**:
- `index.md` — index + roadmap
- `src_epochtimes_fugue_zhou_2005.md` — source: 周怡秀《音樂中的復格形式》大紀元 2005
- `concept_fugue.md` — fugue 結構、樂句邊界判斷規則草案、Bach Invention 適用性
- `concept_counterpoint.md` — 多聲部樂句獨立性、per-hand DP 為何正確、voice separation 隱藏問題

**Key insights for fingering system**:
1. 對位 = 每聲部 / 每手獨立樂句結構，邊界**不需對齊**（解釋 mvt4 LH/RH 不對稱不是 bug）
2. 主題重入聲 = 樂句邊界（比音高跳幅更精準的訊號）
3. Fugue 不規律樂句長度 → 現有 Pass 3 「4/8 bar 週期」對 Bach Invention 系統性錯誤

**Next**:
- P0: `analysis_bach_inv_4_d_minor.md` — 把 mvt4 m50 case 寫成可驗證的單元（包含當前 RH 在 m50 漏接的根因 + subject identification）
- P1: `concept_subject_imitation_detection.md` — 主題偵測演算法（草案在 concept_fugue §7）

## [2026-05-26] expand | PIG-driven coverage to 89% (6 new pages)

User 指出 PIG 包含不同時期 / 不同作曲家，phrase 切錯會系統性影響指法評估。決定按 PIG 覆蓋優先序批次新增 6 頁，把覆蓋率從 15% 提到約 89%。

**Pages created (6)**:
- `concept_classical_period_sentence.md` (P0) — 古典 period (4+4) / sentence (2+2+4) / cadence (PAC/IAC/HC/DC)；涵蓋 Mozart 20 + Beethoven 21 + Schubert 5 = 46 曲
- `concept_chopin_lyrical_phrase.md` (P1) — 浪漫派不規律長樂句、禁用 4-bar fallback、texture / pattern 訊號；涵蓋 Chopin 23+ 其他浪漫 = 39 曲
- `composer_beethoven_phrasing.md` (P2) — phrase expansion / compression / hemiola / tempo 切換；按早 / 中 / 晚期細分；涵蓋 Beethoven 21 曲
- `concept_impressionist_phrasing.md` (P3) — Debussy/Ravel texture-driven、cadence 失效、modal scales；涵蓋 12 曲
- `composer_schubert_long_phrase.md` (P4a) — Lied 旋律 + 遠系轉調訊號；涵蓋 Schubert 5 曲
- `composer_grieg_lyric_pieces.md` (P4b) — Lyric Pieces 規律結構 + modal + drone bass；涵蓋 Grieg 10 曲

**Index updates**:
- 新增 PIG dataset 覆蓋狀態表（89% 覆蓋率）
- 路線圖重排：P0 改為 cadence_detection / subject_imitation_detection / bach_inv_4 analysis

**Key insights for fingering system**:
1. 古典時期：4-bar 週期大致 OK，但 sentence 結構需要 2+2+4 偵測避免在 bar 3 切
2. 浪漫派（Chopin）：**禁用 4-bar fallback**，改靠 LH pattern / texture 訊號
3. Beethoven 中晚期：phrase expansion / compression 普遍，禁用週期 fallback
4. 印象派：cadence 訊號失效，改用 texture / dynamic / tempo 訊號
5. Schubert：古典基底 + 轉調訊號 + 較長樂句（8-16 bar）
6. Grieg：規律 4-8 bar，LH drone 時不參與樂句訊號

**Next**:
- P0: `concept_cadence_detection.md` — 4 種 cadence 偵測（多頁需要）
- P0: `concept_texture_change_detection.md` — 印象派 + 浪漫派需要
- P0: `analysis_bach_inv_4_d_minor.md` — 把 mvt4 m50 case 寫成可驗證單元
- 中期目標：實作 composer-aware `_detect_phrase_starts` dispatcher

## [2026-05-26] tools + first analysis | cadence + subject detection + Bach Inv 4 case study

接續 PIG-driven expansion，把所有 concept 頁引用的工具頁補完，並做第一個 end-to-end analysis 驗證。

**Pages created (3)**:
- `concept_cadence_detection.md` — 4 種 cadence (PAC/IAC/HC/DC) 偵測演算法，music21 實作範例，confidence weight；工具頁，被多 era 概念頁引用
- `concept_subject_imitation_detection.md` — fugue/Invention 主題重入聲偵測，含 4 種模仿變體 (rectus/inversion/retrograde/RI) + 時值變化 (augmentation/diminution) + voice separation 前置考量
- `analysis_bach_inv_4_d_minor.md` — 第一個 end-to-end case，用 [[concept_subject_imitation_detection]] 跑 mvt4 實際資料

**Bach Inv 4 案例的關鍵發現**：

mvt4 subject (len=8) 的入聲位置實測：
- RH: m1, m5, m26, m44 (exposition opening, exposition cont, middle entry, final entry)
- LH: m3, m38, m46 (LH imitation, recap LH, final LH)

→ 結構正確，符合典型 Bach Invention exposition + episode + middle entries + recap + coda 形式

**但 m50 邊界 subject detection 沒找到**：
- m50 在 coda 段（m48-m52）
- 邊界是「figural / sequential boundary」— 一個 sextuplet figure 結束、下一個 figure 開始
- subject detection 與 cadence detection 都不涵蓋此類邊界

**揭露第三類樂句邊界**：
| 類型 | 工具 | mvt4 範例 |
|---|---|---|
| Subject entry | concept_subject_imitation_detection | m1/5/26/44/3/38/46 |
| Cadence | concept_cadence_detection | (典型在段尾) |
| **Figural / Sequential** | **❌ 待寫** | **m50 pos2** |

→ 新 P0：`concept_figural_boundary_detection.md`（從 mvt4 m50 case 揭露）

**Index 更新**：
- 加 cadence + subject + analysis 三筆連結
- 路線圖：標記 3 個 P0 完成，新增 figural boundary 為新 P0

**Next**:
- P0: `concept_figural_boundary_detection.md` (新)
- 中期目標：實作 composer-aware `_detect_phrase_starts` dispatcher (combines 3-4 軸偵測)
- 第一波實作驗證：在 score-claude 端做 PAC 偵測 + Bach Invention subject 偵測的 Phase 1 prototype

## [2026-05-26] 3rd boundary class concept | concept_figural_boundary_detection

接續 analysis_bach_inv_4 揭露第三類樂句邊界 (figural / coda)，補完 concept 頁。

**Page created (1)**:
- `concept_figural_boundary_detection.md` — Figure 操作型定義 (方向一致 + 節奏一致 + 音域 ≤ octave + 無內部休止) + 4 種 figural boundary 事件類型 + 完整偵測演算法（Python 偽碼）+ closure 音歸屬問題（mvt4 m50 為例）+ 與 subject/cadence detection 整合 + Phase 1/2/3 漸進實作路線

**三軸偵測架構至此齊全**：
| 軸 | 工具 | 對應 PIG 範圍 |
|---|---|---|
| Subject entry | concept_subject_imitation_detection | 對位作品 (Bach ~23 曲) |
| Cadence | concept_cadence_detection | 古典 + 浪漫主調 (~80+ 曲) |
| Figural | concept_figural_boundary_detection | episode / coda / etude (其他) |

**Next**: 落地到 `program/run.py` Phase 1 prototype，跑 A/B 看 mvt4 + PIG GMR 影響

## [2026-05-26] Phase 1 + Phase B 落地 + Validation

**Phase 1: figural boundary detection 落地** (score-claude commit e942cd4):
- `_detect_figural_boundaries(groups)` 函式 + USE_FIGURAL_BOUNDARY_DETECTION flag (default OFF)
- 含 fix: 加 FIGURAL_MAX_STEP_SEMITONES=4 限制，避免 closure leap 把 figure range 撐爆 octave 上限
- Validation: m50 pos2 正確被偵測；221 tests pass

**Phase 2.1 mvt4 A/B**: Override match -1.7pp (39.0% → 37.3%). m50 詳 0 變化 — 揭露關鍵發現「樂句邊界必要但不充分」: DP 在新樂句內仍 local-min 選 thumb，需要新 cost rule

**Phase 2.2 Bach Inv 全本** (mvt 1-8, 1002 overrides): aggregate **-0.1pp** (37.4 → 37.3). high variance: mvt1/2 +2-4pp (好), mvt4/6/7 -1.6 to -3.4pp (mvt6 過 red line). 啟發式分不出「真樂句邊界」vs「同樂句內 figural 變化」

**Phase B: 新 concept + 新 cost rule** (`concept_running_passage_thumb_reservation.md`):
- 機制：phrase start 看後續 4 音，若為 stepwise > 5 半音 ascending/descending → 罰「方向 outer finger」
- 目標：捕捉 thumb-under / substitution 慣例 (Bach 風格長階串聯)
- 實作：`_running_passage_thumb_reservation_cost()` + USE_THUMB_RESERVATION flag

**Phase B 實測 penalty sweep** (Bach Inv 1-8):
| penalty | Δ aggregate | m50 flip? |
|---|---|---|
| 0.5-1.5 | -0.4pp | ❌ |
| 3.0 | +0.1pp | ❌ |
| 4.0 | +0.6pp | ❌ |
| **5.0** | **+1.2pp** | **✓** |

penalty=5.0 為必要值（W_PHRASE_ANCHOR + transition seam 在 thumb 上的累積偏好 ~2-3 units 要被克服）。已設為 default。

**Next**:
- PIG val 驗證（28 首）以確認對其他作曲家無 negative spillover
- 若 PIG 健康 → 把 flags default 改 ON
- 加 RUNNING_PASSAGE_OUTER_START_PENALTY 到 _TUNE_SCALARS

## [2026-05-26] Phase 2.3 PIG val + Phase 2.4 Decision

**PIG val 28 首 (GMR-based, both flags ON @ penalty=5.0)**:
| Hand | OFF | ON | Δ |
|---|---|---|---|
| RH | 57.75% | 56.69% | -1.07pp |
| LH | 64.88% | 62.14% | -2.73pp |
| TOTAL | 60.65% | 58.90% | **-1.74pp** |

12 / 28 首 per-piece regression > 2pp（包括 001/002 Bach PIG、011/017 Mozart、021 Chopin、035 Debussy、124 LH -9pp）。
4 首改善（086/097/135/140 RH +3 to +9pp）但被退步遠超。

**這結果與 Phase B Bach Inv (+1.2pp) 並不矛盾** — 兩個 ground truth：
- Bach Inv user override = user 個人 idiom（規則改善 ✓）
- PIG 多人 majority = annotator 平均 idiom（規則推離 ✗）

→ 規則正在做它該做的事：把 DP 推往 user 個人 hand，而非 PIG 平均。
**與 `feedback_personal_biomechanics.md` 完全一致** — user 個人 ≠ PIG 多人平均，PIG 是「上限參考」非「優化目標」。

**Phase 2.4 Decision: default 維持 OFF**

理由：
1. 雖然 GMR ≠ cost red line (`_cost_sanity_breaches`)，12 / 28 首顯著退步部署風險高
2. 規則受益需 user 已教過該曲 override；無 override 時只是把 DP 推離 PIG 平均（對陌生曲子變差）
3. 未來路徑：per-piece config（單曲 opt-in）+ 改用 cost-based 紅線檢查（而非 GMR）

**長期啟示**：phrase-aware cost rules 可能需要「per-style scope」而非「global enable」。對位作品 + 用戶教過 override 的場合 ON；其他場合 OFF。下一輪 wiki 應該考慮 `concept_per_style_cost_rule_scoping` 之類的元規則。

## [2026-05-26] roadmap batch | 5 pages (3 composer + 2 concept)

清理 index.md 上的高 ROI TODO，連續寫 5 頁。

**Composer pages (3)**:
- `composer_chopin_phrasing.md` — Chopin 23 PIG 曲，按 genre 細分 (Nocturne/Etude/Ballade/Mazurka/Waltz/Prelude/Polonaise/Scherzo/Impromptu) + 邊界訊號優先序 + 為何禁用 4-bar fallback 對 Chopin 特別重要
- `composer_mozart_phrasing.md` — Mozart 20 PIG 曲，sonata-allegro 段落結構詳解 + 為何是 cadence detection 演算法的純正驗證 baseline + vs Beethoven 對比
- `composer_debussy_phrasing.md` — Debussy 9 PIG 曲，按 collection 細分 (Suite Bergamasque / Préludes / Études / Images / Children's Corner) + Whole-tone/Pentatonic/Octatonic 對指法的影響 + Pedal 重要性

**Concept pages (2)**:
- `concept_phrase_elision.md` — 樂句重疊問題（一句結尾 = 下句開始）；「歸前」決定 + 對 motif/cadence detection 的影響；浪漫派頻繁
- `concept_modulation_as_phrase_signal.md` — 第四類樂句邊界訊號（轉調）；music21 key signature change 偵測 + filter tonicization；對 Schubert/Beethoven/Chopin 關鍵

**Index 路線圖**：5 個 TODO 已標完成；剩下 P0 (cadence+subject 實作), P1 (texture_change), P4 (Rachmaninoff, modal_scale), P5 (二十世紀, 雜項) 等。

**PIG 覆蓋度**：composer pages 從 3 個（Beethoven/Schubert/Grieg）增到 6 個（+ Chopin/Mozart/Debussy），三大 composer bloc (Bach/Mozart/Chopin) + Debussy 全部有專頁。

## [2026-05-26] roadmap completion batch — 5 more pages (PIG 100%)

接續清完 index.md 剩餘 P1/P4/P5 TODOs，新增 5 頁，wiki PIG 覆蓋從 ~89% 推到 **100%**。

**Concept pages (2)**:
- `concept_texture_change_detection.md` (P1) — 第五類樂句邊界訊號工具頁：density/register/dynamic/pedal 變化偵測；[[concept_impressionist_phrasing]] + [[composer_debussy_phrasing]] 核心需求
- `concept_modal_scale_fingering.md` (P4) — Modal/pentatonic/whole-tone/octatonic 對指法 + cadence detection 的影響；跨 wiki_piano + wiki_phrase

**Composer pages (3)**:
- `composer_rachmaninoff_phrasing.md` (P4) — 後期浪漫補完，4 PIG 曲；長 melodic arch + 厚和聲 + 戲劇 climax + 大手前提
- `composer_twentieth_century.md` (P5) — Scriabin + Bartok 合一頁，3 PIG 曲
- `composer_other_pig_pieces.md` (P5) — Mussorgsky/Joplin/Faure/Satie/Dvorak/Albeniz/Scarlatti 合一頁，13 PIG 曲

**wiki 整體狀態**:
- Sources: 1, Concepts: 12, Composers: 8, Analyses: 1 (Bach Inv 4)
- 路線圖剩 **唯一一個 P0**：實作 cadence + subject detection 到 `program/run.py::_detect_phrase_starts`
- 其他待寫項是 per-piece analysis 系列 (analysis_mozart_k283 / analysis_chopin_op9_no2 / etc) — 隨 debugging 需要逐一補

## [2026-05-26] P0 final — cadence detection (PAC Phase 1) 實作落地

完成 wiki_phrase concept_cadence_detection.md 的 Phase 1 (PAC only) 落地。
score-claude commit d344183.

Architecture:
- `_detect_cadence_boundaries(groups)` 用 music21 chordify + RomanNumeralFromChord
- `_PHRASE_CTX` module-level dict 傳 mxl_path（不動 `_detect_phrase_starts` signature）
- Pass 6 hook in `_detect_phrase_starts`（only fires if mxl_path in ctx）
- BACH_INV_PHRASE_FLAGS schema 加 "cadence" key
- _process_mvt_book 寫 mvt_path 進 ctx，per-mvt 清 cache

mvt4 啟用 cadence flag 後實測：
- **PAC 偵測 0 個** — Bach 對位 texture (chordify 把 multi-voice 揉一起)
  + 嚴格 V→I 根位 + soprano tonic 條件對 Bach 偏嚴
- DP 0 finger changes; aggregate match unchanged
- 與 concept §5 預期一致：對位音樂失靈

**對 Bach 效益低（如預期）；對 Mozart/Beethoven/Chopin/Schubert 預期會 fire**
（傳統 cadence 常見）。實作就緒、未來逐曲驗證可加進 BACH_INV_PHRASE_FLAGS。

**wiki_phrase 整體狀態 (final)**:
- Pages: 22 total (1 source + 12 concepts + 8 composers + 1 analysis + index/log)
- PIG 覆蓋: 100% (150/150)
- 5 類偵測器全 implemented in `_detect_phrase_starts`:
  Pass 1 (hard breaks) + Pass 1b (anacrusis) + Pass 2 (period inference) +
  Pass 3 (週期 fallback) + Pass 4 (figural, opt-in) + Pass 5 (subject, opt-in) +
  Pass 6 (cadence PAC, opt-in)
- 路線圖 P0 全完成；剩 per-piece analysis 隨 debugging 補

**Next session 可能方向**:
- Per-piece analysis 系列（analysis_mozart_k283, analysis_chopin_op9_no2）
- Cadence Phase 2 (IAC/HC/DC)
- 對 Mozart/Beethoven PIG 啟用 cadence flag 跑 A/B
- Cost-based 紅線 (Cost(DP) ≤ Cost(PIG_min)) 取代 GMR 為 deployment 判準
- Per-piece thumb-reservation 啟用其他 mvt（用戶教過 override 的）
