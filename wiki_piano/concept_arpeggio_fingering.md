# Concept: Arpeggio Fingering — 分解和弦指法

> 來源：Czerny *Op.500*, Hanon *The Virtuoso Pianist* §arpeggios, Cortot *Rational Principles of Pianoforte Technique*
> 引用方：[[concept_scale_fingering]], [[concept_thumb_technique]]

## 1. Arpeggio 是什麼

Arpeggio（分解和弦）= 把和弦音逐音奏出，通常沿 root position / inversion 上行或下行。最基本：
- 三和弦 arpeggio: root-3rd-5th
- 七和弦 arpeggio: root-3rd-5th-7th
- 跨八度延伸 arpeggio: 重複進入下一八度

Arpeggio 與 scale 的差異：
- Scale 全 stepwise (二度音程)
- Arpeggio 全 leap (三度以上音程)
- → 兩者需要的指法策略不同

## 2. 為何 arpeggio 需要 thumb-pass

Arpeggio 跨度大（典型每音 ≥ 3 半音），單手伸縮無法覆蓋多個八度。必須**thumb-pass + repositioning**：
- RH 上行 arpeggio: 1-2-3-5 (三和弦) 或 1-2-3-5 (七和弦) → thumb 穿越到下個八度
- LH 上行 arpeggio: 5-3-2-1 (三和弦) → thumb 落到頂音準備下個八度

→ Arpeggio 是練習 thumb-pass 的標準曲目。

## 3. 標準三和弦 arpeggio 指法

⚠ Training-data verification needed:

| 調 | RH 上行 (一八度) | LH 上行 (一八度) |
|---|---|---|
| **C major (root)** | 1-2-3-5 | 5-3-2-1 |
| **G major** | 1-2-3-5 | 5-3-2-1 |
| **D major** | 1-2-3-5 | 5-3-2-1 |
| **A major / E major** | 1-2-3-5 | 5-3-2-1 |
| **F major** | 1-2-3-5 (white-key arrangements) | 5-3-2-1 |
| **B major / F♯ major (黑鍵多)** | 略不同 — 適應 thumb 避黑鍵 | 同 |

→ 多數調的三和弦 arpeggio 用 1-2-3-5（上行）/ 5-3-2-1（下行）標準指法。

## 4. 七和弦 arpeggio 指法

⚠ Training-data verification needed:

七和弦（4 音）arpeggio 標準指法：
- **RH 上行**: 1-2-3-4 (4 音) → thumb 穿越 → 重複下一八度
- **LH 上行**: 5-3-2-1 (4 音) → 同 thumb 位置 → 重複下一八度

某些調（特別 V7 含黑鍵）需調整 — Czerny *Op.500* 列各調具體 fingering。

## 5. 跨八度延伸 arpeggio

跨多個八度的 arpeggio（如 C-E-G-C-E-G-C ...）：
- RH: 1-2-3-1-2-3-1 連續（每八度重複）
- LH: 5-3-2-5-3-2-5（同）

關鍵：每次 thumb 穿越時，下個音準備好接住。Czerny / Hanon 練習多以此 pattern 訓練。

## 6. Arpeggio 與 scale 的指法對比

| 屬性 | Scale | Arpeggio |
|---|---|---|
| 音程 | 全二度 | 全 ≥ 三度 |
| Thumb-pass 頻率 | 每 3-4 音一次 | 每 3-4 音一次（同） |
| 標準指法 | 1-2-3-1-2-3-4-5 | 1-2-3-5 / 1-2-3-4 |
| 失誤點 | Thumb 穿越時 tempo 變化 | Thumb 穿越時音準 / position 失誤 |
| 練習目標 | 連續性 + 速度 | Position 穩定 + 音準 |

→ 都涉及 thumb-pass，但 arpeggio 更挑戰 hand-position 跳躍。

## 7. 對 score-claude DP 的影響

DP 對 arpeggio 處理：
- 識別連續上行 / 下行 ≥ 3 半音音程 → 通過 `MIN_ARPEGGIO_INTERVAL = 3` 啟動 arpeggio 模式
- 套用 C(5,k) 指法分配（每段最多 5 音，超過則切割）
- 標準 1-2-3-5 / 5-3-2-1 通過 cost 計算自然產生

對應主流程 [[score-claude run.py]] §Step 1b arpeggio merge。

## 8. 適用情境

- **Bach 對位作品**：少 arpeggio（對位主導，不是 broken chord）
- **Mozart sonatas**：較多 — alberti bass 是 LH arpeggio 變體
- **Beethoven sonatas**：大量 — broken-chord passages 廣泛
- **Chopin etudes / waltzes**：大量 — Op.10 No.1, Op.25 No.12 是 arpeggio 練習極致
- **Liszt / Rachmaninoff concerto**：跨多八度 arpeggio 是 virtuoso 特色

## 9. 與其他 wiki 頁面的關係

- [[concept_scale_fingering]] — 同樣涉及 thumb-pass，但 stepwise 而非 leap
- [[concept_thumb_technique]] — Thumb-pass 解剖學 + 物理
- [[concept_long_scale_thumb_under]] — Scale 的 thumb-under 相關
- [[concept_finger_span_table]] — arpeggio 音程跨度與 finger span 對應
- [[../wiki_articulation/concept_legato_substitution]] — arpeggio 內音多 detache，少 substitution
