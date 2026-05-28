# Analysis: Bach Invention 5 in E♭ major (BWV 776) — Lyrical Subject 與 3-Flat 黑鍵指法

> 來源：musicology 文獻 + Bach Inventions performance practice
> 對應 PIG：未列入 / Bach Inv 5 非 PIG 主要對象
> 狀態：第三個 Bach Invention analysis 頁；subject detection / cadence detection 演算法輸出**驗證待跑**（⚠ 標記處）
> 觸發 case：3 flats (E♭ major) 的黑鍵 thumb-pass 互動；lyrical descending scale 觸發 long-scale thumb-under 候選

## 1. 為什麼挑這首作為 wiki 第三個 Bach analysis 頁

BWV 776 是 *Two-Part Inventions* (BWV 772–786) 的**第五首**，在 wiki 三首 Bach analysis pair 中扮演**調性 / texture 維度**對照：

- 與 [[analysis_bach_inv_1_c_major]] (C major, 無調號) 對照：BWV 776 有 **3 個降號**，是黑鍵 thumb-pass 互動的最小可行 test case
- 與 [[analysis_bach_inv_4_d_minor]] (D minor, episode/figural 為主) 對照：BWV 776 是 *lyrical / cantabile* 風格，subject 較長且包含 descending scale，更接近 [[concept_running_passage_thumb_reservation]] 的觸發情境
- musicology 上常被視為 *Inventions* 集中**表情最豐富 (espressivo)** 的一首，Schiff Bach Lectures 將其列為 cantabile 教學典範
- 教學定位：學生在掌握前 4 首 (C major / C minor / D major / D minor) 後，BWV 776 是 *3-flat 調性的第一課*，預備後續 Suite-style fingering

## 2. 曲目基本資訊

- **BWV 776**, 約 1722–23 (Bach 37–38 歲, Köthen 時期；與其他 Inventions 同期撰於 *Clavier-Büchlein für Wilhelm Friedemann Bach*)
- **E♭ major** (3 flats: B♭, E♭, A♭), 4/4 拍, **32 小節**（無反覆，through-composed；長度為 BWV 772 的約 1.5 倍）
- 形式：典型 2-voice Invention；exposition / modulation / development / return 四段論
- 主題特色：**descending scale + arpeggio** 結合 — 起句下行八度級進 (cantabile 線條)，後半轉為琶音上行 (active counter-motion)
- Subject 長度：約 1–2 小節（musicology 共識傾向 1.5-bar：m1 完整 + m2 上半，⚠ 待 [[concept_subject_imitation_detection]] 驗證）
- 著名版本：András Schiff (cantabile 經典詮釋), Angela Hewitt (Bach edition 推薦聆聽), Glenn Gould 1964 (articulated 對比)
- 編輯版本爭議：見 [[src_bach_inventions_pedagogy]]

## 3. Subject 識別 — musicology 共識與演算法測試計畫

### 3.1 Subject 長度的歷史辯論

BWV 776 的 subject 因為**包含兩個 sub-motives** (descending scale + arpeggio)，subject 長度判定比 BWV 772 更複雜：

| 派別 | Subject 範圍 | 代表 |
|---|---|---|
| **1.5-bar 派** | m1 完整 + m2 上半 (含 scale + arpeggio 兩個 sub-motives) | Schiff, 多數現代 Urtext 編輯 |
| **2-bar 派** | m1 + m2 完整 phrase | Czerny 教學版傳統 |
| **1-bar 派** | 僅 m1 (僅 descending scale sub-motive) | 部分 Schenkerian 分析 |

對 [[concept_subject_imitation_detection]] 演算法而言，**1.5-bar 假設較精確**：LH 在 m3 出現 8va 下方答句時，重現的是 m1 + m2 上半的完整 contour，而非僅 m1 的 scale 段。

### 3.2 預期 subject entries (待演算法驗證)

依 musicology 共識（1.5-bar subject 假設），預期 [[concept_subject_imitation_detection]] 演算法應抓到：

