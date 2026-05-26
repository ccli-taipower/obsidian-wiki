# Concept: 古典時期樂句結構 — Period 與 Sentence

> 來源：通用音樂理論知識 + Caplin《Classical Form》(1998)、Schoenberg《Fundamentals of Musical Composition》(1967, posth.) 為標準參考
> 涵蓋 PIG：Mozart 20 + Beethoven 21 + Haydn 0 + Schubert 5 = **46 曲 (31%)**
> 狀態：種子頁，第一版 2026-05-26
> 驗證樣本：PIG 011 Mozart K283 1st mov、PIG 061 Beethoven Für Elise

## 1. 為什麼這頁對指法系統重要

古典時期 (約 1750-1820) 的樂句結構**高度規律化**，這既是好消息也是壞消息：

- ✅ 好：樂句邊界訊號**清楚且密集** — cadence、period 對稱、sentence 重複結構都是可機械偵測的
- ⚠ 注意：「規律 = 死板」是迷思 — 古典樂句有 expansion / elision / hybrid 等變形，純 4-bar 周期 fallback 抓不到

當前 `_detect_phrase_starts` Pass 3 的「4 / 8 bar 週期」對古典時期**碰巧大致 OK**（因為古典本來就以 4-bar 為單位），但會漏：
- Sentence 結構的 2+2+4（最後的 cadential 4 bar 是一個完整樂句單位）
- Phrase elision（一句結束 = 下一句開始，重疊一拍 / 一小節）
- 期待外的 phrase expansion（標準 4 bar 被延長為 5、6、7 bar）

## 2. 兩大核心結構

### 2.1 Period (樂段)

典型 8 bar 結構，分兩半對稱：

```
| antecedent (前句, 4 bar) | consequent (後句, 4 bar) |
| basic idea + contrasting | basic idea + cadential   |
| → 半終止 HC              | → 完全終止 PAC           |
```

**判定特徵**：
- 兩半長度相等（多為 4+4，可擴張為 8+8、壓縮為 2+2）
- 前句以**弱**終止收（HC, IAC, DC），後句以**強**終止收（PAC）
- 兩半開頭的旋律材料**相同或相似**（"parallel period"）
- 變體：對比樂段 (contrasting period) — 兩半旋律材料不同，但仍保留弱-強終止對稱

**樂句邊界**：
- 主要邊界：consequent 結尾的 PAC (`idx = end of consequent`)
- 次要邊界：antecedent 結尾的 HC (`idx = end of antecedent` ≈ period 中點)
- DP 應視這兩處為樂句重置點，HC 邊界 weight 略低於 PAC

### 2.2 Sentence (樂句)

典型 8 bar 結構，分**前 4 後 4** 但內部邏輯不同：

```
| presentation (呈示, 4 bar)       | continuation (推進, 4 bar)        |
| basic idea (2) + repetition (2)  | fragmentation (2) + cadence (2)   |
| 同樣 idea 出現兩次              | idea 拆碎 + 收尾終止              |
```

**判定特徵**：
- 前 4 bar 內部是 2+2 重複結構（同 idea 兩次，第二次常移位 / 變化）
- 後 4 bar 內部是「fragmentation + cadential」— motivic 碎片以更短時值流動，最後 2 bar 為終止式
- 整段以 PAC 收尾

**樂句邊界**：
- 主要邊界：sentence 結尾 PAC
- **重要次邊界**：presentation/continuation 交界（bar 5）— 此處 texture 與節奏密度通常變化，DP 應視為次級樂句邊界
- **不**應在 bar 3 (basic idea repetition 起點) 切樂句 — 那是同一個 idea 的重述，不是新樂句

### 2.3 Hybrid 與變形

Caplin 列出多種混合形式 (hybrid theme types)，常見：
- antecedent + continuation (前句正常，後半改為 sentence-style continuation)
- compound basic idea + continuation
- compound basic idea + consequent

對指法系統的實務意涵：**不要硬塞 period 或 sentence 模板** — 偵測 cadence 與 4-bar 對稱是訊號，但允許不符合的長度。

## 3. 終止式（Cadence）四類

樂句邊界的最強訊號。

| 類型 | 縮寫 | 和聲進行 | 強度 | 樂句邊界含義 |
|---|---|---|---|---|
| **完全終止** Perfect Authentic | PAC | V-I (均根位 + soprano 在 tonic) | ⭐⭐⭐ | **強樂句結束**，常為 period / sentence / 段落終點 |
| **不完全終止** Imperfect Authentic | IAC | V-I (任一不在根位 或 soprano 非 tonic) | ⭐⭐ | 中等樂句結束，常為 antecedent 收 |
| **半終止** Half Cadence | HC | 任何進行 → V | ⭐⭐ | **樂句中點**，antecedent 結尾的典型 |
| **欺騙終止** Deceptive | DC | V → vi (替代 I) | ⭐ | 「延後」樂句結束，常促成 phrase expansion |

