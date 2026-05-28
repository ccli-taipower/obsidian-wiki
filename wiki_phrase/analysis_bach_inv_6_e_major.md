# Analysis: Bach Invention 6 in E major (BWV 777) — Strict Canon at the Octave 與 Suspension Chain

> 來源：musicology 文獻 + Bach *Two-Part Inventions* 對位傳統
> 對應 PIG：未列入 / 對照需另行查核
> 狀態：第三個 Bach Invention analysis 頁；strict canon 結構對 phrase detection 的根本挑戰之 case study
> 觸發 case：整曲為 canon 結構 → subject entry detection 預期 over-fire；suspension chain → 無明顯硬 boundary

## 1. 為什麼挑這首作為 wiki 第三個 Bach analysis 頁

BWV 777 在 *Two-Part Inventions* (BWV 772–786) 中是**最具結構獨特性的一首**，理由有三：

- **唯一一首全曲為嚴格 canon at the octave 的 Invention** — 兩聲部 1 小節錯位、8 度模仿，貫穿 62 小節（其他 Invention 採 free imitation / fugal 對位，而非 strict canon）
- **Suspension chain (4-3, 7-6) 從 m1 即出現，貫穿全曲** — Bach 對位最嚴格、ornamental texture 最密集的一首
- 與 [[analysis_bach_inv_1_c_major]] 形成**極端對照**：Inv 1 是 free imitation 的 simple exposition pattern（典型 subject/answer/episode 架構）；Inv 6 是 strict canon 的單一 contrapuntal device 貫穿到底。三首一起 (Inv 1 / 4 / 6) 代表 Bach Invention 風格光譜的三個端點

對 [[concept_subject_imitation_detection]] / [[concept_texture_change_detection]] / [[concept_figural_boundary_detection]] 的演算法測試而言，**Inv 6 是 hard case 樣本** — 多數啟發式（density-shift, pitch-jump, rest-gap）在此首都會失效或誤觸。

## 2. 曲目基本資訊

- **BWV 777**, 約 1723 (Bach 38 歲, Köthen)
- **E major**, 4 升記號, **3/8 拍**, **62 小節**
- 形式：**非常規 2-voice Invention** — 全曲為 strict canon at the octave，RH 領奏、LH 嚴格 1 小節錯位於下方 8 度
- 主題特色：**suspension chains + syncopation** 是核心；每小節後半 beat 持續 dissonance → 進 resolution；ornamental 程度遠高於 Inv 1/2/3
- 教學定位：難度顯著高於前幾首；suspension / syncopation 對位教學的鋼琴典範
- 著名版本：András Schiff (尊重 canon 結構之 voicing 分層), Glenn Gould 1964 / 1981 (兩版 articulation 差異是 canon-vs-romantic 解讀的對照組), Angela Hewitt
- 編輯版本爭議：見 [[src_bach_inventions_pedagogy]]；canon 結構源頭可溯至 [[src_fux_gradus_ad_parnassum]] *species counterpoint* 的 strict imitation 規則

## 3. Subject 識別 — strict canon 的特殊狀態

### 3.1 「Subject」概念在 canon 結構下的崩解

在 fugue / free-imitation Invention（如 Inv 1）中，subject = 一段有明確開頭與結尾的 thematic material；entries 是 discrete 事件。但在 **strict canon 結構下**：

- RH 從 m1 開始的整段旋律就是「subject」
- LH 從 m2 開始的整段旋律是同一 subject 8va 下方、延遲 1 小節
- 兩聲部之間**沒有 episode** — canon 從第一個音持續到最後一個音
- 因此**整首曲子是一個延展 62 小節的 subject**，沒有 discrete subject entries 可數

→ 對 [[concept_subject_imitation_detection]] 演算法的意涵：若 algorithm 以「找出 subject 完整 N-bar 樣本，再到別處找 transposed/inverted 重複」為前提，在 Inv 6 上會出現兩種失敗模式：

