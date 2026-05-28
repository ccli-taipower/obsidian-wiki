# Analysis: Bach Invention 8 in F major (BWV 779) — Broken-Triad Subject 與 LH Clef-Change Phrase 框架

> 來源：musicology 文獻 + user-curated `BACH_INV_OVERRIDES[8]` (待擴充)
> 對應 PIG：未列入 / 對照需另行查核
> 狀態：第三個 Bach Invention analysis 頁;subject detection 演算法輸出**驗證待跑**（⚠ 標記處）
> 觸發 case：descending broken triad subject、3/4 拍 cross-bar motif、LH bass→treble clef change 段

## 1. 為什麼挑這首作為 wiki 第三個 Bach analysis 頁

BWV 779 在 *Two-Part Inventions* (BWV 772–786) 中具有三項對 wiki 框架特別有價值的特徵：

- **3/4 拍**：與 Inv 3 (BWV 774, D major) 和 Inv 6 (BWV 777, E major) 的 3/8 拍 gigue-like 不同，Inv 8 是 minuet-like 三拍子；提供 *non-3/8 三拍子 Invention* 的 cross-bar motif 驗證案例
- **Descending broken triad subject**：與 Inv 1 / Inv 4 的 stepwise figure subject 形成對比；測試 [[concept_subject_imitation_detection]] 對 *chord-arpeggio motif* 而非 *scalar motif* 的識別能力
- **LH bass→treble clef change**：是 *Two-Part Inventions* 中**最知名的 LH 譜號臨時變更案例**；提供 [[concept_modulation_as_phrase_signal]] 與譜號變更的**獨立性測試**
- 與 [[analysis_bach_inv_1_c_major]] / [[analysis_bach_inv_4_d_minor]] 三首合看：C major + D minor + F major，4/4 + 3/8 + 3/4，stepwise + chromatic + broken-triad，覆蓋 *Inventions* 集主要 form 變數

## 2. 曲目基本資訊

- **BWV 779**, 約 1722–23 (Bach 37–38 歲, Köthen)
- **F major** (1 flat), **3/4 拍**, **34 小節**（無反覆，through-composed）
- 形式：典型 2-voice Invention；exposition / modulation / return 三段論
- 教學定位：*Inventions* 集第 8 首；3/4 拍下的 Bach 鍵盤教學典範
- 主題特色：**descending broken triad** + 上揚 16 分音符 figure；典型 F major *bright, joyful* character；與 Inv 1 的上行 stepwise subject 截然不同
- 著名版本：András Schiff (Bach Lectures), Angela Hewitt (Hyperion), Glenn Gould 1964 — Schiff 與 Hewitt 在此曲詮釋上特別受推崇
- 編輯版本爭議：見 [[src_bach_inventions_pedagogy]]

## 3. Subject 識別 — musicology 共識與演算法測試計畫

### 3.1 Subject 長度與 figure 結構

BWV 779 的 subject 約 1-2 小節（4 個 quarter beats + 後續 16 分音符 figure）：

| 組成 | 內容 |
|---|---|
| **Head motif** | Descending broken triad (F-A-C 或 root-third-fifth pattern) |
| **Continuation** | 上揚 16 分音符 figure，補完 1-2 小節 phrase |
| **Cadential close** | 短暫落在 V 或回 I |

與 Inv 1 (BWV 772) 的純 stepwise subject 不同，Inv 8 的 head motif 是 **chord-arpeggio 性質**。對 [[concept_subject_imitation_detection]] 演算法的意涵：

- 若演算法只比對 *interval sequence*，descending broken triad（major third + minor third 或變體）模式須與 stepwise (whole/half step) 模式並列為兩個獨立 subject template
- ⚠ **演算法目前是否能識別 broken triad 為 motif unit 待驗證**

### 3.2 預期 subject entries (待演算法驗證)

依 musicology 共識（broken triad subject 假設），預期演算法應抓到：

| Entry | 手 | 段落角色 |
|---|---|---|
| m1 pos1 | RH | Exposition — subject 第一次呈現（F major broken triad）|
| 約 m3 | LH | Exposition — **8va 下方模仿** (典型 Bach Inv 答句慣例，參 [[concept_counterpoint]] §模仿規則) |
| m7-m8 附近 | LH or RH | 過渡 — subject 開始片段化發展 |
| m11 / m15 附近 | 兩手交替 | Middle entries 在 V 段（C major）|
| m25-m28 附近 | RH 為主 | Return — subject 重現主調 |

