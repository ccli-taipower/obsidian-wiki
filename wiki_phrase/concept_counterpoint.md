# Concept: Counterpoint 對位 — 多聲部樂句獨立性

> 來源：[[src_epochtimes_fugue_zhou_2005]] + 通用音樂理論擴增
> 狀態：種子頁，第一版 2026-05-26

## 1. 一句話定義

**Counterpoint** (對位法，源法文 contrepoint = punctus contra punctum = 「點對點」)：兩條以上獨立旋律 (voice / part) 同時進行的寫作技法。每條旋律保有自身的旋律邏輯與樂句結構，同時與其他聲部形成和聲與節奏互動。

## 2. 對指法系統的核心啟示

**每條聲部 / 每隻手有獨立的樂句結構，兩者不必同步。**

這直接解釋了 mvt4 m50 的偵測不對稱：
- LH 在 m50 偵測到樂句邊界（音高跳 +15 半音觸發 hard break）
- RH 在 m50 漏接（同樣 figural 邊界但只跳 -9 半音）

從對位理論看，這**不是**「LH 對 RH 錯」或反之 — 而是**兩條聲部各自有獨立樂句結構**，剛好在 m50 都到達樂句邊界，只是觸發機制（pitch jump magnitude）不對稱。

→ `_detect_phrase_starts` per-hand 跑是**對的**；要修的是內部觸發機制太依賴音高跳幅，看不到聲部各自的 figural 結構。

## 3. 對位的兩個基本性質（文章原引）

| 性質 | 描述 | 對指法 / 樂句的意義 |
|---|---|---|
| **抗衡 (independence)** | 各聲部保有獨立性 | 樂句邊界**不對齊**是常態，不是 bug |
| **互補 (complementarity)** | 各聲部避免擁擠、互相支持 | 一聲部樂句結尾常與另一聲部新樂句起點重疊；過渡期可能跨小節 |

## 4. 對位的歷史脈絡（脈絡參考）

| 時期 | 風格 | 代表 |
|---|---|---|
| 文藝復興 (1450-1600) | 嚴格對位、Palestrina style | Palestrina, Lassus |
| 巴洛克 (1600-1750) | 自由對位 + 和聲 fugue | Bach (peak), Handel, Couperin |
| 古典 (1750-1820) | 對位讓位於主調 (homophony), 對位作為發展手法 | Mozart Sym.41, Beethoven 晚期 fugues |
| 浪漫 (1820-1900) | 對位作為 texture / 學術致敬 | Brahms, Reger |
| 二十世紀 | 復興對位作為非調性主軸 | Bartók, Hindemith, Shostakovich preludes & fugues |

## 5. 對位類型（合成知識）

### 5.1 嚴格對位 (Strict / Species Counterpoint)
- Fux 1725《Gradus ad Parnassum》確立教學體系
- 第一類 (note against note) → 第五類 (florid)
- 對指法不太相關（學理練習而非實際曲目）

### 5.2 自由對位 (Free Counterpoint)
- Bach 風格主導
- 與和聲規則並行
- Fugue / Invention / Sinfonia 的實際寫法
- **對指法系統最相關**

### 5.3 模仿對位 (Imitative Counterpoint)
- 一聲部呈現旋律，另一聲部隨後重述
- 模仿可在 prime / 5th / 4th / 8va 等音程
- Fugue 是模仿對位的最高度組織化形式
- 詳見 [[concept_fugue]]

### 5.4 非模仿對位 (Non-imitative Counterpoint)
- 聲部間旋律不重複，但互相獨立
- 常見於 chorale prelude 上下聲部、homophonic 中的內聲部
- 樂句邊界依各聲部自身的旋律邏輯

## 6. 對位作品的樂句分析 workflow（建議流程）

```
1. 識別聲部數 (RH 譜表 + LH 譜表 ≠ 2 voices 必然；
   可能 RH 一手雙聲部、或共用譜表的聲部分離)
   → 暫時假設「RH = 1 voice, LH = 1 voice」(Bach Invention 適用)
   → 多聲部作品 (Bach 3-part Sinfonias) 需要 voice separation
     先決條件，詳見 wiki_piano/src_voice_separation.md

2. 對每條聲部獨立做樂句分析（per-voice phrase detection）
   - 主題 / motif 重入 → 樂句邊界
   - cadence → 樂句邊界
   - 音高 / register reset → 樂句邊界候選（非絕對）

3. 對齊檢查：兩聲部樂句邊界**不需要**對齊
   - 對齊是巧合，不是必然
   - 不要為了「整齊」強行對齊

4. 指法 DP 在每條聲部 / 每隻手獨立跑（現狀正確）
   - 各自的 W_PHRASE_ANCHOR / per-phrase budget 獨立
```

## 7. Voice separation 的隱藏問題

當前實作假設 **RH = 上聲部，LH = 下聲部** — Bach Inventions 大致成立，但有反例：

- **跨譜表聲部編碼**（stem direction 標示真實聲部）：見 [[../score-claude/memory/feedback_cross_staff_stem_direction.md]] 與 `SINGLE_PDF_HAND_REASSIGN` 機制
- **RH 雙聲部**：Bach Sinfonias (3 聲部) 常將 2 條聲部塞進 RH 譜表，stem 方向區分
- **LH 跨譜表伴奏**：浪漫派 octave / arpeggio bass

→ 樂句分析在 voice separation 不準時會誤判。Bach Inventions (2 聲部) 安全；Sinfonias 與其他作品要視情況補 voice separation 前處理。

## 8. 與「同音型同指法 HARD」原則的整合

[[../score-claude/memory/feedback_personal_biomechanics]] 要求同音型同指法。對位作品的特殊情況：

- **同主題在不同聲部**：RH 與 LH 都唱主題，是否該用「相同指法」？答案：**否**。LH 與 RH 指法本來就 mirror 不對稱（拇指方向相反），加上音高位置不同，「相同指法」物理上不能複製。
- **同聲部同主題**：在同一隻手內、主題重入聲使用相同指法 — **是**，這是原則的核心案例。

## 9. 待補頁面

- [[concept_subject_imitation_detection]] — 主題 / 模仿偵測演算法
- [[concept_cadence_detection]] — 終止式偵測
- [[concept_voice_separation_for_phrasing]] — voice separation 對樂句分析的影響
- [[analysis_bach_inv_4_d_minor]] — mvt4 case study
- [[composer_bach_invention_phrasing]] — Bach Invention 風格特化

