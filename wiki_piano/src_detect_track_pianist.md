---
title: "手部偵測與追蹤技術（2 篇）"
date_ingested: 2026-04-10
source_type: academic_paper_collection
sources:
  - "Gorodnichy, Dmitry O.; Yogeswaran, Arjun. Detection and Tracking of Pianist Hands and Fingers. NRC-CNRC Canada / University of Ottawa."
  - "Zhang, Fan et al. (2020). MediaPipe Hands: On-device Real-time Hand Tracking. Google Research. arXiv:2006.10214."
tags: [computer_vision, hand_tracking, finger_detection, MIDI, video_recognition, piano_teaching, MediaPipe, landmark]
---

# 手部偵測與追蹤技術

2 篇論文涵蓋鋼琴家手部追蹤和通用手部姿態估計技術。

## 1. Gorodnichy & Yogeswaran — Detection and Tracking of Pianist Hands

電腦視覺應用：從影片中偵測和追蹤鋼琴家的手與手指。

### 系統架構

1. 攝影機架設在鍵盤上方
2. 同步 MIDI 數據與影片
3. 偵測手部 → 追蹤手指 → 標注「哪根手指彈哪個鍵」
4. 產生標注影片供遠端教學使用

### 應用場景

- **遠端鋼琴教學**：學生不僅能聽到老師彈什麼，還能看到用哪根手指
- **自動指法標注**：從演奏影片中提取指法資訊
- **樂譜製作**：自動產生含指法標注的樂譜
- **合成手指動畫**：生成虛擬鋼琴演奏動畫

## 2. Zhang et al. (2020) — MediaPipe Hands: On-device Real-time Hand Tracking

### 核心貢獻

⭐ Google 的**即時手部追蹤解決方案**，僅需 RGB 攝影機，在行動裝置上即時運行，預測 21 個 2.5D 手部關鍵點。

### 雙階段架構

| 階段 | 模型 | 輸入 | 輸出 |
|------|------|------|------|
| **BlazePalm 偵測器** | SSD 單次偵測器 | 全幅影像 | 手掌邊界框 |
| **Hand Landmark 模型** | 回歸網路 | 裁切後手部影像 256×256 | 21 個 2.5D 關鍵點 |

### 為何偵測手掌而非手部

- 手掌是剛性物體（如拳頭、攤開手的手掌形狀不變）
- 估計方形邊界框即可（忽略長寬比）
- 非最大值抑制在雙手自遮擋時仍有效
- 減少錨點數量 3-5 倍

### Hand Landmark 模型

3 個輸出頭（共享特徵提取器）：
1. **21 個關鍵點**：x, y 座標 + 相對深度（相對於手腕）
2. **手部存在旗標**：用於觸發偵測器重啟
3. **慣用手分類**：左/右手

### 訓練數據

| 數據集 | 數量 | 用途 |
|--------|------|------|
| In-the-wild | 6K 張 | 手掌偵測器 + 關鍵點 |
| In-house | 10K 張（30 人） | 關鍵點（覆蓋所有手勢） |
| Synthetic | 100K 張（3D 模型渲染） | 深度監督 + 關鍵點 |

混合真實+合成數據的效果最佳（MSE 13.4% vs 純真實 16.1%）。

### 模型尺寸與速度

| 模型 | 參數量 | MSE | Pixel 3 | Samsung S20 | iPhone 11 |
|------|--------|-----|---------|------------|-----------|
| Light | 1M | 11.83 | 6.6ms | 5.6ms | 1.1ms |
| **Full** | **1.98M** | **10.05** | **16.1ms** | **11.1ms** | **5.3ms** |
| Heavy | 4.02M | 9.82 | 36.9ms | 25.8ms | 7.5ms |

Full 模型在質量和速度之間取得最佳平衡。

### 即時追蹤優化

- 手掌偵測器僅在**第一幀**和**手部遺失**時運行
- 後續幀從前一幀的 landmark 推導邊界框
- 大幅降低計算量

### 應用

- 手勢辨識（手指彎曲/伸直狀態 → 預定義手勢映射）
- AR 效果
- 跨平台：Android、iOS、Web（TensorFlow.js）

## 與本專案的關聯

| 技術 | 指法標註軟體啟示 |
|------|----------|
| 21 關鍵點包含所有手指尖和關節 | 可從鋼琴演奏影片中追蹤每根手指的位置 |
| 2.5D 深度估計 | 可判斷手指是否在按鍵（垂直方向） |
| 左/右手分類 | 自動區分雙手 |
| 即時推理（~16ms） | 支援即時指法回饋 |
| 開源（mediapipe.dev） | 可直接整合 |
| 與 Moryosef (2023) 的 APFD 系統互補 | MediaPipe 提供底層手部追蹤，APFD 系統加入鍵盤-手指映射 |

## 相關頁面

- [[src_computational_fingering]] — Moryosef 影片指法提取（使用類似技術）
- [[concept_piano_fingering_principles]]
- [[src_piano_biomechanics_papers]] — 手指運動學