### Cadence 偵測對指法的實務規則

- **PAC 後**：phrase reset 強訊號，DP `INTER_PHRASE_SCALE` 完全切斷耦合（已是現狀）
- **HC 後**：phrase reset 中訊號，可保留 `PHRASE_SEAM_TC_SCALE` 較高（如 0.7-1.0），讓 antecedent → consequent 的手位有些連續性
- **DC 後**：**不應**視為樂句邊界 — 預期的 PAC 被延後，真正的樂句邊界在後面的真正 PAC
- 終止式偵測本身是 `concept_cadence_detection` 的範圍（待寫）

## 4. 古典時期樂句邊界偵測啟發式（草案）

按優先序：

| 訊號 | 操作型定義 | 信心度 |
|---|---|---|
| PAC 偵測（V-I 根位 + soprano 落 1） | 和聲分析 → V 和弦後接 I 和弦 | ⭐⭐⭐ |
| HC 偵測 | V 和弦持續 ≥ 1 小節，或 V 後接休止 | ⭐⭐ |
| 4-bar 對稱（Period 訊號） | 第 4 + 第 8 bar 都落在強拍 cadence-like 位置 | ⭐⭐ |
| 2+2 重複（Sentence presentation） | bar 1-2 motif 在 bar 3-4 移位重複 → bar 5 為樂句**次**邊界 | ⭐⭐ |
| 強拍進入（downbeat entry） | 樂句多在小節 1 拍起 | ⭐ |

## 5. PIG 驗證樣本與預期收穫

### 011 Mozart K283 1st mov (G major Sonata)
- 經典 sonata-allegro 教科書範例
- 主題：8 bar parallel period (bar 1-4 antecedent → HC, bar 5-8 consequent → PAC)
- 次主題：sentence structure (常見的 2+2+4)
- **預期收穫**：driven detection 應在 bar 4 (HC) + bar 8 (PAC) 立樂句邊界；現有 Pass 3 應該也會在 bar 5 / bar 9 立邊界（碰巧對齊）— 但 sentence 主題的「不要在 bar 3 切」需要新規則

### 034 Beethoven Op.13 Pathétique 1st mov
- Grave 引子 (4 bar) 然後 Allegro 主題 (period)
- **預期收穫**：Grave → Allegro 的 tempo / texture 切換是強樂句訊號（現有偵測器看不到）

### 061 Beethoven Für Elise
- A-B-A-C-A rondo, A 段是 sentence (a-a-b-c, 8 bar 共四個 2-bar 子單位)
- **預期收穫**：A 段內部 2+2+4 sentence 偵測；B/C 段切換是 strong phrase boundary

## 6. 與其他 wiki 頁面的關係

- 與 [[concept_fugue]] 對比：fugue 樂句長度跟主題長度走、不規律；古典樂句**規律對稱**。同一隻手不同曲子要切換 detection mode
- 與 [[concept_counterpoint]] 對比：古典時期是 homophonic（旋律 + 伴奏）為主，多聲部獨立性低；可預設「LH 樂句邊界 = RH 樂句邊界」(對位作品則否)
- 預備頁面：
  - [[concept_cadence_detection]] (TODO) — PAC/IAC/HC/DC 演算法
  - [[concept_phrase_elision]] (TODO) — 一句結束 = 下一句開始的處理
  - [[composer_mozart_phrasing]] (TODO)
  - [[composer_beethoven_phrasing]] (TODO — P2 待寫)

## 7. 與現有 DP 的整合方案（草案）

```
新 _detect_phrase_starts 子模組：classical_period_detector(groups)

1. 嘗試偵測終止式（cadence_detector）：
   - 用 music21 chord analysis 找 V → I (PAC/IAC) 與 → V (HC) 進行
   - 對每個偵測點記錄類型 + 信心度

2. 若整段是 homophonic 8-bar 規律：
   - bar 4 末 HC + bar 8 末 PAC → period 偵測 → 立兩個樂句邊界 (PAC 為主、HC 為次)

3. 若 bar 1-2 motif 在 bar 3-4 重複：
   - sentence 偵測 → bar 5 立次邊界，bar 8 末為主邊界

4. 若 cadence 不確定但 4-bar 規律明顯：
   - 退回現有 Pass 3 fallback (但只在古典時期啟用)

5. 適用條件：
   - 作曲家 ∈ {Mozart, Haydn, early Beethoven, early Schubert, Hummel}
   - 或 tempo marking ∈ {Allegro, Andante, Menuetto} 等古典慣用
   - 或檢測到 Alberti bass / homophonic texture
```

**實作風險**：cadence 偵測本身是難題，music21 的 RomanNumeralFromChord 不總是準。Phase 1 先做「4-bar 對稱 + 2-bar 重複偵測」(純結構訊號)，cadence 偵測作為 Phase 2 升級。

## 變更日誌
- 2026-05-26: 創立。第一批古典時期 phrase 概念。所有 TODO 連結為占位。
