# Phrase Analysis Wiki 樂句分析 Wiki

> Last updated: 2026-05-26 | Sources: 1 | Concepts: 12 | Composers: 8 | Analyses: 4 | Raw: 0

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
| 後期浪漫 (Rachmaninoff) | 4 | [[composer_rachmaninoff_phrasing]] ✅ |
| 印象 (Debussy + Ravel) | 12 | [[concept_impressionist_phrasing]] + [[composer_debussy_phrasing]] ✅ |
| 二十世紀 / 現代 (Scriabin + Bartok) | 3 | [[composer_twentieth_century]] ✅ |
| 其他 (Mussorgsky + Joplin + Faure + Satie 等) | 13 | [[composer_other_pig_pieces]] ✅ |

**目前覆蓋：150 / 150 = 100%**（按曲數）— PIG 28 val 全涵蓋。

## Concepts (通用)

- [Fugue 賦格](concept_fugue.md) — 主題 / 答題 / 插曲 / 開展部 / Stretto；Bach Inventions 適用
- [Counterpoint 對位](concept_counterpoint.md) — 多聲部樂句獨立性；解釋兩手樂句邊界不對齊
- [Classical Period & Sentence](concept_classical_period_sentence.md) — 古典時期 4+4 period 與 2+2+4 sentence 結構；四種 cadence (PAC/IAC/HC/DC)
- [Chopin & 浪漫派抒情樂句](concept_chopin_lyrical_phrase.md) — 不規律長樂句 + 禁用 4-bar fallback；浪漫派 cadence 退化
- [Impressionist Phrasing](concept_impressionist_phrasing.md) — Debussy/Ravel texture-driven phrasing；cadence 失效
- [⭐ Cadence Detection](concept_cadence_detection.md) — PAC/IAC/HC/DC 偵測演算法 (music21 RomanNumeral)；工具頁，多概念引用
- [⭐ Subject Imitation Detection](concept_subject_imitation_detection.md) — fugue / Invention 主題重入聲偵測；正向 + 倒影 + 逆行 + 逆行倒影 + 時值變化
- [⭐ Figural Boundary Detection](concept_figural_boundary_detection.md) — 第三類樂句邊界（figure 切換）；處理 episode / coda 段不被 subject + cadence 涵蓋的部分；mvt4 m50 case 揭露
- [⭐ Running Passage Thumb Reservation](concept_running_passage_thumb_reservation.md) — phrase-start anchor cost rule；長階運行音起手避免「最外側 finger」以保留 thumb 給 thumb-under；解 mvt4 m50 case 揭露的 DP 短視野問題；實測 penalty=5.0 為必要值
- [Phrase Elision](concept_phrase_elision.md) — 樂句重疊（一句結尾 = 下句開始）；「歸前」決定 + 對 motif/cadence detection 的影響；浪漫派頻繁
- [Modulation as Phrase Signal](concept_modulation_as_phrase_signal.md) — 第四類樂句邊界訊號（轉調）；key signature change 偵測 + filter tonicization；對 Schubert/Beethoven/Chopin 關鍵
- [⭐ Texture Change Detection](concept_texture_change_detection.md) — 第五類樂句邊界訊號（紋理變化）：density / register / dynamic / pedal；印象派 + 浪漫派核心工具
- [Modal Scale Fingering](concept_modal_scale_fingering.md) — Modal / pentatonic / whole-tone / octatonic 對指法 + 樂句的影響；跨 wiki_piano + wiki_phrase

## Composers (作曲家特化)

