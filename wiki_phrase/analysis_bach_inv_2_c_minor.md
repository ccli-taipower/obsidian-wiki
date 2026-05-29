# Analysis: Bach Invention 2 in C minor (BWV 773) — Canon-like Imitation 與 Chromatic Voice-Leading

> 來源：musicology 文獻 + user-curated `BACH_INV_OVERRIDES[2]`
> 對應 PIG：未列入 / 對照需另行查核
> 狀態：第三個 Bach Invention analysis 頁；subject detection 演算法輸出**驗證待跑**（⚠ 標記處）
> 觸發 case：canon-like RH/LH 緊密追逐 + 主題內含 chromatic 元素的雙重挑戰

## 1. 為什麼挑這首作為 wiki 第三個 Bach analysis 頁

BWV 773 是 *Two-Part Inventions* (BWV 772–786) 集中**最接近嚴格 canon**的一首，補上前兩個 analysis 頁尚未覆蓋的角度：

- [analysis_bach_inv_1_c_major](analysis_bach_inv_1_c_major.md) 示範 exposition–modulation–coda 三段論的「**modulation + cadence 主導**」邊界類型
- [analysis_bach_inv_4_d_minor](analysis_bach_inv_4_d_minor.md) 示範 episode/coda 段「**figural boundary 主導**」邊界類型
- 本頁 (Inv 2) 示範**imitation 緊密度極高**時，per-hand 樂句邊界對齊 vs 不對齊的張力——[concept_subject_imitation_detection](concept_subject_imitation_detection.md) 與 per-hand DP 之間的最尖銳測試
- 此外 BWV 773 主題本身含 chromatic descent，提供 [concept_modulation_as_phrase_signal](concept_modulation_as_phrase_signal.md) 在**非 modulation 但有 chromatic voice-leading** 情境的延伸驗證

`BACH_INV_OVERRIDES[2]` 已有 user-curated 指法分布橫跨主題呈示、模仿、cadential extension 三大區域，足以支撐 case-study 級分析。

## 2. 曲目基本資訊

- **BWV 773**, 約 1722–23 (Bach 37–38 歲, Köthen)
- **C minor**, 4/4 拍, **27 小節**（無反覆，through-composed；含較長 cadential extension 至 m27）
- 形式：典型 2-voice Invention；exposition / development(modulation) / recap 三段論
- **特色**：*Two-Part Inventions* 集中**最接近嚴格 canon** 的一首；RH 與 LH 模仿距離短（約半小節到一小節），兩聲部緊密追逐
- 主題特色：descending arpeggio（8va 下行展開）起頭 + 上行 chromatic motion 收尾，長度約 1–2 小節，比 Inv 1 主題長且更具方向性
- 教學定位：通常排在 Inv 1 之後第二首學；canon-like writing 與 chromatic 元素使難度顯著提升
- 著名版本：Glenn Gould（特別緩慢的 tempo）、András Schiff（cantabile）、Angela Hewitt
- 編輯版本爭議：見 [src_bach_inventions_pedagogy](src_bach_inventions_pedagogy.md)（articulation 與 ornament realisation）

## 3. Subject 識別 — musicology 共識與演算法測試計畫

### 3.1 Subject 長度與型態

BWV 773 的 subject 比 Inv 1 更具辨識度：

| 元素 | 描述 |
|---|---|
| **頭部 motive** | 下行琶音（broken-chord descent，跨八度） |
| **連接** | 短的 turn/neighbour 圖形 |
| **尾部** | 上行 chromatic 音階（半音級進）連到 cadential 位置 |
| **總長度** | 約 1.5–2 小節（m1 至 m2 上半，較多 analysts 採此跨度） |

主要 musicology 共識（單一派為主）：**約 2-bar subject**。Inv 1 那種 1-bar vs 2-bar 的辯論在這首較少出現，因為 chromatic 尾部與 cadential 收尾把主題的「完整性」綁定得更緊。詳見 [src_bach_inventions_pedagogy](src_bach_inventions_pedagogy.md)。