⚠ **以上是 musicology 預測，尚未跑 `_detect_subject_entries` 驗證**。實際 entries 將補入 `_implementation_status.md`，本頁僅記錄理論預測。

### 3.3 倒影 (Inversion) 與 voice exchange

BWV 779 中段傾向 **voice exchange** 多於 strict inversion——RH/LH 角色互換比 motif 倒影更頻繁。這與 Inv 4 (BWV 775) 的 strict inversion 主導風格形成對比。對演算法意涵：voice exchange detection 是獨立軸，與 inversion detection 不互斥，須分開實作或標記。

## 4. 三段曲式對應到 form

| 段落 | 小節 (user mN) | 調性 | 角色 |
|---|---|---|---|
| **Exposition** | m1–m7 | F major | RH subject (m1) → LH 8va 模仿（約 m3）→ 短暫展開 |
| **Modulation to C major (V)** | m8–m20 | C major (V) | 主題在屬調出現；含 sequence + voice exchange；**LH 譜號變更可能發生於此段** |
| **Return + cadential extension** | m21–m34 | F major (回主) | Final subject entries + cadential close |

→ m7–m8、m20–m21 是兩個明顯的**段落邊界**，皆可由 [[concept_modulation_as_phrase_signal]] 偵測；最終 cadence 由 [[concept_cadence_detection]] 偵測。

## 5. Case Study A — Descending Broken-Triad Subject 對手位的影響

### 5.1 RH 起手 fingering 邏輯

F major broken triad (F-A-C, e.g. F4-A4-C5) 作為起首 head motif，跨度為 **perfect fifth (7 半音)**。RH 起手有兩個合理選擇：

| 選擇 | f1-f3-f5 (root-third-fifth) | f1-f2-f5 |
|---|---|---|
| **手位含意** | 寬手位、典型 broken-chord 指法 | 拇指—食指—小指，後續 stepwise figuration 友善 |
| **下行 broken triad 後接 16 分音符** | f5 已在 C5 高位，下行 figure 自然往中音域行 | f5 同上，但 f2 已用，inner fingers 餘量較少 |
| **概念對應** | 對應 broken-chord 廣義跨度規則 | 對應 [[concept_running_passage_thumb_reservation]] |

→ Subject head 的 fingering 不能孤立決定，**必須考慮其後 16 分音符 figure 的走向**。這是 phrase-level fingering reasoning 的典型 case：head motif 本身可有多解，後續 figure 才決定唯一解。

### 5.2 對演算法的意涵

[[concept_subject_imitation_detection]] 標記 subject head 後，DP 在 head + continuation 兩段必須當作**單一 fingering unit** 處理，避免 head 用本地最優、continuation 卡死。對應 wiki_piano 的 finger span table 規則：RH (1,5) comfort span = 7-12 半音，broken F major triad（7 半音）落在 comfort range，但其後 figure 若需在 C5 上方延伸到 D5/E5，f5 已 used 將強迫 hand jump。

## 6. Case Study B — LH Bass-to-Treble Clef Change 段的 Phrase 邊界意義

### 6.1 為什麼 Bach 在 LH 用 treble clef

3/4 拍 F major Invention 中段 modulation 到 C major (V) 後，LH 聲部跨入中央 C 上方音域是常見現象。Bach 為避免 LH 譜表出現過多 ledger lines（5 線以上），選擇**臨時將 LH 譜號改為 treble clef**，結束相關段落後改回 bass clef。

→ 這是 **engraving 慣例**，不是 voice change，也不是 hand re-assignment——LH 仍由左手彈奏，僅是記譜換譜號。

### 6.2 Clef change 與 phrase boundary 的關係

Clef change 是 **記譜事件**，phrase boundary 是 **musical event**。兩者**不一定同步**，但在 Bach Inventions 中**常同時發生**，因為：

- Engraver 通常在 phrase / 段落邊界處切換譜號（與斷句點對齊，視覺乾淨）
- LH 跨入中央 C 上方常意味著 voice exchange 或 modulation——本身就是 phrase signal

對 [[concept_modulation_as_phrase_signal]] 演算法的意涵：**不應將 clef change 直接當 phrase boundary**，因為這會把 engraving 決策（記譜方便）與 musical structure 混淆。正確做法是**獨立偵測 modulation / cadence / figural boundary，再驗證是否與 clef change 對齊**。若對齊則互相印證；若不對齊則代表此 clef change 純為 engraving，不應觸發 phrase reset。

