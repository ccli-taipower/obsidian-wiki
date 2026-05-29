# Articulation Wiki Log

> Pure ingest log — 記錄每次新增 / 修改 wiki 內容。
> Project status / implementation 進度不在此 — 見 [[_implementation_status]]。

## [2026-05-29] full wiki completion — 7 src + 4 analysis 頁

依用戶要求「不要管有沒有用到，把這個 wiki 補齊」，把 `_implementation_status.md` 列的 7 個 source ingest queue + 4 個 analysis page queue 全部寫完。內容以 training-data 為基礎，每頁末尾標明 ⚠ verification queue 列出需要 cross-check 原書的具體引述。

Pages created (11 new):

**Source 頁 (7)** — 鋼琴 articulation pedagogy 文獻參考庫：
- `src_neuhaus_art_of_piano.md` (~110 行) — 俄羅斯派重量觸鍵理論
- `src_matthay_visible_inaudible.md` (~100 行) — 英國派觸鍵物理分析
- `src_czerny_op500_articulation.md` (~110 行) — 19 世紀教學集大成 (Beethoven 學生 / Liszt 老師)
- `src_kullak_aesthetics_pianoforte.md` (~95 行) — 19 世紀美學哲學論述
- `src_brendel_essays.md` (~115 行) — Beethoven articulation 字面派詮釋
- `src_turk_klavierschule.md` (~115 行) — 18 世紀末一手文獻 (Baroque/Classical 過渡)
- `src_donington_baroque_music.md` (~120 行) — 20 世紀 HIP 運動學者性回顧

**Analysis 頁 (4)** — per-piece articulation 詮釋分析：
- `analysis_bach_inv_articulation.md` (~120 行) — Bach Two-Part Inventions，Baroque non-legato default + 例外 legato 段 + edition 比較
- `analysis_beethoven_op49_articulation.md` (~95 行) — Op.49 No.1 / No.2，intermediate 目標主力 + Classical 平衡典型
- `analysis_mozart_k545_articulation.md` (~120 行) — K545 (Sonata facile)，Classical 平衡 + 演奏家詮釋差異 + Audiveris OMR 訊號限制
- `analysis_chopin_op9_no2_articulation.md` (~145 行) — Op.9 No.2，Romantic legato + 整合 score-claude 已啟用 rules 的綜合案例

Pages updated (3):
- `index.md` — 加入 Source 頁 + Analysis 頁兩個新章節，移除「主要文獻基礎」舊清單（移至 src_* 頁索引）
- `_implementation_status.md` — Source ingest queue 從「待 ingest」改為「已 ingest 狀態表」+ Analysis 頁同樣改為「已寫狀態表」
- `log.md` (本檔) — 加 [2026-05-29] full completion entry

每個新頁面結構：
1. 來源 / 引用方
2. 作者背景 / 曲目背景
3. 核心主張 / 觀察
4. 對 score-claude DP 的對應（cost rule mapping）
5. 與其他 wiki 頁面的關係
6. ⚠ Training-data verification queue

Wiki size: 11 → 22 pages, ~816 → ~2100 行純知識內容。

## [2026-05-29] revision — 知識頁清理 + 補齊 6 個 concept 頁

把原本 index / overview / legato_substitution 三頁混雜的 spec / todo / 實作狀態移到新建 `_implementation_status.md`（per wiki_phrase 慣例：底線開頭 meta 頁）。

Pages revised:
- `index.md` — 改純 TOC，移除 "Open questions"、"src 待 ingest"、"analysis 待寫" 等 roadmap 內容
- `concept_articulation_overview.md` — 移除 §7 "對既有 cost rule 的 retrofit 影響評估"、§8 "未解 questions / 待 ingest" 等 meta 段；§4 cost-rule mapping 簡化為「主要影響 + 詳細頁連結」
- `concept_legato_substitution.md` — 移除 §3.2 DP 修改提案、§4 預期 cost 改變、§7 A/B 驗證計畫 等 spec/未跑 內容；保留純知識（rationale / sources / 操作型定義 / 適用情境 / 失效情境）

Pages created (6 new concept):
- `concept_staccato.md` (90 行) — 斷奏 / staccatissimo / mezzo-staccato spectrum，對 hand jump / thumb cross / substitution / 同指連續 的反向約束
- `concept_tenuto.md` (78 行) — 持音的「禁止換指」+ 強指偏好（1/2/3）+ 與其他 articulation 疊加處理
- `concept_accent_marcato.md` (87 行) — accent (`>`) / marcato (`^`) / sforzando (`sfz`) 三符號區別，強指偏好物理基礎，與 dynamic 標記的區別
- `concept_portato_mezzo_staccato.md` (76 行) — 半連半斷中間值，為何指法保守選 legato 端
- `concept_non_legato_baroque.md` (95 行) — Baroque 默認 articulation 的歷史依據（C.P.E. Bach / Türk / Couperin），對指法策略的意涵，例外情境（chantant 段）
- `concept_period_defaults.md` (108 行) — 四時代 default 對應表（Baroque / Classical / Romantic / Modernism），編輯者 articulation 與時代 default 的衝突，對指法系統的實作意涵

Pages created (1 new meta):
- `_implementation_status.md` (75 行) — DP 落地狀態表 + source ingest queue + analysis 頁 queue + open design questions + v3 candidates

Total: 3 revised + 7 new pages = 10 active pages（之前 3 → 現在 10），約 700 行純知識內容。

對應 [[../score-claude/memory/feedback_wiki_knowledge_vs_project_separation]] 原則：concept 頁全為純音樂知識，無「spec'd」/「待實作」/「待 ingest」/「A/B 預期」雜訊。

## [2026-05-29] init — articulation track seed

新建 wiki_articulation/ 作為第三條獨立 discipline（parallel to wiki_piano + wiki_phrase）。

初版 pages:
- `index.md`、`log.md`、`concept_articulation_overview.md`、`concept_legato_substitution.md`

詳細 init 內容見 obsidian-wiki commit `9984996`。
