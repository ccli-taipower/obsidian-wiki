# Phrase Analysis Wiki 樂句分析 Wiki

樂句分段 (phrase segmentation) 是鋼琴指法系統的上游問題 — 樂句切錯，指法不可能對。本 wiki 與 [[../wiki_piano/index]] 並列，是獨立的學習與知識累積 track。

詳見 [[../score-claude/memory/feedback_phrase_analysis_is_its_own_discipline]]。

> **Project status / TODO / 實作進度** 不在本頁 — 見 [[_implementation_status]] 與 [[../score-claude/memory/project_phrase_detection_v1_phase1_phaseB]]。本 wiki 介面保留為知識內容，與 project tracking 分開（[[../score-claude/memory/feedback_wiki_knowledge_vs_project_separation]]）。

## 核心原則

- 樂句分析 = 獨立學科，與生物力學並列、不互相替代
- 不同作曲家 / 曲式有不同樂句邏輯，無法用 override 教
- 所有規則須有 wiki / 理論出處，禁止 magic 常數
- 工作流程：(1) 讀譜 → (2) 樂句切分（用此 wiki）→ (3) 指法（用 wiki_piano）

## PIG Dataset 風格涵蓋

| 時期 / 風格 | PIG 曲數 | 主要 wiki 頁面 |
|---|---|---|
| 巴洛克 (Bach + Scarlatti) | 23 | [[concept_fugue]] + [[concept_counterpoint]] |
| 古典 (Mozart) | 20 | [[concept_classical_period_sentence]] + [[composer_mozart_phrasing]] |
| 古典→浪漫過渡 (Beethoven) | 21 | [[composer_beethoven_phrasing]] |
| 早期浪漫 (Schubert) | 5 | [[composer_schubert_long_phrase]] |
| 浪漫 (Chopin + Schumann + Liszt + Brahms + Mendelssohn 等) | 49 | [[concept_chopin_lyrical_phrase]] + [[composer_chopin_phrasing]] |
| 浪漫民族樂派 (Grieg) | 10 | [[composer_grieg_lyric_pieces]] |
| 後期浪漫 (Rachmaninoff) | 4 | [[composer_rachmaninoff_phrasing]] |
| 印象 (Debussy + Ravel) | 12 | [[concept_impressionist_phrasing]] + [[composer_debussy_phrasing]] |
| 二十世紀 / 現代 (Scriabin + Bartok) | 3 | [[composer_twentieth_century]] |
| 其他 (Mussorgsky + Joplin + Faure + Satie 等) | 13 | [[composer_other_pig_pieces]] |

## Concepts (通用)

- [Fugue 賦格](concept_fugue.md) — 主題 / 答題 / 插曲 / 開展部 / Stretto；Bach Inventions 適用
- [Counterpoint 對位](concept_counterpoint.md) — 多聲部樂句獨立性；解釋兩手樂句邊界不對齊
- [Classical Period & Sentence](concept_classical_period_sentence.md) — 古典時期 4+4 period 與 2+2+4 sentence 結構；四種 cadence (PAC/IAC/HC/DC)
- [Chopin & 浪漫派抒情樂句](concept_chopin_lyrical_phrase.md) — 不規律長樂句 + 禁用 4-bar fallback；浪漫派 cadence 退化
- [Impressionist Phrasing](concept_impressionist_phrasing.md) — Debussy/Ravel texture-driven phrasing；cadence 失效
- [Phrase Elision](concept_phrase_elision.md) — 樂句重疊（一句結尾 = 下句開始）；「歸前」決定 + 對 motif/cadence detection 的影響；浪漫派頻繁
- [Modulation as Phrase Signal](concept_modulation_as_phrase_signal.md) — 第四類樂句邊界訊號（轉調）；key signature change 偵測 + filter tonicization；對 Schubert/Beethoven/Chopin 關鍵
- [Modal Scale Fingering](concept_modal_scale_fingering.md) — Modal / pentatonic / whole-tone / octatonic 對指法 + 樂句的影響；跨 wiki_piano + wiki_phrase

## Concepts (偵測工具)

- [Cadence Detection](concept_cadence_detection.md) — PAC/IAC/HC/DC 偵測演算法 (music21 RomanNumeral)
- [Subject Imitation Detection](concept_subject_imitation_detection.md) — fugue / Invention 主題重入聲偵測；正向 + 倒影 + 逆行 + 逆行倒影 + 時值變化
- [Figural Boundary Detection](concept_figural_boundary_detection.md) — 第三類樂句邊界（figure 切換）；處理 episode / coda 段
- [Running Passage Thumb Reservation](concept_running_passage_thumb_reservation.md) — phrase-start anchor cost rule；長階運行音起手避免最外側 finger 以保留 thumb
- [Texture Change Detection](concept_texture_change_detection.md) — 第五類樂句邊界訊號（紋理變化）：density / register / dynamic / pedal

## Composers (作曲家特化)

- [Mozart (per-form)](composer_mozart_phrasing.md) — sonata-allegro / slow mov / rondo；古典 period/sentence 純正範本
- [Beethoven](composer_beethoven_phrasing.md) — 對古典 period/sentence 的擴張與壓縮；按早 / 中 / 晚期細分
- [Schubert](composer_schubert_long_phrase.md) — Lied 旋律 + 遠系轉調作為樂句訊號
- [Chopin (per-genre)](composer_chopin_phrasing.md) — Nocturne / Etude / Ballade / Mazurka / Waltz / Prelude / Polonaise / Scherzo / Impromptu 各 genre
- [Grieg](composer_grieg_lyric_pieces.md) — Lyric Pieces 系列，規律結構 + modal 色彩
- [Rachmaninoff](composer_rachmaninoff_phrasing.md) — 後期浪漫長 melodic arch + 厚和聲 + 戲劇 climax + 大手前提
- [Debussy (per-collection)](composer_debussy_phrasing.md) — Suite Bergamasque / Préludes / Études / Images / Children's Corner
- [20th Century (Scriabin + Bartok)](composer_twentieth_century.md) — atonal/post-tonal phrase；mystic chord + modal/asymmetric meter
- [Other PIG composers](composer_other_pig_pieces.md) — Mussorgsky/Joplin/Faure/Satie/Dvorak/Albeniz/Scarlatti

## Analyses (per-piece)

- [Bach Invention 4 in D minor (BWV 775)](analysis_bach_inv_4_d_minor.md) — Subject identification + 三類樂句邊界互補必要性
- [Mozart K283 G major 1st mov](analysis_mozart_k283_first_mov.md) — Sonata-allegro 教科書範例；期望 cadence detection 表現
- [Chopin Nocturne Op.9 No.2 E♭ major](analysis_chopin_op9_no2_nocturne.md) — 浪漫派 lyrical 範本；fioritura 處理 + elision 案例
- [Debussy Clair de Lune](analysis_debussy_clair_de_lune.md) — 印象派 ABA' + texture-driven phrasing

## Sources

- [周怡秀《音樂中的復格形式》(大紀元 2005)](src_epochtimes_fugue_zhou_2005.md) — 中文百科文章，定義 fugue / 對位 / 模仿

## Raw (待擴增來源)

預計擴增來源：
- Caplin《Classical Form》
- Schoenberg《Fundamentals of Musical Composition》
- Rothstein《Phrase Rhythm in Tonal Music》
- Lerdahl-Jackendoff《A Generative Theory of Tonal Music》
- Fux《Gradus ad Parnassum》(英譯)
- Howat《Debussy in Proportion》
- Bach Inventions 演奏 / 教學註解