### 3.2 預期 subject entries (待演算法驗證)

依 musicology 共識，預期 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 演算法應抓到：

| Entry | 手 | 段落角色 |
|---|---|---|
| m1 pos1 | RH | Exposition — subject 第一次呈現（C minor） |
| **m3 pos1** | **LH** | Exposition — **屬調 (G minor) 答句**（非 8va 單純模仿，已接近 fugal real/tonal answer 慣例） |
| m7 附近 | RH or LH | Modulation 起點 — subject 移調至 E♭ major（相對大調） |
| m11–m15 附近 | 兩手交替 | Development middle entries（含 voice-exchange 與 sequence） |
| m16–m21 附近 | RH 為主 | Return entries 進 cadential extension |

⚠ **以上是 musicology 預測，尚未跑 `_detect_subject_entries` 驗證**。實際 entries 將補入 `_implementation_status.md`。

### 3.3 Canon-like writing 對 entry detection 的衝擊

與 Inv 1 的「RH subject → 兩拍後 LH 答句」相比，Inv 2 的模仿距離更短且更**機械式緊密**——某些段落幾乎可視為 free canon。這對 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 提出新需求：

- **重疊處理**：當 LH 答句已開始而 RH subject 尾巴仍進行時，演算法需區分「subject 結束 / countersubject 開始」的時間點
- **真假答句辨識**：m3 LH 是否為 tonal answer（屬調直接回應），需配合 [concept_fugue](concept_fugue.md) §exposition convention 判斷
- **Inversion 偵測**：BWV 773 偶有倒影片段，但**不如 Inv 4 / Inv 8 密集**；inversion detector 若返回大量匹配，多半是 chromatic motion 局部音程巧合，建議提高信心門檻

## 4. 三段曲式對應到 form

| 段落 | 小節 | 調性 | 角色 |
|---|---|---|---|
| **Exposition** | m1–m6/7 | C minor → 過渡 | RH subject (m1–m2) → LH 屬調答句 (m3) → countersubject 互動展開 |
| **Modulation to E♭ / G minor** | m7–m15 | E♭ major（相對大調）→ G minor（屬小調） | 主題在新調出現；中段 sequence 與 voice-exchange |
| **Return** | m16–m21 | 回 C minor | Subject material 在主調回歸 |
| **Cadential extension** | m22–m27 | C minor (Picardy 第三可選) | 較長的 cadential 收尾（比 Inv 1 的 m21-m22 PAC 延伸更久） |

→ m6–m7、m14–m15、m21–m22 是三個明顯的**段落邊界**，皆可由 [concept_modulation_as_phrase_signal](concept_modulation_as_phrase_signal.md) 偵測；m26–m27 的 final PAC 由 [concept_cadence_detection](concept_cadence_detection.md) 偵測。注意此曲 cadential extension 長達 5–6 小節，比 Inv 1 的 2 小節長甚多——cadence detector 在 m22 觸發後，後續 m23–m27 仍可能誤判為新樂句，需配合 [concept_phrase_elision](concept_phrase_elision.md) 處理。

注意：依 *project_bach_inv_measure_mapping*，**Inv 2 的 user mN 與 program mN 一致（無偏移）**，但 `CLEF_CORRECTIONS[2]` 對 LH m4 有 bass→treble 修正——任何涉及 LH m4 的分析都需先確認譜號狀態。

## 5. Case Study A — Canon-like 段落的 per-hand 邊界張力

### 5.1 為什麼挑這段

Inv 2 的 canon-like 區段（典型如 exposition 後半與 development middle entries）讓兩聲部的**樂句邊界錯位**：RH subject 第 k 拍結束時，LH 答句才到第 k–2 拍——兩手的「呼吸點」不同步。