| Entry | 手 | 段落角色 |
|---|---|---|
| m1 pos1 | RH | Exposition — subject 第一次呈現 (E♭ 起音) |
| m3 附近 | LH | Exposition — **8va 下方模仿** (參 [[concept_counterpoint]] §模仿規則) |
| m10–m12 附近 | LH or RH | Modulation — subject 移調至 B♭ major (V) |
| m17–m20 附近 | 兩手交替 | Development — subdominant (A♭ major) excursion 中的 middle entries |
| m22–m25 附近 | 兩手交替 | Voice exchange 段（⚠ 兩手主題互換是 BWV 776 已知 musicology 特徵但需逐音驗證）|
| m27–m30 附近 | RH 為主 | Return + final entries 進 PAC 之前 |

⚠ **以上是 musicology 預測，尚未跑 `_detect_subject_entries` 驗證**。實際 entries 將補入 `_implementation_status.md`，本頁僅記錄理論預測。

### 3.3 倒影 (Inversion) 與 Sequence 分析

BWV 776 中**倒影主題不顯著**（Bach 在 BWV 775 (Inv 4) 才大量使用 strict inversion）。但 BWV 776 中段有顯著的 **sequence + voice exchange** — m17–m26 區段 subject material 在兩手間互換時，配合下行 5th 序列（標準 Bach modulation device）。對演算法的意涵：sequence detection 在這首應**返回明顯密集匹配**，可作為 [[concept_modulation_as_phrase_signal]] 的良性訊號。

## 4. 四段曲式對應到 form

| 段落 | 小節 (user mN) | 調性 | 角色 |
|---|---|---|---|
| **Exposition** | m1–m9 | E♭ major | RH subject (m1) → LH 8va 模仿 (m3) → counter-development with both voices |
| **Modulation to B♭** | m10–m16 | B♭ major (V) | 主題在屬調出現；sequence 序列下行帶到 V 的穩定 cadence |
| **Subdominant excursion** | m17–m26 | A♭ major (IV) → C minor (vi) → 過渡 | 標準 Bach「離調至下屬」strategy；voice exchange 密集區 |
| **Return + final cadence** | m27–m32 | E♭ major (回主) | Final subject entries + cadential extension + PAC |

→ m9–m10、m16–m17、m26–m27 是三個明顯的**段落邊界**，皆可由 [[concept_modulation_as_phrase_signal]] 偵測；m31–m32 PAC 由 [[concept_cadence_detection]] 偵測。

⚠ 確切調性轉折點需逐小節對 score 確認；本頁 boundary 估計以 musicology 共識 8/8/10/6 比例切分。

## 5. Case A — 3 Flats 對指法選擇的影響

### 5.1 為什麼挑這個議題

C major 的 BWV 772 + D minor 的 BWV 775 都是**單調號**或**無調號**曲目；BWV 776 的 3 flats 是 Bach Inv 集中**第一個多調號考驗**。這對指法演算法的影響在於：

- E♭ / A♭ / B♭ 三音均為**黑鍵**
- E♭ major 音階：E♭ – F – G – A♭ – B♭ – C – D – E♭ → 7 音中**3 個黑鍵**
- 黑鍵頻率高 → 拇指落黑鍵機率高 → `THUMB_PASS_BLACK_PENALTY = 1.5` (Parncutt Rule 11) 觸發頻率高

### 5.2 對 DP cost 結構的影響

E♭ major 與 C major 比較，預期 DP behavior 變化：

| Cost 項 | C major (BWV 772) | E♭ major (BWV 776) | 結果 |
|---|---|---|---|
| `THUMB_PASS_BLACK_PENALTY = 1.5` | 偶發觸發 | 高頻觸發（scale 經過黑鍵）| BWV 776 中 thumb-pass 應更傾向落在 F/C/D (白鍵) |
| `LH_PINKY_BLACK_KEY_PENALTY = 2.0` | 罕見 | LH 和弦 root 含 E♭/A♭/B♭ 時頻繁 | LH 和弦 voicing 應傾向 f4 而非 f5 在黑鍵 |
| `PINKY_BLACK_MELODY_PENALTY = 0.8` | 罕見 | RH 旋律 cantabile 段尾常落 E♭ | RH 旋律 f5 在 E♭5 / B♭5 應加 0.8 |

