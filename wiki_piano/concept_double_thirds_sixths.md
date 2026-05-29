# Concept: Double Thirds / Sixths — 雙音三度 / 六度 指法

> 來源：Czerny *Op.500* §double notes, Chopin *Etudes* Op.25 No.6 (double thirds), Cortot *Rational Principles of Pianoforte Technique* §double notes
> 引用方：[[concept_chord_fingering]], [[concept_finger_substitution]]

## 1. Double notes 是什麼

Double notes（雙音）= 一手同時演奏兩音，但**不是和弦** — 是兩條獨立旋律線同時推進。最常見：
- **Double thirds** (雙音三度): 兩音相距 3 度（4 半音 = major / 3 半音 = minor）
- **Double sixths** (雙音六度): 兩音相距 6 度（9 半音 = major / 8 半音 = minor）
- **Double octaves**（[[concept_octave_fingering]]）: 兩音相距 8 度

Double notes 段是鋼琴**最難的純技術項目之一** — Chopin Op.25 No.6 是 double-thirds etude 的代表。

## 2. 為何 double notes 比單音難

物理上：
- **兩音同時 attack** 需要兩個手指同步
- **連續 double notes** 需要兩條線同時 legato — 接近不可能 (一條線 legato 需要 substitution，兩條線同時 substitution 物理超難)
- **音準** 要求 — 兩音同時不對齊（一前一後）= 演奏失誤

→ Double notes 是高難度技巧，多數情況屬 advanced 範圍。

## 3. Double thirds 標準指法

⚠ Training-data verification needed:

| RH 上行 thirds 連續 | 指法選項 |
|---|---|
| C-E / D-F / E-G / ... | **1-3 / 2-4 / 1-3 / 2-4 連續** 交替 (上 finger 2-4 / 下 finger 1-3) |
| 或 | **1-3 / 2-5 / 1-3 / 2-5** (上 5 給黑鍵) |
| 或 | **2-4 / 1-3 / 2-4 / 1-3** (反向) |

關鍵：**沒有完美 legato 解** — 每次交替都有微小斷裂。Chopin etude 練的就是讓這些斷裂**聽不見**。

## 4. Double sixths 標準指法

⚠ Training-data verification needed:

| RH 上行 sixths 連續 | 指法選項 |
|---|---|
| C-A / D-B / E-C / ... | **1-5 / 2-4 / 1-5 / 2-4 連續** (上音 5 與 4 交替) |
| 或 | **1-4 / 2-5 / 1-4 / 2-5** |
| 慢速段 | **1-5 / 1-5 連續** (像八度但下音用 1)，配 wrist motion |

Double sixths 比 double thirds **稍容易些**（音程大，手指有更多空間），但仍是高難度。

## 5. Chopin Op.25 No.6 — Double Thirds Etude

Chopin *Etude in G♯ minor Op.25 No.6* 是 double thirds 的標準練習曲：
- 整曲 RH 連續 double thirds（少數段除外）
- Tempo Allegro — 高速 double thirds
- 是「**鋼琴最難的曲目之一**」公認

⚠ Training-data verification needed: 演奏家共識：
- Chopin 自己標 1-3 / 2-4 為主
- 後續演奏家有不同 fingering 變體
- 完全沒有「正確」單一指法 — 看手大小 + 個人偏好

## 6. Double notes 的 substitution

⚠ Training-data verification needed:

雖然兩條線同時 legato 很難，部分情境可做 substitution：
- **下音 substitution + 上音持指**: substitution 下音時上音持住，再切換上音
- **上音 substitution + 下音持指**: 反之
- **同時 substitution**: 物理上幾乎不可能（兩手指同時釋放 + 兩手指同時 attack）

Chopin 在 Op.25 No.6 部分段落有 substitution 標記，是 advanced 技巧。

## 7. 黑鍵 + 白鍵混合 double notes

⚠ Training-data verification needed:

當 thirds / sixths 包含黑鍵 + 白鍵混合：
- 一手指上白鍵、另一手指上黑鍵 → hand position 不同高度
- 需要 wrist 微微傾斜 / arm 補正
- 黑鍵指偏好 2-3-4（中間指），thumb / 5 較少上黑鍵

## 8. 對 score-claude DP 的影響

DP 對 double notes 處理：
- 識別 chord 內兩音為 thirds / sixths interval
- 套用 [[concept_chord_fingering]] 標準分配
- 不啟用 [[concept_finger_substitution]] rule 在連續 double notes 段（substitution 物理太難）

實作上 score-claude 對 chord 處理（含 thirds/sixths）由 `_assignment_cost` 處理，不需 special-case rule。

## 9. 適用作曲家 / 曲目

| 作曲家 | Double-notes 段 |
|---|---|
| **Bach** | Inventions / Sinfonias 偶見 thirds 段，少 sixths |
| **Mozart** | Sonatas 中等 — 部分 cantabile thirds 段 |
| **Beethoven** | 較多 — Op.106 Hammerklavier 大量 double thirds |
| **Chopin** | 大量 — Op.25 No.6 double thirds, Op.10 No.2 chromatic thirds |
| **Liszt** | 大量 — *Hungarian Rhapsody* double sixths, *Transcendental Etudes* |
| **Brahms** | 多 — *Variations on a Theme by Paganini* double thirds 段 |

## 10. 與其他 wiki 頁面的關係

- [[concept_chord_fingering]] — Double notes 是兩音 chord 的特殊形式
- [[concept_finger_substitution]] — 連續 double notes 段 substitution 限制
- [[concept_finger_span_table]] — thirds (4 半音) / sixths (9 半音) finger span
- [[concept_octave_fingering]] — 八度是 double notes 的最大形式
- [[../wiki_articulation/concept_legato_substitution]] — double notes legato 限制
