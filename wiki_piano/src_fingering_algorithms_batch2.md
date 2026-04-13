---
title: "鋼琴指法演算法論文 — 第二批（4 篇）"
date_ingested: 2026-04-09
source_type: academic_paper_collection
sources:
  - "Telles, Ana (2020). Piano fingering strategies as expressive and analytical tools for the performer. In Contemporary Piano Music (Cambridge Scholars), pp.151-180."
  - "Nellåker, Eric & Lu, Xingye. Optimal piano fingering for simple melodies. KTH Royal Institute of Technology, DD143X."
  - "Andersson, Mikael & Håkansson, Mira Yao. Generating Ergonomic Fingerings for Piano. KTH Royal Institute of Technology, DD143X."
  - "Liao, Wei & Fan, Cheng (2025). A Multimodal-Based Fingering Analysis Method for Piano Playing. IEEE Access 13, 205288-205300."
tags:
  - fingering_algorithm
  - dp
  - contemporary
  - interpretation
  - unconventional_fingering
---

# 鋼琴指法演算法論文 — 第二批

4 篇論文：1 篇學術書章節（指法作為分析與表現工具）、2 篇 KTH 學位論文（Parncutt 模型的演算法實作）、1 篇多模態 Transformer 指法分析（IEEE Access 2025）。

## 1. Telles (2020) — 指法策略作為表現與分析工具

### 核心論點

指法不僅是技術手段，更是**認知與分析工具**——能幫助演奏者理解音樂結構，特別是在當代音樂中。作者主張應突破標準指法的限制，採用更全面（包含非傳統）的指法方法，以充分實現作品的表現潛力。

### 大師對指法的觀點

多位大師一致認為指法應從**音樂詮釋**出發，而非純粹人體工學：

| 大師 | 觀點 |
|------|------|
| **Neuhaus** | 應先建立「美學上正確的指法」，由作品的精神、性格和作者的鋼琴風格決定 |
| **Brendel** | 音樂決定一切——指法、踏板、手部動作 |
| **De Larrocha** | 先仔細研究音樂，找出指法最困難的段落；指法是安全的基礎 |
| **Kogan** | 不舒適的指法若能更清楚表達作曲家意圖，可能優於舒適的指法 |
| **Schelling** | 困難的指法往往導致更好的詮釋 |
| **Parncutt** | 最佳指法 = 物理、解剖、運動、認知、詮釋各種約束之間的折衷 |

### 標準指法 8 原則

Telles 總結的傳統「標準」指法原則：
1. 每個音由一根手指彈奏，產生特定音色
2. 大小調音階：1、5 不上黑鍵；用 123 和 1234 組合
3. 半音階：離鍵奏（1-2/1-3 交替）或連奏（123/1234 組合），1、5 不上黑鍵
4. 和弦與琶音：由音程距離決定；閉合手位用交替指（1-3, 2-4, 3-5），伸展手位用相鄰指
5. 顫音：通常用 1、2、3 的組合
6. 雙音：手分為上下兩半（下半 1-2-3，上半 3-4-5）
7. 八度：白鍵 1-5，黑鍵 1-4；1-5 也可用於黑鍵
8. 重複音：換指（321321 或 43214321 或交替如 212121、313131）

### 三指法 vs 五指法

兩大歷史流派，由 Kogan (2006) 定義：

| 流派 | 代表人物 | 特徵 | 優勢 |
|------|---------|------|------|
| **三指法** | Czerny、Leschetizky | 主要用 1-2-3；手幾乎不動的 legato | 解決了手指「均等化」問題和拇指穿越小指的困難 |
| **五指法** | Liszt、Busoni | 用所有 5 指包括拇指上黑鍵 | 更少手位變化 → 更快速度；更長的「自動化鏈」；更少有意識的位置命令 |

legato 的概念從「連接」演變為「幻覺式連接」和 non legato，手獲得了更大的移動自由度。

### 拇指上黑鍵的歷史演變

| 時期 | 態度 |
|------|------|
| C.P.E. Bach (1753) | 黑鍵極少由小指彈，只在必要時由拇指彈 |
| Chopin | 毫不猶豫地在黑鍵上使用拇指 |
| Liszt 以後 | 持續尋找替代音階指法 |
| Busoni (1918) | 提出 12345 連續指法、拇指穿越 5 指 |
| Cortot (1928) | 練習從每個音符的拇指開始的音階 |
| Messiaen (via Loriod) | 練習 12121212 / 13131313 的所有大小調音階 |
| 當代 | 拇指上黑鍵越來越常見，甚至被鼓勵使用以獲得更有表現力的觸鍵 |

