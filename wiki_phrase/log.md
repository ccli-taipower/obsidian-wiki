# Phrase Analysis Wiki Log

> Pure ingest log — 記錄每次新增 / 修改 wiki 內容。
> Project status / implementation 進度不在此 — 見 [_implementation_status](_implementation_status.md)。

## [2026-05-29] gap fill — 5 composer + 5 concept 頁

依用戶要求補齊 wiki_phrase gap。原 wiki 缺少 Bach 作為 composer-level 主題頁 (對位主要測試對象但無專頁) + Brahms/Schumann/Haydn/Scarlatti 等 intermediate 範圍作曲家；亦缺 hypermeter / Baroque phrasing / GPR / anacrusis / phrase anchor 等基礎 phrase 理論概念。

Composer pages added (5):
- `composer_bach_phrasing.md` — J.S. Bach 對位作品樂句邏輯 + 12/15 mvts BACH_INV_PHRASE_FLAGS 啟用對應 + WTC / Sinfonias / Suites
- `composer_brahms_phrasing.md` — 不規則 hypermeter + phrase elision 大量使用 + 對位 + homophonic 混合
- `composer_schumann_phrasing.md` — 文學詩意樂句 + character piece 集合 + inner voice melody
- `composer_haydn_phrasing.md` — Classical 形式奠基者 + Sentence/Period + surprise 不規則
- `composer_scarlatti_phrasing.md` — Iberian Baroque + binary form + 不規則 phrase + hand-crossing

Concept pages added (5):
- `concept_baroque_phrasing.md` — 巴洛克樂句邏輯整體論 (Fortspinnung / 對位 / dance form / cadence types)
- `concept_hypermeter.md` — 4-bar / 8-bar hypermeter unit 與 phrase 對應；Rothstein 1989 phrase expansion/contraction
- `concept_grouping_preference_rules.md` — Lerdahl-Jackendoff GTTM 七條 grouping rules + score-claude DP 對應 (約 70%)
- `concept_anacrusis_pickup.md` — 弱起 / 起頭弱拍處理 + 偵測啟發式 + chain anacrusis
- `concept_phrase_anchor.md` — score-claude DP 操作型概念 (`_implied_anchor` + W_PHRASE_ANCHOR cost rule)

Pages updated:
- `index.md` — 標題說明加 wiki_articulation 連結；Concepts (通用) 加 5 頁；Composers 加 5 頁
- `log.md` (本檔) — 加 2026-05-29 gap fill entry

每頁底部有 ⚠ Training-data verification queue 列出需 cross-check 的引述 (per wiki_articulation 慣例)。

Wiki size: 45 → 55 active pages, +1000 行純知識內容。

## [2026-05-29] revision — Bach Inv 7 (BWV 778) 啟用 subject_tol=0.7 (chromatic 校正)

infrastructure 落地後 (score-claude `42c9f5e` per-piece `SUBJECT_MATCH_TOLERANCE` override)，跑 Inv 7 enablement A/B + split-test：

- `tmp/diag_subject_tol_inv7.py`: tol 0.8→0.7 把 RH 0 entries 解到 4 entries (m3/m11/m11/m12, 命中 wiki §7 預測 m11-14)
- `tmp/diag_inv7_enablement.py`: figural+thumb+subject@0.7 combined: RH -13.82 ✓, LH +0.34 ⚠
- `tmp/diag_inv7_split.py`: isolated 出 `USE_THUMB_RESERVATION` 是 LH 唯一 breach 軸 (+4.57); subject@0.7 本身 SAFE (-6.22 RH / -0.50 LH)

最終啟用：`BACH_INV_PHRASE_FLAGS[7] = {figural: True, thumb: False, subject: True, subject_tol: 0.7}`。Production cost: **RH -22.68 / LH -7.05, 0 breach**。

Pages revised (1):
- `analysis_bach_inv_7_e_minor.md` §「三類樂句邊界」表 Subject entry row — 移除 ⚠ chromatic tolerance 待校準警示，加入實測啟用結果

