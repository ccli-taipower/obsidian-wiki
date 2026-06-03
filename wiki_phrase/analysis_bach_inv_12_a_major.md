---
tags:
  - analysis
  - bach
  - invention
  - phrase
  - compound-metre
---

# Analysis: Bach Invention 12 in A major (BWV 783) — 12/8 Arpeggiated Figuration 與 Sparse Subject@0.7

> 來源：musicology 文獻 + **cached MXL 實跑偵測**（`mvt12.mxl`，2026-06-03 grounding）
> 對應 program：mvt12；出貨設定 **`figural + thumb + subject@0.7`**（`BACH_INV_PHRASE_FLAGS[12]`）
> 狀態：第 12 個 Bach Invention analysis 頁
> 觸發 case：12/8 compound、broken-chord figuration、subject 在 @0.8 全 miss 須降 @0.7 才稀疏命中

## 1. 為什麼挑這首

BWV 783 是 *compound-metre + 琶音 figuration* 下 subject 偵測的 marginal case：@0.8 完全 miss，@0.7 才抓到稀疏 entries。它支持 per-piece `subject_tol` 旋鈕的存在（與 Inv 9「@0.8 即 robust」形成對照）。

## 2. 曲目基本資訊

- **BWV 783**, 約 1722–23（Köthen）
- **A major**（3 sharps，cached `key_sharps=3` ✓），**12/8 拍**（compound quadruple；cached MXL timesig 解析失敗顯示 `?`，canonical 為 12/8），**21 小節**
- 形式：2-voice Invention；arpeggiated / broken-chord figuration，A major 的 bright, flowing character
- 主題特色：琶音化 head motif + 連續 8 分音群，compound metre 的搖曳律動
- 教學定位：12/8 下的琶音指序與兩手對話

## 3. Subject / Figural 識別 — 實跑偵測輸出

| 手 | subject@0.8 | subject@0.7 | figural |
|---|---|---|---|
| **RH** | **0** | m9（1）| 16（m2×3, m5, m6, m8×2, m10…）|
| **LH** | **0** | m19, m21（2）| 15（m2, m3, m4×3, m5, m12×2…）|

**關鍵觀察 — @0.8 全 miss，@0.7 稀疏命中**：
- Inv 12 的 broken-chord subject 在 @0.8 完全偵測不到（琶音化使每次重現的 interval signature 變動較大）
- 降到 @0.7 才抓到 RH m9、LH m19/m21 —— 稀疏但真實
- → 與 Inv 9（chromatic 卻 @0.8 robust）對照，Inv 12 是「**figuration 變體破壞 signature → 須鬆容差**」的另一型；與 Inv 7（自由半音）並列為 @0.7-necessary 群組
- thumb ON：與 Inv 10 不同，Inv 12 的 12/8 broken-chord 段落兩手皆容忍 thumb-reservation（baroque pattern），cost sweep 通過

## 4. 三段曲式對應到 form

| 段落 | program mN | 調性 | 角色 |
|---|---|---|---|
| **Exposition** | m1–m8 | A major | RH 琶音 subject → LH 模仿 |
| **Modulation / development** | m9–m18 | E major (V) / f# minor (vi) | subject 片段 m9 再現 + sequence |
| **Return + cadence** | m19–m21 | A major（回主）| LH m19/m21 final entries → cadential close |

## 5. Case — Compound metre 的 figural 密度與 subject 稀疏的並存

Inv 12 同時是「figural 有中度密度（RH16/LH15）」+「subject 稀疏（@0.7 共 3）」的 case：
- 出貨 `figural + thumb + subject@0.7` 三軸並用，figural 提供主結構，subject@0.7 補強 form 段落點（m9 / m19）
- long-scale thumb-under 規則無關（Inv 12 是琶音非音階），但與 [concept_running_passage_thumb_reservation](concept_running_passage_thumb_reservation.md) 相關（12/8 連續 8 分音群觸發 thumb reservation）

## 6. 與其他 wiki 頁面的關係

- 與 [analysis_bach_inv_9_f_minor](analysis_bach_inv_9_f_minor.md) 構成 **subject tolerance 對照**（@0.8-robust vs @0.7-necessary，但 Inv 12 的原因是 figuration 變體而非自由半音）
- 與 [analysis_bach_inv_7_e_minor](analysis_bach_inv_7_e_minor.md) 同列 @0.7-necessary 群組
- 對 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 提供 **broken-chord figuration → signature 變動 → 須 @0.7** 的 case
- 對 [concept_running_passage_thumb_reservation](concept_running_passage_thumb_reservation.md) 提供 12/8 compound 觸發案例
- 啟用裁決依 score-claude memory *project_bach_inv_subject_detection_validation_2026-05-28*
- 分析獨立性依 *feedback_phrase_analysis_is_its_own_discipline*
