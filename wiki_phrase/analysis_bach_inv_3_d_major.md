# Analysis: Bach Invention 3 in D major (BWV 774) — 3/8 舞曲節拍與躍進主題

> 來源：musicology 文獻 + 預期 `BACH_INV_OVERRIDES[3]` 教學素材
> 對應 PIG：未列入 / 對照需另行查核
> 狀態：第三個 Bach Invention analysis 頁；subject detection 與 phrase detection 演算法輸出**驗證待跑**（⚠ 標記處）
> 觸發 case：3/8 拍 hypermeter 與 `_detect_phrase_starts` Pass 2 fallback 互動；ascending leap subject 的 RH 起手位

## 1. 為什麼挑這首作為 wiki 第三個 Bach analysis 頁

BWV 774 補足 [[analysis_bach_inv_1_c_major]]（C 大調 4/4，through-composed）與 [[analysis_bach_inv_4_d_minor]]（D 小調 3/8，episode-heavy）所未涵蓋的座標：

- **3/8 拍 + 大調 + dance-like character** — Inv 4 同為 3/8 但情緒陰鬱、Inv 1 為 4/4 步行；BWV 774 是唯一同時具備「3/8 + 上揚 + 舞曲」三條件的 Invention
- **Ascending leap subject** — 主題以八度或六度躍進開頭，與 Inv 1 (上行音階) / Inv 4 (下行 figure) 形成對比；對 [[concept_subject_imitation_detection]] 提供「leap-initiated subject」的測試案例
- **3/8 拍與 `_detect_phrase_starts` Pass 2 (4-bar fallback) 的互動** — 4-bar period 在 3/8 拍意義不同（4 bars × 3/8 = 12 eighth-notes ≈ 4/4 的 1.5 bars），需釐清 hypermeter 假設
- 教學定位上是 3/8 拍的入門曲，預備後續 minuet / gigue 風格作品

## 2. 曲目基本資訊

- **BWV 774**, 約 1723 (Bach 38 歲, Köthen — *Two-Part Inventions* 集第 3 首)
- **D major** (2 升), **3/8 拍**, **59 小節**（無反覆，through-composed）
- 形式：典型 2-voice Invention；exposition / modulation / subdominant-excursion / return 四段
- 主題特色：**ascending leap (octave or sixth)** + 緊接下行 16 分音符 figure；energetic、上揚 character
- Subject 長度：musicology 共識約 1 小節（= 3 個 8 分拍, 或 6 個 16 分音符位置）；但因 3/8 拍小節短，**跨小節 subject (m1→m2 pos1) 可能性需驗證**
- 教學定位：3/8 拍的 first taste，預備 minuet / gigue 風格的 hypermeter 感
- 著名版本：András Schiff (lively, light articulation), Angela Hewitt (dance-like phrasing, longer notes inégales), Glenn Gould 1964 (uncharacteristically lyrical for Gould)
- 編輯版本爭議：見 [[src_bach_inventions_pedagogy]]

## 3. Subject 識別 — musicology 共識與演算法測試計畫

### 3.1 Subject 長度的不確定性

不同於 [[analysis_bach_inv_1_c_major]] 的 1-bar vs 2-bar 兩派論辯，BWV 774 的 subject 長度因 **3/8 拍的小節極短**而本身就需驗證：

| 假設長度 | 16 分音符位置數 | musicological 對應 |
|---|---|---|
| **6 (1 小節)** | m1 完整 | 主流共識；leap + 下行 figure 自成單位 |
| **8 (1 又 1/3 小節)** | m1 + m2 前半 | 若 subject 延伸至 m2 pos1 結束 |
| **12 (2 小節)** | m1 + m2 完整 | 與 hypermeter 2-bar 群組一致 |

對 [[concept_subject_imitation_detection]] 演算法而言：應對此曲嘗試 length ∈ {6, 8, 12} 三組假設，以 LH 答句模仿位置（m3 或 m4）的匹配度決定哪一組成立。

### 3.2 預期 subject entries (待演算法驗證)

