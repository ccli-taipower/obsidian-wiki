---
title: "強化學習與元啟發式指法演算法（3 篇）"
date_ingested: 2026-04-10
source_type: academic_paper_collection
sources:
  - "Ramoneda, Pedro; Miron, Marius; Serra, Xavier (2021). Piano Fingering with Reinforcement Learning. arXiv:2111.08009."
  - "Gao, Wanxiang et al. (2023). Generating Fingerings for Piano Music with Model-Based Reinforcement Learning. Applied Sciences 13, 11321."
  - "Balliauw, Matteo; Herremans, Dorien; Palhazi Cuervo, Daniel; Sörensen, Kenneth (2017). A variable neighbourhood search algorithm to generate piano fingerings for polyphonic sheet music. International Transactions in Operational Research 24, 509-535."
tags:
  - reinforcement_learning
  - DQN
  - model_based_RL
  - metaheuristic
  - VNS
  - polyphonic
  - fingering_algorithm
  - combinatorial_optimization
---

# 強化學習與元啟發式指法演算法

3 篇論文探索了 DP 以外的指法搜索策略：深度 Q 學習、基於模型的 RL、以及變鄰域搜尋（VNS）元啟發式。

## 1. Ramoneda et al. (2021) — Piano Fingering with Reinforcement Learning

### 核心貢獻

首次將**深度強化學習（DQN）**應用於鋼琴指法生成，將樂譜視為環境、手指選擇視為動作。

### 方法

- **狀態** s = (cf, cn, nn)：當前手指、當前音符、下一音符
- **動作** a：選擇下一個手指（1-5）
- **獎勵函數** r：手位不變 → 正獎勵；手位改變 → 負獎勵；解剖學不可行 → 懲罰
- **策略** π：以 Fully Connected DQN 估計 Q 函數
- 使用 Experience Replay 穩定訓練
- 僅處理**右手單聲部**（左手可透過對稱鏡像）

### 評估

5 個遞增複雜度的實驗（EX1-EX5）：
- EX1-EX2：簡單序列，agent 成功學到不換手位
- EX3：C 大調音階（複雜環境），獎勵函數震盪
- EX4-EX5：需 2 次手位變換的 C 大調音階

### GRU 合成模型

使用 PianoPlayer 產生 >1500 首 Musescore 樂譜的合成指法數據集，以 GRU 網路訓練，達到 **78% 平衡準確率**。

### 限制

- 僅限單聲部旋律
- 環境模型過於簡化
- 收斂速度慢，比離線方法需要更多時間

## 2. Gao et al. (2023) — Model-Based Reinforcement Learning

### 核心貢獻

⭐ 首次將**基於模型的 RL**（Prioritized Sweeping）應用於指法生成，建立更精確的環境模型，支援和弦指法。

### MDP 建模

- **狀態** s = (i, f_g, n_next)：音符位置、當前指法組合、下一時刻音符
- **手特徵矩陣 M_f**：5×5 矩陣，記錄每對手指的最大展距和最大交叉距離（以白鍵距離計）
- **白鍵距離 d_k**：將所有音符轉為白鍵距離（黑鍵計 0.5），解決 Parncutt 原始距離矩陣的問題

### 獎勵函數的三個指標

| 指標 | 定義 | 作用 |
|------|------|------|
| **伸展率 r_s** | (d_k - d_nature) / (d_max - d_nature) | 接近 1 = 接近最大伸展，不舒適 |
| **手移動量** | 當前手位與前一手位的白鍵距離 | 懲罰頻繁的手位變換 |
| **交叉指法** | 手指交叉的跨距 | 懲罰不自然的手指交叉 |

### Invalid Action Masking

⭐ 核心創新：預先過濾解剖學不可能的指法組合（超過 M_f 最大展距、手指交叉違規），**縮小搜索空間**，提高取樣效率。

### Prioritized Sweeping

取代傳統 Q-table 的全枚舉，使用基於 key-value 儲存的表格式 RL，配合優先掃描加速收斂。

### 樂譜分段

提出將樂譜按音符間的**停頓點**分段，各段可平行求解。

### 與 V6 DP 的對應

| Gao MBRL | V6 DP |
|----------|-------|
| 手特徵矩陣 M_f | FINGER_COMFORT_SPAN / FINGER_MAX_SPAN |
| 伸展率 r_s | span_cost |
| 手移動懲罰 | position_change_cost |
| Invalid Action Masking | V6 的 feasibility check |
| 樂譜分段 | V6 的樂句感知分段 |

