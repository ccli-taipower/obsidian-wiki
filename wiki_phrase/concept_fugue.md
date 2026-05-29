# Concept: Fugue 賦格 — 結構與樂句邊界

> 來源：[src_epochtimes_fugue_zhou_2005](src_epochtimes_fugue_zhou_2005.md) (周怡秀, 大紀元 2005) + 通用音樂理論擴增
> 狀態：種子頁，第一版 2026-05-26

## 1. 一句話定義

**Fugue**（中譯「賦格」或「復格」）是一種以**模仿 (imitation)** 與 **對位 (counterpoint)** 為核心特徵的多聲部音樂曲式。詞源 "fugue" 來自拉丁 fuga = 逃逸，意指聲部之間追逐、模仿。

## 2. 為什麼這頁對指法系統重要

指法系統 (`assign_fingering_v6`) 要先把樂句切對才能算出對的指法（見 [../wiki_piano/](../wiki_piano/.md) 的生物力學原則）。Fugue / 對位作品的樂句結構**不適合**用泛用啟發式（音高跳幅、休止符長度）切分，因為：

- 每條聲部 (voice) 有獨立樂句線
- 樂句邊界常出現在**主題重入聲**的位置，而不是音高跳幅大的位置
- Bach Inventions（2 聲部、與 fugue 同源）是當前 repertoire 的核心，這套規則直接適用

## 3. Fugue 的結構元素

### 3.1 主題系列

| 元素 | 中譯 | 角色 | 樂句意義 |
|---|---|---|---|
| **Subject** | 主題 | 開頭呈現的單一旋律，定義全曲動機 | **每一次重入聲 = 樂句起點** |
| **Answer** | 答題 | 主題在另一聲部以 5 度（real / tonal）或 4 度移動的模仿 | 同上，樂句起點 |
| **Countersubject** | 對主題 | 一聲部唱主題時，另一聲部唱的對位旋律；通常會重複使用 | 與主題同一樂句，不是新起點 |

### 3.2 段落結構

```
Exposition (呈示部)
  ├─ Voice 1: Subject  (tonic)
  ├─ Voice 2: Answer   (dominant) + V1: Countersubject
  ├─ Voice 3: Subject  (tonic) + V1/V2 continue
  └─ Voice 4: Answer   (dominant) + ...
       ↓
Episode (插曲 / divertissement)
  自由對位，常用主題的 motivic fragment 做 sequence
       ↓
Middle entries / Development (開展部)
  主題在關係調 (relative major, dominant minor, etc.) 重新呈現
       ↓
Final entries + Coda (結束部)
  回到主調，常用 stretto / pedal point 強化結尾
```

### 3.3 模仿的四種形式（文章列舉）

1. **正向 (rectus)**：原樣重現
2. **逆向 (retrograde)**：音符次序反向
3. **正向倒影 (inversion)**：音程方向上下顛倒（上行 → 下行）
4. **逆向倒影 (retrograde inversion)**：同時逆向 + 倒影

文章指出後兩種一般聽眾不易辨認。對指法系統而言：**任何模仿形式都標誌新樂句起點**，識別方法（音名序列、音程序列、TI signature）見 [concept_motif_identity](concept_motif_identity.md) (TODO)。

### 3.4 進階手法

- **Stretto**：主題在尚未結束時，另一聲部已開始重述 → 樂句邊界**極密集**，甚至跨聲部同時起句
- **Augmentation / Diminution**：主題以更長 / 更短時值重現 → 樂句長度倍增 / 倍減
- **Pedal point (持續音)**：常出現於 final entries 之前，是樂句**收束**訊號

## 4. 樂句邊界判斷規則（synthesized）

依重要性排序：

