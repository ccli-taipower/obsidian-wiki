---
title: "ASAP: Aligned Scores and Performances 數據集"
date_ingested: 2026-04-10
source_type: academic_paper
authors: "Francesco Foscarin, Andrew McLeod, Philippe Rigaux, Florent Jacquemard, Masahiko Sakai"
venue: "ISMIR 2020"
tags:
  - dataset
  - score_performance_alignment
  - MusicXML
  - MIDI
  - beat_tracking
  - AMT
  - MAESTRO
---

# ASAP: A Dataset of Aligned Scores and Performances

## 核心貢獻

⭐ **最大的樂譜-演奏對齊數據集**：222 首數位樂譜 × 1068 場人類演奏（>92 小時），提供拍級對齊的 MusicXML + MIDI + 音訊。

## 數據集規模

| 作曲家 | 樂譜數 | MIDI 演奏 | 音訊演奏 |
|--------|--------|----------|--------|
| Bach | 59 | 169 | 152 |
| Beethoven | 57 | 271 | 120 |
| Chopin | 34 | 290 | 109 |
| Liszt | 16 | 121 | 48 |
| Schubert | 13 | 62 | 44 |
| Schumann | 10 | 28 | 7 |
| 其他 9 位 | 33 | 127 | 40 |
| **合計** | **222** | **1068** | **520** |

## 數據格式

每首作品提供：
- **MusicXML 樂譜**（來自 MuseScore 線上圖書館，經手動修正）
- **量化 MIDI**（由 MuseScore3 匯出，音符對齊節拍網格）
- **演奏 MIDI**（來自 MAESTRO 數據集，Yamaha e-competition 真實演奏）
- **音訊**（520 場演奏有音訊）
- **標註**：拍（beat）、強拍（downbeat）、調號、拍號變化

## 標註工作流程

1. 用 Music21 從 MusicXML 提取節拍和調號資訊
2. 用 MuseScore3 匯出 MIDI
3. 用 PrettyMIDI 從 MIDI 提取拍位
4. 將每個強拍對齊到 MusicXML 的小節號
5. 使用 Score2Performance 映射算法對齊樂譜音符與演奏音符
6. 將標註投射到演奏時間軸

約 3% 的小節有錯誤（不正確的時值、隱形小節線等），引入手動修正步驟。

## 與現有數據集的比較

| 數據集 | 規模 | 真實演奏 | 樂譜 | 拍級對齊 | 調號 |
|--------|------|--------|------|--------|------|
| MAPS | 269 | 偽造 | — | 完整 | ✓ |
| MAESTRO | 1282 | ✓ | — | — | — |
| piano-midi | 324 | 偽造 | — | — | — |
| **ASAP** | **1068** | **✓** | **✓** | **✓** | **✓** |

ASAP 的獨特優勢：**同時擁有**真實演奏 MIDI、數位樂譜、和拍級對齊標註。

## 速度變化分析

各作曲家的 BPM 變化標準差 σ(ΔBPM)：
- 最穩定：Bach（σ ≈ 5）
- 最不穩定：Chopin（σ ≈ 15-20）、Liszt（σ ≈ 18）
- ASAP 比 Ballroom 和 SMC 等數據集有**更大的速度變化**

## 設計用途

1. **完整音訊到樂譜 AMT**（Automatic Music Transcription）
2. **節拍結構任務**：拍追蹤、速度估計、節拍對齊、節奏量化

## 與本專案的關聯

| ASAP 特性 | 指法標註軟體啟示 |
|----------|----------|
| 222 首 MusicXML 樂譜 | 可作為指法標註的測試樂譜庫 |
| Score2Performance 對齊 | 可驗證指法在真實演奏中的適用性 |
| 15 位作曲家涵蓋各時期 | 涵蓋不同風格的指法需求 |
| Chopin 最多（290 場） | 與 PIG Dataset 的 Chopin 子集互補 |
| 拍/強拍/調號標註 | 可用於 V6 DP 的樂句感知分段 |

## 相關頁面

- [[src_computational_fingering]] — PIG Dataset（指法數據集）
- [[src_voice_separation]] — McLeod（ASAP 共同作者之一）
- [[concept_piano_fingering_principles]] — 五大共識原則
