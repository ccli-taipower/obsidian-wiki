---
tags:
  - analysis
  - bach
  - invention
  - phrase
---

# Analysis: Bach Invention 14 in B♭ major (BWV 785) — Ornamented Subject 與 RH-Early Subject@0.8

> 來源：musicology 文獻 + **cached MXL 實跑偵測**（`mvt14.mxl`，2026-06-03 grounding）
> 對應 program：mvt14；出貨設定 **`figural + thumb + subject@0.7`**（`BACH_INV_PHRASE_FLAGS[14]`）
> 狀態：第 14 個 Bach Invention analysis 頁
> 觸發 case：B♭ major、ornamented/trill subject、RH subject 在 m3/m9 早早再現（@0.8 即命中）、LH 須 @0.7

## 1. 為什麼挑這首

BWV 785 是 *RH 與 LH subject 偵測容差不對稱* 的 case：RH subject 在 @0.8 即穩定命中（m3/m9），LH 須降到 @0.7 才出現（m15/m16）。這支持「容差需求可能 per-hand 不同」的觀察。

## 2. 曲目基本資訊

- **BWV 785**, 約 1722–23（Köthen）
- **B♭ major**（2 flats，cached `key_sharps=-2` ✓），**4/4 拍**（common time），**20 小節**
- 形式：2-voice Invention；ornamented（trill / mordent）subject + 16 分音群，B♭ major 的 graceful, lively character
- 主題特色：**裝飾音化 head motif**（trill/turn）+ 流動 figuration
- 教學定位：裝飾音與主聲部 figuration 並行的雙手協調

## 3. Subject / Figural 識別 — 實跑偵測輸出

| 手 | subject@0.8 | subject@0.7 | figural |
|---|---|---|---|
| **RH** | **m3, m9**（2）| m3, m9（2，與 @0.8 同）| 26（m1, m2, m4, m5×2, m9×2, m12…）|
| **LH** | **0** | m15, m16（2）| 23（m4, m5×2, m7, m10, m12×2…）|

**關鍵觀察 — per-hand 容差不對稱**：
- **RH @0.8 即命中** m3/m9（@0.7 無增加）→ RH subject signature 穩定，早早再現（m3 = exposition 內的緊接模仿）
- **LH @0.8 全 miss，@0.7 才出 m15/m16** → LH subject 變體較大（裝飾音 / 移調影響 signature）
- → 出貨取 **subject@0.7** 是為涵蓋 LH 的 m15/m16；RH 本不需要降容差。這顯示 per-piece `subject_tol` 旋鈕實際是**取兩手聯集的下界**
- thumb ON：B♭ major baroque pattern，兩手容忍 thumb-reservation，cost sweep 通過

**Figural**：RH 26 / LH 23 中度偏高密度，與 subject 並用構成完整 form 結構。

## 4. 三段曲式對應到 form

| 段落 | program mN | 調性 | 角色 |
|---|---|---|---|
| **Exposition** | m1–m4 | B♭ major | RH ornamented subject (m1) → 緊接 RH m3 再現 → LH 模仿 |
| **Modulation / development** | m5–m14 | F major (V) / g minor (vi) | sequence + figuration；RH m9 subject 再現 |
| **Return + cadence** | m15–m20 | B♭ major（回主）| LH m15/m16 final entries → cadential close |

## 5. 與其他 wiki 頁面的關係

- 對 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 提供 **per-hand 容差不對稱**（RH@0.8 / LH@0.7）的 case；補充「subject_tol = 兩手聯集下界」的實作理解
- 與 [analysis_bach_inv_9_f_minor](analysis_bach_inv_9_f_minor.md)（@0.8 robust）/ [analysis_bach_inv_12_a_major](analysis_bach_inv_12_a_major.md)（@0.7 necessary）構成容差光譜
- 同列 figural+thumb+subject@0.7 群組（Inv 5/6/7/9/12/14）
- 啟用裁決依 score-claude memory *project_bach_inv_subject_detection_validation_2026-05-28*
- 分析獨立性依 *feedback_phrase_analysis_is_its_own_discipline*
