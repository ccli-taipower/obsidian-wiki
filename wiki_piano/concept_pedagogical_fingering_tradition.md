---
concept: 教學傳統指法 (Pedagogical Fingering Tradition)
date_created: 2026-06-05
tags: [piano_fingering, pedagogy, method_books, exam_boards, intermediate, convention]
---

# 教學傳統指法 (Pedagogical Fingering Tradition)

為「**學習**」而非「**演奏**」設計的指法。它優先考慮的不是某次演出的詮釋效果，而是：**可轉移的習慣、模式一致性、手位經濟、發展中的手**。對本專案特別重要——因為目標是**初中階曲目**（見 `project_target_repertoire_intermediate`），而初中階曲目真正的「慣例」就是**教學傳統**，不是演奏家的個人詮釋。

## 教學指法 vs 演奏指法

| | 教學傳統指法 | 演奏家指法 |
|---|---|---|
| 目的 | 建立可靠、可轉移的技術習慣 | 服務特定詮釋 / 音色 / 個人手 |
| 偏好 | 標準模式、一致性、強指在重點 | 視效果可打破慣例 |
| 對象 | 發展中的手（常較小、獨立性未成熟）| 成熟演奏家 |
| 本專案 | **目標曲目的對應慣例（hypothesis bank）** | 明確排除（advanced 不在範圍）|

> ⚠️ 教學傳統指法是 **hypothesis bank**（四源架構中的 Wiki 角色），不是 ground truth。提案必須通過 **user override 驗證**，且會與**個人生物力學**（手大小、span 表）衝突——不可盲目套用。

## 主要傳統來源

- **技術 / 方法書**：Hanon（純機械、五指獨立）、Czerny（速度與音群 pattern）、Burgmüller（音樂性小品 Op.100）、Beyer、以及現代方法（Alfred / Faber / Bastien）。這些書把指法當作**反覆操練的 pattern**，pattern 一致性是核心。
- **考級體系**：ABRSM、Trinity、RCM（皇家音樂學院）——它們出版**附指法的考級曲目**，這些指法是分級曲目的**事實標準（de-facto standard）**。
- **Urtext + 編訂指法**：Henle、Wiener Urtext 的編者指法，介於學術與教學之間。

## 核心教學原則（最能餵 DP 的部分）

1. **五指手位（five-finger position）為家** — 手以一個 5 音位置為基準，盡量減少移位。對應 `[[concept_hand_position_stability]]` + DP 的 phrase anchor。
2. **標準音階 / 琶音指法** — thumb-under、以 3-4 分組。詳 `[[concept_standard_scale_arpeggio_fingering]]`，對應 DP 的 `[[concept_long_scale_thumb_under]]`。
3. **模式一致性（pattern consistency）** — **同音型 → 同指法**，這樣肌肉記憶才能形成。⭐ **這正是本專案的 HARD 原則「同音型同指法」的教學論證來源**（biomech + learning + muscle memory）。
4. **手位經濟** — 盡量少換位；能在一個手位完成的不要硬移。
5. **強指落重點** — 強拍 / 旋律重點音避免用 f4 / f5 等弱指（與 articulation 的 marked-finger 規則呼應）。
6. **預備而非反應（prepare, don't react）** — 指法須提前安排好下一步，不是走到才決定。對應 DP 的 look-ahead transition cost。

## 與 DP 的對應

| 教學原則 | DP 環節 |
|---|---|
| 標準音階 thumb-under | `USE_LONG_SCALE_THUMB_UNDER` / `[[concept_long_scale_thumb_under]]` |
| 五指手位 / 手位經濟 | phrase anchor (`W_PHRASE_ANCHOR`) / `[[concept_hand_position_stability]]` |
| 模式一致性 | 同音型同指法（HARD；DP motif 機制，目前 override 為主）|
| 強指落重點 | register / agility 項 + articulation marked-finger |
| 手大小自適應 | `HAND_SIZE` + `[[concept_finger_span_table]]` |

## 待補頁面（此 track 起頭，後續擴充）

- `concept_standard_scale_arpeggio_fingering`（已建）— 標準音階 / 琶音指法
- （未來）考級指法慣例（ABRSM / Trinity 分級曲目的編訂邏輯）
- （未來）Burgmüller / Czerny 練習曲的 finger-pattern 教學邏輯
- （未來）發展中的手：手大小、跨度限制與初學者指法簡化