Lucette Descaves (1990): 雖然原則上禁止初學者在黑鍵上使用拇指，但實際上它聽起來更好，並且賦予演奏者權威感和柔順的表現性觸擊。

### 單指技法（Martellato）

20-21 世紀作曲家發展出使用**單一強指**（拇指、食指或中指）彈奏極大聲孤立音的技法。Stockhausen、Zimmerman、Bussotti、Kagel、Pousseur 等作曲家使用。常與手交替（源自 Liszt）結合。

極端案例：Loriod-Messiaen 建議在 Messiaen 某些段落使用**拳頭**以產生極大聲響。Bochmann 和 Béreau 的作品也明確要求使用拳頭。

### Busoni 的「技術分句」

Busoni (1894) 提出的概念：依據 (a) 音樂動機、(b) 鍵盤上的位置、(c) 方向變化來分組音符。這種分組應只對演奏者可聽見，觀眾不應察覺——是心理因素而非物理因素。

### 指法作為分析工具

Telles 的核心主張：指法策略（包括非傳統方法）不僅揭示音色、觸法、力度等表現要素，更能揭示旋律、和聲、節奏等**音樂結構**要素。傳統教學文獻主要針對 18-19 世紀曲目，忽略了 Chopin、Liszt、Cortot、Kogan 等人提出的非傳統方法，更忽略了 20-21 世紀大量需要創意指法的當代作品。

### 與 V6 DP 的關聯

| Telles 觀點 | V6 DP 現況 |
|-----------|----------|
| 指法是分析/詮釋工具 | V6 純人體工學，不考慮音樂結構 |
| 不舒適指法可能更好 | V6 最小化不舒適 — 可能與詮釋需求矛盾 |
| 當代音樂需非傳統指法 | V6 的規則基於傳統曲目，當代音樂可能需要完全不同的 cost model |
| 拇指上黑鍵越來越被接受 | V6 的 Thumb-on-Black 懲罰 = 0，符合趨勢 |
| 五指法可能更快 | V6 不區分三指法/五指法流派 |

## 2. Nellåker & Lu (KTH) — 簡單旋律的最佳指法

### 方法

- 基於 Parncutt 1997 的 **13 條規則**（原始 12 條 + 新增 1 條休止規則）
- **休止規則**：休止期間手可重新定位——若休止前後的音程超過 MaxComf 或小於 MinComf，仍有懲罰但降低比率
- 演算法：Java 實作的**樹搜尋**（非 DP）
- 輸入：MIDI 檔；輸出：手指序列
- 使用 Parncutt Table 1 的跨度值（MinPrac/MinComf/MinRel/MaxRel/MaxComf/MaxPrac）

### 測試結果

以 3 首曲子測試，與 2 位有經驗鋼琴家比較：
- Twinkle Twinkle Little Star
- Divenire (Einaudi)
- Eine Kleine Nacht Musik (Mozart)

結論：演算法產生的指法與專業鋼琴家的選擇「夠接近」。

### 限制

- 僅限右手
- 僅限單音旋律（無和弦）
- 樹搜尋非最優效率

### 與 V6 DP 的關聯

V6 已透過 `_detect_phrase_starts` 處理休止與樂句邊界，且使用 DP（非樹搜尋）效率更高。Nellåker 的休止規則驗證了「休止時手可重新定位」的概念——V6 的 `INTER_PHRASE_SCALE = 0.0`（樂句完全獨立）實現了類似效果。

## 3. Andersson & Håkansson (KTH) — 產生人體工學鋼琴指法

### 方法

- **DP + Trellis 圖**方法
- 結合 Hart et al. 演算法（每步考慮從某手指開始彈完剩餘旋律的困難度）與 Parncutt 成本計算
- Hart 演算法：線性時間複雜度（DP 特性）
- Trellis 圖：每個節點 = (音符, 手指)，邊的權重 = 轉換成本；最短路徑 = 最佳指法
- 使用相同的 Parncutt Table 1（reach table）

### 測試結果

與 2 位專業鋼琴家比較：
- 自動產生的指法集合**包含了鋼琴家建議的大部分指法**
- 但同時也包含了**大量低品質的額外指法**——演算法無法充分區分好壞

