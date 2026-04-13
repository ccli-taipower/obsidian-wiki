---
title: "聲部分離演算法（2 篇）"
date_ingested: 2026-04-10
source_type: academic_paper_collection
sources:
  - "McLeod, Andrew; Steedman, Mark (2016). HMM-Based Voice Separation of MIDI Performance. University of Edinburgh."
  - "Karystinaios, Emmanouil; Foscarin, Francesco; Widmer, Gerhard (2023). Musical Voice Separation as Link Prediction: Modeling a Musical Perception Task as a Multi-Trajectory Tracking Problem. IJCAI 2023."
tags:
  - voice_separation
  - HMM
  - GNN
  - link_prediction
  - multi_trajectory_tracking
  - polyphonic
  - MIDI
  - symbolic_music
---

# 聲部分離演算法

聲部分離是將多聲部音樂中的音符分配到各個獨立的旋律線（聲部）中。這是鋼琴指法標註的**前置步驟**——V6 DP 需要知道哪些音符屬於同一聲部，才能正確計算手指轉換成本。

## 1. McLeod & Steedman (2016) — HMM-Based Voice Separation

### 核心貢獻

基於 Huron 的聽覺感知原則建構 HMM，可處理即時 MIDI 輸入，是 GNN 方法之前的 **state-of-the-art**。

### 感知原則（Huron 2001, Tymoczko 2008）

| 原則 | 說明 | HMM 實現方式 |
|------|------|----------|
| **Common Tone Rule** | 同聲部相鄰音符應音高接近 | 音高接近度影響轉移機率 |
| **Avoid Leaps Rule** | 避免大跳 | 聲部音高 = 最近 l 個音的加權平均 |
| **Part-Crossing Rule** | 不同聲部不應交叉 | 排序懲罰 |
| **Temporal Continuity** | 同聲部音符應時間連續 | 時間間隔影響轉移機率 |

### HMM 模型

- **狀態** S：一組單聲部聲部的列表 V_i
- **發射函數**：確定性（每個狀態對應一組同時發音的音符）
- **轉移機率**：基於音高接近度和時間連續性的乘積
- 允許同聲部內音符有**少量重疊**（≤ 前音時值的 50%），適應真實演奏的不精確
- 聲部數量**自動決定**（無需預設）

### 聲部音高計算

Pitch(V) = 最近 l 個音符的**指數加權平均**（每前一個音權重 ×2），允許聲部音域逐漸移動。

### 增量式推理

使用修改版 Viterbi 的 **beam search**，每步只保留前 k 個最佳狀態，支援即時處理。

### 評估

- 語料：**78 首 J.S. Bach 作品**（以原始樂譜的聲部標記為金標準）
- 顯著優於 Chew & Wu (2005) 和其他先前方法
- 在即時 MIDI 輸入上表現與離線版本接近

### 限制

- 假設嚴格單聲部（同一聲部不可同時有多音）
- 修改版 Viterbi 的 beam width 需要手動調整
- 依賴 Huron 原則，可能不適用於非西方音樂

## 2. Karystinaios et al. (2023) — Voice Separation as Link Prediction (GMTT)

### 核心貢獻

⭐ **當前 state-of-the-art**：將聲部分離重新框架為**多軌跡追蹤（MTT）**問題，使用異質圖神經網路（GNN），不依賴任何啟發式規則。

### 問題框架

- 每個音符 = 圖中的節點
- 聲部 = 軌跡（trajectory）：嚴格有序的單聲部音符序列
- 目標 = 預測相鄰音符間是否有連結（link prediction）
- **MTT 約束**：每個音符最多 1 個入邊 + 1 個出邊

### 圖建構

使用 **7 種邊類型**（edge relations）建構異質圖：

| 邊類型 | 條件 | 方向 |
|--------|------|------|
| **onset** | 同時開始 | 無向 |
| **during** | 一音在另一音持續中開始 | 有向 |
| **follow** | 一音在前音結束時開始 | 有向 |
| **silence** | 間隔後開始（無其他音填充） | 有向 |
| + 3 種反向邊 | during⁻¹, follow⁻¹, silence⁻¹ | 有向 |

### 節點特徵

- 音高類別（12 維 one-hot）
- 八度（8 維 one-hot）
- 時值（歸一化 float，用 tanh 壓縮）
- 位置編碼（Laplacian 前 20 特徵向量）

### 模型架構（GMTT）

1. **編碼器**：Residual Gated Convolutions + Jumping Knowledge，對每種邊類型獨立計算，再平均
2. **Bi-LSTM**：在各層卷積輸出上計算注意力權重
3. **連結預測器**：MLP，輸入兩個節點的 embedding 串聯，輸出連結機率

### 正則化損失

⭐ 提出新的**正則化損失**，鼓勵預測的鄰接矩陣 Â 接近線性分配矩陣（每行每列最多一個非零元素）：

L_reg = L1 損失 + L2 損失，強制稀疏性，穩定訓練。

### 後處理

可選的**Hungarian 算法**後處理，將預測鄰接矩陣轉為嚴格的線性分配（保證 MTT 約束）。

### 評估

| 數據集 | McLeod F1 | GMTT F1 | GMTT+LA F1 |
|--------|-----------|---------|------------|
| Bach Inventions | 0.992 | 0.995 | **0.997** |
| Bach Sinfonias | 0.982 | 0.978 | **0.985** |
| WTC I (Fugues) | 0.964 | 0.967 | **0.976** |
| WTC II (Fugues) | 0.964 | 0.962 | **0.972** |
| **Haydn Quartets** | 0.781 | 0.850 | **0.872** |

- 在 **Haydn 弦樂四重奏**上改善最大（F1: 0.781 → 0.872）
- 弦樂四重奏更難：更大音域、更多休止、八度跳躍、聲部交叉
- 總計 1136 首作品（474 MCMA + 662 KernScore），是目前最大的聲部分離評估集

### 消融研究

| 變體 | Haydn F1 | WTC II F1 |
|------|----------|-----------|
| 同質圖（Homogeneous） | 0.809 | 0.943 |
| GraphSage 卷積 | 0.828 | 0.944 |
| 無正則化 | 0.720 | 0.856 |
| 固定正則化權重 | 0.652 | 0.942 |
| **GMTT（完整模型）** | **0.850** | **0.962** |

### 限制

- 假設量化 MIDI（音符對齊到節拍網格）
- 假設嚴格單聲部
- 未處理原始音訊

## 與 V6 DP 的關聯

| 發現 | V6 DP 啟示 |
|------|----------|
| 聲部分離是指法的前置步驟 | V6 目前假設 MusicXML 已提供聲部標記 → 若處理 MIDI 需要先做聲部分離 |
| McLeod HMM 可即時處理 | 適合即時指法建議場景 |
| GMTT 的 7 種邊類型 | 捕捉音符間的多種時間關係，可用於增強 V6 的樂句結構分析 |
| MTT 約束（每音最多 1 入 1 出） | 與 V6 的單聲部 DP 假設一致 |
| Haydn 弦樂四重奏更難 | 聲部交叉、大跳等場景也是 V6 指法困難的場景 |

## 相關頁面

- [src_computational_fingering](src_computational_fingering.md) — Nakamura HMM（指法）
- [src_fingering_rl_metaheuristic](src_fingering_rl_metaheuristic.md) — 多聲部指法演算法
- [concept_piano_fingering_principles](concept_piano_fingering_principles.md) — 五大共識原則
