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
