---
title: "鋼琴指法計算模型論文（2 篇）"
date_ingested: 2026-04-08
source_type: academic_paper_collection
sources:
  - "Nakamura, E., Saito, Y., & Yoshii, K. (2019). Statistical Learning and Estimation of Piano Fingering. Information Sciences."
  - "Moryosef, A., Elazar, Y., & Goldberg, Y. (2023). At Your Fingertips: Extracting Piano Fingering Instructions from Videos. arXiv:2303.03745."
tags: [computational_model, HMM, deep_learning, video_extraction, PIG_dataset, fingering_estimation]
---

# 鋼琴指法計算模型論文

兩篇直接關於**自動指法標注演算法**的論文，與本專案 V6 DP 最為相關。

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
- 與 [[src_detect_track_pianist]] 的 Gorodnichy 系統類似但更先進

## 相關頁面

- [[src_parncutt1997_ergonomic_model]]
- [[concept_finger_span_table]]
- [[concept_piano_fingering_principles]]