依 musicology 共識，預期演算法應抓到（以 user mN 標示）：

| Entry | 手 | 預期調性 | 段落角色 |
|---|---|---|---|
| m1 pos1 | RH | D major (I) | Exposition — subject 首次呈現 |
| m3 / m4 附近 | LH | A major (V) | Exposition — **5度上方答句** (real or tonal answer) |
| m13–m18 區段 | RH or LH | A major (V) | Modulation 後 entries |
| m25–m32 區段 | 兩手交替 | B minor (vi) | Subdominant / relative-minor excursion |
| m41–m50 區段 | 多次密集 | 返主, D major | Return entries — 此曲 final-section entries 密度較 Inv 1 高 |
| m55–m59 | RH | D major | Final cadence 前最後一次 |

⚠ **以上是 musicology 預測，尚未跑 `_detect_subject_entries` 驗證**。實際 entries 將補入 `_implementation_status.md`。

### 3.3 Ascending leap 對 detection 的影響

Inv 1 subject 起手是 stepwise (16 分音符上行)，Inv 4 subject 起手是 broken-triad 下行；BWV 774 的 ascending leap 對 [[concept_subject_imitation_detection]] 構成不同型態的 fingerprint：

- **單音程 fingerprint 過粗**：D5→D6（octave）或 D5→B5（sixth）僅 1 個音程，誤判機率高
- **leap + 後續下行 figure 才是完整 subject 簽章**：演算法應要求至少 5 個連續音程匹配（leap 1 + 下行 figure 4 個 stepwise）
- **TI (transposition-invariant) 比對在 leap subject 更可靠**：A 大調答句的 leap interval (A5→A6 或 A5→F#6) 與原調 leap 半音數相同

→ ⚠ 此預測需在 `_detect_subject_entries` 跑出 BWV 774 結果後檢驗。

### 3.4 倒影 (Inversion) 分析

BWV 774 中**倒影主題不顯著**。與 [[analysis_bach_inv_1_c_major]] 同，Bach 在 BWV 775 (Inv 4) 才大量用 strict inversion。Inv 3 中段主要用 sequence + 移調，inversion detection 應返回稀疏結果。

## 4. 四段曲式對應到 form

| 段落 | 小節 (user mN) | 調性 | 角色 |
|---|---|---|---|
| **Exposition** | m1–m12 | D major (I) | RH subject (m1) → LH 答句 (m3/m4) → 對位發展 |
| **Modulation to A major (V)** | m13–m24 | A major | 主題在屬調出現；含 sequence 與 voice exchange |
| **Subdominant / B minor excursion** | m25–m40 | B minor (vi) → G major (IV) 短暫 | 標準 Bach「離調至相對小調或下屬」 strategy；本段最長 |
| **Return + final cadence** | m41–m59 | D major (回主) | Final subject entries 密集 + cadential extension to PAC |

→ m12–m13、m24–m25、m40–m41 是三個明顯的**段落邊界**，皆可由 [[concept_modulation_as_phrase_signal]] 偵測；m58–m59 PAC 由 [[concept_cadence_detection]] 偵測。

**3/8 拍下的 measure-to-form ratio**：BWV 774 用 59 小節描述四段，每段平均 12–18 小節；對比 Inv 1 (4/4, 22 小節, 三段平均 7 小節) — 同樣 form complexity 在 3/8 拍展開為近 3× 小節數。**這對 `_detect_phrase_starts` Pass 2 (4-bar fallback) 假設有實質衝擊**，見 §5 Case A。

## 5. Case A — 3/8 拍對 phrase detection 的影響

### 5.1 為什麼這是 Case

`_detect_phrase_starts` Pass 2 在無硬斷點時使用「對齊至 2/4/6/8 小節」推斷 phrase_period（fallback = 4）。此 fallback 隱含**4/4 拍 hypermeter 4-bar = 16 拍**的假設。在 3/8 拍下：

- 4 bars × 3/8 = 12 eighth-notes ≈ 4/4 拍的 1.5 小節
- 真正的「呼吸單位」應對應 4/4 拍的 4-bar 群組，即 3/8 拍的 ≈11 小節（4×8 ÷ 3 = 10.67）

→ Pass 2 fallback 在 BWV 774 會**過度切分**樂句（每 4 個 3/8 小節 = 1 個 phrase），與 musicology 共識（每 11–12 個 3/8 小節 = 1 個 phrase）相差近 3×。

### 5.2 預期觸發行為

⚠ **未驗證**：若直接執行 `_detect_phrase_starts` 於 BWV 774：

- **Pass 1 (hard breaks)**：應抓到 m12–m13 / m24–m25 / m40–m41 段落邊界（皆為和聲 cadence + 短暫停頓）；3/8 拍小節跳幅 ≥1 仍會觸發
- **Pass 2 (period inference)**：若 Pass 1 抓到 3 個硬斷點，週期推斷可能落在 ≈12，但若 hard break 漏抓導致 < 2 個，fallback = 4 將失效
- **Pass 3 (soft break insertion)**：依 Pass 2 結果插入軟邊界

### 5.3 修正方向（討論用，不指定實作）

兩種對 3/8 拍的可能修正路徑：

1. **時值正規化 hypermeter**：Pass 2 改以「總 beats / target_phrase_beats」推斷，不直接用 measure 數；target = 32 拍（4/4 4 小節 ≈ 3/8 11 小節）
2. **拍號偵測 + per-time-signature fallback**：偵測為 3/8 / 6/8 時 fallback 改為 8 或 12 小節而非 4

→ 兩路徑都需 `_detect_phrase_starts` 介面變更，且需跨 [[analysis_bach_inv_4_d_minor]] (3/8 D minor) 同步驗證。**目前狀態：BWV 774 屬潛在 future case**，未啟用任何修正。

### 5.4 對 override 教學的影響

如果 Pass 2 過度切分，DP 將每 4 個 3/8 小節 reset 手位一次，產生**不自然的 fingering 切割**（user 視角會看到 m4→m5、m8→m9 等位置出現意料外的指法跳變）。User-curated overrides 將集中在這些位置以強制 hand-continuity — 即 override 密度可作為 phrase boundary 失準的**反向診斷信號**。

## 6. Case B — Ascending leap subject 對 RH 起手位的影響

### 6.1 為什麼這是 Case

BWV 774 m1 RH 起手 = ascending leap (D5 → D6 octave 或 D5 → B5 sixth, 依編輯版本)。對 RH 起手 finger 選擇有兩種主流路徑：

| 路徑 | m1 pos1 finger | 邏輯 |
|---|---|---|
| **A — Span-first** | f1 (拇指) | 拇指在低音，f5 在高音覆蓋 octave；保留全手張開可彈後續下行 figure |
| **B — Agility-first** | f2 (食指) | f2 在低音，f4/f5 在高音；f2 較 f1 靈活，預備下行 figure 的拇指穿越 |

兩派分別對應不同 hand-size 與 spanning 偏好。對 [[../score-claude/memory/feedback_personal_biomechanics]] 的個人化原則，user 將以 override 表達個人選擇。

### 6.2 對 DP cost function 的意涵

`_assignment_cost` 對 octave 跨度的成本（依 `FINGER_COMFORT_MAX_SPAN[(1,5)] = 12`）對 (1,5) 設為 [7, 12] zero-cost zone — 即 f1+f5 彈 octave 在 DP 看來是**零成本最佳解**。這應使路徑 A (f1) 自然從 DP 導出，無需 override。

→ ⚠ **驗證待跑**：若 DP 在 m1 pos1 給出 f1，user 是否仍會 override 為其他指法？若 user 全篇 BWV 774 m1-like 位置都允許 DP 預設，則 ascending leap subject 對 RH 起手位**不需特殊處理**；若 user 系統性 override，則需在 `_assignment_cost` 加入「subject-entry context preference」軸。

### 6.3 與 [[concept_subject_imitation_detection]] 的接口

若 [[concept_subject_imitation_detection]] 正確抓到 RH m1 為 subject entry，**未來可能設計**「subject-entry-aware 起手 finger 偏好」cost 軸 — 但這將跨越 phrase detection 與 biomechanics 兩個 discipline，需依 [[../score-claude/memory/feedback_phrase_analysis_is_its_own_discipline]] 謹慎處理。**目前不規劃實作**。

## 7. 三類樂句邊界並用的必要性

對 BWV 774，三類邊界各覆蓋不同 form 位置：

| 邊界類型 | Inv 3 觸發點 | 工具 |
|---|---|---|
| **Subject entry** | 主題 / 答句: m1 RH + m3/m4 LH (在演算法 template 內, 不會被標為 entry); 演算法掃描自 template 之後 — 實測 RH @ m18/m28/m32/m34/m50/m55, LH @ m12/m30/m40/m44/m53 (musicology 預測 m13-18 + m41-50; alg 部分 ✓ 但有 m28/32/34 等 extras; 見 [[../score-claude/memory/project_bach_inv_subject_detection_validation_2026-05-28]]) | [[concept_subject_imitation_detection]] |
| **Modulation / 段落** | m12-m13, m24-m25, m40-m41 | [[concept_modulation_as_phrase_signal]] |
| **Cadence** | m58-m59 PAC | [[concept_cadence_detection]] |
| **Figural** | 各段內 sequence boundary、下行 figure 切換點 | [[concept_figural_boundary_detection]] |

→ Inv 3 與 sibling analyses 對照：

- **Inv 1** (4/4, 22 小節)：modulation + cadence 主導；form 緊湊
- **Inv 3** (3/8, 59 小節)：modulation 主導；**3/8 拍 hypermeter 是獨立軸**；subject entries 密集於 return 段
- **Inv 4** (3/8, D minor)：figural boundary 主導 (m50 case)；同為 3/8 拍但情緒對比強烈

三首合看支持本 wiki 的核心架構：**單一偵測軸無法完整描述 Bach Invention 樂句結構**；額外地，**3/8 拍引入 hypermeter 假設這條獨立軸**，需與其他偵測軸正交考慮。

## 8. 與其他 wiki 頁面的關係

- 與 [[analysis_bach_inv_1_c_major]] 形成 4/4 vs 3/8 拍對照；與 [[analysis_bach_inv_4_d_minor]] 形成同拍號不同情緒對照
- 應用 [[concept_fugue]] / [[concept_counterpoint]] 對 2-voice Invention 的論述
- 對 [[concept_subject_imitation_detection]] 提供 ascending-leap subject 與多長度假設的驗證 case
- 對 [[concept_modulation_as_phrase_signal]] 提供 m12-m13 / m24-m25 / m40-m41 三個段落邊界
- 對 [[concept_cadence_detection]] 提供 m58-m59 PAC 案例
- 對 [[concept_figural_boundary_detection]] 提供 3/8 拍下 figure 切換的潛在案例
- 對 [[concept_running_passage_thumb_reservation]] 提供 3/8 拍下行 figure 的拇指預留討論點
- Hypermeter 與 3/8 拍 phrase rhythm 討論引 [[src_rothstein_phrase_rhythm]]
- 編輯版本爭議引 [[src_bach_inventions_pedagogy]]
- 對位起源溯至 [[src_fux_gradus_ad_parnassum]]
- Override semantics 解讀依 [[../score-claude/memory/feedback_override_semantics]]、[[../score-claude/memory/feedback_phrase_as_breath]]
- 個人化生物力學原則依 [[../score-claude/memory/feedback_personal_biomechanics]]
- Phrase analysis 獨立性原則依 [[../score-claude/memory/feedback_phrase_analysis_is_its_own_discipline]]
- Measure 對應依 [[../score-claude/memory/project_bach_inv_measure_mapping]]（Inv 3: user mN → program m(N-1)；`CLEF_CORRECTIONS[3]` LH m19–23 bass→treble；prog m26 = ghost）
