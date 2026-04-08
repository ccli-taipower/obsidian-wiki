---
title: "An Ergonomic Model of Keyboard Fingering for Melodic Fragments"
date_ingested: 2026-04-08
source_type: academic_paper
source_file: "raw/PaSlClRaDe97_FingeringModel.pdf"
authors: "Richard Parncutt, John A. Sloboda, Eric F. Clarke, Matti Raekallio, Peter Desain"
journal: "Music Perception, Summer 1997, Vol.14, No.4, 341-382"
tags: [fingering_model, ergonomics, biomechanics, computational_model, span_table, Czerny, DP_algorithm]
---

# Parncutt et al. (1997): An Ergonomic Model of Keyboard Fingering for Melodic Fragments

鋼琴指法計算模型的奠基論文。提出基於人體工學約束的規則系統，從所有可能指法中列舉並評分，預測最佳指法。**與本專案 V6 DP 演算法的跨度表和成本函數直接相關。**

## 模型概述

- **輸入**：旋律片段（以 C 上方的半音數表示音高序列）
- **輸出**：所有可能指法的排名（依難度由易到難）
- **限制**：僅限右手、單音旋律、假設中等力度的連奏
- **方法**：列舉所有合法指法 → 以規則系統評分 → 排名

## 跨度定義（核心術語）

| 術語 | 定義 |
|------|------|
| **MaxPoss** | 兩指之間的最大物理可能跨度（解剖極限）|
| **MaxPrac** | 最大實用跨度（音樂演奏中實際會使用的最大距離）|
| **MinPrac** | 最小實用跨度（最小可接受距離）|
| **MaxRel** | 最大放鬆跨度（手放鬆時的最大自然間距）|
| **MinRel** | 最小放鬆跨度（手放鬆時的最小自然間距）|
| **MaxComf** | 最大舒適跨度（MaxPrac − 2 半音）|
| **MinComf** | 最小舒適跨度（MinPrac + 2 半音）|

## Table 1: 右手所有指對的跨度值（半音）

| 指對 | MinPrac | MaxPrac | MinRel | MaxRel | MaxComf | MinComf* |
|------|---------|---------|--------|--------|---------|----------|
| 1-2 | -5 | 10 | 1 | 5 | 8 | -3* |
| 1-3 | -4 | 12 | 1 | 7 | 10 | -2* |
| 1-4 | -3 | 14 | 1 | 9 | 12 | -1* |
| 1-5 | -1 | 15 | 1 | 10 | 13 | 1* |
| 2-3 | 1 | 2 | 1 | 2 | - | - |
| 2-4 | 1 | 5 | 1 | 3 | - | - |
| 2-5 | 2 | 8 | 1 | 6 | 6 | - |
| 3-4 | 1 | 2 | 1 | 2 | - | - |
| 3-5 | 1 | 5 | 1 | 4 | 3 | - |
| 4-5 | 1 | 4 | 1 | 3 | - | - |

*MinPrac 含拇指的指對為負值（拇指可穿越到另一指下方）。

**重要**：這些數值基於「平均」成年男性鋼琴家。小手可將所有值乘以約 0.9 調整。

## 12 條評分規則

### 基礎規則（跨度相關）

**Rule 1 — Stretch Rule**：每個超過 MaxComf 或小於 MinComf 的半音，加 2 分。

**Rule 2 — Small-Span Rule**：含拇指的指對，音程小於 MinRel 時每半音加 1 分；不含拇指的指對，每半音加 2 分。偏好「下一音下一指」的鄰近原則。

**Rule 3 — Large-Span Rule**：含拇指的指對，音程超過 MaxRel 時每半音加 1 分；不含拇指的指對，每半音加 2 分。

### 位置變化規則

**Rule 4 — Position-Change-Size Rule**：手位移動時，移動距離（半音數）轉為難度分。含拇指加 1 分/半音，不含加 2 分/半音。

**Rule 5 — Position-Change-Count Rule**：每次半位置變化加 2 分，全位置變化加 2 分。同音換指視為半位置變化（1 分）。

### 弱指規則

**Rule 6 — Weak-Finger Rule**：使用小指（5）加 1 分。

### 三四指規則

**Rule 7 — Three-Four-Five Rule**：連續使用 3-4-5 或 5-4-3 加 1 分。

**Rule 8 — Three-to-Four Rule**：3→4 方向不變（如上行 3→4）加 1 分。與 4→3 不同（4→3 更自然）。

### 拇指規則

**Rule 9 — Thumb-on-Black Rule**：拇指彈黑鍵加 1 分。

**Rule 10 — Five-on-Black Rule**：小指彈黑鍵（且前後音為白鍵）加 1 分。

**Rule 11 — Thumb-Passing Rule**：拇指穿越時，同層（白→白或黑→黑）加 1 分；下白上黑（穿越到黑鍵）加 3 分。

**Rule 12 — Thumb-on-Black Passing Rule**：非拇指→黑鍵上的拇指穿越加額外分數。

## 驗證結果

以 7 首 Czerny 練習曲（Op. 821）的開頭片段測試：
- 鋼琴家推薦的指法大多在模型預測的前 10 名中
- 但模型也產生了一些鋼琴家不推薦的高排名指法
- **偵測到的差距**：模型未考慮認知/音樂性因素（如樂句方向、旋律輪廓、重複模式）

## 與本專案 V6 DP 的對應關係

| Parncutt 規則 | V6 DP 對應 |
|-------------|-----------|
| Table 1 跨度表 | `FINGER_MAX_SPAN` / `FINGER_COMFORT_SPAN` / `FINGER_MIN_SPAN` |
| Stretch Rule | `span_cost()` in `_assignment_cost` |
| Small/Large-Span Rule | `_assignment_cost` 的跨度懲罰 |
| Position-Change Rules | `_transition_cost` 的接力成本 |
| Weak-Finger Rule | 無名指和弦懲罰 (`RING_FINGER_CHORD_PENALTY`) |
| Thumb-on-Black Rule | 黑鍵懲罰（V6 目前設為 0）|
| Thumb-Passing Rule | `_transition_cost` 的拇指穿越規則 |
| Three-Four-Five Rule | 未明確實作 |

## 論文的局限性（作者自述）

- 僅限右手單音旋律
- 不處理和弦、裝飾音、重複音換指
- 未考慮音樂詮釋（分句、力度、觸鍵）
- 跨度表基於平均手型，個體差異未建模
- 未結合動態規劃（僅列舉+評分，無路徑最佳化）

## 學術影響

此論文建立了鋼琴指法計算的基礎框架，後續的 Kasimi & Nichols (2007)、Hart, Kochman & Sondhi (2000)、Al Kasimi et al. 等均以此為基礎擴展為 DP/HMM 模型。

## 相關頁面

- [[concept_piano_fingering_principles]]
- [[concept_finger_span_table]]
- [[concept_thumb_technique]]
- [[src_computational_fingering]]
