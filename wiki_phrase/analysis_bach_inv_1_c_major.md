# Analysis: Bach Invention 1 in C major (BWV 772) — Exposition 與 Coda 樂句框架

> 來源：musicology 文獻 + user-curated `BACH_INV_OVERRIDES[1]` (≈85 positions)
> 對應 PIG：未列入 / 對照需另行查核
> 狀態：第二個 Bach Invention analysis 頁；subject detection 演算法輸出**驗證待跑**（⚠ 標記處）
> 觸發 case：m21-22 coda 段 RH override 密集；m6-m7 modulation 邊界

## 1. 為什麼挑這首作為 wiki 第二個 Bach analysis 頁

BWV 772 是 *Two-Part Inventions* (BWV 772–786) 的**首篇**，也是 Bach 教學遺產中最被研究的鍵盤主題之一：

- 是 [concept_fugue](concept_fugue.md) / [concept_counterpoint](concept_counterpoint.md) 框架最乾淨的測試案例（純 2 聲部，無聲部加入 / 退出的混淆）
- C 大調無調號變化、無譜號變化，可隔離出**樂句邊界本身**而不被 key/clef 雜訊掩蓋
- user 已 hand-curate `BACH_INV_OVERRIDES[1]` 涵蓋 ≈85 個位置，分布橫跨 exposition / development / coda 三段
- 與 [analysis_bach_inv_4_d_minor](analysis_bach_inv_4_d_minor.md) 形成對照：mvt4 重點在 episode/coda 內 figural boundary；mvt1 重點在 exposition modulation + cadential coda

## 2. 曲目基本資訊

- **BWV 772**, 約 1722–23 (Bach 37–38 歲, Köthen)
- **C major**, 4/4 拍, **22 小節**（無反覆，through-composed）
- 形式：典型 2-voice Invention；exposition / development / recap 三段論
- 教學定位：W. F. Bach 鍵盤教本首篇，後成 *Clavier-Büchlein* 與 *Inventions* 集第一首
- 主題特色：上行 16 分音符 figure（C–D–E–F–D–E–C–G or similar）—— 西方鍵盤教學史上被引用最頻繁的 subject 之一
- 著名版本：Glenn Gould 1964 (legendary articulated), Angela Hewitt, András Schiff (Bach Lectures)
- 編輯版本爭議：見 [src_bach_inventions_pedagogy](src_bach_inventions_pedagogy.md)

## 3. Subject 識別 — musicology 共識與演算法測試計畫

### 3.1 Subject 長度的歷史辯論

關於 BWV 772 的 subject 長度，主要有兩派：

| 派別 | Subject 範圍 | 代表 |
|---|---|---|
| **2-bar 派** | m1 + m2 完整 phrase | Czerny 教學版、多數現代 Urtext 編輯 |
| **1-bar 派** | 僅 m1 上行 figure (8 群 16 分音符) | Schenkerian 分析、許多現代 Bach 研究者 |

兩派的分歧反映在 fingering 標注傳統：2-bar 派把 m2 視為 subject 延續、傾向手位連貫；1-bar 派把 m2 視為**回應 / 對位** (countersubject-like)、允許 m1-m2 之間 hand reset。詳見 [src_bach_inventions_pedagogy](src_bach_inventions_pedagogy.md)。

對 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 的演算法而言，**1-bar (length≈8 groups) 派假設較好驗證**：m3 LH 的 8va 下方模仿是 1-bar 派的核心證據，因 m3 LH 只重現了 m1 RH 的 figure，未重現 m2。

### 3.2 預期 subject entries (待演算法驗證)

依 musicology 共識（1-bar subject 假設），預期 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 演算法應抓到：

| Entry | 手 | 段落角色 |
|---|---|---|
| m1 pos1 | RH | Exposition — subject 第一次呈現 |
| m3 pos1 | LH | Exposition — **8va 下方模仿** (典型 Bach Inv 答句慣例，參 [concept_counterpoint](concept_counterpoint.md) §模仿規則) |
| m7 附近 | LH or RH | Modulation 起點 — subject 移調至 G 大調 (V) |
| m11 / m15 附近 | 兩手交替 | Development middle entries (subdominant excursion 或 ii–V 序列) |
| m19–m21 附近 | RH 為主 | Final entries 進 PAC 之前 |

⚠ **以上是 musicology 預測，尚未跑 `_detect_subject_entries` 驗證**。實際 entries 將補入 `_implementation_status.md`，本頁僅記錄理論預測。