### 6.3 為什麼 Inv 8 在 OMR 系統上特別 challenging

對 OMR (Optical Music Recognition) 而言，LH 譜號臨時變更是**最容易遺漏整段 voice 的 case**：

- OMR 系統在識別譜號時，若 clef change 緊鄰節線、ledger lines 密集、或 staff 重疊處理失誤，可能誤判 LH 聲部為空
- 結果：clef change 段 LH 整段 voice 缺失，整首 LH analysis 連帶崩潰
- Inv 8 是 *Two-Part Inventions* 中**最常被引用為此類 OMR 失敗案例的曲目**，因為 clef change 持續數個小節且範圍明顯

→ 對 phrase detection 演算法的意涵：若 LH 在中段突然「消失」（音符數異常少），不應假設這是 musical event（如 long rest），而應先檢查譜號變更是否被正確處理。**Phrase boundary 演算法須對 OMR 失敗 robust**——缺失的 voice 不等於 phrase 結束。

### 6.4 3/4 拍 cross-bar motif 的額外挑戰

3/4 拍下 Bach 主題常**跨越節線**（m1 末 1 拍 + m2 頭 2 拍 = 完整 subject head）。OMR 的小節對齊在 cross-bar motif 上容易**把 motif 尾巴歸入下一小節**，造成：

- Fingering 分析時 head motif 被切成兩段，head + continuation 的 fingering unit 邏輯（見 §5.1）破裂
- Phrase boundary 偵測誤把節線當邊界，把單一 phrase 切成兩個

→ 對演算法意涵：[[concept_figural_boundary_detection]] 與 [[concept_subject_imitation_detection]] 都須能**跨節線連續分析**，不可預設「節線 = potential boundary」。

## 7. 三類樂句邊界並用的必要性

對 BWV 779，三類邊界各覆蓋不同 form 位置：

| 邊界類型 | Inv 8 觸發點 | 工具 |
|---|---|---|
| **Subject entry** | m1 RH, 約 m3 LH, middle entries, m25+ final entries | [[concept_subject_imitation_detection]] |
| **Modulation / 段落** | m7-m8 (→ V), m20-m21 (回 I) | [[concept_modulation_as_phrase_signal]] |
| **Cadence** | 最終 PAC（約 m32-m34） | [[concept_cadence_detection]] |
| **Figural** | Cross-bar broken triad 切換點、中段 sequence boundary | [[concept_figural_boundary_detection]] |
| **Clef change**（**非 phrase 邊界**）| LH bass→treble 中段 | 獨立軸；不應觸發 phrase reset |

→ Inv 8 三方對照：
  - Inv 1: modulation + cadence 是主角，stepwise subject
  - Inv 4: figural boundary 是主角 (m50 case)，chromatic subject
  - Inv 8: **broken-triad subject + cross-bar motif + clef change** 是三項獨特挑戰

三首合看支持本套 wiki 的核心架構假設：**單一偵測軸無法完整描述 Bach Invention 樂句結構**，且 **OMR / engraving 事件須與 musical 事件獨立處理**。

## 8. 與其他 wiki 頁面的關係

- 與 [[analysis_bach_inv_1_c_major]] 形成 stepwise vs broken-triad subject 對照
- 與 [[analysis_bach_inv_4_d_minor]] 形成 modulation-driven vs figural-driven 對照
- 應用 [[concept_fugue]] / [[concept_counterpoint]] 對 2-voice Invention 的論述
- 對 [[concept_subject_imitation_detection]] 提供 *broken-triad / chord-arpeggio motif* 識別 case（與 stepwise motif 並列）
- 對 [[concept_modulation_as_phrase_signal]] 提供 m7-m8 / m20-m21 兩個邊界 + **clef change 不應觸發 phrase reset** 的反例
- 對 [[concept_cadence_detection]] 提供 m32-m34 PAC 案例
- 對 [[concept_figural_boundary_detection]] 提供 cross-bar broken-triad figure 切換案例
- 編輯版本爭議引 [[src_bach_inventions_pedagogy]]
- 對位起源溯至 [[src_fux_gradus_ad_parnassum]]
- Override semantics 解讀依 [[../score-claude/memory/feedback_override_semantics]]、[[../score-claude/memory/feedback_phrase_as_breath]]
- 個人化生物力學原則依 [[../score-claude/memory/feedback_personal_biomechanics]]
- Measure 對應依 [[../score-claude/memory/project_bach_inv_measure_mapping]]
