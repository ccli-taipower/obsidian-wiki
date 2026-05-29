# Concept: Legatissimo — 極致連奏

> 來源：Neuhaus《The Art of Piano Playing》§連奏觸鍵, Liszt 演奏傳統
> 引用方：[concept_articulation_overview](concept_articulation_overview.md) §2 (taxonomy 最連端)

## 1. Legatissimo 是什麼

Legatissimo 是 articulation 光譜中**最連**的一端：
- 操作型音長：**100% + 微 overlap**（前音與後音聲響重疊期 > 0 ms）
- 物理：刻意延長前指持續時間，使其聲響與後音 attack 重疊
- 音響效果：類似「**和弦感覺的旋律**」，每個音之間幾乎無分割

對指法的意涵：legatissimo 比 legato 更嚴格要求 finger substitution + 重量觸鍵。

## 2. 為什麼相對少被使用

Legatissimo 不是主流標記，原因：
- 鋼琴物理：彈下音後**自然衰減**，純粹「持續按住」也維持不了多久
- 連續 legatissimo 過長 → 音響「**糊**」掉（多音同時響）
- 大多數演奏家把「**很 legato**」當作 legato 的執行品質，不另外標 legatissimo

→ Legatissimo 通常出現在**特殊表情段**（cantabile 高峰、戲劇性 sustained 段），不是常規標記。

## 3. 典型使用情境

⚠ Training-data verification needed:

| 情境 | 例子 |
|---|---|
| **Liszt sustained melody** | 部分 transcendental etudes 的 cantabile 段 |
| **Scriabin late works** | 大量 legatissimo 標記 |
| **Debussy / Ravel impressionist** | 偶見 legatissimo for blurred-edge melody |
| **20 世紀 lyrical 段** | Rachmaninoff Preludes 慢段、Medtner 抒情 |
| **Pedal-assisted lyrical 段** | Pedal + 手指 legatissimo 雙重共鳴 |

## 4. 對指法的特殊要求

執行 legatissimo 比 legato 更嚴格：
- **同音換指必須完美**：substitution 切換瞬間任何不完美都會被聽見（因為前後音響重疊期需 ≥ 1 ms）
- **強指偏好**：4-5 的釋放延遲在 legatissimo 更明顯，應盡量用 1-2-3
- **手位穩定**：legatissimo 段不應有 hand-position 跳動（小動作會破壞極度連續性）

對指法系統的意涵：legatissimo 段應**強化** [concept_legato_substitution](concept_legato_substitution.md) 規則 + 偏好強指 + 限制 hand-jump 比 legato 更嚴。

## 5. 與其他連奏級別的對比

| 級別 | 音長 | 內部空隙 | 使用頻率 |
|---|---|---|---|
| **Legatissimo** | 100% + overlap | -ε（重疊）| 罕見 |
| **Legato** | 100% | 0 | 常見 |
| **Portato** | ~75% | 短 | 中等 |
| **Non-legato (Baroque)** | ~85% | 微 | Baroque default |
| **Detache (Classical short)** | ~70% | 中 | Classical 常見 |

## 6. 對 score-claude DP 的意涵

目前 DP 不區分 legato 與 legatissimo（都當 legato 處理）。理由：
- Legatissimo 罕見，初中階目標曲目幾乎不出現
- 即使出現，按 legato 處理已能達成大部分效果
- 未來如要區分，可：
  - 增加 USE_LEGATISSIMO flag
  - 提高 LEGATO_SAME_PITCH_REPEAT_PENALTY（更嚴格懲罰同指）
  - 提高強指偏好 weight

## 7. 演奏實踐：legatissimo vs pedal 共鳴

[concept_pedaling_vs_articulation](concept_pedaling_vs_articulation.md) 指出 articulation 應由手指做出，不依賴 pedal。但 legatissimo 是**少數需要 pedal 配合**的標記之一：
- 純手指即使完美 substitution，相鄰兩音之間仍有微小 attack 區隔
- Pedal sustain 提供共鳴「填補」此區隔
- 純粹 finger legatissimo + pedal sustain = 真正 legatissimo 效果

對指法的意涵：legatissimo 段 finger substitution + pedal 同時使用是**正確設計**。但不能因有 pedal 就放棄 substitution。

## 8. 與其他 wiki 頁面的關係

- [concept_articulation_overview](concept_articulation_overview.md) §2 — taxonomy 最連端
- [concept_legato_substitution](concept_legato_substitution.md) — legatissimo 對 substitution 規則的更嚴格版本
- [concept_pedaling_vs_articulation](concept_pedaling_vs_articulation.md) — legatissimo 是少數需 pedal 配合的標記
- [src_neuhaus_art_of_piano](src_neuhaus_art_of_piano.md) §2.1 — Neuhaus 對連奏觸鍵極致的論述

## 9. ⚠ Training-data verification queue

- §3 具體作曲家 legatissimo 使用頻率 + 段落例子（Liszt / Scriabin / Debussy）
- §6 score-claude 未來如何 model legatissimo
