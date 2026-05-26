# Analysis: Mozart Piano Sonata K283 G major, 1st mov

> PIG: 011 (4 annotators: ES, HI, HK, YI / YS, EF)
> 來源：通用 sonata-allegro 分析 + Caplin《Classical Form》sonata 章節 + Rosen《The Classical Style》Mozart sonatas
> 狀態：第二個 per-piece analysis (after Bach Inv 4)，2026-05-26
> 引用方：[[composer_mozart_phrasing]] §7、[[concept_classical_period_sentence]] §5、[[concept_cadence_detection]] §6

## 1. 為什麼挑這首作為 wiki 第二個 analysis

Mozart K283 1st mov (G major, Allegro) 是古典 sonata-allegro 形式的**教科書範例**。Caplin《Classical Form》多次引用本曲做 period / sentence / cadence 示範。對 wiki 的價值：

- 驗證 [[concept_classical_period_sentence]] (period 4+4, sentence 2+2+4) 是否如預期應用
- 驗證 [[concept_cadence_detection]] (PAC/IAC/HC/DC) 對純古典作品的命中率
- 與 [[analysis_bach_inv_4_d_minor]] 對比：對位 vs 主調樂句邏輯
- 為未來 Mozart 系列分析建立 baseline

## 2. 曲目基本資訊

- **K283** (1775, Mozart 19 歲)
- **G major**, 3/4 拍, **Allegro**
- 第一樂章長度：~120 小節（依版本）
- Sonata-allegro 形式：Exposition / Development / Recapitulation

## 3. 預期曲式結構

### 3.1 Exposition (bb. 1-53)

| 區塊 | 小節範圍 | 預期 phrase 邊界 |
|---|---|---|
| 第一主題 (G major) | bb. 1-16 | **bar 4** HC, **bar 8** PAC (period 4+4); 接 codetta to bar 16 |
| Transition / bridge | bb. 17-22 | modulation 到 D major (V) |
| 第二主題 (D major) | bb. 23-43 | sentence-like; **bar 31** HC, **bar 39** PAC |
| Closing theme (codetta) | bb. 43-53 | cadential extension, PAC in D |

### 3.2 Development (bb. 54-71)

| 區塊 | 預期 phrase 邊界 |
|---|---|
| 主題碎片變奏 (e minor, b minor 等) | 段落切換點為主邊界 |
| Re-transition (返回 G major) | strong reset |

### 3.3 Recapitulation (bb. 72-end)

| 區塊 | 預期 phrase 邊界 |
|---|---|
| 第一主題 (G major) | 同 exposition |
| Transition (modified, 留在 G major) | adjusted modulation |
| 第二主題 **in G major** (not D!) | classical sonata convention |
| Closing in G | final PAC, coda |

## 4. 五類偵測器預期表現

| 偵測器 | 預期 | 信心度 |
|---|---|---|
| **Pass 3 (4-bar fallback)** | 與 period 4+4 自然對齊 | ⭐⭐⭐ |
| **Pass 6 (PAC cadence)** | **預期 fire 多次**（bar 8, 16, 39, 53, 等 sonata key 終止點） | ⭐⭐⭐ |
| **Pass 4 (figural)** | 中等 — transition / 副題的 scale runs 會觸發 | ⭐⭐ |
| **Pass 5 (subject imitation)** | 較少 — Mozart 主題不像 fugue 嚴格重述 | ⭐ |
| **thumb-reservation** | 對 LH alberti bass 起手或 RH scale 起手可能 fire | ⭐⭐ |

## 5. PIG 6 annotators 觀察

PIG K283 有 6 個 annotators（ES, HI, HK, YI / YS, EF），多於一般曲目（Bach Inv 多為 4 個）。代表這首是 PIG 的「重要 benchmark」。多 annotators 意味著：

- Annotator 間有 disagreement → 衡量 inter-annotator variance
- DP 與 majority vote 對齊困難度高
- Cost framework 用 `min(cost_pig_min, cost_pp)` 取最強對手會更嚴格

## 6. Cadence 偵測驗證 (Phase 1 PAC) 期望

執行 `_detect_cadence_boundaries(groups)` 對 PIG 011 mxl 預期偵測：

| 預期 PAC | 位置 | 為何 |
|---|---|---|
| Exposition 第一主題尾 | bar 8 V-I in G | 4+4 period 收尾 |
| Exposition 副題尾 | bar 39 V-I in D | sonata 第二主題收尾 |
| Exposition 結束 | bar 53 V-I in D | closing theme PAC |
| Recap 第一主題尾 | bar 79 (推測) V-I in G | recap 對應 bar 8 |
| Recap 結束 / coda PAC | 樂章尾 V-I in G | 全曲收尾 |

實測前 prediction：**3-5 個 PAC 偵測到**。若 music21 RomanNumeralFromChord 對 Mozart 表現良好（chordify 主調 texture 比 Bach 對位乾淨），預期信心度 high。

## 7. 與其他 wiki 頁面的關係

- 父頁 [[composer_mozart_phrasing]]：通則
- 父頁 [[concept_classical_period_sentence]]：純正範本
- 工具頁 [[concept_cadence_detection]]：對 Mozart 預期 fire 良好
- 兄弟頁 [[analysis_bach_inv_4_d_minor]]：對位 vs 主調對比

