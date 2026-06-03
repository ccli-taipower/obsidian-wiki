---
tags:
  - analysis
  - bach
  - invention
  - phrase
  - chromatic
---

# Analysis: Bach Invention 9 in F minor (BWV 780) — Chromatic Sigh-Subject 與 Invertible Counterpoint

> 來源：musicology 文獻 + **cached MXL 實跑偵測**（`tmp/.../mvt9.mxl`，2026-06-03 grounding via `tmp/trackC_bach_inv_9_15_grounding.py`）
> 對應 program：mvt9（book `assign_fingering_v6` call#10）；**measure 為 program-MXL 值**，Inv 9 為 3/4 無 pickup → program ≈ user（無 override 表項，見 *project_bach_inv_measure_mapping*）
> 狀態：第 9 個 Bach Invention analysis 頁；**subject section 為實跑輸出（非預測）** — 與 Inv 1-8 頁的 ⚠ pending 模板不同
> 觸發 case：descending chromatic sigh-subject、3/4 minuet-pace、invertible counterpoint、subject@0.8 robust（與 Inv 7 chromatic-needs-0.7 對照）

## 1. 為什麼挑這首作為 wiki Bach analysis 頁

BWV 780 在 *Two-Part Inventions* 中被廣泛視為**情感最深、半音語言最豐富的一首**，對 wiki 框架有三項價值：

- **Chromatic sigh-subject（嘆息動機）**：subject 含大量半音下行與懸留（suspension / sospiro），是 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 在 *chromatic* 主題上的關鍵測試 — 但與 [analysis_bach_inv_7_e_minor](analysis_bach_inv_7_e_minor.md) 不同（Inv 7 chromatic 須降到 tol=0.7 才命中），**Inv 9 在 tol=0.8 即穩定命中**（見 §3），提供「chromatic ≠ 一定需要鬆容差」的反例
- **Invertible counterpoint（可動對位）**：兩聲部角色可上下互換，subject 在 RH/LH 對稱出現 — 是 [concept_counterpoint](concept_counterpoint.md) §雙重對位的代表
- **3/4 minuet-pace**：與 Inv 8（3/4 minuet-like，broken triad）形成「同拍號、不同 subject 性格」對照；與 Inv 4（3/8 chromatic）形成「同 chromatic、不同拍號」對照

## 2. 曲目基本資訊

- **BWV 780**, 約 1722–23（Köthen 時期）
- **F minor**（4 flats，cached MXL `key_sharps=-4` ✓），**3/4 拍**，**34 小節**（through-composed，無反覆）
- 形式：典型 2-voice Invention；exposition / modulation / return 三段論
- 主題特色：**descending chromatic line + 懸留嘆息動機**；F minor 的 *grave, lamenting* character；情感上常被視為全集頂點
- 教學定位：*Inventions* 集第 9 首；半音聲部進行與雙重對位的教學典範
- 著名版本：András Schiff (ECM/Bach Lectures)、Angela Hewitt (Hyperion)、Glenn Gould — 三者在此曲的 rubato 與聲部平衡詮釋差異大
- 編輯版本爭議：見 [src_bach_inventions_pedagogy](src_bach_inventions_pedagogy.md)

## 3. Subject 識別 — 實跑偵測輸出（grounded 2026-06-03）

`_detect_subject_entries` 在 cached mvt9 MXL 上的實際輸出（subject_len=8）：

| 手 | @ tol=0.8（default） | @ tol=0.7（chromatic-relaxed） |
|---|---|---|
| **RH** | **m9, m12, m29**（3 entries）| m9, m12, m13, m19, m29, m30（6）|
| **LH** | **m9, m12**（2 entries）| m9, m12, m25（3）|

（演算法掃描自各手 template 之後，故 m1 RH / 早期 LH 的 template 本身不列為 entry，與 Inv 7 頁同一慣例。）

**關鍵觀察 — chromatic 但 tol=0.8 即 robust**：

- Inv 9 的 chromatic subject 在 **default tol=0.8** 已給出乾淨、對稱的 RH/LH entries（m9 + m12 兩手同步），不需像 Inv 7 降到 0.7
- 推斷原因：Inv 9 的半音是 **subject 內部一致的固定動機輪廓**（每次重現都帶相同半音 contour），interval signature 反而穩定；Inv 7 的 chromatic 是 *voice-leading descent*（每次變體不同），signature 才會飄
- → 對 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 的意涵：**「chromatic」不是調容差的依據**；依據是「半音屬於 motif 固定輪廓」還是「半音屬於自由聲部進行」。Inv 9（前者）vs Inv 7（後者）是這條區分的對照組

