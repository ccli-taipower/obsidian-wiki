# Concept: Hand Position Stability — 手位穩定性

> 來源：Neuhaus *The Art of Piano Playing* §position, Sandor *On Piano Playing* §hand position, Cortot *Rational Principles*
> 引用方：[concept_thumb_technique](concept_thumb_technique.md), [concept_finger_substitution](concept_finger_substitution.md), [../wiki_articulation/concept_legato_substitution](../wiki_articulation/concept_legato_substitution.md)

## 1. 手位穩定性是什麼

Hand position (手位) = 演奏時手在鍵盤上的**整體空間定位**。手位 stability = 在一個 passage 內**手位穩定不過度漂移**的能力。

判定 stability:
- 一個 passage 內 hand 重心移動範圍小（typically ≤ 1 八度）
- Thumb 在合理位置（不需大幅 stretch / 縮）
- 各指有可靠的「**默認音**」(每指通常彈固定 pitch class)

→ Hand stability 是指法系統的**重要 implicit 目標**。

## 2. 為何 hand stability 重要

| 原因 | 解釋 |
|---|---|
| **可預測性** | 穩定 hand 讓動作可預期，減少失誤 |
| **速度** | 不需要重新 calibrate hand position 可達更高速度 |
| **音準** | 手不漂移就不會擦到鄰音 |
| **疲勞 minimization** | 大量 hand reposition 容易累 |
| **連續性** | Legato 要求 hand 位置穩定（變動會破壞 legato）|

## 3. Hand stability 與 thumb-pass 的關係

⚠ Training-data verification needed:

Thumb-pass 是「**hand position 切換**」事件 — scale / arpeggio 段每 thumb-pass = 一次 hand reposition。

設計良好的指法在 thumb-pass 時：
- 預備性指法準備好下個 position
- Reposition 幅度最小化（理想是僅 thumb 位置變化）
- Wrist + arm 配合補正

→ Scale fingering (1-2-3-1-2-3-4-5) 就是優化 hand stability 的歷史結果。

## 4. Hand stability vs Hand free motion

兩者是 trade-off：

| 高 hand stability | 高 hand free motion |
|---|---|
| 適合：scale / 小範圍 passage | 適合：大跳 / 跨多八度 |
| Substitution 容易 | Substitution 不必要 |
| Wrist motion 局限 | Wrist motion 大幅 |
| 適合 legato | 適合 staccato + jump |

→ 不同段需要不同 stability 程度。Czerny 設計練習針對兩端訓練。

## 5. Hand stability 的判定（演奏 + 系統）

⚠ Training-data verification needed:

對演奏者：
- Scale / arpeggio 段：手應保持「**沿 keyboard 直線移動**」感
- Lyrical melody：手應「**呼吸**」般微小起伏，不大跳
- 對位 texture：每聲部手位獨立，整體不亂

對指法系統：
- 計算 fingering 對應的 implied anchor (thumb 預期位置)
- 計算各音 anchor 偏移量
- 偏移量過大 → hand position 不穩 → 加 cost

對 score-claude DP 的對應：
- `W_PHRASE_ANCHOR = 0.4` — 樂句內手位錨點偏好
- `INTRA_PHRASE_TRANSITION_SCALE = 1.0` — 樂句內過渡 cost (高 = 鼓勵手位穩定)
- `_implied_anchor()` 函式計算各 fingering 的隱含手位

## 6. Phrase boundary 與 hand stability 的解耦

[wiki_phrase](../wiki_phrase/index.md) 樂句邊界是「**手位 free reset**」點：
- 樂句內 → 手位穩定優先
- 樂句邊界 → 手位可自由 reposition 到下個樂句的最佳起手位置

→ Phrase boundary 偵測準確性直接影響 hand stability 策略。

對 score-claude DP 的對應：`INTER_PHRASE_SCALE = 0.0` — 樂句間 transition cost 不計，鼓勵 free reposition。

## 7. Stability 與 finger substitution 的互動

⚠ Training-data verification needed:

兩者**雙向影響**：
- Substitution 是維持 stability 的工具（重新 calibrate 手位給下段準備）
- Stability 要求限制 substitution 過度（過度 substitution = 手位混亂）

平衡：在「**樂句中段需要 substitution 維持 legato**」+「**樂句邊界 substitution 過渡到新位置**」兩種情境下適用，**段內不必要 substitution 應避免**。

[../wiki_articulation/concept_legato_substitution](../wiki_articulation/concept_legato_substitution.md) v2 duration gate (LEGATO_MIN_DURATION ≥ 0.5 QN) 即是「**只在實用價值時 substitution**」的策略。

## 8. Hand stability 在 different styles

| 風格 | Stability 程度 |
|---|---|
| **Bach 對位** | 高 — 兩聲部都需手位穩定 |
| **Classical scale / 跑動段** | 高 — scale fingering 的設計目標 |
| **Romantic lyrical** | 中高 — melody legato 需穩定，但偶爾 wide spread |
| **Romantic virtuoso (Liszt etc.)** | 低 — 大跳 + 廣音域 |
| **Impressionist (Debussy)** | 中 — 沿曲變化大 |
| **Modernism (Bartók etc.)** | 變化 — 看作品 |

→ 不同風格不同 stability 假設。

## 9. 對 score-claude DP 的影響

DP 內隱優化 hand stability:
- `W_PHRASE_ANCHOR` cost rule
- Transition cost 結構鼓勵小範圍 hand motion
- Phrase boundary 偵測讓 hand free reposition

未來改進方向：
- **Per-passage stability mode**: 對 lyrical 段強化 stability、對 virtuoso 段放鬆
- **Style-aware stability**: 對 Bach 強、對 Liszt 弱

是 future direction，未明確實作。

## 10. 與其他 wiki 頁面的關係

- [concept_thumb_technique](concept_thumb_technique.md) — Thumb-pass 是 hand stability 切換的核心動作
- [concept_finger_substitution](concept_finger_substitution.md) — Substitution 與 stability 的互動
- [concept_scale_fingering](concept_scale_fingering.md) — Scale fingering 是 stability 優化的歷史結果
- [concept_wrist_motion](concept_wrist_motion.md) — Wrist 補正動作維持 stability
- [../wiki_articulation/concept_legato_substitution](../wiki_articulation/concept_legato_substitution.md) — Substitution 的 stability 平衡
- [wiki_phrase](../wiki_phrase/index.md) — Phrase boundary 是 stability reset 點
