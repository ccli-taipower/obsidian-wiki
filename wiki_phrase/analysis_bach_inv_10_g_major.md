---
tags:
  - analysis
  - bach
  - invention
  - phrase
---

# Analysis: Bach Invention 10 in G major (BWV 781) — Gigue-Figuration 與 Subject 軸的不適用

> 來源：musicology 文獻 + **cached MXL 實跑偵測**（`mvt10.mxl`，2026-06-03 grounding via `tmp/trackC_bach_inv_9_15_grounding.py`）
> 對應 program：mvt10；**未啟用任何 phrase flag**（`BACH_INV_PHRASE_FLAGS` 無 mvt10 條目）
> 狀態：第 10 個 Bach Invention analysis 頁；**記錄「為何偵測軸不適用」的負面 case**
> 觸發 case：9/8 gigue 連續音群、subject 0 命中、cost-framework sweep 顯示 both-hands breach → 不啟用

## 1. 為什麼這首是有價值的「負面 case」

並非每首 Invention 都需要 phrase flag。BWV 781 是 *Inventions* 集裡 **subject-imitation 軸與 thumb-reservation 軸都不適用**的代表，記錄它能避免未來盲目對全 15 首套用同一組 flag：

- **9/8 gigue 連續音群**：快速三連音 / 16 分音符的 running figuration，非離散可模仿主題
- **Subject 0 命中**（見 §3）：演算法在兩個容差下都抓不到 subject re-entry — 不是 bug，是曲子本質
- **cost-framework sweep 顯示 both-hands breach**：`diag_bach_inv_remaining_sweep.py`（2026-05-29）對 mvt10 顯示啟用 flag 後兩手皆 cost breach → 保守 not-enabled

## 2. 曲目基本資訊

- **BWV 781**, 約 1722–23（Köthen）
- **G major**（1 sharp，cached `key_sharps=1` ✓），**9/8 拍**（compound triple），**32 小節**
- 形式：2-voice Invention；gigue-like 連續音群，pastoral / joyful character
- 主題特色：**running figuration over 9/8**；以音階 / 琶音 motif 連續推進，無強對比的 head-motif
- 教學定位：compound metre 下的均勻指序與 voice 交織練習

## 3. Subject 識別 — 實跑偵測輸出（subject 軸不適用）

| 手 | @ tol=0.8 | @ tol=0.7 |
|---|---|---|
| **RH** | **0 entries** | **0 entries** |
| **LH** | **0 entries** | **0 entries** |

**為何 0 命中（非 bug）**：
- Inv 10 的 figuration 是 **sequential running passage**（音階段 + 琶音），不是帶穩定 TI signature 的離散主題
- [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 依「opening N groups 的 interval signature 在他處重現」運作；當開頭本身是連續音階時，signature 是「一串 +2 半音」這類**非特異 pattern**，要嘛到處假命中、要嘛（去重後）全 miss → 此處為後者
- → 設計意涵：**running-figuration invention 應走 figural 軸，不走 subject 軸**

**Figural**：RH 15 boundaries（m2/9/10/11/11/12/13/17…），LH 18（m5/6/7/8/11/12/13/14…）— figural 軸有訊號，但 cost sweep 顯示啟用後 breach（見 §4）。

## 4. 為何不啟用 — cost-framework 裁決

| 軸 | 偵測結果 | 啟用？ |
|---|---|---|
| subject | 0 命中 | ❌ 無訊號 |
| figural | RH15/LH18 訊號 | ❌ sweep 顯示 both-hands cost breach |
| thumb | — | ❌ 9/8 running 段 thumb-reservation 在快速音群製造 breach |

→ mvt10 與 mvt13 同列 **未啟用**（CLAUDE.md「13/15 mvts」的兩個例外）。但兩者原因不同：
- **mvt10**：figural 有訊號但啟用 breach（gigue figuration）
- **mvt13**：LH baseline cost 本身異常高（alberti-like，見 [analysis_bach_inv_13_a_minor](analysis_bach_inv_13_a_minor.md) + *project_lh_baseline_cost_outliers_2026-05-29*）

## 5. 與其他 wiki 頁面的關係

- 與 [analysis_bach_inv_13_a_minor](analysis_bach_inv_13_a_minor.md) 構成 **「不啟用」雙 case 對照**（figuration-breach vs baseline-outlier）
- 對 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 提供 **running-figuration → subject 軸不適用** 的負面 case
- 對 [concept_figural_boundary_detection](concept_figural_boundary_detection.md) 提供「figural 有訊號但 cost 不容許啟用」的取捨案例
- 啟用裁決依 score-claude memory *project_bach_inv_subject_detection_validation_2026-05-28*（grounding 延伸）
- 分析獨立性主張依 *feedback_phrase_analysis_is_its_own_discipline*
