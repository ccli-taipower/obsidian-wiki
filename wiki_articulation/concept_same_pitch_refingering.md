# Concept: Same-Pitch Refingering — 同音換指四動機總覽

> 來源：彙整自下列既有 concept 頁；新增動機 B 見 [concept_dynamic_shaping_refingering](concept_dynamic_shaping_refingering.md)
> 引用方：[concept_articulation_overview](concept_articulation_overview.md)、[index](index.md)

「同音換指」（同一音高用不止一根手指）在鋼琴上其實是**兩種物理上不同的現象**、由**四種動機**驅動。本頁是 taxonomy 與導航中心 —— 各動機的完整內容在所連頁面，本頁只負責**區分與索引**，不複製。

## 1. 兩種物理現象（先分清）

| | 持鍵換指 (held substitution) | 重彈換指 (re-struck refingering) |
|---|---|---|
| 鍵 | **按著不放**，手指靜默交替 | **放掉再彈**，每音獨立 attack |
| 重新發聲 | 否（不 re-attack）| 是（每音都 attack）|
| 樂譜 | 通常單一持音 + slur | 通常寫成多個同音音符 |
| 典型動機 | A（legato）、C（換手位準備）| B（強弱塑形）、D（重複音技術）|

→ 同一個「同音換指」字眼下，持鍵與重彈是**不同技術**；混為一談會導致規則套錯（如把重彈的 4-3-2-1 當成 legato substitution）。物理區分詳見 [../wiki_piano/concept_repeated_note_fingering §4](../wiki_piano/concept_repeated_note_fingering.md)。

## 2. 四動機

### A — Legato 維持（持鍵）
旋律線在同音上要維持 legato，**必須**靜默換指（前指還按、後指接住、前指鬆），否則 audibly broken。自 18 世紀末為標準教學（Neuhaus、Matthay、Czerny、Türk）。
→ 完整內容：[concept_legato_substitution](concept_legato_substitution.md)

### B — 強弱塑形（重彈）
重複/交替音型中刻意把強拍配強指、弱拍配弱指，讓節拍輪廓從指法力度差浮現（C.P.E. Bach gute/schlechte Noten、Couperin inégalité）。**四動機中唯一未模、且現代有爭議**（重量學派反對依賴手指力度差）。
→ 完整內容：[concept_dynamic_shaping_refingering](concept_dynamic_shaping_refingering.md)（本批新增）

### C — 樂句過渡 / 換手位準備（持鍵或重彈）
在樂句邊界或位置轉換前換指，為**下一句的手位**鋪路（Czerny 的「預備性換指」）。同一音型在不同 entry context 因此可有不同指法 —— 這正是「同音型同指」的細則（per motif × entry context，不是 per motif 單獨）。
→ 完整內容：[concept_legato_substitution §4 預備性換指](concept_legato_substitution.md)；entry-context 觀點見 [../wiki_phrase/index](../wiki_phrase/index.md)

### D — 重複音技術（重彈）
快速重複同音用輪指（3-2-1 / 4-3-2-1）求**均勻、速度、抗疲勞**（鋼琴 action 需 reset，同指彈不快）。Liszt *La Campanella* 為代表。方向與 B **相反**（D 求均勻、B 求不均）。
→ 完整內容：[../wiki_piano/concept_repeated_note_fingering](../wiki_piano/concept_repeated_note_fingering.md)

## 3. 黑白鍵：橫切修正因子（非第五動機）

鍵色不構成「換不換指」的動機，但**修正換哪根指**：
- 拇指避免落黑鍵（黑鍵較高較內，拇指落黑鍵姿勢不利；Parncutt Rule 11，見 [../wiki_piano/concept_piano_fingering_principles](../wiki_piano/concept_piano_fingering_principles.md)）
- 同音重複序列若該音是黑鍵，輪指偏好把長指（2/3）留給它、避免 4/5 在黑鍵的尷尬伸展
- 在 A/B/C/D 任一動機決定「要換指」之後，鍵色才介入決定**具體指序**

→ 因此黑白鍵是套在四動機之上的 filter，不與它們並列。

## 4. 與「同音型同指」HARD 原則的關係

score-claude 的核心 HARD 原則是**同音型同指**（same-MOTIF → same-fingering），常被誤讀為「同音同指」（same-pitch → same-finger）。本頁四動機正說明兩者不衝突：
- 「同音型同指」要求的是**跨出現**一致（同一音型在 m4 與 m12 用同一套指序）
- 動機 A/B/C/D 都是**單次出現內**的換指（一個音型內部用多指）
- 兩者正交：一串 `3-5-2-5`（B 動機，單次內多指）若在曲中重複出現，同音型同指要求兩次都用 `3-5-2-5`

→ 真正的細則是 C 指出的：同音型同指運作於 **(motif × entry context)**；不同 entry 容許不同指法。

## 5. 與其他 wiki 頁面的關係

- [concept_articulation_overview](concept_articulation_overview.md) — articulation taxonomy 母頁
- [concept_legato_substitution](concept_legato_substitution.md) — 動機 A（+ C 的預備性換指）
- [concept_dynamic_shaping_refingering](concept_dynamic_shaping_refingering.md) — 動機 B（新增）
- [concept_tenuto](concept_tenuto.md) — **禁止**同音換指的情境（tenuto 強制 hold 此指）
- [concept_accent_marcato](concept_accent_marcato.md) — 顯式 accent 的強指偏好（B 的有標記近親）
- [../wiki_piano/concept_finger_substitution](../wiki_piano/concept_finger_substitution.md) — substitution 的生物力學/技巧面
- [../wiki_piano/concept_repeated_note_fingering](../wiki_piano/concept_repeated_note_fingering.md) — 動機 D
