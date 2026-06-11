# Concept: Dynamic-Shaping Refingering — 為強弱塑形而換指

> 來源：C.P.E. Bach *Versuch* (1753) §gute/schlechte Noten、Couperin *L'Art de toucher* (1716) §inégalité、Czerny *Op.500* §accentuation、Kullak *Die Ästhetik des Klavierspiels* §nuance、Neuhaus *The Art of Piano Playing* §weight；現代反方見 Taubman / Roskell（[../wiki_piano/concept_weak_finger_development](../wiki_piano/concept_weak_finger_development.md)）
> 引用方：[concept_same_pitch_refingering](concept_same_pitch_refingering.md)（動機 B）、[concept_accent_marcato](concept_accent_marcato.md)

同一音高在重複或交替音型中，**刻意分配不同強度的手指**，讓節拍重音自然落在強指、弱拍落在弱指 —— 用手指力度差直接刻出「強-弱-次強-弱」的韻律，而不是靠每一音的意識性力度控制。這是 [concept_same_pitch_refingering](concept_same_pitch_refingering.md) 四動機中**唯一目前 score-claude 完全未模、且文獻上仍有爭議**的一條。

## 1. 現象

例：一小節四個重複的 C5（4/4 拍，強-弱-次強-弱）

- 單指彈：`5-5-5-5` → 四音力度均等，無節拍輪廓
- 強弱換指：`3-5-2-5`（或 `2-4-3-5`）→ 強拍落強指（2/3）、弱拍落弱指（5/4）→ 節拍重音**從指法本身浮現**

關鍵：這是「重彈換指」(re-struck)，不是持鍵 substitution；每一音都有獨立 attack（與 [concept_legato_substitution](concept_legato_substitution.md) 的持鍵靜默換指物理上不同）。

## 2. 老派依據：強拍弱拍 × 手指力度

### C.P.E. Bach《Versuch》— gute / schlechte Noten
C.P.E. Bach 把拍子分為「好音 (gute Noten / 內在強拍)」與「壞音 (schlechte Noten / 弱拍)」，主張演奏應讓兩者**自然有別**。配合鍵盤手指力度的天生不對稱，把好音交給強指是達成此區別的直接手段。見 [src_cpe_bach_versuch](src_cpe_bach_versuch.md)。

### Couperin《L'Art de toucher》— inégalité
法國 Baroque 的 *notes inégales*（不均等）傳統，要求成對音中第一個略長略重。指法選擇（強指落第一音）是實踐 inégalité 的常見手段之一。見 [src_couperin_lart_de_toucher](src_couperin_lart_de_toucher.md)。

### Czerny《Op.500》§accentuation + Kullak §nuance
19 世紀教學把「重音落於有利手指」視為清晰 accentuation 的條件。Kullak《美學》進一步把這種**透過指法分配達成的微觀 nuance** 列為表現力的一部分。

### 手指力度不對稱（生物力學底）
f2/f3 由獨立屈肌驅動、相對有力；f4 受 *juncturae tendinum* 與 f3/f5 連動、最弱；f1（拇指）強但運動軸不同；f5 短弱但可由手臂支撐。詳 [../wiki_piano/concept_hand_anatomy](../wiki_piano/concept_hand_anatomy.md)、[../wiki_piano/concept_finger_independence](../wiki_piano/concept_finger_independence.md)。→ 強拍配 2/3、弱拍配 4/5 的對應有解剖學基礎。

## 3. 現代反方：手臂重量 vs 手指力度

⚠ 這一條是**爭議點，非共識**（不同於動機 A 的 legato 必要性）。

20 世紀以降的重量／協調學派（Taubman、Roskell、Sandor 一脈）**反對**以手指力度差作為動態來源：
- 主張動態應由**手臂重量 + 落鍵速度**控制，手指只是傳力末端
- 刻意「弱指彈弱音」被視為強化手指不均、阻礙 finger independence 訓練
- 詳 [../wiki_piano/concept_weak_finger_development](../wiki_piano/concept_weak_finger_development.md)

→ 因此 dynamic-shaping refingering 在現代教學中**不是普世規則**，而是：
1. 在**高速**段落，手臂逐音調整來不及時，指法分配是唯一可行的微觀重音手段
2. 在**古樂 inégalité / Classical 風格**詮釋中作為 stylistic 選項
3. 進階者刻意運用，初學者多被勸阻（以免依賴力度差）

## 4. 與 accent / marcato 的區別

[concept_accent_marcato](concept_accent_marcato.md) 已有「accented 音偏好強指」規則 —— 但那是針對**樂譜明確標記**的 accent（`>` / `^` / `sfz`）。本頁是針對**無標記的隱性節拍重音**（metric stress）。

| | accent / marcato | dynamic-shaping refingering |
|---|---|---|
| 觸發 | 樂譜顯式 accent 符號 | 隱性拍子強弱（無符號）|
| 範圍 | 單一被標音 | 重複/交替音型整串的輪廓 |
| 確定性 | 高（譜上寫了）| 低（詮釋性、風格相依）|

## 5. 操作型訊號（若未來建模）

dynamic-shaping refingering 的候選觸發條件：
- 重複同音 ≥ 3，或同音佔主的交替音型
- 落在有明確 metric hierarchy 的拍號（4/4、3/4 強-弱-弱…）
- 非快到無法換指、也非 Baroque perpetual-motion non-legato（那裡均勻才對）
- 風格傾向支持 inégalité / cantabile inflection

滿足時：強拍位置偏好強指（2/3/1）、弱拍位置偏好弱指（4/5），形成週期性指法輪廓。

## 6. 對 score-claude DP 的意涵

**目前未模。** 這會是 DP 第一個**刻意偏離「最省力指法」**的軸 —— cost function 至今最小化費力，而本動機要求**為表現而選非最省力手指**。因此：
- 它不能只是又一條 effort cost，而是一個**表現層偏好**（類似 [../wiki_piano/concept_musical_fingering](../wiki_piano/concept_musical_fingering.md) 的「指法即詮釋」立場）
- 因爭議性（§3）+ 風格相依，若實作必為 **opt-in、預設 OFF**，且需 metric-hierarchy 偵測
- 列為 candidate，未實作；與動機 D（[../wiki_piano/concept_repeated_note_fingering](../wiki_piano/concept_repeated_note_fingering.md) 的速度/均勻導向）方向**不同甚至相反**（D 求均勻、B 求不均）

## 7. 與其他 wiki 頁面的關係

- [concept_same_pitch_refingering](concept_same_pitch_refingering.md) — 本頁的 parent（四動機總覽，動機 B）
- [concept_accent_marcato](concept_accent_marcato.md) — 顯式 accent 的強指偏好（本頁的「有標記版」）
- [../wiki_piano/concept_repeated_note_fingering](../wiki_piano/concept_repeated_note_fingering.md) — 動機 D，求均勻速度，與本頁方向相反
- [../wiki_piano/concept_hand_anatomy](../wiki_piano/concept_hand_anatomy.md) — 手指力度不對稱的解剖學
- [../wiki_piano/concept_weak_finger_development](../wiki_piano/concept_weak_finger_development.md) — 現代反方（弱指應訓練至均勻，非利用其弱）
- [../wiki_piano/concept_musical_fingering](../wiki_piano/concept_musical_fingering.md) — 「指法即詮釋」的上位立場
