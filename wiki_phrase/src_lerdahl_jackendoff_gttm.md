# Source: Fred Lerdahl & Ray Jackendoff《A Generative Theory of Tonal Music》

> MIT Press, 1983, English
> ISBN: 978-0262120944
> Ingested: 2026-05-28

## 一句話總結

GTTM 提出對任何調性音樂段落的四套**平行階層分析**（grouping / metrical / time-span reduction / prolongational reduction），並以**Well-Formedness Rules + Preference Rules** 的雙層架構刻劃聽者對音樂結構的內在直覺。是算法音樂分析的基石之一，**其 Preference Rule 框架就是 cost-based DP 的概念前身**，與本專案的指法 DP 與樂句偵測直接對應。

## 重點概念清單（供其他 concept 頁引用）

### Grouping Structure（分組結構）— 與樂句偵測最直接相關

聽者把連續音流切割成階層化的**群組**（motif → phrase → period → section）。由 Grouping Preference Rules (GPRs) 決定。**這是本專案 `_detect_phrase_starts` 的理論依據**。

#### Grouping Preference Rules (GPRs) — 全套 7 條

- **GPR 1（Alternative Form）**：避免長度為 1 的群組；單音不構成群組（與本專案 onset cluster / 和弦 grouping 同源）
- **GPR 2（Proximity）**：兩種子規則
  - **2a (Slur/Rest)**：大休止 / 連結線斷裂 → 群組邊界
  - **2b (Attack-Point)**：音與音間 inter-onset interval (IOI) 顯著大於前後 → 邊界
  - **➜ 直接對應本專案 Pass 1 hard break 的「休止間隙 > 0.75 拍」**
- **GPR 3（Change）**：相鄰兩音間任一面向顯著變化即標邊界
  - **3a (Register)**：音域跳動
  - **3b (Dynamics)**：力度變化
  - **3c (Articulation)**：奏法（legato → staccato）
  - **3d (Length)**：時值（短 → 長）
  - **3e (Timbre / Pitch-Class)**：音色 / 音高類別
  - **➜ 對應 Pass 1「音高重心跳幅 > PHRASE_BREAK_THRESHOLD」**；其他子規則本專案目前未用
- **GPR 4（Intensification）**：GPR 2/3 各維度信號越強，邊界階層越高；多維度同時觸發 → 大段落邊界
  - **➜ 本專案目前只用 binary boundary，沒用 intensification scoring；可作 future work**
- **GPR 5（Symmetry）**：偏好等長群組
  - **➜ 對應 Pass 2「推斷最常見樂句長度，對齊至 2/4/6/8 小節」**
- **GPR 6（Parallelism）**：重複出現的音樂材料應分到平行位置的群組
  - **➜ 對應 motif consistency（HARD rule），見 `[[../score-claude/memory/feedback_personal_biomechanics]]`**
- **GPR 7（Time-Span and Prolongational Stability）**：偏好讓 grouping 結果使更高層 reduction 更穩定（cross-component 條件）

### Metrical Structure（節拍結構）

每個音事件被指派**多層次的強弱位**（beat / measure / hypermeasure）。

- **Hypermeter**：跨小節的強弱模式，典型 2-bar 或 4-bar group
- 與 grouping 不同：grouping 是音的「分塊」，metrical 是強弱「點」
- **➜ 對應本專案 Pass 2 4-小節週期 fallback + 終止式判斷的「下一組落在強拍」條件**
- **Metrical Preference Rules (MPRs)** 包含：parallelism、strong beat early、length、bass、harmony stability、cadence

### Time-Span Reduction（時間跨度約簡）

從 grouping + metrical 出發，建構音事件的**階層樹**：每層保留各 time-span 中「結構最穩定」的音（拍位強 + 和聲協和 + 旋律重要）。

- 與 Schenker 分析有家族相似
- 越底層 = 越「裝飾性」，越頂層 = 越「結構性」
- **本專案目前未使用**；未來可能用於 cadence weighting 或主題識別

### Prolongational Reduction（延伸約簡）

刻劃**緊張 ↔ 鬆弛**的樹狀流動：每個事件如何「延長」前事件、或「解決」到後事件。

- 樹節點分三類：
  - **Strong prolongation**：相同音 / 和弦延續
  - **Weak prolongation**：相關但變形
  - **Progression**：和聲推進（傾向 → 解決）
- 與 harmonic function（T-S-D-T）密切相關
- **本專案目前未使用**；未來可能用於終止式強度量化

### Well-Formedness Rules (WFRs) vs. Preference Rules (PRs)

GTTM 對兩種規則嚴格區分：

| 類型 | 性質 | 數量 | 類比 |
|---|---|---|---|
| **WFR** | 句法 / 結構性硬約束，必須滿足 | 少 | 程式語言文法、和聲規則的「不可平行五度」 |
| **PR** | 加權軟偏好，多條規則同時起作用 | 多（每個 component 5-10 條） | cost-based DP 的 cost term |

- WFR 例：grouping 必須是**非重疊、階層巢狀**的（exception: elision）
- PR 例：所有 GPRs
- **衝突解決**：由「global optimization」決定 — 所有 PR 加權後找總分最佳的分析
- **➜ 這是本專案 DP cost 架構（cost_assignment + cost_transition + phrase budgets 全部加總取 min）的概念原型**

