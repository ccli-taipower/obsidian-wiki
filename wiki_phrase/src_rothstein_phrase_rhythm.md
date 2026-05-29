# Source: William Rothstein《Phrase Rhythm in Tonal Music》

> Schirmer Books (Macmillan), 1989, English
> ISBN: 978-0028721910
> Ingested: 2026-05-28 (⚠ training-data summary; book not directly ingested)

## 一句話總結

Rothstein 把調性音樂的「樂句 (phrase)」與「節拍 / hypermeter」放在同一個分析平面，提出「**phrase rhythm = 樂句結構與超小節 (hypermeter) 互動的節奏模式**」這個核心命題。書中以 Mozart、Beethoven、Chopin、Brahms 為主要材料，系統化討論 **phrase expansion / contraction / elision / hypermetric reinterpretation**，並承襲 Schenker 與 Lerdahl-Jackendoff (GTTM) 的階層觀。對本專案而言，**Rothstein 是「為什麼 4-小節 fallback 有時對、有時錯」的權威解釋**，也是 `concept_phrase_elision` 的理論源頭。

## 重點概念清單（供其他 concept 頁引用）

### Phrase（樂句）— Rothstein 的工作定義

- 「**一段朝向終止式 (cadence) 運動的音樂單位**」⚠ training-data inferred — verify exact wording
- 強調 **goal-directed motion**：phrase 必須有「方向」與「目的地」，而目的地通常是 cadence
- 與 motif / sub-phrase 區分：後者更短、未必有 cadence
- **➜ 對應本專案 `_detect_cadence_boundaries`** 把 cadence 當作 phrase-end 強錨點的設計

### Hypermeter（超小節）

跨小節層級的強弱結構。典型樣式：

| Bar | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Hyper-beat | **strong** | weak | mod-strong | weak |

- 4-bar hypermeasure 是 Common Practice 時期最常見的「default」
- 也存在 2-bar、3-bar、6-bar、8-bar hypermeter，視作品而定
- 承接 Cone (1968) 與 Lerdahl-Jackendoff (1983) 的 hypermeter 概念，加上更精細的「**衝突 / 對齊**」討論
- **➜ 直接對應本專案 Pass 2 的 2/4/6/8 小節週期 fallback**

### Phrase Rhythm = Phrase × Hypermeter 的互動

兩個維度可以「對齊」或「錯開」：

- **對齊 (congruent)**：phrase 邊界落在 hyper-strong bar；phrase 長度 = hypermeasure 長度
- **錯開 (incongruent)**：phrase 邊界出現在 hyper-weak bar，或 phrase 跨多個 hypermeasure
- Rothstein 把後者稱為 **metric / hypermetric dissonance**（imbroglio 是一種極端形式）

### Phrase Model vs. Realization

- 每個樂句都有底層的「**model (model phrase)**」— 通常規整、4-bar、cadence 落在第 4 小節
- 作曲家會用各種技巧讓「surface (實際譜面)」偏離 model
- 分析的工作：找出 model，並命名 surface 用了哪種偏離技巧

### Phrase Expansion（樂句擴展）— 五種主要技巧 ⚠ list inferred

1. **重複 (repetition)**：把樂句的某一小段重複，把 4-bar 拉長成 5/6/7-bar
2. **延伸 (extension)**：把 cadence 後或 cadence 前加裝飾段
3. **括號 / 插入 (parenthesis)**：在樂句中段插入一段「離題」材料
4. **欺騙終止 (deceptive cadence) + 再嘗試**：V→vi 後再次衝向 cadence
5. **Cadential elaboration**：把 cadential progression (I⁶/₄–V⁷–I) 本身擴大
- **➜ 解釋為什麼 Chopin / Schubert 樂句常 5/6/7/9 bar — 不是「奇怪」而是 4-bar model 被 expand**

### Phrase Contraction / Overlap / Elision

- **Contraction**：把 4-bar 壓縮成 3-bar（少見）
- **Overlap**：兩相鄰樂句共享 1-2 bar 重疊區
- **Elision (省略 / 合流)**：**前一句的最後一小節 = 後一句的第一小節**
  - 此小節同時是 cadence 解決 + 新樂句起始
  - 在 hypermeter 上表現為「該強拍兼任兩個角色」
- **➜ 對應本專案 `concept_phrase_elision` 的整個議題**

### Hypermetric Reinterpretation（超小節重解）

- 一個原本 hypermetrically 是「4 (weak)」的小節，被「**重新解釋**」為下一 hypermeasure 的「1 (strong)」
- 通常與 elision 同時發生
- Rothstein 在分析中常以「→ 1」記號標記重解點
- **➜ 對本專案有實際意義**：phrase elision 點的指法不該完全 reset 手位，因為該小節同時服務兩個樂句

### Imbroglio / Metric Dissonance

- 用以指「phrase 與 meter 嚴重不對齊」的段落
- 例：phrase 邊界落在小節中段（mid-bar phrase start）
- 或：3 拍子上的 phrase 顯出 2 拍 grouping (hemiola family)
- **➜ 解釋為什麼某些 Chopin / Schumann 段落 measure-aligned phrase detection 必然失敗**

### 與 Schenker / GTTM 的關係

| 來源 | Rothstein 取用什麼 |
|---|---|
| Schenker | 階層觀、background/middleground/foreground、prolongation |
| Lerdahl-Jackendoff (GTTM) | hypermeter 概念、grouping × metrical 分離分析 |
| Cone (1968 《Musical Form and Musical Performance》) | hypermetric downbeat |

Rothstein 的貢獻：把這些工具系統化用於 **phrase × meter 互動** 的具體分析。

## 歷史與作曲家

