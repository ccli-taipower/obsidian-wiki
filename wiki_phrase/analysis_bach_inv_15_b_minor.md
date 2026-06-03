---
tags:
  - analysis
  - bach
  - invention
  - phrase
  - data-caveat
---

# Analysis: Bach Invention 15 in B minor (BWV 786) — Figural-Only 終曲（完整 grounding via clean reference）

> 來源：musicology 文獻 + **完整曲 MXL 實跑偵測**（clean kern→MXL reference，2026-06-03）
> 對應 program：mvt15；出貨設定 **`figural only`（thumb OFF、subject OFF）**（`BACH_INV_PHRASE_FLAGS[15]`）
> 狀態：第 15 個（最後一個）Bach Invention analysis 頁 — **15 首全集完成**
> 📌 **grounding 已補完**：先前 cached `mvt15.mxl`（Audiveris）截斷於 mm.1-12；本頁 grounding 改用 **完整 22-小節 clean reference**（`input/reference/BWV786_Bach_Invention15_Bm.musicxml`，478 notes / 22 measures，kern.humdrum.org BWV 786）

## 1. Cached-MXL 截斷 → 已用 clean reference 補完

**Production caveat（仍有效）**：cached `mvt15.mxl`（Audiveris OMR 自 Inventions 書冊）只含 **mm.1–12**（canonical BWV 786 為 22 小節）。production 標注 pipeline 若用此 cached MXL 會漏後半段 → **未來教 override 前須重跑 Audiveris 確認 mvt15 完整 sheet 範圍**。

**Grounding 已解決**：本頁的 subject/figural 偵測改用 **完整 22-小節 clean kern→MXL reference**（acquire script `tmp/acquire_bach15_beethoven_op49.py`，2026-06-03），不再受截斷限制。clean reference 為 reference/eval 用途（無 OMR pixel → 不走標注 pipeline，per *reference_mozart_kern_mxl_source*），但對 phrase grounding 完全足夠。

→ 教訓：9-15 batch 的 cached MXL 並非全部完整；phrase grounding 應優先用 clean kern reference，OMR cached 僅 production 用且須驗證範圍（呼應 *project_bach_inv_measure_mapping*「跑 pipeline 看範圍」原則）。

## 2. 曲目基本資訊

- **BWV 786**, 約 1722–23（Köthen）
- **B minor**（2 sharps ✓），**4/4 拍**，**22 小節**（clean reference 確認；cached OMR 誤截為 12）
- 形式：2-voice Invention；fast 16 分音群 sequential figuration，B minor 的 driving / energetic character
- 主題特色：sequential 16th-note figure；集內收束曲，動力性強
- 教學定位：*Inventions* 集終曲；快速 sequence 與兩手交織

## 3. Subject / Figural 識別 — 完整曲實跑偵測輸出（22m）

| 手 | subject@0.8 | subject@0.7 | figural |
|---|---|---|---|
| **RH** | **m5, m19**（2）| m5, m14, m19（3）| 17（m2, m3, m4×2, m5, m8, m9, m10…）|
| **LH** | **0** | **0** | 15（m2, m5×2, m6, m8×2, m9×2…）|

**觀察（完整曲，截斷疑慮解除）**：
- RH subject @0.8 命中 **m5（exposition 緊接）+ m19（return entry）** — 截斷版只看到 m5，完整版才顯示 return 段的 m19；@0.7 再加 development 的 m14
- **LH 0 命中為真**（非截斷 artifact）：完整 22 小節下 LH 兩容差皆 0 → Inv 15 的 LH 確實不帶可偵測的 subject re-entry（與先前頁面「可能是截斷」的 hedge 相反，現確認為 genuine）
- 出貨 **figural-only** 判斷成立：thumb OFF（B minor 快速 LH 段落破壞 thumb-reservation，與 Inv 3/11 同 pattern）；subject OFF（RH 雖有 m5/m19，但 LH 全 0 → cost sweep 的 both-hands-improve 不通過，與 Inv 11「偵測 ≠ 啟用」同理）
- → figural（RH17/LH15）是兩手均衡的可靠軸

## 4. 三段曲式對應到 form（完整曲）

| 段落 | 小節 | 調性 | 角色 |
|---|---|---|---|
| **Exposition** | m1–m6 | B minor | RH subject (m1) → RH m5 緊接 → LH 模仿 |
| **Modulation / development** | m7–m16 | D major (III) / f# minor (v) | sequence 密集；@0.7 RH m14 subject 片段 |
| **Return + cadence** | m17–m22 | B minor（回主）| RH m19 final entry → cadential close（可能 Picardy 3rd）|

## 5. 與其他 wiki 頁面的關係

- 完成 [analysis_bach_inv_1_c_major](analysis_bach_inv_1_c_major.md) … 至本頁的 **15 首全集 analysis 覆蓋**
- 同列 figural-only 群組（Inv 3/11/15）— 快速 LH 段落 thumb OFF
- 與 [analysis_bach_inv_11_g_minor](analysis_bach_inv_11_g_minor.md) 同為「RH 有 subject 但 LH 全 0 → 偵測 ≠ 啟用」case
- 對 [concept_figural_boundary_detection](concept_figural_boundary_detection.md) 提供集內終曲的 sequential figuration case
- clean kern→MXL reference 來源依 *reference_mozart_kern_mxl_source*；cached OMR 完整性需驗證，呼應 *project_bach_inv_measure_mapping*
- 啟用裁決依 score-claude memory *project_bach_inv_subject_detection_validation_2026-05-28*
- 分析獨立性依 *feedback_phrase_analysis_is_its_own_discipline*