| 失敗模式 | 機制 | 預期表現 |
|---|---|---|
| **Over-fire** | 每個 RH 小節的下一小節在 LH 都是 subject 的 1-bar 片段 → 每小節都被標為 entry | ⚠ 預期 algorithm 在 60+ 個位置標 entry，phrase boundary 失去意義 |
| **Trivial-match** | Algorithm 把整曲視為單一 subject re-stating，回傳 1 entry | 也失去 phrase 結構訊息 |

任一失敗模式都意味著 **subject-entry-based phrase detection 不適用此首**。

### 3.2 Musicology 共識：canon 結構本身 = 樂句結構

對 strict canon 而言，phrase 分段的依據**不在 subject entry**，而在：

| 依據 | 在 Inv 6 的對應 |
|---|---|
| **Suspension resolution 點** | 每個 4-3 / 7-6 suspension 的 resolution = 局部 phrase 收束點 |
| **Tonal goal (cadence)** | 進入新調區的 cadence = section boundary |
| **Sequence 起點/終點** | Bach 大量使用 sequence 推進 modulation |

→ 這呼應 [[../score-claude/memory/feedback_phrase_analysis_is_its_own_discipline]]：**phrase 分析是獨立學科，canon 結構本身就是樂句結構**。Inv 6 的「樂句」不是由 entry 切出來的離散段，而是由 suspension chain 的張力-解決循環構成的連續流。

### 3.3 倒影 (Inversion) 分析

BWV 777 中**倒影主題不顯著**。Bach 在此首聚焦於 strict octave canon，未引入 inversion 變形（與 BWV 775 Inv 4 大量 inversion 對比）。對演算法的意涵：inversion detection 在這首應**返回稀疏結果**，若返回密集匹配，多半是 canon 內部音程巧合（因 LH 是 RH 的 8va 下方平移，所有 inversion 候選都是 false positive 的高風險源）。

## 4. 三段曲式對應 (但比例異於 Inv 1)

| 段落 | 小節 (user mN) | 調性 | 角色 |
|---|---|---|---|
| **Exposition** | m1–m20 | E → 過渡 | RH 起 subject (m1) → LH 8va 下方 canon (m2) → 在 V/I 之間反覆 sequence |
| **Modulation to B major (V)** | m21–m38 | B major | Canon 繼續但於屬調區展開；含 sequence 與短暫離調 |
| **Return + final cadence** | m39–m62 | 回 E major | 回主 + final cadential extension（canon 結構持續至最後一個解決音） |

→ m20–m21、m38–m39 是兩個明顯的**段落邊界**，皆可由 [[concept_modulation_as_phrase_signal]] 偵測；m61–m62 final PAC 由 [[concept_cadence_detection]] 偵測。但**段內**（如 m1–m20 之間）的 phrase 細分極難 — 詳見 §5。

## 5. Case A — Strict Canon 對 phrase detection 的根本挑戰

### 5.1 為什麼這是 hard case

Strict canon at the octave 對所有現有 phrase detection 啟發式都造成困難：

| 偵測軸 | 在 Inv 6 失效原因 |
|---|---|
| **Rest gap** ([[concept_figural_boundary_detection]] §pitch jump 也適用) | Canon 結構下兩聲部交錯填滿，幾乎無同時休止；suspension chain 不允許「斷氣」 |
| **Pitch jump** | Suspension chain 的旋律線是 stepwise 為主，音高重心連續移動，極少 octave-class 跳幅 |
| **Density shift** ([[concept_texture_change_detection]]) | Texture **均勻** — chord density 高且穩定、figure 切換少 → density-shift voting 無觸發點 |
| **Subject re-entry** ([[concept_subject_imitation_detection]]) | 如 §3.1 — over-fire 或 trivial-match，皆無法區隔 phrase 邊界 |

→ 結論：**Inv 6 的 phrase 結構不是由演算法可偵測的局部訊號標示出來的**，而是由 contrapuntal logic（suspension chain 解決點、tonal goal）決定。

### 5.2 兩聲部樂句邊界**必然錯位 1 小節**

