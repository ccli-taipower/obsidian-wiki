# Phrase Analysis Wiki 樂句分析 Wiki

> Last updated: 2026-05-26 | Sources: 1 | Concepts: 2 | Analyses: 0 | Raw: 0

樂句分段 (phrase segmentation) 是鋼琴指法系統的上游問題 — 樂句切錯，指法不可能對。本 wiki 與 [[../wiki_piano/index]] 並列，是獨立的學習與知識累積 track。

詳見 [[../score-claude/memory/feedback_phrase_analysis_is_its_own_discipline]]。

## 核心原則

- 樂句分析 = 獨立學科，與生物力學並列、不互相替代
- 不同作曲家 / 曲式有不同樂句邏輯，無法用 override 教
- 所有規則須有 wiki / 理論出處，禁止 magic 常數
- 工作流程：(1) 讀譜 → (2) 樂句切分（用此 wiki）→ (3) 指法（用 wiki_piano）

## Concepts

- [Fugue 賦格](concept_fugue.md) — 結構、主題 / 答題 / 插曲 / 開展部，樂句邊界判斷規則草案；Bach Inventions 適用
- [Counterpoint 對位](concept_counterpoint.md) — 多聲部樂句獨立性；解釋 per-hand `_detect_phrase_starts` 兩手邊界不對齊是常態

## Analyses (per-piece / per-composer)

_尚無。第一個目標：`analysis_bach_inv_4_d_minor.md` (mvt4 m50 case study)_

## Sources

- [周怡秀《音樂中的復格形式》(大紀元 2005)](src_epochtimes_fugue_zhou_2005.md) — 中文百科文章，定義 fugue / 對位 / 模仿 / Bach 復格藝術

## Raw (待擴增)

- 預計來源：Caplin 《Classical Form》、Schoenberg 《Fundamentals of Musical Composition》、Lerdahl-Jackendoff GTTM、Fux Gradus ad Parnassum (英譯)、Bach Inventions 演奏 / 教學註解

## 路線圖

| 優先序 | 項目 | 狀態 |
|---|---|---|
| P0 | `analysis_bach_inv_4_d_minor` — 把 mvt4 m50 case 寫成可驗證的單元 | TODO |
| P1 | `concept_subject_imitation_detection` — 主題重入聲偵測演算法 | TODO |
| P2 | `concept_cadence_detection` — 終止式偵測 | TODO |
| P3 | 其他 Bach Invention mvt 樂句結構分析 | TODO |
| P4 | 浪漫主義樂句 (Chopin, Schumann) | TODO |
| P5 | 古典時期樂句 (Mozart, Haydn antecedent-consequent) | TODO |