→ **預期 BWV 776 是測試這三條黑鍵 cost rule 在 high-density 情境下表現的良性 case**。若 DP 在 BWV 776 上的 PIG 表現顯著低於 BWV 772（差距 > 5pp），可能指示某條黑鍵罰**校準不足**（非 user 演奏實態）。⚠ 實測待跑。

### 5.3 與 user override 的潛在互動

若 user 對 BWV 776 教導 overrides，預期會出現**與 C major 不同的 fingering pattern**：

- E♭ major 音階上行：RH 常用指法 3-1-2-3-1-2-3-4 或 2-1-2-3-1-2-3-4（拇指落 G / C 白鍵）
- E♭ major 音階下行：RH 4-3-2-1-3-2-1 或 5-4-3-2-1-3-2-1
- LH 八度跨度 (E♭2 → E♭3) 含黑鍵時，f5-f1 vs f4-f1 選擇被 `LH_PINKY_BLACK_KEY_PENALTY` 牽引

→ 這對 [[../score-claude/memory/feedback_personal_biomechanics]] 的**個人化原則**形成有趣對比：黑鍵指法選擇有較強的**生物力學基底** (Sandor: 黑鍵指法的 3-4 finger group 偏好較不依個人差異)，user override 在 BWV 776 上應顯示**較高的 cross-piece consistency**（與 BWV 772 比較）。⚠ 待 user 教 overrides 驗證。

## 6. Case B — Lyrical Descending Scale 觸發 Long-Scale Thumb-Under

### 6.1 為什麼挑這個議題

BWV 776 開頭 subject 即包含 **descending scale 段** (m1 RH: E♭5 → D5 → C5 → B♭4 → A♭4 → G4 → F4 → E♭4，下行八度級進)。這正是 [[concept_running_passage_thumb_reservation]] 的觸發情境，也是 `project_long_scale_thumb_under` rule 的 candidate scenario。

### 6.2 與 Long-Scale Thumb-Under Rule 的關係

依 [[../score-claude/memory/project_long_scale_thumb_under]]：

> Cancels `_transition_cost` WRONG_DIRECTION + THUMB_PASS_UPWARD_EXTRA on thumb-pass inside scale segments

BWV 776 m1 RH descending scale 的指法（musicology 共識）：

- **Schiff cantabile 推薦**：5-4-3-2-1-3-2-1 (下行時 f1 穿越 / thumb-under twice)
- **Czerny 傳統**：5-4-3-2-1-4-3-2-1 (添加 f4 作為 second thumb-under pivot)

兩種指法均包含**至少一次 thumb-under in scale segment**。若 BWV 776 啟用 long-scale rule：

- DP 在 m1 RH scale 段應接受 thumb-under 而不加罰
- DP 預期輸出與 Schiff 詮釋對齊（5-4-3-2-1-3-2-1）

### 6.3 BWV 776 作為 Long-Scale Rule 的驗證 candidate

雖然 `project_long_scale_thumb_under` 目前 (2026-05-27) 已驗證 K545 + K283（Mozart 古典時期 scale-heavy 曲目），但 Bach Inv 5 是**巴洛克 cantabile 的對應 case**：

| 對照維度 | K545 (Mozart) | BWV 776 (Bach) |
|---|---|---|
| 風格 | Classical Alberti + scale | Baroque cantabile + scale |
| Scale 長度 | 較長 (8+ 音) | 中等 (8 音八度級進) |
| 觸發頻率 | 高 (跑動段落) | 中 (lyrical line) |
| Long-scale rule benefit | +7.56pp (verified) | ⚠ 預期 mild +1~+3pp |

→ BWV 776 可作為 long-scale rule 在 **baroque texture** 下的驗證 case，但 Bach Inv 一般非訓練主要對象，per-piece opt-in 啟用前應先評估 ROI。

