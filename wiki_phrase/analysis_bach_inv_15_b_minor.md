---
tags:
  - analysis
  - bach
  - invention
  - phrase
  - data-caveat
---

# Analysis: Bach Invention 15 in B minor (BWV 786) — Figural-Only 與 Cached-MXL 截斷 Caveat

> 來源：musicology 文獻 + **cached MXL 實跑偵測**（`mvt15.mxl`，2026-06-03 grounding）
> 對應 program：mvt15；出貨設定 **`figural only`（thumb OFF、subject OFF）**（`BACH_INV_PHRASE_FLAGS[15]`）
> 狀態：第 15 個（最後一個）Bach Invention analysis 頁
> ⚠ **DATA CAVEAT**：cached MXL 僅含 **mm.1–12**（canonical BWV 786 為 ~21–22 小節）→ 後段未涵蓋，本頁偵測 grounding 不完整

## 1. ⚠ Cached-MXL 截斷 Caveat（首要聲明）

cached `mvt15.mxl` 的 measure 抽取顯示 **僅 12 小節**（`measures=12`），而 canonical BWV 786 為 ~21–22 小節。意涵：

- 本頁的 subject / figural grounding **只反映 mm.1–12**，後半段（development 後段 + return + final cadence）**未被偵測涵蓋**
- 不確定截斷來源：可能是 Audiveris 書冊分頁、measure 編號 reset、或 export 不完整
- → **修復建議**：重抓完整單曲譜（如 IMSLP / craigsapp Bach kern）或重跑 Audiveris 確認 mvt15 的完整 sheet 範圍；在此之前，本頁標記為 **incomplete grounding**
- 此 caveat 本身是有價值的記錄：提醒 9-15 batch 的 cached MXL 並非全部完整，未來教 override 前須先驗證 measure 範圍（呼應 *project_bach_inv_measure_mapping* 的「跑 pipeline 看範圍」原則）

## 2. 曲目基本資訊

- **BWV 786**, 約 1722–23（Köthen）
- **B minor**（2 sharps，cached `key_sharps=2` ✓），**4/4 拍**，**canonical ~21–22 小節**（cached 僅 12）
- 形式：2-voice Invention；fast 16 分音群 sequential figuration，B minor 的 driving / energetic character
- 主題特色：sequential 16th-note figure；集內收束曲，動力性強
- 教學定位：*Inventions* 集終曲；快速 sequence 與兩手交織

## 3. Subject / Figural 識別 — 實跑偵測輸出（僅 mm.1–12）

| 手 | subject@0.8 | subject@0.7 | figural |
|---|---|---|---|
| **RH** | **m5**（1）| m5（1）| 11（m2, m3, m4×2, m5, m8, m9, m10…）|
| **LH** | **0** | **0** | 9（m2, m5×2, m6, m8×2, m9×2）|

**觀察（受截斷限制）**：
- RH subject 在 m5 命中（@0.8）— exposition 內的緊接模仿
- LH 0 命中 — 但**可能因截斷**而非真正無 subject（後段 LH entries 未被涵蓋）
- 出貨 **figural-only**：thumb OFF（B minor 快速 LH 段落破壞 thumb-reservation，與 Inv 3/9/11 同 pattern）；subject OFF（mm.1-12 內 subject 訊號不足以通過 cost sweep，但此判斷受截斷影響）
- → figural（RH11/LH9）是 mm.1-12 內較可靠的軸

## 4. 三段曲式對應到 form（canonical，超出 cached 範圍部分為文獻推定）

| 段落 | 小節（canonical）| 調性 | 角色 | cached 涵蓋？ |
|---|---|---|---|---|
| **Exposition** | m1–m6 | B minor | RH subject (m1) → RH m5 緊接 → LH 模仿 | ✅ |
| **Modulation / development** | m7–m16 | D major (III) / f# minor (v) | sequence 密集 | ⚠ 部分（cached 止於 m12）|
| **Return + cadence** | m17–m22 | B minor（回主）| final entries → cadential close（可能 Picardy 3rd）| ❌ 未涵蓋 |

## 5. 與其他 wiki 頁面的關係

- 完成 [analysis_bach_inv_1_c_major](analysis_bach_inv_1_c_major.md) … 至本頁的 **15 首全集 analysis 覆蓋**
- 同列 figural-only 群組（Inv 3/11/15）— 快速 LH 段落 thumb OFF
- 對 [concept_figural_boundary_detection](concept_figural_boundary_detection.md) 提供集內終曲的 sequential figuration case
- ⚠ data caveat 提醒：cached MXL 完整性需驗證，呼應 *project_bach_inv_measure_mapping*
- 啟用裁決依 score-claude memory *project_bach_inv_subject_detection_validation_2026-05-28*
- 分析獨立性依 *feedback_phrase_analysis_is_its_own_discipline*
