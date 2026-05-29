# Phrase Analysis Wiki 樂句分析 Wiki

樂句分段 (phrase segmentation) 是鋼琴指法系統的上游問題 — 樂句切錯，指法不可能對。本 wiki 與 [../wiki_piano/index](../wiki_piano/index.md)（生物力學 + 指法物理）+ [../wiki_articulation/index](../wiki_articulation/index.md)（連結 / 斷奏 / 觸鍵詮釋）並列，是三條獨立 wiki track。

詳見 *feedback_phrase_analysis_is_its_own_discipline*。

> **Project status / TODO / 實作進度** 不在本頁 — 見 [_implementation_status](_implementation_status.md) 與 *project_phrase_detection_v1_phase1_phaseB*。本 wiki 介面保留為知識內容，與 project tracking 分開（*feedback_wiki_knowledge_vs_project_separation*）。

## 核心原則

- 樂句分析 = 獨立學科，與生物力學並列、不互相替代
- 不同作曲家 / 曲式有不同樂句邏輯，無法用 override 教
- 所有規則須有 wiki / 理論出處，禁止 magic 常數
- 工作流程：(1) 讀譜 → (2) 樂句切分（用此 wiki）→ (3) 指法（用 wiki_piano）

## PIG Dataset 風格涵蓋

| 時期 / 風格 | PIG 曲數 | 主要 wiki 頁面 |
|---|---|---|
| 巴洛克 (Bach + Scarlatti) | 23 | [concept_fugue](concept_fugue.md) + [concept_counterpoint](concept_counterpoint.md) |
| 古典 (Mozart) | 20 | [concept_classical_period_sentence](concept_classical_period_sentence.md) + [composer_mozart_phrasing](composer_mozart_phrasing.md) |
| 古典→浪漫過渡 (Beethoven) | 21 | [composer_beethoven_phrasing](composer_beethoven_phrasing.md) |
| 早期浪漫 (Schubert) | 5 | [composer_schubert_long_phrase](composer_schubert_long_phrase.md) |
| 浪漫 (Chopin + Schumann + Liszt + Brahms + Mendelssohn 等) | 49 | [concept_chopin_lyrical_phrase](concept_chopin_lyrical_phrase.md) + [composer_chopin_phrasing](composer_chopin_phrasing.md) |
| 浪漫民族樂派 (Grieg) | 10 | [composer_grieg_lyric_pieces](composer_grieg_lyric_pieces.md) |
| 後期浪漫 (Rachmaninoff) | 4 | [composer_rachmaninoff_phrasing](composer_rachmaninoff_phrasing.md) |
| 印象 (Debussy + Ravel) | 12 | [concept_impressionist_phrasing](concept_impressionist_phrasing.md) + [composer_debussy_phrasing](composer_debussy_phrasing.md) |
| 二十世紀 / 現代 (Scriabin + Bartok) | 3 | [composer_twentieth_century](composer_twentieth_century.md) |
| 其他 (Mussorgsky + Joplin + Faure + Satie 等) | 13 | [composer_other_pig_pieces](composer_other_pig_pieces.md) |

## Concepts (通用)

- [Fugue 賦格](concept_fugue.md) — 主題 / 答題 / 插曲 / 開展部 / Stretto；Bach Inventions 適用
- [Counterpoint 對位](concept_counterpoint.md) — 多聲部樂句獨立性；解釋兩手樂句邊界不對齊
- [Classical Period & Sentence](concept_classical_period_sentence.md) — 古典時期 4+4 period 與 2+2+4 sentence 結構；四種 cadence (PAC/IAC/HC/DC)
- [Chopin & 浪漫派抒情樂句](concept_chopin_lyrical_phrase.md) — 不規律長樂句 + 禁用 4-bar fallback；浪漫派 cadence 退化
- [Impressionist Phrasing](concept_impressionist_phrasing.md) — Debussy/Ravel texture-driven phrasing；cadence 失效
- [Phrase Elision](concept_phrase_elision.md) — 樂句重疊（一句結尾 = 下句開始）；「歸前」決定 + 對 motif/cadence detection 的影響；浪漫派頻繁
- [Modulation as Phrase Signal](concept_modulation_as_phrase_signal.md) — 第四類樂句邊界訊號（轉調）；key signature change 偵測 + filter tonicization；對 Schubert/Beethoven/Chopin 關鍵
- [Modal Scale Fingering](concept_modal_scale_fingering.md) — Modal / pentatonic / whole-tone / octatonic 對指法 + 樂句的影響；跨 wiki_piano + wiki_phrase
- [Baroque Phrasing](concept_baroque_phrasing.md) — 巴洛克樂句邏輯 (Fortspinnung / 對位 / dance form) + 與 Classical 對比
- [Hypermeter 大週期感](concept_hypermeter.md) — 4-bar / 8-bar hypermeter unit 與 phrase 對應；Rothstein 1989 phrase expansion/contraction
- [Grouping Preference Rules (GPR)](concept_grouping_preference_rules.md) — Lerdahl-Jackendoff GTTM 七條 grouping rules + score-claude DP 對應
- [Anacrusis / Pickup](concept_anacrusis_pickup.md) — 弱起 / 起頭弱拍處理 + 偵測啟發式 + chain anacrusis
- [Phrase Anchor 樂句手位錨點](concept_phrase_anchor.md) — score-claude DP 操作型概念 (`_implied_anchor` + W_PHRASE_ANCHOR cost rule)

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
- [J.S. Bach](composer_bach_phrasing.md) — 對位作品樂句邏輯 + 12/15 mvts BACH_INV_PHRASE_FLAGS 啟用對應 + WTC / Sinfonias / Suites 結構
- [Haydn](composer_haydn_phrasing.md) — Classical 形式奠基者 + Sentence/Period + surprise 不規則
- [Schumann](composer_schumann_phrasing.md) — 文學詩意樂句 + character piece 集合 + inner voice melody
- [Brahms](composer_brahms_phrasing.md) — 不規則 hypermeter + phrase elision 大量使用 + 對位 + homophonic 混合
- [Scarlatti](composer_scarlatti_phrasing.md) — Iberian Baroque + binary form + 不規則 phrase + hand-crossing