對 *feedback_phrase_as_breath* 的「呼吸 = 邊界 reset」原則而言，per-hand DP 的傳統做法（每手獨立切樂句）在這裡產生**結構性張力**：

- 若 RH / LH 各自找最佳 phrase split → 兩手的 reset 點不同，但音樂上是**一個 contrapuntal phrase**
- 若強制兩手共用 phrase split → 一手會被迫在非自然位置 reset

### 5.2 Override pattern 觀察

在 canon-like 段落，`BACH_INV_OVERRIDES[2]` 顯示一個重複出現的 pattern：**兩手在不同 measure pos 各自有 reset-type override**，且兩個 reset 點之間相隔約半小節到一小節——這正對應 imitation distance。

→ 換言之，user 教的指法**保留了 per-hand 邊界錯位**，沒有強制兩手同步 reset。這支持「per-hand phrase split」設計，但對 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 提出新要求：**subject entry 在兩手之間的時間差需明確標出**，否則 DP 在 LH 邊界處可能繼承來自 RH 的 phrase context，造成手位混亂。

### 5.3 對演算法的意涵

- **保留 per-hand phrase split**：不改 `_run_phrase_dp` 的 per-hand 結構
- **Subject entry 帶 hand-label**：[concept_subject_imitation_detection](concept_subject_imitation_detection.md) 輸出需附 `hand` 欄位，讓 DP 在另一手不誤判
- **Imitation distance 作為 phrase-seam tolerance**：若 LH entry 落在 RH subject 結束後 < 1 小節，視為 contrapuntal overlap，**不**將 RH 結束點當作 LH 樂句起點——對應 [concept_phrase_elision](concept_phrase_elision.md) 的對位版本

⚠ 上述邏輯尚未在程式碼中實作；本頁僅記錄需求。

## 6. Case Study B — Chromatic Descent 段落（briefer）

BWV 773 主題尾部與多個 development 段落含密集 chromatic motion（半音級進）。這些段落**並非 modulation 事件**——調性短時間內不變——但仍具備 [concept_modulation_as_phrase_signal](concept_modulation_as_phrase_signal.md) 所列的「voice-leading 訊號」特徵：

- **音高重心連續推進**：chromatic 半音級進使 [concept_figural_boundary_detection](concept_figural_boundary_detection.md) 的「音高重心跳幅」偵測在這裡幾乎不會觸發（每步只變 1 半音）
- **手位連續滑移**：chromatic 段內 fingering 必須處理頻繁的 thumb-pass 或 cross-finger，與 diatonic 段的「以 finger group 為單位移動」邏輯不同

→ 對 [concept_modulation_as_phrase_signal](concept_modulation_as_phrase_signal.md) 的**延伸用法**：即使無 modulation，密集 chromatic motion 仍可視為 voice-leading-driven phrase signal。`BACH_INV_OVERRIDES[2]` 在 chromatic 段落常出現**thumb-pass 集中**的 override pattern，與 [concept_running_passage_thumb_reservation](concept_running_passage_thumb_reservation.md) 的「跑動段預留拇指」原則衝突——chromatic 段反而要求**頻繁拇指穿越**，不能 reserve。

對 DP 的意涵：是否啟用 [concept_running_passage_thumb_reservation](concept_running_passage_thumb_reservation.md) 應**per-segment** 決定，而非 per-piece：diatonic running passages 啟用、chromatic descent 段關閉。⚠ 此分層尚未在 phrase-detection v1 實作。

## 7. 三類樂句邊界並用的必要性 — Inv 1 / Inv 2 / Inv 4 對照