## 3. Balliauw et al. (2017) — Variable Neighbourhood Search (VNS)

### 核心貢獻

⭐ **首個**能處理**複雜多聲部**鋼琴音樂的指法演算法，使用元啟發式避免 DP/圖搜索在多聲部上的指數爆炸。

### 問題建模

- 指法問題 = **部分約束滿足問題（PCSP）**，已知為 **NP-hard**
- 每個音符 = 圖中的頂點，指法 = 值域 {1,2,3,4,5}
- 邊罰函數 = 15 條規則的加權總和

### 距離矩陣與虛擬黑鍵

改進 Parncutt 距離定義：在 E-F 和 B-C 之間加入**虛擬黑鍵**（鍵 6 和 14），使距離計算在黑白鍵之間一致。八度 = 15 個單位（而非 12 半音）。

### 15 條規則

改編自 Parncutt 1997、Jacobs 2001、Al Kasimi 2007：
- 規則 1-2：距離超出 MaxComf/MinRel → 懲罰
- 規則 3：三連音距離檢查
- 規則 5-7：特定手指（4 指、3-4 連用、白鍵黑鍵轉換）
- 規則 8-9：拇指彈黑鍵、5 指彈白鍵
- 規則 10-12：拇指穿越方向、換指法
- 規則 13-14：**超出 MinPrac/MaxPrac**（硬約束，高懲罰 +10）
- 規則 15：同音換指

### VNS 演算法

三種鄰域結構：

| 鄰域 | 操作 | 大小 |
|------|------|------|
| **Change1** | 改變單個音符的指法 | (5-s)·t |
| **Change2** | 同時改變兩個音符的指法 | 約 s²·(5-s)² |
| **SwapPart** | 交換長音符在和弦內的指法分配 | 視和弦結構而定 |

流程：隨機初始解 → Swap 預處理 → 隨機選擇 Change1/SwapPart 順序 → Change2 → 若無改善則擾動（perturbation） → 迭代至收斂。

### 使用者個性化

⭐ 距離矩陣（MinPrac, MaxPrac, MinRel, MaxRel, MinComf, MaxComf）**可由使用者自訂**，實現個人化指法。作者明確指出「for pianists with smaller hands, tables with reduced absolute values... are available」。

### 實驗結果

- 測試曲目包括 Chopin、Beethoven 等 9 首不同複雜度的作品
- 與出版樂譜指法比較：平均 **45% 音符指法完全一致**
- 算法在 5 秒內可完成最複雜的曲目

## 三篇論文的比較

| 特性 | Ramoneda 2021 | Gao 2023 | Balliauw 2017 |
|------|-----------|----------|-----------|
| **方法** | Model-free DQN | Model-based RL | VNS 元啟發式 |
| **聲部** | 僅單聲部 | 和弦（多音同時） | 完整多聲部 |
| **手** | 僅右手 | 雙手（分開處理） | 雙手（分開處理） |
| **個人化** | 無 | M_f 矩陣可自訂 | 距離矩陣可自訂 |
| **與 Parncutt 關係** | 獎勵函數受啟發 | 白鍵距離取代 | 15 規則改編自 Parncutt |
| **實用性** | 概念驗證 | 中等 | ⭐ 最實用 |

## 與 V6 DP 的整體關聯

- V6 DP 使用的是**精確 DP**，而非啟發式或 RL，在單聲部上保證全局最優
- Balliauw 的 VNS 提供了 V6 在多聲部場景下的替代方案
- Gao 的 M_f 矩陣和 Invalid Action Masking 可啟發 V6 的個人化擴展
- 三篇論文共同確認：**距離矩陣個人化**是指法演算法的關鍵需求

## 相關頁面

- [src_parncutt1997_ergonomic_model](src_parncutt1997_ergonomic_model.md) — Parncutt 12 條規則（Balliauw 改編為 15 條）
- [src_computational_fingering](src_computational_fingering.md) — Nakamura HMM、PIG Dataset、⭐ Ramoneda 2022 ArGNN（同一團隊的後續工作）
- [src_fingering_algorithms_batch2](src_fingering_algorithms_batch2.md) — Telles、KTH 論文、Liao Transformer
- [concept_finger_span_table](concept_finger_span_table.md) — 跨度表（VNS 的距離矩陣對應）
- [concept_piano_fingering_principles](concept_piano_fingering_principles.md) — 五大共識原則
