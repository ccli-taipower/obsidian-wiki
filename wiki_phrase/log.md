# Phrase Analysis Wiki Log

> Pure ingest log — 記錄每次新增 / 修改 wiki 內容。
> Project status / implementation 進度不在此 — 見 [[_implementation_status]]。

## [2026-05-26] init — fugue / counterpoint seed

新建 wiki_phrase/ 作為樂句分段獨立 discipline (parallel to wiki_piano/)。

Pages created:
- `index.md`
- `src_epochtimes_fugue_zhou_2005.md` — source: 周怡秀《音樂中的復格形式》大紀元 2005
- `concept_fugue.md` — fugue 結構、樂句邊界判斷規則、Bach Invention 適用性
- `concept_counterpoint.md` — 多聲部樂句獨立性、per-hand DP 為何正確、voice separation 隱藏問題

## [2026-05-26] PIG-driven era/composer expansion — 6 pages

按 PIG 150 曲的時期 / 作曲家覆蓋優先序新增頁面。

Pages created:
- `concept_classical_period_sentence.md` — 古典 period (4+4) / sentence (2+2+4) / cadence (PAC/IAC/HC/DC)
- `concept_chopin_lyrical_phrase.md` — 浪漫派不規律長樂句、禁用 4-bar fallback、texture / pattern 訊號
- `composer_beethoven_phrasing.md` — phrase expansion / compression / hemiola / tempo 切換；按早 / 中 / 晚期細分
- `concept_impressionist_phrasing.md` — Debussy/Ravel texture-driven、cadence 失效、modal scales
- `composer_schubert_long_phrase.md` — Lied 旋律 + 遠系轉調訊號
- `composer_grieg_lyric_pieces.md` — Lyric Pieces 規律結構 + modal + drone bass

## [2026-05-26] tool pages + first analysis

Pages created:
- `concept_cadence_detection.md` — 4 種 cadence (PAC/IAC/HC/DC) 偵測演算法、music21 實作範例
- `concept_subject_imitation_detection.md` — fugue/Invention 主題重入聲偵測，含 4 種模仿變體 + 時值變化 + voice separation 前置考量
- `analysis_bach_inv_4_d_minor.md` — Bach Invention 4 (BWV 775) subject identification + 三類樂句邊界分析

## [2026-05-26] figural boundary concept (3rd class)

Pages created:
- `concept_figural_boundary_detection.md` — Figure 操作型定義 + 4 種 figural boundary 事件類型 + 完整偵測演算法 + closure 音歸屬問題 + 與 subject/cadence detection 整合

## [2026-05-26] running passage thumb reservation

Pages created:
- `concept_running_passage_thumb_reservation.md` — phrase-start anchor cost rule；長階運行音起手避免「最外側 finger」以保留 thumb 給 thumb-under；橋接 wiki_phrase 與 wiki_piano

## [2026-05-26] roadmap batch — composer细分 + 2 concepts