Canon 的定義即為「同樣材料延遲 N 小節」。Inv 6 是 1-bar canon，因此：

- RH 在 mN 處的 phrase boundary（若有）= LH 在 m(N+1) 處的 phrase boundary
- **Cross-hand 樂句邊界邏輯不適用** — 兩手永遠錯位 1 小節
- Per-hand DP 在這首是**必要的**（不能用兩手共用 phrase boundary 做 hand-coupling）

→ 對 score-claude 的 `_run_phrase_dp` 架構（per-hand 獨立 DP）而言，這是 strict canon 結構的天然優勢；但若未來引入 cross-hand phrase coupling，Inv 6 是必須排除的 corner case。

### 5.3 Suspension chain 對 phrase boundary 偵測的根本封鎖

Suspension 的結構是：**preparation → suspension (dissonance) → resolution**，三步橫跨小節線。在 Inv 6 中，suspension chain 意味著：

- 每小節後半 beat 都有 dissonance 在「等待解決」
- 解決點通常落在下一小節的強拍
- 因此**小節線本身不是 phrase boundary** — 反而是 phrase 中段的張力點

→ 任何以小節線 / 強拍 / pitch-class change 為 phrase boundary 候選的啟發式，在 Inv 6 上都會錯標：把 phrase 中段標成邊界。

→ 對應到 [[concept_cadence_detection]] 的 Phase 2 設計：cadence detection 用 measure-final chord 上的 Roman numeral 判斷 PAC/IAC — 此啟發式在 Inv 6 上需特別小心，因為 suspension chain 會讓「measure-final chord」是 dissonant 而非 cadential triad，⚠ 演算法輸出待驗證。

## 6. Case B — Suspension Chain 對 fingering 的影響

### 6.1 Suspension resolution 點：hand reset 還是維持？

Suspension chain 在鋼琴 fingering 上提出對位傳統與生物力學之間的 tension：

- **對位傳統觀點**：suspension 的 voice-leading 是連續的（preparation 與 suspension 是同一音、suspension 與 resolution 是 stepwise），fingering 應維持同指或鄰指以表達 legato voice line
- **生物力學觀點**：3/8 拍 + 密集 ornament + suspension chain 持續 → RH/LH 累積疲勞快，每 4-8 小節應有 hand-position reset 以避免 [[concept_running_passage_thumb_reservation]] 描述的 thumb-overuse

→ 這兩個觀點**在 Inv 6 上幾乎不可調和** — Bach 寫作沒有給「自然 reset 點」。鋼琴家的解決方式通常是：

| Strategy | 機制 |
|---|---|
| **Schiff approach** | 嚴格依 voice line 規劃 fingering，accept 較高疲勞、追求 voicing 清晰度 |
| **Gould approach** | 在 sequence repetition 邊界（每 2-bar 或 4-bar sequence unit）做 hand reset，犧牲部分 voice-leading 連續性 |
| **Hybrid (most editions)** | RH 跟 voice line，LH 找 sequence 邊界 reset |

→ 對 score-claude DP 的意涵：若未來實作 Inv 6 級別的 strict canon support，per-phrase budget 啟發式（如 `WRIST_EXT_PHRASE_BUDGET`, `THUMB_PASS_PHRASE_BUDGET`）需以 **sequence-unit 邊界** 而非 phrase boundary 為單位。Sequence unit 在 Inv 6 通常是 2 小節或 4 小節，需由 [[concept_modulation_as_phrase_signal]] 或專門的 sequence-detection 提供。⚠ 演算法 sequence-detection 尚未實作。

### 6.2 Canon 結構下 LH 不可獨立規劃

因 LH 是 RH 的嚴格 8va 下方平移、延遲 1 小節，LH fingering **不能獨立最佳化** — 必須與 RH 在同一段 thematic material 的 fingering 結構同形（modulo register adjustment）。這呼應 [[../score-claude/memory/feedback_personal_biomechanics]] 的「同手 + 同音型 → 同生物力學最優 → 同手指選擇」原則，但**跨手套用**：strict canon 下 RH 與 LH 共用一條 thematic line，其 fingering 在演奏邏輯上應對應。

