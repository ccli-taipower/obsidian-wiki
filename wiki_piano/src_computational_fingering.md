---
title: "鋼琴指法計算模型論文（3 篇）"
date_ingested: 2026-04-10
source_type: academic_paper_collection
sources:
  - "Nakamura, E., Saito, Y., & Yoshii, K. (2019). Statistical Learning and Estimation of Piano Fingering. Information Sciences."
  - "Moryosef, A., Elazar, Y., & Goldberg, Y. (2023). At Your Fingertips: Extracting Piano Fingering Instructions from Videos. arXiv:2303.03745."
  - "Ramoneda, P., Jeong, D., Nakamura, E., Serra, X., & Yoshii, K. (2022). Automatic Piano Fingering from Partially Annotated Scores using Autoregressive Neural Networks. ACM Multimedia 2022."
tags: [computational_model, HMM, deep_learning, video_extraction, PIG_dataset, ThumbSet, autoregressive, GNN, fingering_estimation, beam_search, soft_labels]
---

# 鋼琴指法計算模型論文

三篇直接關於**自動指法標注演算法**的論文，與本專案 V6 DP 最為相關。

## 1. Nakamura et al. (2019) — Statistical Learning and Estimation of Piano Fingering

### 核心貢獻
以 HMM（隱馬可夫模型）為基礎的指法估計，是目前 state-of-the-art。

### 方法比較
- **Constraint-based**（如 Parncutt 1997）：手動設定規則和參數
- **HMM-based**（本文）：從數據中**學習**轉移機率和成本
- **DNN-based**：深度神經網路直接預測，但效果不如高階 HMM

### PIG Dataset (Piano Fingering Dataset)
- 150 首西方古典鋼琴曲（Bach、Mozart、Chopin + 其他 24 位作曲家）
- 每首由 1 位以上鋼琴家標注指法
- 總計 309 個標注版本（6,557 小節、100,044 個音符）
- **同一段落不同鋼琴家的指法可能不同** → 評估指標需要考慮多解答

| 子集 | 作曲家數 | 曲數 (小節; 音符) | 有多版指法的段落 |
|------|--------|----------------|-----------|
| Bach | 1 | 10 (218; 3,657) | 40 (872; 14,628) |
| Mozart | 1 | 10 (185; 2,546) | 60 (1,110; 15,276) |
| Chopin | 1 | 10 (244; 4,022) | 50 (1,220; 20,110) |
| Misc | 24 | 120 (2,533; 38,501) | 159 (3,355; 50,030) |
| **Total** | **24** | **150 (3,180; 48,726)** | **309 (6,557; 100,044)** |

### 關鍵發現
- 高階 HMM 優於所有其他方法（包括 DNN）
- 模型能量化**個人差異**（不同鋼琴家的指法偏好）
- 局限：忽略樂句邊界、音程方向與手的互依性

### 與 V6 DP 的對應
| Nakamura HMM | V6 DP |
|-------------|-------|
| 轉移機率 | `_transition_cost` |
| 發射機率 | `_assignment_cost` |
| 高階依賴 | 樂句感知 DP |
| PIG Dataset | 可用於驗證 V6 輸出 |

## 2. Moryosef et al. (2023) — At Your Fingertips: Extracting Piano Fingering from Videos

### 核心貢獻
從 YouTube 鋼琴演奏影片中**自動提取指法標注**。

### 系統架構
1. 偵測鍵盤位置和手部邊界框
2. 手部姿態估計（左/右手分類）
3. 手指偵測（識別每根手指的位置）
4. 與 MIDI 數據同步 → 確定哪根手指彈哪個音

### 成果
- F1 Score: 97%（在自建數據集上）
- 建立了 **Automatic Piano Fingering Dataset (APFD)**：從 90 部影片提取 196K 高品質指法標注
- 目前最大的自動標注指法數據集

### GAN-based 域適應
使用 CycleGAN 將合成影像轉換為真實影像風格，解決訓練數據不足問題。

### 與本專案的關聯
- 可作為 learn 流程的擴展：從影片而非 PDF 提取指法
- APFD 數據集可用於驗證 V6 DP 輸出
- 與 [src_detect_track_pianist](src_detect_track_pianist.md) 的 Gorodnichy 系統類似但更先進

## 3. Ramoneda et al. (2022) — Automatic Piano Fingering from Partially Annotated Scores

### 核心貢獻

⭐ 提出 **ThumbSet** 大規模指法數據集（2523 首）+ **自迴歸神經網路**（ArLSTM / ArGNN），在 PIG 測試集上**超越所有 HMM 基線**。

### ThumbSet 數據集

從 MuseScore 網站收集的群眾標注指法數據：

| 特性 | ThumbSet | PIG |
|------|---------|-----|
| 曲數 | **2523** | 150 |
| 標注來源 | MuseScore 群眾標注 | 專業鋼琴家 |
| 標注覆蓋率 | **52%**（部分標注） | 100%（完整標注） |
| 音符數 | ~700K | 100K |
| 品質 | 噪聲較大（非專家） | 高品質 |

- 託管於 Zenodo
- 曲目涵蓋多種風格和難度

### 自迴歸模型架構

兩種模型共享**解碼器**（autoregressive LSTM），差異在編碼器：

