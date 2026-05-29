# Concept: Octave Fingering — 八度指法

> 來源：Czerny *Op.500* §octaves, Hanon *The Virtuoso Pianist* §60 (octave 練習), Sandor *On Piano Playing* §wrist octave
> 引用方：[concept_thumb_technique](concept_thumb_technique.md), [concept_wrist_motion](concept_wrist_motion.md), [analysis_small_hands_advice](analysis_small_hands_advice.md)

## 1. 八度的指法選項

鋼琴上一個八度 = 12 半音。標準八度演奏：
- **下音**: 拇指 (f1)
- **上音**: 小指 (f5) 或 無名指 (f4)

不像單音，八度本質**只有兩個音同時**，指法選擇主要是「**上音用 5 還是 4**」。

| 上音用 5 | 上音用 4 |
|---|---|
| 標準 / detache / staccato 八度 | Legato 八度 (連續八度滑接) |
| 跳躍八度（jump octaves） | 黑鍵八度（4 較靈活）|
| 大跨度（hand 大）| 小手 small hands 替代 |

## 2. 連續八度的 legato 處理

連續八度（octave passages）legato 演奏的關鍵：1-5 / 1-5 連續間很難真正 legato（手腕動作 + thumb 到下個位置）。技巧：

| 技巧 | 描述 |
|---|---|
| **1-4 / 1-5 交替** | 上音用 4 對黑鍵 + 用 5 對白鍵；提供更多 legato 連接 |
| **Wrist 連接** | 手腕水平移動 maintain 連接感，filling thumb-pass 空隙 |
| **Pedal-assisted** | Sustain pedal 補足 finger 間的 attack 銜接 |
| **Hand jump 接受** | 快速 octave 段不強求 legato，detache 處理 |

## 3. 黑鍵八度的特殊性

當八度兩音都在黑鍵（如 C♯-C♯, F♯-F♯）：
- 手部位置內移（黑鍵在白鍵內側）
- Thumb 在黑鍵上不穩定 — 物理上 thumb 在 white-key 邊緣更穩
- 解決：**4-3-4-3 連續** (替代 1-5-1-5)，避免 thumb 上黑鍵

⚠ Training-data verification needed: Czerny / Liszt 派傳統有「黑鍵八度避免 thumb」原則。

## 4. 八度跳躍 (jump octaves)

八度跳躍（如連續八度間隔大幅跳動）：
- 每個八度獨立 attack
- Hand position 重新 calibrate 每次
- 不需要 legato 連接

典型曲目：Liszt *Hungarian Rhapsody* 第二樂句、Tchaikovsky concerto 大跳八度段。

## 5. 八度技巧的物理基礎

⚠ Training-data verification needed:

Sandor *On Piano Playing* §wrist octave 提出八度的物理：
- 不靠手指運動 — 八度動作主要由**手腕 + 前臂**完成
- 手指（1 + 5 或 1 + 4）保持固定 hand-shape
- 重複動作來自 wrist 上下 + 前臂支撐

→ 八度練習 = 手腕 + 前臂技術練習，不是手指獨立性練習。

對指法的意涵：八度段不啟用 [concept_finger_substitution](concept_finger_substitution.md) 規則（substitution 是手指間的事，八度是 wrist-based 動作）。

## 6. 小手演奏八度的策略

⚠ Training-data verification needed:

手小（八度跨度勉強）演奏者：
- 用 1-4 替代 1-5（4 比 5 稍微近）
- Wrist 平移 + slight arm rotation 補足
- 接受微小 break（不強求完美 legato）
- 必要時跨手分配（一手彈下音、另一手彈上音）

詳見 [concept_small_hands](concept_small_hands.md) + [analysis_small_hands_advice](analysis_small_hands_advice.md) §八度章節。

## 7. 對 score-claude DP 的影響

DP 對八度處理：
- 識別 chord 內音為「八度」(下音 + 上音 12 半音間隔)
- 標準分配：1 (下音) + 5 (上音)，黑鍵或小手情境改 1 + 4
- LH 對應：5 (下音) + 1 (上音)，LH 八度 thumb 在頂音

實作上 [concept_chord_fingering](concept_chord_fingering.md) 中的 chord 指法分配機制已涵蓋八度。

## 8. 八度技巧訓練

教學進階順序：
1. 單一八度（穩定 hand position）
2. 連續八度 detache（focus on wrist motion）
3. 連續八度 legato（4-3-5 交替）
4. 八度音階（連續八度沿音階上行下行）
5. 八度跳躍（不同音域間移動）
6. 八度伴奏線（如 Schubert lieder accompaniment）
7. 八度旋律（如 Chopin Op.53 Polonaise）
8. 八度 octaves passages（virtuoso 段如 Liszt 練習曲）

## 9. 與其他 wiki 頁面的關係

- [concept_thumb_technique](concept_thumb_technique.md) — 八度下音 thumb 解剖學
- [concept_wrist_motion](concept_wrist_motion.md) — 八度的 wrist-based 動作
- [concept_chord_fingering](concept_chord_fingering.md) — 八度作為兩音 chord 處理
- [concept_small_hands](concept_small_hands.md) — 小手演奏八度的限制
- [analysis_small_hands_advice](analysis_small_hands_advice.md) — 小手八度策略