### 限制

- 僅限右手、單音旋律
- 缺乏有效的品質篩選機制

### 與 V6 DP 的關聯

V6 使用類似的 DP 方法但有更豐富的 cost model：
- `_assignment_cost`（生物力學評分）比 Parncutt 的 12 規則更細緻
- `_transition_cost`（接力規則、雙聲部交替接力等）解決了「大量低品質」問題
- 樂句感知 DP + 重複段落一致性進一步篩選
- 同時處理左右手與和弦（非僅右手單音）

## 4. Liao & Fan (2025) — 多模態鋼琴指法分析方法

### 核心貢獻

⭐ **IEEE Access 2025**——基於 Transformer 的多模態指法分析框架，達到 **Finger Accuracy 0.96、Direction Accuracy 0.94**。

### 方法

- **Transformer encoder** + 兩個專用模組：
  - **Position-Aware Encoding (PAE)**：嵌入絕對和相對時間特徵（onset 時間、duration、IOI），處理音樂中不規則的時間間隔（rubato、非同步觸法）
  - **Dynamic Channel Attention (DCA)**：自適應地重新加權不同模態的重要性——速度在表現性分句中主導，踏板狀態和運動方向在和弦區域更顯著
- **雙輸出頭**：MLP_id（預測 Finger ID: L1-L5, R1-R5）+ MLP_dir（預測 Finger Motion Direction: up/down/left/right）
- **訓練損失**：cross-entropy (finger ID) + cross-entropy (direction) + Jensen-Shannon Divergence (temporal smoothness)

### 數據集

- **MAESTRO**（~200 小時 Disklavier 鋼琴錄音）作為基礎
- **RoboPianist**（物理模擬）產生初始指法標注 → 由 3 位專家鋼琴家手動驗證修正（Cohen's κ = 0.87）
- 另收集小規模真實演奏數據集（3 位鋼琴教師在 Yamaha MIDI 鋼琴上演奏 Czerny、Bach Inventions）

### 多模態特徵

| 特徵 | 說明 | 範例值 |
|------|------|------|
| Note Name | 科學音高記號 | B4 |
| Note Duration | 持續時間 | 0.75s |
| Pitch | MIDI 音高 | 71 |
| Velocity | 觸鍵力度 (0-127) | 96 |
| Pedal State | 延音踏板狀態 | Sustain=ON |
| Finger ID | 使用的手指 | R3 |
| Finger Motion Direction | 觸鍵前手指運動方向 | up |
| Inter-Onset Interval | 與前音的時間間隔 | 0.35s |
| Pitch Interval | 與前音的音程 | +2 半音 |

### 結果

| 指標 | 數值 |
|------|------|
| Finger Accuracy | **0.96** |
| Finger Direction Accuracy | **0.94** |

### 與 V6 DP 的關聯

| Liao & Fan 2025 | V6 DP |
|----------------|-------|
| 多模態（MIDI+生物力學+踏板） | 僅用音高序列 |
| Transformer（全局注意力） | 樂句內 DP（局部最佳化） |
| 預測 Finger Direction | V6 不預測手指運動方向 |
| 96% 準確率 | 未與 PIG Dataset 比較 |
| 需要 MIDI velocity/pedal | V6 僅需 MusicXML 音高 |
| 需要 GPU 訓練 | V6 純 CPU、即時推理 |

**啟示**：Liao & Fan 證明加入速度、踏板、時間間隔等多模態特徵可顯著提升指法預測準確率。V6 未來可考慮從 MusicXML 讀取 velocity 和 pedal 資訊作為額外評分維度。

## 相關頁面

- [src_parncutt1997_ergonomic_model](src_parncutt1997_ergonomic_model.md) — Parncutt 1997 原始模型（3 篇論文共同基礎）
- [src_computational_fingering](src_computational_fingering.md) — Nakamura HMM + Moryosef 影片提取
- [concept_musical_fingering](concept_musical_fingering.md) — 指法 = 音色/詮釋選擇
- [concept_piano_fingering_principles](concept_piano_fingering_principles.md) — 五大共識原則
- [concept_thumb_technique](concept_thumb_technique.md) — 拇指穿越技巧的歷史演變
- [analysis_period_style_fingering](analysis_period_style_fingering.md) — 不同時期的指法差異
