# Composer: Beethoven 樂句 — 對古典模板的擴張與壓縮

> 來源：通用音樂理論 + Caplin《Classical Form》Part III、Rosen《The Classical Style》、Rothstein《Phrase Rhythm》Beethoven 章節
> 涵蓋 PIG：Beethoven 21 曲 (14%)
> 狀態：種子頁，第一版 2026-05-26
> 驗證樣本：PIG 061 Für Elise、PIG 034 Pathétique 1st mov

## 1. 為什麼 Beethoven 單獨開一頁

Beethoven 跨在古典 (Mozart 學徒期) 與浪漫 (晚期奏鳴曲 / 弦樂四重奏) 之間，**樂句策略獨特** — 故意「打破」古典規律性以製造戲劇張力：

- 早期 (Op.1-30 左右)：繼承 Mozart/Haydn 的 period / sentence，但偶有擴張
- 中期 (Op.31-90 含 Eroica, Appassionata, Waldstein)：**phrase expansion / compression** 成為核心手段
- 晚期 (Op.101 後)：自由 fantasia 風格，樂句邊界依「論述邏輯」而非結構模板

這直接影響指法系統 — 不能用統一規則跑所有 Beethoven 曲；應按時期 + 作品個別判斷。

## 2. Beethoven 對古典樂句的四種變形手法

### 2.1 Phrase Expansion (樂句擴張)

預期 4 bar 的樂句被延長為 5、6、7、8 bar，常用手法：
- **Sequence 重複**：把樂句中段的 motive 用 sequence 重複一次，多出 2 bar
- **Deceptive cadence 延後 PAC**：預期的 PAC 被 DC (V-vi) 替代，後面再加 cadential extension 才到真正 PAC
- **Pedal-point insertion**：在 dominant pedal 上拖 2-4 bar 增加張力後再解決

**偵測訊號**：偵測到「預期 PAC 位置卻是 DC 或長 pedal」→ 樂句真實邊界推後

### 2.2 Phrase Compression (樂句壓縮)

兩個樂句透過 elision 合併，總長度 < 預期 4+4：
- 第 4 bar 末 PAC 同時是第 5 bar 開頭 → 8 bar 期待縮短為 7 bar
- 在 sentence 結構中，continuation 的 fragmentation 加速碎裂，cadence 提早出現

**偵測訊號**：cadence 落點 + 強拍 motif 同時 → 同一拍是邊界

### 2.3 Hemiola 與跨樂句節拍

把 3/4 拍譜面組成 2-bar 為 1 個 6 拍的「假 6/4」單位（hemiola），或反之。樂句邊界與小節線錯位。

**偵測訊號**：節奏重音模式與譜面節拍號不符 — Audiveris 不直接抽，需從 articulation marking + rhythmic grouping 推

### 2.4 Tempo / Texture 切換 (跨段落樂句)

Beethoven 常在大型作品內穿插 tempo / character 切換（Grave-Allegro, Adagio-Allegro），切換點 = strong phrase boundary。

**偵測訊號**：tempo marking 變化（Audiveris 可能抽得到 `<sound tempo>` 或 `<words>`），dynamic 突變（`fp`, `sfz` 後接 `p` 或 `pp`），texture 突變

## 3. 按時期細分

### 3.1 早期 (PIG 中：Op.10, Op.13 早期等)
- 樂句結構 **可預測**，大致用 [[concept_classical_period_sentence]] 規則
- 仍以 8-bar period / sentence 為主
- Cadence 偵測高信心度

### 3.2 中期 (PIG 中：Op.27, Op.31, Op.53, Op.57, WoO 等)
- **頻繁 phrase expansion** — 4-bar fallback 會錯
- 著名範例：Op.31 No.2 "Tempest" 1st mov 主題 — 表面 4+4 對稱，內部含多次 expansion
- **DC + extension** 模式常見
- 對 PIG 影響最大的時期（PIG 大部分 Beethoven 曲落在此處）

### 3.3 晚期 (PIG 中：Op.106 Hammerklavier, Op.110, Op.111 等如有)
- 自由 fantasia 風格，樂句邊界依**和聲邏輯**與**主題發展**
- Fugue / fugato 段落混入，需用 [[concept_fugue]] 規則
- **若 PIG 包含晚期作品，預期偵測難度最高**

### 3.4 對 PIG 21 首的初步分類

