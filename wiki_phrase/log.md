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
