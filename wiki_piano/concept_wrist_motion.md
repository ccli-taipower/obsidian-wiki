# Concept: Wrist Motion — 手腕運動

> 來源：Matthay *The Visible and Invisible* §wrist, Sandor *On Piano Playing* §wrist motion, Neuhaus *The Art of Piano Playing* §觸鍵 (含 wrist 角色)
> 引用方：[concept_octave_fingering](concept_octave_fingering.md), [concept_forearm_rotation](concept_forearm_rotation.md), [concept_thumb_technique](concept_thumb_technique.md)

## 1. Wrist 在鋼琴演奏中的角色

手腕（wrist）連接前臂與手掌，扮演**動作 transmission + 動作 generation** 雙重角色：
- **Transmission**: 把前臂重量傳遞到手指
- **Generation**: 產生獨立的彈奏動作（八度、跳躍、staccato）

→ Wrist 不只是「被動關節」，是鋼琴技術的核心**動作源**之一。

## 2. Wrist 動作的四個自由度

⚠ Training-data verification needed:

| 自由度 | 動作 | 鋼琴應用 |
|---|---|---|
| **上下** (flexion / extension) | 向上 / 向下 | 八度的主要動作；staccato 加速 |
| **左右** (radial / ulnar deviation) | 拇指側 / 小指側 | scale 段 thumb-pass 配合動作 |
| **旋轉** (pronation / supination) | 掌心朝下 / 朝上 | 與前臂旋轉協同（[concept_forearm_rotation](concept_forearm_rotation.md)）|
| **圓周** (circumduction) | 上述組合的圓周動作 | virtuoso 段（Chopin / Liszt 大跳）|

## 3. Wrist 八度技術（最常被引用的應用）

⚠ Training-data verification needed:

Sandor *On Piano Playing* §wrist octave 詳述：
- 連續八度的動作主要來自 wrist 上下
- 手指（1 + 5）保持固定 shape
- 前臂 + arm 提供重量支撐
- Wrist 是「**accelerator**」— 每一八度的 attack 速度由 wrist 控制

對指法的意涵：[concept_octave_fingering](concept_octave_fingering.md) 不只是指法選擇，更是 wrist motion 訓練。

## 4. Wrist 在 staccato 中的角色

[../wiki_articulation/concept_staccato](../wiki_articulation/concept_staccato.md) §3 提到三層 staccato（finger / wrist / arm staccato）：
- **Finger staccato**: wrist 不動，純手指動作
- **Wrist staccato**: wrist 上下產生 attack
- **Arm staccato**: 整 arm 動作（最大 attack 力）

→ 不同 staccato 變體 = 不同 wrist 動作程度。

## 5. Wrist freedom — 避免 stiffness

⚠ Training-data verification needed:

學生常見錯誤：**wrist 僵硬**（stiff wrist）：
- 把 wrist 鎖死「保持手型」
- 不讓 wrist 補正手指動作
- 結果：手指過勞 + 動作受限

Neuhaus / Matthay 教學主張：**wrist 必須保持 free / flexible** 才能：
- 補正不完美的指法
- 提供 dynamic 變化
- 防止 finger strain

對 [analysis_common_fingering_injuries](analysis_common_fingering_injuries.md) 的意涵：wrist 僵硬是 focal dystonia / strain 高風險訊號。

## 6. Wrist motion 與 fingering 的互動

⚠ Training-data verification needed:

| 情境 | Wrist motion 角色 |
|---|---|
| Scale 段 thumb-pass | Wrist 微微向 ulnar 側補正，使 thumb 自然到下個位置 |
| 大跳音程 | Wrist 預先轉到目標方向，減少 finger 跨度需求 |
| Substitution | Wrist 保持中性，讓 finger 切換不受干擾 |
| Voicing | Wrist 偏向突出指側，傳遞額外重量 |
| Trill | Wrist 鎖住，純手指動作（trill 是 finger independence test）|

## 7. Wrist 與 forearm rotation 的區別

⚠ Training-data verification needed:

兩者常被混淆：

| 屬性 | Wrist motion | [concept_forearm_rotation](concept_forearm_rotation.md) |
|---|---|---|
| 動作部位 | 手腕關節 | 前臂內外旋（橈骨繞尺骨）|
| 動作方向 | 上下 / 左右 / 旋轉 | 純內外旋（forearm pronation/supination）|
| 典型應用 | 八度、staccato、跳躍 | tremolo, alberti bass, 大跨度 broken chords |
| Sandor 分類 | "wrist motion" | "rotation" |

→ 兩者常**共同作用**，但教學上應分開訓練。Sandor *On Piano Playing* 明確分章區分。

## 8. 對 score-claude DP 的影響

DP 對 wrist motion 目前**不 model**：
- DP 計算 finger sequence，假設 wrist 自由補正
- Wrist motion 的「該不該做 / 怎麼做」由演奏者層處理
- DP 不會對 wrist-stiff 的 fingering 增加 cost

是 known 限制。對 advanced 曲目（virtuoso pass / 八度連續段）需考慮 wrist-motion-aware fingering，未實作。

## 9. 教學進階

| 階段 | Wrist 訓練 |
|---|---|
| 入門 | Wrist 自由動 + 不僵硬（基本姿勢）|
| 初中階 | Wrist 配合 scale + arpeggio 自然補正 |
| 中階 | Wrist 主導八度練習 |
| 進階 | 不同 staccato 變體（finger / wrist / arm）區分 |
| Virtuoso | Wrist + rotation + arm 整合複雜動作 |

## 10. 與其他 wiki 頁面的關係

- [concept_octave_fingering](concept_octave_fingering.md) — Wrist motion 是八度技術核心
- [concept_forearm_rotation](concept_forearm_rotation.md) — 互補但獨立的動作軸
- [concept_thumb_technique](concept_thumb_technique.md) — Thumb-pass 配合 wrist motion
- [analysis_common_fingering_injuries](analysis_common_fingering_injuries.md) — Wrist stiffness 與 strain 關係
- [../wiki_articulation/concept_staccato](../wiki_articulation/concept_staccato.md) §3 — Wrist staccato 變體