### 6.4 Thumb Reservation 的可能觸發

m1 後半 → m2 上半的 arpeggio 段 (E♭ – G – B♭ 上行琶音) 是典型 [[concept_running_passage_thumb_reservation]] 場景：拇指若在 scale 段尾 (m1 結束 E♭4) 已使用，arpeggio 段 (m2 開頭重新上行) 需要 reset 拇指位置。

依 thumb reservation 原則：跑動段落中拇指不應落在「easy 黑鍵」位置（避免後續被迫穿越）。BWV 776 m1-m2 接縫處的 fingering 選擇正是測試 reservation rule 的 sweet spot。

## 7. 三類樂句邊界並用的必要性

對 BWV 776，三類邊界各覆蓋不同 form 位置：

| 邊界類型 | Inv 5 觸發點 | 工具 |
|---|---|---|
| **Subject entry** | m1 RH, m3 LH, m10–m12 modulation entries, m22–m25 voice exchange, m27–m30 final entries | [[concept_subject_imitation_detection]] |
| **Modulation / 段落** | m9–m10, m16–m17, m26–m27 | [[concept_modulation_as_phrase_signal]] |
| **Cadence** | m31–m32 PAC, 可能 m16 IAC (modulation end) | [[concept_cadence_detection]] |
| **Figural** | m1-m2 scale→arpeggio sub-motive 切換、m17-m26 sequence 內 figure 轉折 | [[concept_figural_boundary_detection]] |
| **Texture (黑鍵指法)** | 全曲適用，但 m17–m26 voice exchange 段最密集 | (黑鍵 cost rules，非獨立 phrase 軸) |

→ Inv 5 與其他兩首 analysis 對照：
  - [[analysis_bach_inv_1_c_major]]: modulation + cadence 主導，coda figural 補充
  - [[analysis_bach_inv_4_d_minor]]: figural boundary 主導 (m50 case)，subject entry 抓不到 episode/coda
  - **Inv 5: subject entry + thumb-related rules 主導**（cantabile + 3-flat black-key 互動）

三首合看支持本套 wiki 的核心架構假設：**單一偵測軸無法完整描述 Bach Invention 樂句結構**；不同曲目觸發不同 boundary axes。

## 8. 與其他 wiki 頁面的關係

- 與 [[analysis_bach_inv_1_c_major]]、[[analysis_bach_inv_4_d_minor]] 形成 Bach Inv triplet (C major / D minor / E♭ major)，涵蓋不同調性 + form 主導軸
- 應用 [[concept_fugue]] / [[concept_counterpoint]] 對 2-voice Invention 的論述
- 對 [[concept_subject_imitation_detection]] 提供 1.5-bar subject 假設的驗證 case (與 BWV 772 1-bar 派形成對照)
- 對 [[concept_modulation_as_phrase_signal]] 提供 m9–m10 / m16–m17 / m26–m27 三個調性轉折點
- 對 [[concept_cadence_detection]] 提供 m31–m32 PAC + m16 IAC 案例
- 對 [[concept_running_passage_thumb_reservation]] 提供 m1-m2 cantabile descending scale + arpeggio 接縫案例
- 對 `[[../score-claude/memory/project_long_scale_thumb_under]]` 提供 baroque cantabile candidate（與 Mozart K545/K283 形成 era 對照）
- 黑鍵指法討論引 [[src_bach_inventions_pedagogy]]（Schiff cantabile 推薦 vs Czerny 傳統）
- 對位起源溯至 [[src_fux_gradus_ad_parnassum]]
- Override semantics 解讀依 [[../score-claude/memory/feedback_override_semantics]]、[[../score-claude/memory/feedback_phrase_as_breath]]
- 個人化生物力學原則依 [[../score-claude/memory/feedback_personal_biomechanics]]
- Measure 對應依 [[../score-claude/memory/project_bach_inv_measure_mapping]]（mvt5 對應 entries 須查表）