Pages created:
- `composer_chopin_phrasing.md` — Chopin 按 genre 細分 (Nocturne/Etude/Ballade/Mazurka/Waltz/Prelude/Polonaise/Scherzo/Impromptu)
- `composer_mozart_phrasing.md` — sonata-allegro 段落結構詳解；古典 period/sentence 純正範本；vs Beethoven 對比
- `composer_debussy_phrasing.md` — Debussy 按 collection 細分 (Bergamasque/Préludes/Études/Images/Children's Corner) + Whole-tone/Pentatonic/Octatonic 對指法的影響 + Pedal 重要性
- `concept_phrase_elision.md` — 樂句重疊問題；「歸前」決定 + 對 motif/cadence detection 的影響
- `concept_modulation_as_phrase_signal.md` — 第四類樂句邊界訊號（轉調）；music21 key signature change 偵測 + filter tonicization

## [2026-05-26] roadmap completion batch — PIG 100% coverage

Pages created:
- `concept_texture_change_detection.md` — 第五類樂句邊界訊號（紋理變化）：density/register/dynamic/pedal
- `concept_modal_scale_fingering.md` — Modal/pentatonic/whole-tone/octatonic 對指法 + cadence detection 的影響
- `composer_rachmaninoff_phrasing.md` — 後期浪漫長 melodic arch + 厚和聲 + 戲劇 climax + 大手前提
- `composer_twentieth_century.md` — Scriabin + Bartok 合一頁
- `composer_other_pig_pieces.md` — Mussorgsky/Joplin/Faure/Satie/Dvorak/Albeniz/Scarlatti 合一頁

## [2026-05-26] per-piece analyses

Pages created:
- `analysis_mozart_k283_first_mov.md` — Mozart Piano Sonata K283 G major 1st mov; sonata-allegro 結構分析
- `analysis_chopin_op9_no2_nocturne.md` — Chopin Nocturne Op.9 No.2 E♭ major; 浪漫派 lyrical + LH waltz pattern + fioritura + elision
- `analysis_debussy_clair_de_lune.md` — Debussy Clair de Lune (Suite Bergamasque No.3); 印象派 ABA' 結構 + B 段 arpeggio wash

## [2026-05-26] knowledge/project separation refactor

依 [[../score-claude/memory/feedback_wiki_knowledge_vs_project_separation]] 原則重構：
- 所有 concept/composer/analysis page 移除「變更日誌」「Phase 1 完成」「實測修正/延伸」「待執行驗證」等 project 性質段落，保留純知識
- 新增 `_implementation_status.md` 吸收 implementation 進度、A/B 結果、commit refs、TODO 等
- `index.md` 移除「路線圖」table；保留純索引 / TOC / PIG 風格涵蓋表
- `log.md` (本檔) 重構為 pure ingest log；project status 移到 `_implementation_status.md`

## [2026-05-28] sources batch — 7 src pages 全填

清空 index.md 的「Raw (待擴增來源)」清單，全 7 個 source ingest 完成。每頁依 `src_epochtimes_fugue_zhou_2005.md` 模板：一句話總結 → 重點概念 → 歷史 → 文章未涵蓋 → 對指法系統的啟示。

Pages created (7):
- `src_caplin_classical_form.md` (136 行) — Caplin 1998，cadence taxonomy / sentence-period / hybrid theme types；PAC+IAC scope 哲學源頭
- `src_schoenberg_fundamentals.md` (97 行) — Schoenberg 1967，sentence (Satz) / Grundgestalt / liquidation 原型定義
- `src_rothstein_phrase_rhythm.md` (156 行) ⚠ — Rothstein 1989，hypermeter / phrase expansion-contraction / elision / imbroglio；4-bar fallback 與 PHRASE_SEAM_TC_SCALE 依據
- `src_lerdahl_jackendoff_gttm.md` (149 行) — GTTM 1983，Grouping Preference Rules (GPR 1-7) 對應 `_detect_phrase_starts` Pass 1/2；preference-rule framework 啟發本系統 cost-based DP 架構
- `src_fux_gradus_ad_parnassum.md` (91 行) — Fux 1725 (Mann 英譯)，五種對位法 / cantus firmus / suspension / clausula vera；Bach Inv 對位邏輯祖先
- `src_howat_debussy_in_proportion.md` (70 行) ⚠ — Howat 1983，Golden Section / Fibonacci proportion in Debussy；texture phase 結構分割支援
- `src_bach_inventions_pedagogy.md` (172 行) ⚠ — Czerny / Bischoff / Landowska / Schiff / Donington / Henle / Wiener Urtext / Bärenreiter 跨傳統教學註解 + Inv 1/4/8 phrase boundary 分歧記錄

⚠ marked pages = training-data 推測為主，需後續 raw 來源 ingest 驗證；每頁有 ⚠ Training-data verification needed section 列待驗證 claim（共 26 items across 3 pages）。

Total 871 行 wiki 知識內容新增。
