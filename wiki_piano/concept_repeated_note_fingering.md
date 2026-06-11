# Concept: Repeated Note Fingering — 同音重複指法

> 來源：Czerny *Op.500* §repeated notes, Liszt *La Campanella*（repeated-note 經典）, Sandor *On Piano Playing* §repetition
> 引用方：[concept_finger_substitution](concept_finger_substitution.md), [../wiki_articulation/concept_legato_substitution](../wiki_articulation/concept_legato_substitution.md), [../wiki_articulation/concept_same_pitch_refingering](../wiki_articulation/concept_same_pitch_refingering.md)（四動機之 D）

## 1. 同音重複是什麼

同音重複 = 連續多次彈同一個音（高度、音名相同）。常見：
- 連續 2 音重複（簡單）
- 連續 3 音以上（如 Liszt *La Campanella* RH 三重音重複）
- 高速 tremolo-like 重複

物理挑戰：每彈一次都需 hammer 完全 reset（鋼琴 action 限制），即使理論上同指可彈，**換指通常更有效率**。

## 2. 標準同音重複指法

⚠ Training-data verification needed:

### 2.1 連續 2 音重複

| Tempo | 推薦 fingering |
|---|---|
| 慢 | 同指可 (3-3 / 2-2) |
| 中速 | 換指 (3-2 / 4-3) |
| 快速 | 必須換指 |

### 2.2 連續 3 音重複（Liszt *La Campanella* 經典）

| 演奏者 | 經典指法 |
|---|---|
| **Liszt 派傳統** | **4-3-2-1** (依次降序) |
| **替代** | **3-2-1** (3 音時降序) |
| **慢段** | **3-2-3-2** (來回) |

→ Liszt 的 **4-3-2-1** 在連續 3 音重複（La Campanella）成為標準傳統。

### 2.3 連續 4+ 音重複

- **4-3-2-1-4-3-2-1...** 循環（標準）
- **4-3-2-1-2-3-4-3-2-1...** 波浪式（cadence 段）

## 3. 為何同音重複需要換指

物理上：
- 鋼琴 action 需要約 30-50 ms 釋放 + 重新 attack
- 同指彈下 + 釋放 + 再彈下: 一個動作完成
- 換指彈下 + 鬆開（前指）+ 新指彈下: 各動作分散，**整體更快**

→ 同音重複 ≥ 8 音/秒（Allegro tempo 16th-note）通常需要換指才能 sustain。

## 4. 同音重複與 legato substitution 的區別

⚠ Training-data verification needed:

| 屬性 | 同音重複 (repeated notes) | Legato substitution |
|---|---|---|
| 場景 | 樂譜寫多個同音音符 | 樂譜寫單一持音音符 + slur |
| 目標 | 速度 + attack 清晰度 | 維持 legato 連續性 |
| 物理動作 | 每音都有 attack | substitution 不重新 attack |
| 標準指法 | 4-3-2-1 / 3-2-1 降序 | 任意 — 看 hand position |

→ 兩者**不同概念**：repeated notes 是樂譜寫的多個 attack；legato substitution 是同一個音由 release 切換到新手指。

## 5. Hand-position 對 repeated notes 的影響

同音重複的指法**部分取決於前後音 context**：
- 前後音都在附近 → 同音重複用內側指（2-3）
- 前後音跨度大 → 同音重複作為「跳到下個 position 的橋樑」

例：Liszt *La Campanella* m1 開頭 D♯6 三重音 → 接後續 melodic line — fingering 應為 4-3-2 然後 thumb 接下個 position。

## 6. 對 score-claude DP 的影響

DP 對 repeated notes 處理：
- 識別連續同音 (midi 相同) → [../wiki_articulation/concept_legato_substitution](../wiki_articulation/concept_legato_substitution.md) rule 可能觸發
- **但** legato substitution 是針對 slur 內的同音；repeated notes 通常**非** slur 段
- DP 目前對非-slur 同音重複**無 special-case** — 依 cost 自然選擇

未來 v3 candidate：**repeated-note pattern detection** — 偵測連續 3+ 同音段強制 4-3-2-1 / 3-2-1 fingering。未實作。

## 7. 適用作曲家 / 曲目

| 作曲家 | 同音重複使用 |
|---|---|
| **Bach** | 極少 — 對位寫作不偏好同音重複 |
| **Mozart** | 偶見 — 部分 sonata theme 短 repeated notes |
| **Beethoven** | 中等 — Op.10 No.1 mvt1 開頭 G repeated notes |
| **Chopin** | 少 — 浪漫派偏向 legato melody |
| **Liszt** | **極多** — *La Campanella* 是 repeated-note virtuoso 代表 |
| **Scarlatti** | 多 — sonata 中常見 |
| **Prokofiev** | 多 — *Toccata* / piano sonata 大量 |
| **Bartók** | 中 — *Allegro Barbaro* 等 |

## 8. 訓練曲目

| 訓練目標 | 推薦曲目 |
|---|---|
| 入門同音重複 | Czerny *Op.299* / *Op.740* 相關練習曲 |
| 4-3-2-1 連續 | Czerny *Op.740* 部分練習 |
| 高速 repeated | Hanon §60 trill variant |
| Performance 級別 | Liszt *La Campanella*, Ravel *Alborada del gracioso* |

## 9. 與其他 wiki 頁面的關係

- [concept_finger_substitution](concept_finger_substitution.md) — substitution 與 repeated notes 的物理區分
- [concept_hand_anatomy](concept_hand_anatomy.md) — 換指速度的解剖學限制
- [../wiki_articulation/concept_legato_substitution](../wiki_articulation/concept_legato_substitution.md) — slur 內同音 vs repeated notes 的概念區分
- [../wiki_articulation/concept_articulation_and_tempo](../wiki_articulation/concept_articulation_and_tempo.md) — repeated notes 速度與換指策略