從 label 可初步判斷（精確按時期分需 BWV/Op. 號查證）：
- 061 Für Elise (WoO 59, 1810, 中期)
- 062 Minuet in G (WoO 10-2, 1795 前後, 早期)
- 034 Pathétique Op.13 (1798, 早期/中期過渡)
- 其他 18 曲待按 Op. 號分（後續工作）

## 4. Beethoven 特有的樂句邊界訊號

| 訊號 | 描述 | 信心度 |
|---|---|---|
| **Sforzando (sfz) + 後接 pp** | 戲劇張力後的釋放，常為樂句結尾 + 新樂句起點 | ⭐⭐⭐ |
| **fortepiano (fp) + 持續** | 突強後立即弱，常為樂句**內部**強調，**不是**樂句邊界 | (反訊號) |
| **Tempo 切換** | Adagio→Allegro, Grave→Vivace 等 | ⭐⭐⭐ |
| **休止符延長 (rest ≥ 1 bar)** | 古典作曲家少見、Beethoven 常用作戲劇停頓 | ⭐⭐⭐ |
| **Fermata (延長記號)** | 樂句明確結束點 | ⭐⭐⭐ |
| **Cadential extension** | PAC 後再加 2-4 bar 強化主和弦，整段為一個大樂句 | ⭐⭐ |
| **Hemiola** | 跨小節重音模式 | ⭐ (需 articulation 偵測) |

## 5. 與 Mozart / 早期 Beethoven 差異

| 特徵 | Mozart / 早期 Beethoven | 中晚期 Beethoven |
|---|---|---|
| 樂句長度 | 4 / 8 規律 | **不規律** (4-11+) |
| Cadence 清晰度 | ⭐⭐⭐ V-I 根位 | ⭐⭐ 常被擴張 / 延後 |
| 樂句邊界落點 | 規律強拍 | **可在弱拍** (跨小節線) |
| Phrase elision | 偶爾 | **頻繁** |
| 結構模板適用性 | period / sentence 直接套用 | **彈性**，需 case-by-case |

## 6. PIG 驗證樣本

### 061 Für Elise (WoO 59, A minor)
- A-B-A-C-A rondo 結構
- A 段：8-bar sentence (a-a-b-a' 各 2 bar)
- B 段：8 bar period-like，C 段：戲劇對比 + 半音進行
- **預期收穫**：rondo 段落切換是 strong boundary；A 段內部 sentence 結構應被偵測（避免在 bar 3 切）

### 034 Pathétique Op.13 1st mov
- Grave 引子 (10 bar) + Allegro di molto e con brio (主題開始)
- Grave 引子內部多個 fp + 戲劇休止
- **預期收穫**：Grave → Allegro 切換**必須**是 strong phrase boundary（tempo 訊號）；Grave 內部多重戲劇停頓也是邊界

### 081 / 082 / 083 (其他中期 sonata mov，待按 Op. 確認)
- 預期：sonata-allegro 結構下，主題 / 副題 / development / recap 切換為大段落邊界

## 7. 與其他 wiki 頁面的關係

- 主要依賴 [[concept_classical_period_sentence]] 作為起點，加 Beethoven-specific 擴張變形
- 中晚期需參考 [[concept_chopin_lyrical_phrase]] 部分概念（不規律長度、phrase elision）
- 待寫：
  - [[concept_cadence_detection]] (PAC/IAC/HC/DC 偵測演算法)
  - [[concept_phrase_expansion]] (sequence / DC extension 偵測)
  - [[concept_articulation_phrase_signal]] (sfz/fp/fermata 對樂句的訊號意義)

## 8. 演算法整合建議

```
beethoven_phrase_detector(groups, period_estimate):

1. 若曲目 < Op.30：用 classical_period_sentence_detector 為主

2. 若曲目 ∈ Op.30-Op.100 (中期)：
   a. 偵測 cadence (PAC / DC / extension)
   b. 偵測 tempo / dynamic 戲劇切換
   c. 不啟用 4-bar fallback (Pass 3 disabled for Beethoven mid-late)
   d. 偵測長 rest / fermata 作為強樂句邊界

3. 若曲目 > Op.100 (晚期)：
   a. 大量倚賴 cadence + 主題重入聲偵測
   b. 若含 fugato 段落，呼叫 [[concept_fugue]] 規則

4. PIG 大致按 label 中的 Op. 號估時期；
   若無 Op. 號則保守用早期規則
```

## 變更日誌
- 2026-05-26: 創立。Beethoven 特化頁。早期 / 中期 / 晚期區分為主軸。