| 邊界類型 | Inv 1 主要觸發點 | Inv 2 主要觸發點 | Inv 4 主要觸發點 |
|---|---|---|---|
| **Subject entry** ([concept_subject_imitation_detection](concept_subject_imitation_detection.md)) | Template: m1 RH + m3 LH (alg 不掃 template 內); 實測 RH @ m6/m12/m18/m19, LH @ m4/m6/m7 | Template: m1 RH + m3 LH 屬調答; 實測 RH @ m13/m23, LH @ m25 (musicology 預測 m11-15 modulation entries; alg 在屬調答後稀疏觸發) | Template: m1 RH + m3 LH; 實測 RH @ m18/m28/m32/m34/m50/m55, LH @ m12/m30/m40/m44/m53 |
| **Modulation / 段落** ([concept_modulation_as_phrase_signal](concept_modulation_as_phrase_signal.md)) | m6-m7, m14-m15, m18-m19 | m6-m7 (→E♭), m14-m15 (→g), m21-m22 (回 C) | mvt4 特定 modulation 邊界 |
| **Cadence** ([concept_cadence_detection](concept_cadence_detection.md)) | m21-m22 PAC | m26-m27 final PAC（+長 cadential extension） | episode 內小 cadences |
| **Figural** ([concept_figural_boundary_detection](concept_figural_boundary_detection.md)) | m20-m21 coda figure 切換 | chromatic descent 段落內**反例**（無 figural 跳幅但仍需邊界） | **m50 case (主角)**, episode figural shifts |

→ 三首合看：
  - **Inv 1**：modulation + cadence 為主、subject entry + figural 為輔
  - **Inv 2**：**subject entry 主導**（canon-like 密集 entries）、cadence 因 long extension 而需配合 elision、figural detector 在 chromatic 段反成 false-negative
  - **Inv 4**：figural boundary 主導（m50），subject entry 在 episode 失效

三首支持本套 wiki 的核心架構假設：**單一偵測軸無法完整描述 Bach Invention 樂句結構**；Inv 2 進一步顯示，**同一偵測軸在不同段落需 per-segment 開關**，不能 per-piece 一刀切。

## 8. 與其他 wiki 頁面的關係

- 與 [analysis_bach_inv_1_c_major](analysis_bach_inv_1_c_major.md) 形成 progression pair：Inv 1 主題模仿較鬆，Inv 2 緊密成 canon-like；對 imitation detector 是難度漸進
- 與 [analysis_bach_inv_4_d_minor](analysis_bach_inv_4_d_minor.md) 形成 contrast pair：Inv 2 強調 subject entry 主導，Inv 4 強調 figural boundary 主導
- 應用 [concept_fugue](concept_fugue.md) / [concept_counterpoint](concept_counterpoint.md) 對 2-voice 緊密 imitation 與 tonal answer 慣例的論述
- 對 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 提供 canon-like distance、tonal answer、hand-labelled entry 三項驗證需求
- 對 [concept_modulation_as_phrase_signal](concept_modulation_as_phrase_signal.md) 提供 m6-m7（→E♭）/ m14-m15（→g）/ m21-m22（回主）三個邊界，並延伸到「非 modulation 的 chromatic voice-leading」邊界
- 對 [concept_cadence_detection](concept_cadence_detection.md) 提供 long cadential extension（m22–m27）→ 需配合 [concept_phrase_elision](concept_phrase_elision.md) 避免 m23+ 誤判為新樂句
- 對 [concept_figural_boundary_detection](concept_figural_boundary_detection.md) 提供 chromatic 段的 false-negative 反例
- 對 [concept_running_passage_thumb_reservation](concept_running_passage_thumb_reservation.md) 提供 chromatic 段「不能 reserve」的反例 — 證明該規則需 per-segment 而非 per-piece
- 編輯版本爭議引 [src_bach_inventions_pedagogy](src_bach_inventions_pedagogy.md)
- 對位起源溯至 [src_fux_gradus_ad_parnassum](src_fux_gradus_ad_parnassum.md)
- Override semantics 解讀依 *feedback_override_semantics*、*feedback_phrase_as_breath*
- 個人化生物力學原則依 *feedback_personal_biomechanics*
- Measure 對應依 *project_bach_inv_measure_mapping*（Inv 2 無偏移；注意 LH m4 譜號修正）