## [2026-05-29] revision — Chopin Op.9 No.2 §7 fioritura 全曲算法實測

取得 musetrainer/library Op.9 No.2 全曲 MXL (m0-m37) 跑 `_detect_fioritura_ranges`，校正 wiki §7 原本以 B0-12 excerpt 推斷的 canonical case 位置。

Pages revised (1):
- `analysis_chopin_op9_no2_nocturne.md` §7 — 原 "bar 16 周邊 + bar 24 + Coda" 改為精確 "m13-14 (var1) + m21-22 (var1 重現) + m24 (var2) + m33-35 (Coda)"；新增 §7.1 算法實測 (11 RH ranges, 0 LH) + §7.2 校正記錄

關鍵發現：
- Wiki 原本說 "bar 16 周邊" 不準確 — var 1 fioritura 實在 m13-14；m16 是 var 1 結束後
- bar 24 ✓ + Coda m33-35 ✓ 兩個 canonical case 算法精準命中
- 演算法另抓到 m4 / m5-6 / m26 / m29 等 wiki §7 原本未列舉的 ornamental fioritura
- LH 0 範圍符合設計 (waltz triplets duration ≥ 0.25 QN → 自然 break runs)
- USE_FIORITURA_FILTER ON 將過濾 9 處 RH figural boundaries (m4 / m6 / m13 / m14 / m21 / m22 / m24×2 / m35)

Diag: `tmp/diag_fioritura_op9_no2_full.py`

## [2026-05-29] revision — 7 Bach Inv analyses: fix m3 LH 預測誤述 + Inv 6 over-fire 預測推翻

Validation 結果（見 *project_bach_inv_subject_detection_validation_2026-05-28*）顯示原始 wiki musicology 預測與 `_detect_subject_entries` 演算法輸出在 7 頁有差距。本次修訂統一在 §「三類樂句邊界並用」表的 Subject entry row 加入演算法實測 entries，並澄清 m3 LH 在演算法 template 內、永不為 detected entry。

Pages revised (7):
- `analysis_bach_inv_1_c_major.md` §7 row — 加入 RH @ m6/m12/m18/m19, LH @ m4/m6/m7
- `analysis_bach_inv_2_c_minor.md` §7 row — 三 mvts 並列改用 Template + 實測 entries 格式
- `analysis_bach_inv_3_d_major.md` §7 row — 加入 RH @ m18/m28/m32/m34/m50/m55, LH @ m12/m30/m40/m44/m53
- `analysis_bach_inv_5_eb_major.md` §7 row — 加入 RH @ m23/m27, LH @ len=8 全 miss (tolerance 標記)
- `analysis_bach_inv_6_e_major.md` 4 處 — 推翻 over-fire 二分預測：實測為 sparse-but-misaligned (RH 3 + LH 2 entries 集中 m25-m48 中段)；§3.1 表加 third failure mode column，§5.1 / §7 row 同步更新
- `analysis_bach_inv_7_e_minor.md` §7 row — 加入 RH @ len=8 全 miss, LH @ m3 (chromatic tolerance 標記)
- `analysis_bach_inv_8_f_major.md` §7 row — 加入 RH @ m13, LH @ m12 (musicology 預測多數 miss)

Inv 4 是唯一不需修訂的頁（validation 顯示 alg 輸出與該頁 §3.1 既有 6/8/12 sweep + alg-test 結果完全一致）。

關鍵概念校正：musicology 上的「主題答句 m3 LH」≠ 演算法上的 detected entry。`_detect_subject_entries` 從 first 8 real groups 建 template、scan_start 在 template 之後 — m3 LH 多落在 template 內，因此即使是「subject answer」也不會出現在 alg output。後續 analysis 頁應先跑 alg 再寫預測。

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

依 *feedback_wiki_knowledge_vs_project_separation* 原則重構：
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
