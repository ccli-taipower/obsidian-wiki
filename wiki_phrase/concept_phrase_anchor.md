# Concept: Phrase Anchor — 樂句手位錨點

> 來源：score-claude DP 設計 (Parncutt-inspired), Czerny *Op.500* §hand position 章節, Neuhaus《The Art of Piano Playing》§hand position
> 引用方：[[../wiki_piano/concept_hand_position_stability]], [[concept_running_passage_thumb_reservation]]

## 1. Phrase Anchor 是什麼

**Phrase anchor** = 一個樂句內**手的中心位置**（hand position centroid）。是「**這個樂句手應該停在哪**」的單一參考點。

定義 (per score-claude DP)：
- 樂句內各音的 implied thumb position 之 **median**
- 或：樂句內音域 (range) 的**中位數**
- → 樂句內 fingering 選擇應**減少手位偏離 anchor 的程度**

→ Phrase anchor 是 [[../wiki_piano/concept_hand_position_stability]] 的具體**操作型實現**。

## 2. 為何需要 phrase anchor 概念

⚠ Training-data verification needed:

不同 fingering 選擇對應不同 hand position：
- Fingering A: thumb 多在 G4 → hand 偏低
- Fingering B: thumb 多在 C5 → hand 偏中
- Fingering C: thumb 多在 F5 → hand 偏高

當樂句覆蓋 C4-A5 範圍時：
- 選擇讓 thumb 集中在 E5 附近的 fingering = hand 在「**中心**」位置
- 選擇讓 thumb 移動範圍大的 fingering = hand 「**不穩定**」

→ Phrase anchor 提供「**hand stability**」的可量化標準。

## 3. Phrase Anchor 的計算 ⚠

⚠ Training-data verification needed:

對單樂句計算 anchor (per score-claude `_implied_anchor`):

```
implied_anchor(f_to_m, hand) =
    if hand == "right":
        median(midi - NATURAL_OFFSET[finger])  for each note
    else:  # left
        median(midi + NATURAL_OFFSET[finger])  for each note
```

其中 `NATURAL_OFFSET = {1: 0, 2: 2, 3: 4, 4: 5, 5: 7}` (semitones from thumb)。

物理意涵：把每個音 backtrack 到「**假設 thumb 對應這個音時，thumb 應該的位置**」，取 median 為樂句 anchor。

## 4. Phrase Anchor 的 cost 應用

⚠ Training-data verification needed: score-claude DP cost rule:

```
W_PHRASE_ANCHOR = 0.4  # 樂句錨點 偏好權重
cost += W_PHRASE_ANCHOR * |implied_anchor(current_fingering) - phrase_anchor|
```

意涵：fingering 選擇若使 implied anchor 偏離 phrase target anchor，加 cost。

對 fingering 結果：DP 偏好讓**樂句內 thumb 停留在 anchor 附近**的 fingering — 等同 hand stability 優化。

## 5. Phrase Anchor 與 Pivot 的區別

| 屬性 | Phrase Anchor | Pivot |
|---|---|---|
| 層級 | 樂句層級 — 整 phrase 的中心 | 動作層級 — thumb-pass 的轉折點 |
| 持久度 | 整 phrase 維持 | 短暫（thumb-pass 瞬間）|
| 用途 | Hand position centroid | Scale / arpeggio thumb-pass 位置 |
| 計算 | Median of implied positions | thumb 落點 |

→ Pivot 是樂句內部的 thumb-pass 點（[[../wiki_piano/concept_long_scale_thumb_under]]）；anchor 是樂句整體的中心。兩者不同概念。

## 6. Phrase Anchor 與 phrase boundary 的互動

樂句**之間**手位可 free reposition (per `INTER_PHRASE_SCALE = 0.0`)：
- 樂句 A 結束：anchor 在 G4
- 樂句 B 開始：anchor 可在 C5（新位置）
- 兩 phrase 之間 free reposition 動作

→ Phrase anchor 概念為「**樂句獨立優化**」原則的支柱。

## 7. 適用情境

⚠ Training-data verification needed:

| 情境 | Phrase Anchor 有效性 |
|---|---|
| Mozart / Haydn 平衡 phrase | 高 — 樂句內手位確實應穩定 |
| Bach 對位作品 | 中 — 對位線各自 anchor，每聲部獨立 |
| Chopin lyrical melody | 高 — 抒情段需 hand stability |
| Liszt virtuoso 大跳段 | 低 — phrase 內 hand 必然大幅 reposition |
| 不規則 phrase length (Brahms) | 中 — anchor 概念適用但 phrase 邊界偵測難 |

→ Phrase anchor 對**規則 phrase length + 限定音域** 的曲目最有效。

## 8. 對 score-claude DP 的具體實現

DP 內 phrase anchor 的角色：
- `_implied_anchor()`: 計算 implied anchor of given fingering choice
- Phrase target anchor: 樂句內音域 median ± NATURAL_OFFSET (per hand)
- `W_PHRASE_ANCHOR = 0.4`: 主要 cost weight (per 2026-05-20 retune)
- `W_PHRASE_ANCHOR_PER_NOTE`: per-note 加權變體

對應 [[score-claude memory project_retune_v2_2026-05-20]] 的調參記錄。

## 9. Phrase Anchor 的學術依據

⚠ Training-data verification needed:

雖然「phrase anchor」一詞為 score-claude DP 內部用語，其概念有教學文獻支持：

| 來源 | 對應概念 |
|---|---|
| **Neuhaus《Art of Piano Playing》** | "hand position center" (手位中心) — 演奏者應「**感受**」每段的手位中心 |
| **Czerny《Op.500》** | "natural hand position" (自然手位) — 標準 5-finger position |
| **Parncutt 1997 ergonomic model** | Cost penalty for hand position changes — 量化的 hand stability |
| **Sandor《On Piano Playing》** | "hand center of gravity" — 重力中心類比 |

→ Phrase anchor 是這些教學概念的**演算法形式化**。

## 10. 與其他 wiki 頁面的關係

- [[../wiki_piano/concept_hand_position_stability]] — Phrase anchor 是 stability 的操作型
- [[../wiki_piano/concept_thumb_technique]] — Anchor 與 thumb-pass 互動
- [[concept_running_passage_thumb_reservation]] — Running passage 中的 thumb reservation rule 借用 anchor 概念
- [[concept_phrase_elision]] — Elision 時兩 phrase anchor 過渡處理
- [[../wiki_piano/src_parncutt1997_ergonomic_model]] — Parncutt 1997 hand position cost

## 11. ⚠ Training-data verification queue

- §3 `_implied_anchor` 公式的具體數學推導
- §4 W_PHRASE_ANCHOR = 0.4 的 retune 歷史
- §7 各 phrase 類型 anchor 適用度的學術驗證
- §9 各教學文獻 "hand position center" 引述