| 模型 | 編碼器 | 特點 |
|------|--------|------|
| **ArLSTM** | 雙向 LSTM | 將多聲部壓縮為 pitch sequence（按時間排列所有音符） |
| **ArGNN** | Gated Graph Neural Network (GGNN) | 用圖結構編碼多聲部關係：**onset edges**（同時發聲）+ **next edges**（時序相鄰） |

#### ArGNN 圖結構

- 每個音符為節點，特徵 = (pitch, duration, onset)
- **Onset edges**：連接同時發聲的音符（捕捉和弦/多聲部關係）
- **Next edges**：連接時間上相鄰的音符（捕捉旋律線）
- GGNN 執行多輪訊息傳遞，學習音符間的上下文關係

#### Beam Search 解碼

- 自迴歸解碼：逐一預測每個音符的指法（以前一步預測為輸入）
- **Beam width k=6**：保留前 6 個最佳候選序列
- 確保指法序列的**連貫性**（避免相鄰音符指法衝突）

### 處理噪聲標注的技術

ThumbSet 的群眾標注品質不一（inter-annotator agreement ~70%），需要特殊處理：

1. **Soft labels（軟標籤）**：將 one-hot 標籤（如 [0,0,1,0,0]）改為平滑分布（如 [0.06, 0.06, 0.76, 0.06, 0.06]），30% 質量均勻分配給其他手指——防止模型過度擬合噪聲標注
2. **資料增強**：
   - **Hand inversion**：左右手互換（映射指法 1↔1, 2↔5, 3↔4）
   - **Time inversion**：將音符序列反轉
   - **Octave transposition**：±1 八度移調

### 實驗結果（PIG 測試集）

| 模型 | M_gen ↑ | M_high ↑ | M_soft ↑ | M_rec ↑ | M_cp ↓ |
|------|---------|----------|----------|---------|--------|
| Nakamura HMM | 54.71 | 61.75 | 81.40 | 68.90 | 3.08 |
| DNN (Nakamura) | 39.86 | 45.72 | — | — | — |
| Ramoneda DQN (2021) | 47.00 | — | — | — | — |
| ArLSTM-s | 58.25 | 64.23 | 84.47 | 74.60 | 1.60 |
| ArGNN-s | 60.12 | 66.45 | 85.20 | 76.34 | 1.23 |
| **ArGNNThumb-s** | **62.77** | **68.87** | **86.15** | **78.55** | **0.99** |

- **ArGNNThumb-s**：ArGNN + ThumbSet 預訓練 + PIG 微調 + soft labels
- M_gen（一般匹配率）超越 Nakamura HMM **+8.06**
- **M_cp = 0.99**（手位變換率幾乎與專家標注相同，Nakamura HMM = 3.08）

### 評估指標

| 指標 | 定義 |
|------|------|
| M_gen | 一般匹配率（correct / total） |
| M_high | 最高匹配率（取所有參考標注的最佳匹配） |
| M_soft | 軟匹配（允許 ±1 指法差異部分計分） |
| M_rec | 回覆率（考慮多種正確解答） |
| M_cp | 手位變換率（越低越好，越接近人類） |

- 開源評估框架：`PRamoneda/APF_eval`（GitHub）

### 關鍵洞見

1. **預訓練的力量**：ThumbSet 雖噪聲大但規模大（2523 vs 150），預訓練後微調效果顯著
2. **圖結構優於序列**：ArGNN > ArLSTM，因為圖能直接編碼同時發聲的多聲部關係
3. **Soft labels 是關鍵**：處理噪聲標注的有效策略，可推廣至其他標注品質不一的任務
4. **自迴歸 > 獨立預測**：逐步解碼確保序列連貫（M_cp ≈ 1），HMM 的 M_cp = 3 表示手位頻繁不必要地變換

### 與 V6 DP 的對應

| Ramoneda 2022 | V6 DP |
|---------------|-------|
| Onset edges（同時發聲） | 和弦指法約束（同手的多音符） |
| Next edges（時序相鄰） | DP 轉移（前一音→後一音） |
| Beam search（k=6） | DP 最優路徑（全域最優） |
| Soft labels | — （V6 無需處理噪聲） |
| M_cp ≈ 1（手位變換率） | W_POSITION_CHANGE（懲罰不必要的手位變換） |
| ThumbSet 預訓練 | — （V6 為規則型，無預訓練） |
| 多聲部圖結構 | V6 目前為**單聲部**；ArGNN 的方法啟示未來多聲部擴展 |

### 開放資源

| 資源 | 連結/位置 |
|------|---------|
| ThumbSet 數據集 | Zenodo |
| 原始碼 | GitHub: `PRamoneda/Automatic-Piano-Fingering` |
| 評估框架 | GitHub: `PRamoneda/APF_eval` |

## 相關頁面

- [src_parncutt1997_ergonomic_model](src_parncutt1997_ergonomic_model.md)
- [concept_finger_span_table](concept_finger_span_table.md)
- [concept_piano_fingering_principles](concept_piano_fingering_principles.md)
- [src_fingering_rl_metaheuristic](src_fingering_rl_metaheuristic.md) — Ramoneda 2021 DQN（同一研究團隊的早期 RL 方法）
- [src_voice_separation](src_voice_separation.md) — 聲部分離（ArGNN 的 onset/next edges 類似 Karystinaios 的圖結構）
- [src_asap_dataset](src_asap_dataset.md) — ASAP 數據集（可與 ThumbSet 互補）
