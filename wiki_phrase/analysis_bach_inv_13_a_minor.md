---
tags:
  - analysis
  - bach
  - invention
  - phrase
  - cost-outlier
---

# Analysis: Bach Invention 13 in A minor (BWV 784) — Alberti-like Figuration 與 LH Baseline-Cost Outlier

> 來源：musicology 文獻 + **cached MXL 實跑偵測**（`mvt13.mxl`，2026-06-03 grounding）
> 對應 program：mvt13；**未啟用任何 phrase flag**（`BACH_INV_PHRASE_FLAGS` 無 mvt13 條目）
> 狀態：第 13 個 Bach Invention analysis 頁；記錄 **LH baseline-cost outlier** 的負面 case
> 觸發 case：arpeggiated / alberti-like broken-chord perpetual motion、subject 0 命中、figural RH 僅 2、**LH baseline cost 異常高**（per *project_lh_baseline_cost_outliers_2026-05-29*）

## 1. 為什麼這首是「不啟用」的另一型

Inv 13 與 Inv 10 同列未啟用，但原因不同：
- **Inv 10**：figural 有訊號，但啟用後 cost breach（gigue figuration）
- **Inv 13**：**LH baseline cost 本身異常高**（broken-chord perpetual motion 的固有大跳 pattern），任何偵測軸都無法改善 → no axis helps

這是「DP cost 反映真實生物力學需求、不是 bug」的代表（per *project_lh_baseline_cost_outliers_2026-05-29*）。

## 2. 曲目基本資訊

- **BWV 784**, 約 1722–23（Köthen）
- **A minor**（無 key signature，cached `key_sharps=?` = A minor 無升降 ✓），**4/4 拍**，**約 22 小節**（cached 25，含 pickup/ghost 偏移）
- 形式：2-voice Invention；arpeggiated broken-chord perpetual motion，A minor 的 restless / etude-like character
- 主題特色：**琶音化 broken-chord figure**（alberti-like）連續推進；兩手快速交替分解和弦
- 教學定位：分解和弦的均勻觸鍵與手位移動 etude

## 3. Subject / Figural 識別 — 實跑偵測輸出（多軸不適用）

| 手 | subject@0.8 | subject@0.7 | figural |
|---|---|---|---|
| **RH** | **0** | **0** | **2**（m13, m25）|
| **LH** | **0** | **0** | 7（m5×2, m15, m16×2, m17, m18）|

**為何多軸不適用**：
- **subject 0 命中**（兩容差）：broken-chord figuration 與 Inv 10 同理 — 非離散可模仿主題
- **figural RH 僅 2**：RH 的分解和弦過於均勻連續，figure 切換點稀疏 → figural 軸幾乎無訊號
- → subject + figural 雙軸皆失效；唯一可能的 thumb 軸又遇 LH baseline 問題（見 §4）

## 4. LH Baseline-Cost Outlier — 核心問題

per *project_lh_baseline_cost_outliers_2026-05-29*（記錄 Inv 13 LH cost ≈ 4244，與 Chopin Op.9 No.1 LH 並列異常高）：

- **根因**：alberti-like broken-chord 的 LH 固有**大跳 pattern** — 每組分解和弦要求手位在寬音域反覆移動，DP `_transition_cost` 如實反映此生物力學負荷
- **不是 bug**：高 cost 是曲子真實難度的正確量化，不是演算法錯誤
- **無 quick win**：per-piece cost normalization 是 architectural change，非單曲修補；啟用任何 phrase flag 都無法降低這個 baseline
- → mvt13 保持未啟用：「**no axis helps**」是結論而非待辦

## 5. 與其他 wiki 頁面的關係

- 與 [analysis_bach_inv_10_g_major](analysis_bach_inv_10_g_major.md) 構成 **「不啟用」雙 case 對照**（Inv 10 = figuration-breach，Inv 13 = baseline-outlier）
- 對 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) + [concept_figural_boundary_detection](concept_figural_boundary_detection.md) 同時提供**雙軸失效**的負面 case
- LH baseline-cost 現象的 canonical 記錄：score-claude memory *project_lh_baseline_cost_outliers_2026-05-29*
- cost 反映真實需求依 *feedback_personal_biomechanics*；分析獨立性依 *feedback_phrase_analysis_is_its_own_discipline*