## Analyses (per-piece)

Bach *Two-Part Inventions* (BWV 772-786):
- [Bach Invention 1 in C major (BWV 772)](analysis_bach_inv_1_c_major.md) — Exposition + modulation 邊界 + m21-22 coda case study; subject 長度 1-bar/2-bar 派爭議
- [Bach Invention 2 in C minor (BWV 773)](analysis_bach_inv_2_c_minor.md) — Canon-like imitation + chromatic descent; per-hand phrase split 張力
- [Bach Invention 3 in D major (BWV 774)](analysis_bach_inv_3_d_major.md) — 3/8 拍 hypermeter + ascending leap subject; Pass 2 fallback 不適用
- [Bach Invention 4 in D minor (BWV 775)](analysis_bach_inv_4_d_minor.md) — Subject identification + 三類樂句邊界互補必要性
- [Bach Invention 5 in E♭ major (BWV 776)](analysis_bach_inv_5_eb_major.md) — 3 flats 黑鍵指法 + lyrical descending scale → long-scale thumb-under candidate
- [Bach Invention 6 in E major (BWV 777)](analysis_bach_inv_6_e_major.md) — Strict canon at the octave + suspension chain; subject 概念崩解 case
- [Bach Invention 7 in E minor (BWV 778)](analysis_bach_inv_7_e_minor.md) — Chromatic descent + leading-rest entries; chromatic≠modulation disambiguation
- [Bach Invention 8 in F major (BWV 779)](analysis_bach_inv_8_f_major.md) — Broken-triad subject + 3/4 cross-bar motif + LH clef-change phrase 獨立性
- [Mozart K283 G major 1st mov](analysis_mozart_k283_first_mov.md) — Sonata-allegro 教科書範例；期望 cadence detection 表現
- [Chopin Nocturne Op.9 No.2 E♭ major](analysis_chopin_op9_no2_nocturne.md) — 浪漫派 lyrical 範本；fioritura 處理 + elision 案例
- [Debussy Clair de Lune](analysis_debussy_clair_de_lune.md) — 印象派 ABA' + texture-driven phrasing

## Sources

理論 / 分析學 (modern):
- [Caplin《Classical Form》(1998)](src_caplin_classical_form.md) — formal functions / sentence-period / cadence taxonomy；本系統 cadence detector 的 PAC+IAC scope 哲學源頭
- [Schoenberg《Fundamentals of Musical Composition》(1967)](src_schoenberg_fundamentals.md) — sentence (Satz) / period / liquidation / Grundgestalt 原型定義
- [Rothstein《Phrase Rhythm in Tonal Music》(1989)](src_rothstein_phrase_rhythm.md) ⚠ — hypermeter / phrase expansion-contraction / elision；4-bar fallback 與 PHRASE_SEAM_TC_SCALE 的依據
- [Lerdahl & Jackendoff《GTTM》(1983)](src_lerdahl_jackendoff_gttm.md) — Grouping Preference Rules / hypermeter / preference-rule framework；本系統 cost-based DP 架構的祖先

歷史 / 對位法:
- [Fux《Gradus ad Parnassum》(1725)](src_fux_gradus_ad_parnassum.md) — 五種對位法 / cantus firmus / suspension；Bach Inventions 對位邏輯的源頭
- [周怡秀《音樂中的復格形式》(大紀元 2005)](src_epochtimes_fugue_zhou_2005.md) — 中文百科文章，定義 fugue / 對位 / 模仿

作曲家 / 曲目特化:
- [Howat《Debussy in Proportion》(1983)](src_howat_debussy_in_proportion.md) ⚠ — Golden Section / Fibonacci proportion in Debussy；texture-driven phrase 結構分割理論
- [Bach Inventions Pedagogy Survey](src_bach_inventions_pedagogy.md) ⚠ — Czerny / Bischoff / Landowska / Schiff / Donington / modern Urtext 跨傳統教學註解

⚠ = training-data 推測為主，書本未直接 ingest，需後續 raw 來源比對。