### Preference-Rule 框架作為 cost-based DP 的靈感來源

GTTM 自己沒有給出明確的權重數值，但提出：

1. 每條 PR 可被獨立違反
2. 違反程度可量化
3. 所有 PR 加總後做全局最佳化
4. 多條 PR 相互強化 → 「robust」分析；相互衝突 → 「ambiguous」分析

**➜ 與本專案完全對應**：每個 cost term 對應一條 PR；W_PHRASE_ANCHOR、STEP_AGILITY、ULNAR_SURCHARGE 等都是 PR 的加權實現；DP 全局最佳化 = PR 衝突解決機制。

## 歷史與作曲家

- 1983 出版，MIT Press；屬「generative grammar of music」傳統，受 Chomsky 句法理論啟發
- 作者：Lerdahl 為作曲家 + 理論家；Jackendoff 為認知語言學家（Chomsky 學生）
- 後續發展：Hamanaka et al. 的 **GTTM Analyzer**（2006-）嘗試計算化實作；Marsden 2010 提出可計算的 reduction algorithm；Lerdahl 2001《Tonal Pitch Space》延伸 prolongational reduction
- 對 MIR / algorithmic composition / music cognition 三個領域都有深遠影響
- 影響範圍：適用「西方共通慣用法時期」(Bach → Brahms) 為主；對非調性、非西方音樂的擴展是後續研究主題

## 文章未涵蓋（要 P1 補的）

- ❌ 具體的演奏 / 指法建議（GTTM 是分析理論，不是演奏理論）
- ❌ 各 PR 的權重數值（書中刻意不給）
- ❌ 對位 / 多聲部各聲部的獨立 grouping（暗示有，但未細談）
- ❌ Phrase elision 的具體處理（WFR 雖容許但缺少充分例子）
- ❌ 計算化實作（書是純理論；實作待 Hamanaka / Marsden 等人）
- ❌ 拍號變化、節奏自由段落（rubato / cadenza）的處理

## 對指法系統的啟示（synthesized — 不是文章原文）

1. **`_detect_phrase_starts` Pass 1 的硬斷點規則直接源於 GPR 2 + GPR 3**：
   - 「休止間隙 > 0.75 拍」= GPR 2a (Slur/Rest)
   - 「小節跳躍」= GPR 2b (Attack-Point) 的離散化
   - 「音高重心跳幅 > PHRASE_BREAK_THRESHOLD」= GPR 3a (Register)
   - **應在 `_detect_phrase_starts` docstring 標註此 lineage 以增強 traceability**

2. **Pass 2 的 2/4/6/8 小節週期 fallback 對應 GPR 5 (Symmetry) + Hypermeter**：
   - 在無 hard break 的曲段（如 3/8 拍無休止符），預設 phrase_period=4 = 假設 4-bar hypermeter
   - 這在 Common Practice 時期 (Bach-Brahms) 是強假設；20 世紀後音樂需放寬

3. **GPR 6 (Parallelism) = 本專案 HARD motif consistency**：
   - 「同 motif → 同 fingering」是 GPR 6 在指法 domain 的鏡像
   - 但 GTTM 把 parallelism 當 PR（軟）而本專案當 HARD requirement
   - 差異來源：聽覺感知容許小變化（PR 軟）；肌肉記憶不容許（HARD）
   - 詳見 `[[../score-claude/memory/feedback_personal_biomechanics]]`

4. **GPR 4 (Intensification) 是未實作的 boundary scoring 機會**：
   - 目前 hard break = binary；多面向同時觸發時應加權產生「強邊界」
   - 強邊界可放寬 phrase budget reset（thumb-pass / ulnar drift）
   - 弱邊界保留 micro-segment 但不 reset budget
   - 對應 `_detect_texture_boundaries` 已用的 voting-score 架構 — 可推廣到主 phrase detection

5. **WFR / PR 雙層架構驗證了本專案的 cost 架構**：
   - WFR = 硬限制（如「k≥3 chord 必含拇指（適用手）」、「FINGER_MAX_SPAN」）
   - PR = 軟 cost（span_cost、velocity、ulnar 等）
   - 全局 DP min = GTTM 的 global optimization
   - **這提供本專案 cost-based 架構的學理支撐，不只是 ad-hoc engineering**

6. **Time-span / Prolongational reduction 尚未使用，但是未來終止式加權的潛在資源**：
   - 終止式偵測目前依賴 music21 roman + measure-final chord (Phase 2)
   - 若整合 prolongational tree，可量化「終止強度」(PAC > IAC > HC > DC)
   - **Deferred**：先把 cadence Phase 2 / texture detection 跑穩再考慮

7. **承認 grouping 結果在多聲部音樂中可能不對齊**：
   - GTTM 對 monophonic / homophonic 設計；對 counterpoint 各聲部獨立 grouping 暗示但未細談
   - **➜ 與 `[[src_epochtimes_fugue_zhou_2005]]` 啟示 1 一致**：兩手樂句邊界不必同步
   - 本專案 `_detect_phrase_starts` per-hand 跑是對的

詳見 [[concept_figural_boundary_detection]]、[[concept_texture_change_detection]]、[[concept_phrase_elision]] 與 [[../score-claude/memory/feedback_phrase_as_breath]]、[[../score-claude/memory/feedback_phrase_analysis_is_its_own_discipline]]。
