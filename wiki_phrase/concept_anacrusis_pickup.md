# Concept: Anacrusis / Pickup — 弱起 / 起頭弱拍處理

> 來源：Cooper-Meyer《Rhythmic Structure of Music》(1960), Caplin《Classical Form》§anacrusis, Brendel essays §pickup
> 引用方：[[concept_classical_period_sentence]], [[concept_phrase_elision]]

## 1. Anacrusis / Pickup 是什麼

Anacrusis (希臘文「**上拍**」) = **弱起音** — 樂句開始於 measure 末尾（弱拍）而非 measure 起首（強拍）。常稱「**pickup notes**」或「**pickup measure**」。

例：「Happy Birthday」開頭 — "Hap-py" 兩音是 anacrusis，"birth-day" 落在強拍。

→ Anacrusis 是**樂句結構**特徵，不是 measure 結構特徵。

## 2. Anacrusis 的長度分類

⚠ Training-data verification needed:

| 長度 | 描述 |
|---|---|
| **短 anacrusis** (1 音) | 最常見 — 4/4 中 1 個 8th-note pickup |
| **中 anacrusis** (2-4 音) | 常見 — Mozart sonata 主題開頭 |
| **長 anacrusis** (5+ 音 或 整 bar) | 罕見 — Beethoven 後期戲劇性開頭 |
| **Double anacrusis** | 兩段 anacrusis 套疊 — Brahms 偶見 |

## 3. Anacrusis 對樂句偵測的挑戰

⚠ Training-data verification needed:

Anacrusis 在 phrase 偵測時容易**誤判**：
- Anacrusis 屬於 **下一 phrase**，不是上一 phrase
- 樂句邊界應在 anacrusis **前**（不在 anacrusis 後）
- 但 anacrusis 在 measure 中位置 = 上一 measure 末尾，演算法易誤判為上 phrase

對 score-claude DP 的對應：`_detect_phrase_starts` Pass 1b 專門 anacrusis 偵測，把 anacrusis 標為**下一 phrase 起點**而不是當前 phrase 一部分。

## 4. Anacrusis 偵測規則 ⚠

⚠ Training-data verification needed:

當代 phrase 偵測 anacrusis 啟發式：
| 規則 | 描述 |
|---|---|
| **Duration test** | Anacrusis 音通常較短（< 0.5 QN）|
| **Position test** | 在 measure 末尾（offset > PICKUP_MIN_OFF）|
| **Prev-note test** | 前一音較長（≥ PICKUP_PREV_MIN）|
| **Next-measure test** | 後一音是 measure 起首（下個 measure beat 1）|

score-claude DP 的 `PICKUP_MAX_DUR = 0.5`, `PICKUP_MIN_OFF = 3.0`, `PICKUP_PREV_MIN = 1.0` 是此啟發式的常數實現。

## 5. Anacrusis 在不同時代的使用

⚠ Training-data verification needed:

| 時代 | Anacrusis 使用 |
|---|---|
| **Baroque (Bach)** | 中等 — French Suite Allemande 常 anacrusis 開頭 |
| **Classical (Mozart/Haydn)** | 高 — Sonata theme 開頭 anacrusis 普遍 |
| **Romantic (Chopin/Schumann)** | 高 — Lyrical melody 常 anacrusis 開頭 |
| **Modernism (Bartók)** | 中 — 較自由節奏 |

→ Anacrusis 是 18-19 世紀標準 phrase 開頭技巧。

## 6. Anacrusis chains (連續 anacrusis)

⚠ Training-data verification needed:

**Double pickup** / **Triple pickup** 結構：
- 上 phrase 結束音 + 短 anacrusis + 更短 anacrusis → 下 phrase 起首
- Phrase 之間有「**rolling**」過渡感
- Brahms / Schumann 浪漫派常用

對 score-claude DP 的對應：`_detect_phrase_starts` Pass 1b 中 back-chain (擴展 anacrusis_candidates) 處理 chain 情境。

## 7. Anacrusis 與 phrase elision 的區別

⚠ Training-data verification needed:

| 屬性 | Anacrusis | Phrase Elision |
|---|---|---|
| 時間結構 | 下 phrase 起首於上 phrase 結束**之後** | 兩 phrase **重疊**於同一音 |
| 邊界位置 | 在 anacrusis 前 | 在 elision 音上 |
| 偵測難度 | 中（measure 位置線索）| 高（需語法分析）|
| 出現頻率 | 普遍 | 中等 |

→ 兩者**經常混淆**，但結構性不同。詳見 [[concept_phrase_elision]]。

## 8. 對指法的意涵

Anacrusis 段的指法考慮：
- **第一個 anacrusis 音**：常用 thumb (1) 或 強指 (2-3) — 因為是 phrase 起點，需要 stable hand position
- **連續 anacrusis 音**：依音域與 next-measure 強拍對應 — 為下個強拍**準備手位**
- **下個 strong beat 音**：通常 melody 主音 — 強指偏好 (1/2/3)

→ Anacrusis fingering 與**樂句首音 fingering**邏輯相同。

## 9. 對 score-claude DP 的具體影響

DP 對 anacrusis 處理（`_detect_phrase_starts` Pass 1b）：
- 在 4/4 (BEATS_PER_MEASURE = 4) 假設下精確
- 對 3/4 / 6/8 (compound) anacrusis 處理需 `_PHRASE_CTX["measure_ql"]` (per [[../score-claude/memory/project_2026-05-29_session_arc]] §time-sig fix)
- 對 3/8 anacrusis：PICKUP_MIN_OFF = 3.0 過高，3/8 measure 最大 offset 1.5 → anacrusis 偵測不會觸發 (known 限制)

## 10. 與其他 wiki 頁面的關係

- [[concept_classical_period_sentence]] — Classical period 常以 anacrusis 開始 antecedent
- [[concept_phrase_elision]] — Anacrusis vs elision 區分
- [[concept_hypermeter]] — Anacrusis 對 hypermeter 計數影響
- [[../wiki_articulation/concept_articulation_overview]] §6 — Anacrusis 不是 phrase boundary 而是新 phrase 起點

## 11. ⚠ Training-data verification queue

- §2 各 anacrusis 長度的學術 / 教學常規
- §4 PICKUP_MAX_DUR / PICKUP_MIN_OFF 等常數的學術依據
- §5 各時代 anacrusis 使用頻率的學術文獻
- §7 Anacrusis vs phrase elision 區別的學術論述