### 3.3 倒影 (Inversion) 分析

BWV 772 中**倒影主題不顯著**。Bach 在 BWV 775 (Inv 4) 才大量使用 strict inversion。Inv 1 的中段更傾向用**sequence + 移調**而非倒影。對演算法的意涵：inversion detection 在這首應**返回稀疏結果**，若返回密集匹配，多半是 sequence 內局部音程巧合，需提高信心門檻。

## 4. 三段曲式對應到 form

| 段落 | 小節 (user mN) | 調性 | 角色 |
|---|---|---|---|
| **Exposition** | m1–m6 | C → 過渡 | RH subject (m1) → LH 8va 模仿 (m3) → 開始發展 |
| **Modulation to G** | m7–m14 | G major (V) | 主題在屬調出現；含 sequence 與 voice exchange |
| **Subdominant excursion** | m15–m18 | F or D minor (短暫) | 標準 Bach「離調至下屬」 strategy |
| **Return + final cadence** | m19–m22 | C major (回主) | Final subject entries + cadential extension |

→ m6–m7、m14–m15、m18–m19 是三個明顯的**段落邊界**，皆可由 [concept_modulation_as_phrase_signal](concept_modulation_as_phrase_signal.md) 偵測；m21–m22 PAC 由 [concept_cadence_detection](concept_cadence_detection.md) 偵測。

## 5. Case Study — m21–m22 Coda 段的 fingering 邏輯

### 5.1 為什麼挑這段

`BACH_INV_OVERRIDES[1]` 在 m19–m21（user 視角）有 ≈10 個 RH overrides + 數個 LH overrides — 是整首 override 最密集的區段。musicology 上這也是**form 上最具張力的位置**：subject material 已退場，純 cadential figuration 衝向 PAC。

### 5.2 m21 (user) ≡ m20 (program) 的偏移

依 *project_bach_inv_measure_mapping* §Inv 1：

