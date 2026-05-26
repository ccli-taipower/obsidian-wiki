# Phrase Analysis Wiki 樂句分析 Wiki

> Last updated: 2026-05-26 | Sources: 1 | Concepts: 8 | Composers: 3 | Analyses: 1 | Raw: 0

樂句分段 (phrase segmentation) 是鋼琴指法系統的上游問題 — 樂句切錯，指法不可能對。本 wiki 與 [[../wiki_piano/index]] 並列，是獨立的學習與知識累積 track。

詳見 [[../score-claude/memory/feedback_phrase_analysis_is_its_own_discipline]]。

## 核心原則

- 樂句分析 = 獨立學科，與生物力學並列、不互相替代
- 不同作曲家 / 曲式有不同樂句邏輯，無法用 override 教
- 所有規則須有 wiki / 理論出處，禁止 magic 常數
- 工作流程：(1) 讀譜 → (2) 樂句切分（用此 wiki）→ (3) 指法（用 wiki_piano）

## PIG Dataset 覆蓋狀態

當前 wiki 覆蓋估計（150 曲總計）：

| 時期 / 風格 | PIG 曲數 | wiki 頁面 |
|---|---|---|
| 巴洛克 (Bach + Scarlatti) | 23 | [[concept_fugue]] + [[concept_counterpoint]] ✅ |
| 古典 (Mozart) | 20 | [[concept_classical_period_sentence]] ✅ |
| 古典→浪漫過渡 (Beethoven) | 21 | [[composer_beethoven_phrasing]] ✅ |
| 早期浪漫 (Schubert) | 5 | [[composer_schubert_long_phrase]] ✅ |
| 浪漫 (Chopin + Schumann + Liszt + Brahms + Mendelssohn 等) | 49 | [[concept_chopin_lyrical_phrase]] ✅ (Chopin 為主) |
| 浪漫民族樂派 (Grieg) | 10 | [[composer_grieg_lyric_pieces]] ✅ |
| 後期浪漫 (Rachmaninoff) | 4 | ❌ TODO |
| 印象 (Debussy + Ravel) | 12 | [[concept_impressionist_phrasing]] ✅ |
| 二十世紀 / 現代 (Scriabin + Bartok) | 3 | ❌ TODO |
| 其他 (Mussorgsky + Joplin + Faure + Satie 等) | 13 | ❌ TODO |

**目前覆蓋：~134 / 150 = 89%**（按曲數），剩 11% 為後期浪漫 / 二十世紀 / 雜項。

## Concepts (通用)

- [Fugue 賦格](concept_fugue.md) — 主題 / 答題 / 插曲 / 開展部 / Stretto；Bach Inventions 適用
- [Counterpoint 對位](concept_counterpoint.md) — 多聲部樂句獨立性；解釋兩手樂句邊界不對齊
- [Classical Period & Sentence](concept_classical_period_sentence.md) — 古典時期 4+4 period 與 2+2+4 sentence 結構；四種 cadence (PAC/IAC/HC/DC)
- [Chopin & 浪漫派抒情樂句](concept_chopin_lyrical_phrase.md) — 不規律長樂句 + 禁用 4-bar fallback；浪漫派 cadence 退化
- [Impressionist Phrasing](concept_impressionist_phrasing.md) — Debussy/Ravel texture-driven phrasing；cadence 失效
- [⭐ Cadence Detection](concept_cadence_detection.md) — PAC/IAC/HC/DC 偵測演算法 (music21 RomanNumeral)；工具頁，多概念引用
- [⭐ Subject Imitation Detection](concept_subject_imitation_detection.md) — fugue / Invention 主題重入聲偵測；正向 + 倒影 + 逆行 + 逆行倒影 + 時值變化
- [⭐ Figural Boundary Detection](concept_figural_boundary_detection.md) — 第三類樂句邊界（figure 切換）；處理 episode / coda 段不被 subject + cadence 涵蓋的部分；mvt4 m50 case 揭露

## Composers (作曲家特化)

- [Beethoven](composer_beethoven_phrasing.md) — 對古典 period/sentence 的擴張與壓縮；按早 / 中 / 晚期細分
- [Schubert](composer_schubert_long_phrase.md) — Lied 旋律 + 遠系轉調作為樂句訊號
- [Grieg](composer_grieg_lyric_pieces.md) — Lyric Pieces 系列，規律結構 + modal 色彩

## Analyses (per-piece)

- [⭐ Bach Invention 4 in D minor (BWV 775)](analysis_bach_inv_4_d_minor.md) — 第一個 end-to-end case study；揭露**第三類樂句邊界**（figural / coda）— subject detection + cadence detection 都不涵蓋；驅動下一輪 concept TODO

## Sources

- [周怡秀《音樂中的復格形式》(大紀元 2005)](src_epochtimes_fugue_zhou_2005.md) — 中文百科文章，定義 fugue / 對位 / 模仿 / Bach 復格藝術

## Raw (待擴增)

- 預計來源：Caplin 《Classical Form》、Schoenberg 《Fundamentals of Musical Composition》、Rothstein 《Phrase Rhythm in Tonal Music》、Lerdahl-Jackendoff GTTM、Fux Gradus ad Parnassum (英譯)、Bach Inventions 演奏 / 教學註解、Howat《Debussy in Proportion》

## 路線圖

| 優先序 | 項目 | 狀態 |
|---|---|---|
| ~~P0~~ | ~~`analysis_bach_inv_4_d_minor`~~ | ✅ 完成 (揭露 figural boundary 缺失) |
| ~~P0~~ | ~~`concept_cadence_detection`~~ | ✅ 完成 (含 music21 演算法) |
| ~~P0~~ | ~~`concept_subject_imitation_detection`~~ | ✅ 完成 (含 4 種變體 + 時值變化) |
| ~~P0~~ | ~~`concept_figural_boundary_detection`~~ | ✅ 完成 (direction reversal + closure 處理) |
| **P0** | **實作**：把 cadence + subject + figural 三軸落地到 `program/run.py` 的 `_detect_phrase_starts` | **進行中** |
| P1 | `concept_texture_change_detection` — 印象派需要 | TODO |
| P1 | `concept_phrase_elision` — 古典 / 浪漫共用 | TODO |
| P2 | `concept_modulation_as_phrase_signal` — Schubert / Beethoven | TODO |
| P3 | `composer_chopin_phrasing` — Chopin 細分（Nocturne / Ballade / Etude / Mazurka / Waltz / Prelude） | TODO |
| P3 | `composer_mozart_phrasing` — Mozart 細分 | TODO |
| P3 | `composer_debussy_phrasing` — Debussy 細分 | TODO |
| P4 | `composer_rachmaninoff_phrasing` — 後期浪漫補完 | TODO |
| P4 | `concept_modal_scale_fingering` (mode 對指法 + 樂句的影響) | TODO |
| P5 | 二十世紀 / 現代 (Scriabin, Bartok) | TODO |
| P5 | 其他作曲家 (Mussorgsky, Joplin, Faure, Satie) | TODO |