**實際出貨設定 vs grounding 的張力**：`BACH_INV_PHRASE_FLAGS[9]` 出貨為 **`figural + subject@0.7`（thumb OFF）** — 由 cost-framework red-line sweep（`diag_bach_inv_remaining_sweep.py`，both-hands-improve 規則）選定。但本頁 grounding 顯示 **@0.8 已乾淨命中**（RH m9/12/29 + LH m9/12）。
- 解讀：@0.7 是**保守 headroom，非嚴格必要** — Inv 9 的 chromatic subject 不像 Inv 7 那樣強制需要鬆容差
- thumb OFF 的理由與 Inv 3/7/11/15 同：fast LH chromatic/octave 段落會讓 thumb-reservation 在 LH 產生 cost breach
- （註：`BACH_INV_PHRASE_FLAGS` dict 頂部註解「Not enabled: mvts 9,10,13」為 **stale** — mvt9 實際在 dict 中=已啟用；真正未啟用為 10/13，符合 CLAUDE.md 的 13/15）

**Figural**：RH 16 boundaries（m5/6/9/11/12/15/16…），LH 10（m2/6/9/14/25/28…）。m9 / m12 同時是 subject entry + figural boundary → 高信心 form 段落點。

## 4. 三段曲式對應到 form

| 段落 | program mN | 調性 | 角色 |
|---|---|---|---|
| **Exposition** | m1–m8 | F minor | RH subject (m1) → LH 模仿（早期）→ 雙重對位呈示 |
| **Modulation / development** | m9–m24 | A♭ major (III) / C minor (v) 等短暫離調 | subject 密集再現（m9/m12 兩手同步 entry）+ 半音 sequence + voice exchange |
| **Return + final cadence** | m25–m34 | F minor（回主） | LH m25 final entry → RH m29 重現 → cadential close（可能 Picardy 3rd → F major chord）|

→ m8–m9、m24–m25 為兩個主要 **form 段落邊界**，皆與 §3 的 subject/figural 偵測點吻合（m9 entry cluster、m25 LH return）。

## 5. Case — Chromatic subject 的 tolerance 校準（Inv 9 vs Inv 7）

Inv 9 是 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) tolerance 設計的關鍵對照 case：

| | Inv 7 (BWV 778) | Inv 9 (BWV 780) |
|---|---|---|
| Chromatic 來源 | voice-leading descent（自由半音下行）| subject 內固定嘆息動機 |
| @ tol=0.8 | RH 全 miss（須降 0.7）| **RH m9/m12/m29 命中** |
| 半音對 signature 的影響 | 每次變體 → signature 飄 | 每次同輪廓 → signature 穩 |
| @0.8 必要性 | **嚴格必要**（@0.8 失效）| **非必要**（@0.8 已 robust）|
| 出貨設定 | figural + subject@0.7 (thumb OFF) | figural + subject@0.7 (thumb OFF) — @0.7 為保守 headroom |

**設計結論**：per-piece `subject_tol` 旋鈕的存在理由不是「曲子有沒有半音」，而是「半音是否破壞 motif 的 TI signature 穩定性」。Inv 9 證明 chromatic 主題也能在 default tol 穩定偵測（@0.8）；出貨仍取 @0.7 純為保守，而 Inv 7 才是 @0.7 嚴格必要的 case。避免「見 chromatic 就放寬」的過度泛化。

## 6. 與其他 wiki 頁面的關係

- 與 [analysis_bach_inv_7_e_minor](analysis_bach_inv_7_e_minor.md) 構成 **chromatic subject tolerance 對照組**（自由半音 vs 固定動機半音）
- 與 [analysis_bach_inv_4_d_minor](analysis_bach_inv_4_d_minor.md) 構成「chromatic minor，不同拍號（3/8 vs 3/4）」對照
- 與 [analysis_bach_inv_8_f_major](analysis_bach_inv_8_f_major.md) 構成「同 3/4 拍，不同 subject 性格（broken triad vs chromatic sigh）」對照
- 應用 [concept_fugue](concept_fugue.md) / [concept_counterpoint](concept_counterpoint.md) 對 2-voice invertible counterpoint 的論述
- 對 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 提供 **chromatic-but-robust-at-0.8** 的 tolerance 校準反例
- 編輯版本與教學脈絡引 [src_bach_inventions_pedagogy](src_bach_inventions_pedagogy.md)
- 對位起源溯至 [src_fux_gradus_ad_parnassum](src_fux_gradus_ad_parnassum.md)
- Measure 對應依 *project_bach_inv_measure_mapping*；偵測 grounding 依 score-claude memory *project_bach_inv_subject_detection_validation_2026-05-28*（本頁為其 9-15 延伸）
- 個人化生物力學原則依 *feedback_personal_biomechanics*；樂句呼吸依 *feedback_phrase_as_breath*；分析獨立性依 *feedback_phrase_analysis_is_its_own_discipline*
