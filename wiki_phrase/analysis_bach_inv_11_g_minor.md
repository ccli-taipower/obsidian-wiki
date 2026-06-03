---
tags:
  - analysis
  - bach
  - invention
  - phrase
---

# Analysis: Bach Invention 11 in G minor (BWV 782) — Figural-Dominated 與 Subject 偵測到卻不啟用

> 來源：musicology 文獻 + **cached MXL 實跑偵測**（`mvt11.mxl`，2026-06-03 grounding）
> 對應 program：mvt11；出貨設定 **`figural only`（thumb OFF、subject OFF）**（`BACH_INV_PHRASE_FLAGS[11]`）
> 狀態：第 11 個 Bach Invention analysis 頁
> 觸發 case：高密度 figural（RH 40 / LH 30）、subject 雖偵測到 entries 卻**未啟用** → 偵測 ≠ 啟用的代表

## 1. 為什麼挑這首

BWV 782 示範了一個重要區分：**「偵測到 subject entries」不等於「應啟用 subject 軸」**。Inv 11 的 subject detection 在兩手都有命中（§3），但出貨設定刻意只開 figural — 因 cost-framework sweep 的 both-hands-improve 規則未通過 subject。

## 2. 曲目基本資訊

- **BWV 782**, 約 1722–23（Köthen）
- **G minor**（2 flats，cached `key_sharps=-2` ✓），**4/4 拍**，**約 22–23 小節**（cached 23）
- 形式：2-voice Invention；flowing 16 分音符 figuration，G minor 的 plaintive character
- 主題特色：sequential 16th-note figure，密集 figural 切換（見 §3 RH 40 boundaries）
- 教學定位：小調 sequence 與兩手交織的密集 figural 練習

## 3. Subject / Figural 識別 — 實跑偵測輸出

| 手 | subject@0.8 | subject@0.7 | figural |
|---|---|---|---|
| **RH** | m13, m18（2）| m6, m13, m18, m21（4）| **40** boundaries（m1×4, m2×4, m4, m5…）|
| **LH** | m19（1）| m18, m19（2）| **30** boundaries（m3×2, m4×4, m7, m8…）|

**關鍵觀察 — 偵測到 subject 但不啟用**：
- subject@0.8 在 RH m13/m18、LH m19 有真實命中，並非 0-signal（與 Inv 10/13 不同）
- 但 `BACH_INV_PHRASE_FLAGS[11]` 出貨為 **figural-only** — cost-framework sweep（both-hands-improve）下，加 subject 未讓兩手同時改善 / 或在某手 breach
- → 設計意涵：**啟用裁決的最終仲裁是 cost red-line，不是「偵測軸有沒有訊號」**。這與 *feedback_personal_biomechanics*「cost 是真相」一致 — wiki 偵測軸是 hypothesis，cost sweep 是 gate
- thumb OFF：G minor 快速 LH chromatic/octave 段落會讓 thumb-reservation 在 LH 製造 breach（與 Inv 3/9/15 同 pattern）

**Figural-dominated**：RH 40 / LH 30 是 9-15 群組中最高的 figural 密度 → Inv 11 的樂句結構由 figure 切換主導，subject re-entry 為輔。

## 4. 三段曲式對應到 form

| 段落 | program mN | 調性 | 角色 |
|---|---|---|---|
| **Exposition** | m1–m6 | G minor | RH figure → LH 模仿；高密度 figural 起 |
| **Modulation / development** | m7–m18 | B♭ major (III) / D minor (v) | sequence 密集；subject 片段 m13/m18 再現 |
| **Return + cadence** | m19–m23 | G minor（回主）| LH m19 final entry → cadential close |

## 5. 與其他 wiki 頁面的關係

- 與 [analysis_bach_inv_10_g_major](analysis_bach_inv_10_g_major.md)（subject 0 命中）對照：Inv 11 是「subject 有命中但不啟用」，Inv 10 是「subject 無命中」— 兩種不同的 not-subject-enabled 路徑
- 對 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 提供 **「偵測 ≠ 啟用，cost red-line 仲裁」** 的關鍵 case
- 對 [concept_figural_boundary_detection](concept_figural_boundary_detection.md) 提供集內**最高 figural 密度**的 figural-dominated case
- 啟用裁決依 score-claude memory *project_bach_inv_subject_detection_validation_2026-05-28*
- cost 為最終仲裁依 *feedback_personal_biomechanics*；分析獨立性依 *feedback_phrase_analysis_is_its_own_discipline*