- [Beethoven](composer_beethoven_phrasing.md) — 對古典 period/sentence 的擴張與壓縮；按早 / 中 / 晚期細分
- [Schubert](composer_schubert_long_phrase.md) — Lied 旋律 + 遠系轉調作為樂句訊號
- [Grieg](composer_grieg_lyric_pieces.md) — Lyric Pieces 系列，規律結構 + modal 色彩
- [⭐ Chopin (per-genre)](composer_chopin_phrasing.md) — Nocturne / Etude / Ballade / Mazurka / Waltz / Prelude / Polonaise / Scherzo / Impromptu 各 genre 樂句邏輯；最大 PIG composer bloc (23 曲)
- [⭐ Mozart (per-form)](composer_mozart_phrasing.md) — sonata-allegro / slow mov / rondo 形式；古典 period/sentence **純正範本**；驗證 cadence detection 演算法的 baseline
- [⭐ Debussy (per-collection)](composer_debussy_phrasing.md) — Suite Bergamasque / Préludes / Études / Images / Children's Corner 各 collection；time-period 對 cadence 適用性影響大
- [Rachmaninoff](composer_rachmaninoff_phrasing.md) — 後期浪漫長 melodic arch + 厚和聲 + 戲劇 climax + 大手前提
- [20th Century (Scriabin + Bartok)](composer_twentieth_century.md) — atonal/post-tonal phrase；Scriabin mystic chord + Bartok modal/asymmetric meter
- [Other PIG composers](composer_other_pig_pieces.md) — Mussorgsky/Joplin/Faure/Satie/Dvorak/Albeniz/Scarlatti (13 PIG 曲合一頁)

## Analyses (per-piece)

- [⭐ Bach Invention 4 in D minor (BWV 775)](analysis_bach_inv_4_d_minor.md) — 第一個 end-to-end case study；揭露**第三類樂句邊界**（figural / coda）— subject detection + cadence detection 都不涵蓋；驅動下一輪 concept TODO
- [Mozart K283 G major 1st mov](analysis_mozart_k283_first_mov.md) — PIG 011, sonata-allegro 教科書範例；驗證 cadence detection 對純古典作品命中率（預期 3-5 PACs）
- [Chopin Nocturne Op.9 No.2 E♭ major](analysis_chopin_op9_no2_nocturne.md) — PIG 023, 浪漫派 lyrical 範本；揭露 figural detection 對 fioritura 過濾需求 + elision 案例
- [Debussy Clair de Lune](analysis_debussy_clair_de_lune.md) — PIG 037, 印象派 ABA' + B 段 arpeggio wash；揭露 [[concept_texture_change_detection]] Phase 1 實作為下一輪優先

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
| ~~P0~~ | ~~實作 figural detection~~ | ✅ 完成 (Phase 1 落地、A/B 驗證 -0.1pp 中性) |
| ~~P0~~ | ~~實作 thumb reservation~~ | ✅ 完成 (Phase B 落地、penalty=5.0 → +1.2pp aggregate) |
| ~~P0~~ | ~~實作 cadence + subject detection~~ | ✅ 完成 (cadence d344183, subject 7971cfd) — Bach 端 cadence 0 fires (預期); Mozart/Chopin 待逐曲驗證 |
| ~~P1~~ | ~~`concept_phrase_elision`~~ | ✅ 完成 |
| ~~P1~~ | ~~`concept_texture_change_detection`~~ | ✅ 完成 |
| ~~P2~~ | ~~`concept_modulation_as_phrase_signal`~~ | ✅ 完成 |
| ~~P3~~ | ~~`composer_chopin_phrasing`~~ | ✅ 完成 |
| ~~P3~~ | ~~`composer_mozart_phrasing`~~ | ✅ 完成 |
| ~~P3~~ | ~~`composer_debussy_phrasing`~~ | ✅ 完成 |
| ~~P4~~ | ~~`composer_rachmaninoff_phrasing`~~ | ✅ 完成 |
| ~~P4~~ | ~~`concept_modal_scale_fingering`~~ | ✅ 完成 |
| ~~P5~~ | ~~二十世紀 / 現代~~ | ✅ 完成 |
| ~~P5~~ | ~~其他作曲家~~ | ✅ 完成 |
| ~~待寫~~ | ~~per-piece `analysis_*.md` 系列~~ | ✅ 已寫 4 個代表曲 (Bach Inv 4 / Mozart K283 / Chopin Op.9-2 / Debussy Clair de Lune)；其他依 debugging 需要逐一補 |
| **下輪** | `concept_texture_change_detection` Phase 1 落地（從 Clair de Lune 分析揭露為新 P0）| TODO |
| **下輪** | 對 Mozart/Beethoven/Chopin/Schubert 啟用 cadence flag 跑 A/B | TODO |
| **下輪** | Cost-based 紅線 (Cost(DP) ≤ Cost(PIG_min)) 取代 GMR 為 deployment 判準 | TODO |
| **下輪** | Per-piece thumb-reservation 啟用其他用戶教過 override 的 mvt | TODO |