- 1989 出版，作者 William Rothstein 為紐約市立大學音樂理論家
- 主要分析對象：**Mozart、Beethoven、Chopin、Brahms** ⚠ specific pieces not verified
- 強調「**rhythm at the phrase level**」是 19 世紀作曲技巧進化的關鍵維度（相對 18 世紀的相對規整）
- 對 Chopin 的 nocturne 與 mazurka 樂句結構有專門章節 ⚠ chapter inferred
- 影響 1990s+ phrase-rhythm 分析學派；後續發展者：Temperley、Mirka、London (metric perception)
- 為 Caplin (1998)《Classical Form》提供互補視角（Caplin 著重 form function；Rothstein 著重 rhythm）

## 文章未涵蓋（要 P1 補的）

- ❌ 具體的演奏 / 指法建議（理論書，非演奏指南）
- ❌ 對位 / fugue 各聲部獨立 phrase rhythm（書著重主音音樂）
- ❌ 20 世紀後 / 非調性音樂（書範圍 = 調性音樂 Common Practice）
- ❌ 計算化實作（純分析語言）
- ❌ 演奏者如何用 phrase rhythm 知識指導觸鍵 / 呼吸 / 指法 — 本專案 synthesize 的工作

## ⚠ Training-data verification needed

以下 claims 訓練資料只給出概括理解，若要當作硬論據引用請翻書核對：

1. **Phrase 定義的精確 wording**：「a unit aiming at a cadence」是否確實為 Rothstein 文字
2. **Phrase expansion 的五種技巧分類** — 訓練資料給出的清單可能與書中順序 / 命名不完全對應
3. **是否有專門 Chopin chapter** — 印象中有，但章節編號 / 標題未確認
4. **「Imbroglio」一詞是否為 Rothstein 直接使用** — 此詞在 Krebs (1999) 《Fantasy Pieces》中更明確；Rothstein 可能用其他術語表達相同概念
5. **Hypermetric reinterpretation 的記號 (→ 1)** — 訓練資料推斷；實際書中記號形式待確認
6. **書中具體分析的曲目** — 不要在沒查證下引用 Op.X No.Y 的具體分析
7. **書的章節結構** — 訓練資料只記得主題群，章節編號未知
8. **Rothstein 對「phrase 必須有 cadence」的嚴格程度** — 是否容許「open phrase」(無 cadence) 待查

## 對指法系統的啟示（synthesized — 不是書中原文）

1. **本專案 Pass 2 的 4-bar 預設 = Rothstein 的「default 4-bar hypermeter」**：
   - `_detect_phrase_starts` Pass 2 對齊 2/4/6/8 小節邊界，根源即 Common Practice 時期的 4-bar hypermeter 統計常態
   - **應在 `_detect_phrase_starts` docstring 把 Rothstein 列為 lineage 之一**（與 GTTM 並列）

2. **Phrase expansion 解釋「為什麼 4-bar 不總是對」**：
   - Chopin nocturne 樂句常 5/6/7/9 bar — 不是「壞數據」，而是 model phrase 被 expand
   - **➜ 對 `concept_chopin_lyrical_phrase`「禁用 4-bar fallback」提供理論支撐**
   - **➜ 對 PIG val Chopin 曲目評估時，4-bar fallback 應被 cadence detection 取代**

3. **Phrase elision 是公認難題，不是本專案獨有**：
   - Rothstein 全書最大篇幅之一就是 elision / overlap
   - **➜ `concept_phrase_elision` 應引述 Rothstein 的「hypermetric reinterpretation」框架**
   - **➜ 實作建議**：elision 點的手位 reset 應「半 reset」(soft reset)，因為該小節同時收尾 + 起頭

4. **Cadence-anchored phrase boundary 有理論依據**：
   - Rothstein「phrase = aim at cadence」直接支持本專案 `_detect_cadence_boundaries` 把 cadence 當主錨點
   - 4-bar fallback 只是 cadence 失敗時的 backup — 這個優先序與 Rothstein 一致
   - **➜ 在 `concept_cadence_detection` 標註此 lineage**

5. **Imbroglio / metric dissonance 解釋「為什麼有些段落根本不該 phrase-detect」**：
   - 高度 rubato / 自由節奏段落，phrase × meter 嚴重錯開
   - 強行 phrase detection 可能害多於益
   - **➜ 建議未來新增 flag `USE_PHRASE_DETECTION = False` 對特定段落 opt-out**
   - **➜ Chopin op9 no2 nocturne 是候選 case**

6. **Hypermetric reinterpretation 對指法的具體意義**：
   - 在 elision 小節，該音同時是「前句 cadence 收音」+「後句起音」
   - 純粹用「樂句結束 → 手位完全 reset」會錯失 cadence 的接力
   - **➜ 對 `PHRASE_SEAM_TC_SCALE` 的 0.5 倍率正好對應這個「半保留」的精神**（前句末和弦的 f2m 帶入下句首和弦 cost）— 可在 docstring 標註此 Rothstein 對應

7. **Phrase Model vs Realization 給未來「樂句長度推斷」更穩固框架**：
   - 目前 Pass 2 推斷「最常見樂句長度」屬統計手法
   - 若採 Rothstein 視角：先假設 4-bar model → 偵測 expansion 技巧 → 推回 surface 長度
   - 這是 future work，但比純頻率法更可解釋

詳見 [concept_classical_period_sentence](concept_classical_period_sentence.md)、[concept_phrase_elision](concept_phrase_elision.md)、[concept_chopin_lyrical_phrase](concept_chopin_lyrical_phrase.md)、[concept_cadence_detection](concept_cadence_detection.md) 與 [src_lerdahl_jackendoff_gttm](src_lerdahl_jackendoff_gttm.md)、[src_caplin_classical_form](src_caplin_classical_form.md)。