| 訊號 | 操作型定義 | 信心度 |
|---|---|---|
| **主題重入聲** | 偵測主題 motif 在任一聲部再次出現（pitch-class sequence / interval sequence 匹配） | ⭐⭐⭐ 高 |
| **Episode 開始** | exposition 結束後第一個非主題段落 | ⭐⭐ 中（需 cadence 偵測輔助） |
| **半 / 完全終止式 (cadence)** | V→I, V→i, IV→I etc.，常落在強拍 | ⭐⭐ 中 |
| **持續音終止** | bass 持續音 + 上方聲部解決 | ⭐⭐⭐ 高 |
| 音高跳幅 > 12 半音 | 現有 `PHRASE_BREAK_THRESHOLD` | ⭐ 低（易漏 figural 邊界） |
| 4 / 8 小節週期 | 現有 Pass 3 fallback | ⭐ 低（fugue 樂句長度不規律） |

## 5. Bach Inventions 特別說明

Bach 15 Inventions (BWV 772–786) **不是嚴格的 fugue**（只有 2 聲部，沒有完整 exposition），但繼承 fugue 的：

- 主題 + 模仿（RH 先呈現，LH 隨後在 8 度或 5 度模仿）
- 對位寫作（兩聲部獨立）
- 插曲與主題段落交替
- 結尾回主調

→ 本頁所有樂句規則對 Bach Inventions 適用。Inventions 因為只有 2 聲部，**每隻手對應一個聲部**，所以 per-hand `_detect_phrase_starts` 概念上完全正確；問題只在「沒看到主題重入」。

具體 mvt 分析見：
- [analysis_bach_inv_4_d_minor](analysis_bach_inv_4_d_minor.md) (TODO — mvt4 m50 case 的直接出處)
- [analysis_bach_inv_general_patterns](analysis_bach_inv_general_patterns.md) (TODO)

## 6. 與其他曲式的對照（P1 擴增）

| 曲式 | 樂句長度典型 | 邊界線索 |
|---|---|---|
| **Fugue / Invention** | 不規律，跟主題長度走（Bach Inv 多為 1-2 bar） | **主題重入** 為主 |
| **古典時期奏鳴曲** | 規律 4 / 8 bar antecedent-consequent | 半終止 / 完全終止式、和聲節奏 |
| **浪漫主義抒情曲** | 長線條，常 8-16 bar | melodic contour + dynamic 收束、rubato 呼吸點 |
| **二十世紀對位** (Bartók, Hindemith) | 不規律 | 對位密度變化、texture shift |

當前實作的 `_detect_phrase_starts` Pass 3 (4/8 bar 週期) 對 **古典奏鳴曲** 合理，但對 fugue 系統性錯誤。後續要建：
- [concept_motif_subject_detection](concept_motif_subject_detection.md) (TODO) — 主題識別演算法
- [concept_cadence_detection](concept_cadence_detection.md) (TODO) — 終止式偵測
- [analysis_fugue_phrasing_vs_classical_phrasing](analysis_fugue_phrasing_vs_classical_phrasing.md) (TODO)

## 7. 立即可動的演算法草案（草案，未實作）

```
input: per-hand groups (notes ordered)
output: list of phrase-start indices

1. 在曲首 N 拍（4-8 bar）抽取「候選 subject」：
   - RH 第一個非 pickup 的小節為起點
   - 取連續 K 個音 (K ∈ [4, 16]) 作為主題候選

2. 對每個候選 subject，用 transposition-invariant signature
   (intervals 序列) 在 LH 與 RH 後續位置做 substring match
   - 匹配閾值：>= 80% interval 一致
   - 允許 augmentation / diminution（時值縮放但音程一致）

3. 每個匹配位置 + 1 = 樂句起點候選

4. 與現有 hard breaks (rest / pitch-jump / cadence) 取聯集

5. 若曲長 ≥ 16 bar 且樂句起點密度過低 (< 1 per 8 bar)，
   啟動 4-bar 週期 fallback（現有 Pass 3 邏輯）
```

此演算法待驗證 — 先做 mvt4 case study ([analysis_bach_inv_4_d_minor](analysis_bach_inv_4_d_minor.md)) 看是否正確抓到 m50 boundary。