> Inv 1: user mN → program m(N-1), N≥2 (Audiveris pickup treble staff bug, MXL #1)

因此 user m21 = program m20。所有 override 註解都標 user 視角；演算法看到的是 program 視角。這是**form-level analysis 與 pos-level override 的座標翻譯層**，與 phrase 偵測無關但討論 m21 時必須先釐清。

### 5.3 三類邊界共同作用

m20-m22 (program) 區段：

| Boundary 類型 | 工具 | m20-m22 是否觸發 |
|---|---|---|
| **Cadence (PAC)** | [concept_cadence_detection](concept_cadence_detection.md) | ✅ m22 final chord = I (C major), 預期觸發 |
| **Figural boundary** | [concept_figural_boundary_detection](concept_figural_boundary_detection.md) | ✅ m20-m21 多次 figure 切換（descending → ascending sextuplet pattern） |
| **Subject entry** | [concept_subject_imitation_detection](concept_subject_imitation_detection.md) | ⚠ 不確定；coda 段傾向 subject 已退場 |

→ 三類邊界中**兩類同時觸發**正是 coda 的 musicological 標誌：cadence 結構 + figural climax。

### 5.4 RH m21 pos1 = f5 的解讀

user override `("right", 20, 1): 5` (= user m21 pos1 = C5 用 f5)。

這是 wiki 框架下的 **prep-type override** (*feedback_override_semantics*) — f5 開在 C5 預備手位往**下方**展開後續 cadential figure（m21 pos12 = E4, pos13 = D4 ... 一路下行至 cadential trill / final chord）。若 DP 純看 m21 pos1 局部 cost，會偏好 f3 / f4（C5 在 RH 中音域中性位置），但這會讓接下來下行段被 stranded 在 inner fingers。

→ **這個 override 是樂句邊界後的「手位 reset」**，意義對應 *feedback_phrase_as_breath* 的「呼吸 = 邊界 reset」原則。f5 不是 m21 pos1 的最佳生物力學選擇，是**下一個 phrase 的最佳起手位置**。

### 5.5 LH m21 pos10 = f3 的解讀

user override `("left", 20, 10): 3` (LH m21 pos10 = G2 用 f3)。

LH 在 coda 段需配合 RH 的下行 cadential figuration，這個 f3 是**pivot-type override** — 為了 LH 在 cadential trill 期間維持穩定 hand-anchor，f3 落在 G2 比 DP 偏好的 f4/f5 更靠中間，**保留 f5 給最終低音根音**。

## 6. 第二個 Case (briefer) — m6-m7 modulation 邊界

m6 是 exposition 結束、m7 開始往 G 大調 modulation。user override 在這帶有 6 個 RH 連續位置 `m6 pos1/3/5/7/14` + `m7 pos1/2`，特徵是：

- m6 內 RH 用 1–2–1–2 交替 (pos1=1, pos3=2, pos5=1, pos7=2) — Alberti-style ostinato 指法
- m6 pos14 = 3 (rise to B4) — figure 收尾上行 pivot
- **m7 pos1 = 2, pos2 = 1** — modulation 後 RH **拇指穿越**（thumb-pass downward）— G4 → G4 同音換指 reset

→ m6-m7 的 fingering 邏輯：exposition 段 figure 結束後，m7 的拇指穿越**標示 modulation 起點**。這正是 [concept_modulation_as_phrase_signal](concept_modulation_as_phrase_signal.md) 的具體體現：modulation 不只是和聲事件，也是手位 reset 事件。

對演算法的意涵：若 [concept_modulation_as_phrase_signal](concept_modulation_as_phrase_signal.md) 在 m7 處標 phrase boundary，DP 應在 m6→m7 接縫處允許「拇指穿越免罰 / 手位重置」(對應 `PHRASE_SEAM_TC_SCALE = 0.5`)，user 教的 m7 pos1=2 + pos2=1 將自然從 cost 結構導出。**驗證待跑**。

## 7. 三類樂句邊界並用的必要性

對 BWV 772，三類邊界各覆蓋不同 form 位置：

| 邊界類型 | Inv 1 觸發點 | 工具 |
|---|---|---|
| **Subject entry** | 主題 / 答句: m1 RH + m3 LH (在演算法 template 內, 不會被標為 entry); 演算法掃描自 template 之後 — 實測 RH @ m6/m12/m18/m19, LH @ m4/m6/m7 (見 *project_bach_inv_subject_detection_validation_2026-05-28*) | [concept_subject_imitation_detection](concept_subject_imitation_detection.md) |
| **Modulation / 段落** | m6-m7, m14-m15, m18-m19 | [concept_modulation_as_phrase_signal](concept_modulation_as_phrase_signal.md) |
| **Cadence** | m21-m22 PAC | [concept_cadence_detection](concept_cadence_detection.md) |
| **Figural** | m20-m21 coda 內 figure 切換、episode 段內 sequence boundary | [concept_figural_boundary_detection](concept_figural_boundary_detection.md) |

→ Inv 1 與 [analysis_bach_inv_4_d_minor](analysis_bach_inv_4_d_minor.md) 對照：
  - Inv 4: figural boundary 是主角 (m50 case)，subject entry 抓不到 episode/coda 邊界
  - Inv 1: **modulation + cadence 是主角**，subject entry 抓 exposition / final entries，figural 補 coda 細節

兩首合看支持本套 wiki 的核心架構假設：**單一偵測軸無法完整描述 Bach Invention 樂句結構**。

## 8. 與其他 wiki 頁面的關係

- 與 [analysis_bach_inv_4_d_minor](analysis_bach_inv_4_d_minor.md) 形成 compare-contrast pair（不同 form 段的邊界類型主導）
- 應用 [concept_fugue](concept_fugue.md) / [concept_counterpoint](concept_counterpoint.md) 對 2-voice Invention 的論述
- 對 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 提供 1-bar vs 2-bar subject 假設的驗證 case
- 對 [concept_modulation_as_phrase_signal](concept_modulation_as_phrase_signal.md) 提供 m6-m7 / m14-m15 / m18-m19 三個明顯邊界
- 對 [concept_cadence_detection](concept_cadence_detection.md) 提供 m21-m22 PAC 案例
- 對 [concept_figural_boundary_detection](concept_figural_boundary_detection.md) 提供 m20-m21 coda 內 figure 切換案例
- 編輯版本爭議引 [src_bach_inventions_pedagogy](src_bach_inventions_pedagogy.md)
- 對位起源溯至 [src_fux_gradus_ad_parnassum](src_fux_gradus_ad_parnassum.md)
- Override semantics 解讀依 *feedback_override_semantics*、*feedback_phrase_as_breath*
- 個人化生物力學原則依 *feedback_personal_biomechanics*
- Measure 對應依 *project_bach_inv_measure_mapping*