⚠ score-claude 目前的 per-hand 獨立 DP **未明確處理此跨手對應**；motif consistency 五輪嘗試（v1–v4b + P3）皆為同手範圍，未涵蓋 canon 結構下跨手對應。Inv 6 是此空白的清晰測試案例。

## 7. 三類樂句邊界的相對失效

對比 [[analysis_bach_inv_1_c_major]] 與 [[analysis_bach_inv_4_d_minor]]，Inv 6 的邊界類型分布如下：

| 邊界類型 | Inv 6 觸發點 | 工具 | 預期可靠度 |
|---|---|---|---|
| **Subject entry** | 無 discrete entries (全曲為單一 canon) | [[concept_subject_imitation_detection]] | ❌ 不適用 |
| **Modulation / 段落** | m20-m21, m38-m39 | [[concept_modulation_as_phrase_signal]] | ✅ 段落級可用 |
| **Cadence** | m61-m62 final PAC, 可能 m38 區域中段 cadence | [[concept_cadence_detection]] | ⚠ suspension chain 干擾，待驗證 |
| **Figural** | Texture 均勻 → 觸發稀疏 | [[concept_figural_boundary_detection]] | ⚠ 預期低觸發 |
| **Texture change** | 全曲 texture 均勻 → 無觸發 | [[concept_texture_change_detection]] | ❌ 不適用 |

→ Inv 6 的特殊性在於：**4 個現有 detection 軸中有 2 個完全不適用、2 個僅段落級可用**。中段（如 m5–m18、m22–m36）內的 phrase 細分**沒有任何啟發式覆蓋**。

→ 此結果支持 [[../score-claude/memory/feedback_phrase_analysis_is_its_own_discipline]] 的論點：**strict canon 需要獨立的 sequence-unit detection 工具**，不能由現有 4 軸補位。是 wiki_phrase/ 未來需擴充的方向之一。

## 8. 與其他 wiki 頁面的關係

- 與 [[analysis_bach_inv_1_c_major]] 形成 simple-vs-strict canon 對照（Inv 1 free imitation；Inv 6 strict canon）
- 與 [[analysis_bach_inv_4_d_minor]] 形成 inversion-vs-canon 對照（Inv 4 inversion-heavy；Inv 6 octave-canon-heavy）
- 三首一起 (Inv 1 / 4 / 6) 代表 Bach Invention 風格光譜的 simple / inversion / canon 端點
- 對 [[concept_fugue]] / [[concept_counterpoint]] 提供 strict canon 端點案例
- 對 [[concept_subject_imitation_detection]] 提供「subject 概念崩解」的反面 case — 演算法需有對 strict canon 的特殊處理或排除規則
- 對 [[concept_texture_change_detection]] 提供「texture 均勻」的反面 case — 確認 density-shift voting 在此首應稀疏
- 對 [[concept_cadence_detection]] 提供 suspension chain 干擾 measure-final chord 啟發式的 corner case
- 對 [[concept_figural_boundary_detection]] 提供 suspension chain 阻擋 pitch-jump / rest-gap 啟發式的 corner case
- Canon + suspension 結構起源溯至 [[src_fux_gradus_ad_parnassum]] *species counterpoint* 的 strict imitation 規則
- 編輯版本爭議引 [[src_bach_inventions_pedagogy]]
- Phrase 分析作為獨立學科的論點依 [[../score-claude/memory/feedback_phrase_analysis_is_its_own_discipline]]
- 個人化生物力學原則依 [[../score-claude/memory/feedback_personal_biomechanics]]（並提出 strict canon 下跨手對應的延伸問題）
- Override semantics 解讀依 [[../score-claude/memory/feedback_override_semantics]]、[[../score-claude/memory/feedback_phrase_as_breath]]
- Measure 對應依 [[../score-claude/memory/project_bach_inv_measure_mapping]]
