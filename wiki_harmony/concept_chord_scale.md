---
concept: "和弦音階對應（Chord-Scale Theory）"
date_created: 2026-06-18
tags: [harmony, chord_scale, improvisation, modes, music_theory]
---

# 和弦音階對應（Chord-Scale Theory）

> 前置知識：[concept_modes — 教會調式](concept_modes.md)（七種調式的結構與特徵音）
> 建議先讀：[concept_seventh_chord — 七和弦](concept_seventh_chord.md)（五種常見七和弦的結構）

你已經認識七種調式，也學會了七和弦的結構。現在要把這兩個知識連起來：**每一個和弦都暗示著一條音階，可以用來寫旋律或即興演奏。** 和弦提供骨架（chord tones），音階填滿縫隙（available tensions）——這就是和弦音階對應理論（chord-scale theory）的核心。

---

## 1. 什麼是和弦音階對應（Chord-Scale Theory）

- **每個和弦都暗示一條音階**：和弦音（chord tones）是「安全」的骨架音，音階則補上剩下的音，提供可用的張力音（available tensions）。
- **目的**：為即興演奏和旋律寫作提供系統化的選音邏輯——看到和弦符號，就知道可以用哪些音。
- **起源**：1950 年代 George Russell 的《Lydian Chromatic Concept of Tonal Organization》是理論先驅，後經 Berklee 音樂學院的爵士教學體系發揚光大，成為現代爵士教育的基石。

> **核心觀念**：和弦音階對應不是「規則」，而是「地圖」。地圖告訴你哪些路可以走，但你不必每條都走。

---

## 2. 大調順階和弦的對應音階

以 C 大調為例，七個順階七和弦各自對應一個調式。這其實就是把你在 [concept_modes](concept_modes.md) 學過的調式，和 [concept_seventh_chord](concept_seventh_chord.md) 學過的順階七和弦對齊：

| 級數 | 和弦 | 對應音階 | 避免音（Avoid Note） |
|------|------|----------|---------------------|
| I | Cmaj7 | C Ionian | F（♮4，與三音 E 形成小二度，聽起來像 sus4） |
| ii | Dm7 | D Dorian | —（無避免音） |
| iii | Em7 | E Phrygian | F（♭2，與根音 E 半音衝突）、C（♭6） |
| IV | Fmaj7 | F Lydian | —（無避免音，#4 是色彩音！） |
| V | G7 | G Mixolydian | C（♮4，與三音 B 形成小二度） |
| vi | Am7 | A Aeolian | F（♭6，視情境而定） |
| vii° | Bm7♭5 | B Locrian | C（♭2，與根音 B 半音衝突） |

**規律**：

- 每個順階和弦對應的音階，**用的都是同一組 C 大調的音**（C D E F G A B），只是起始音不同。
- 這就是調式的實際應用場景：不只是理論上的音階排列，而是告訴你「在這個和弦上，用這些音即興」。

---

## 3. 什麼是避免音（Avoid Note）

避免音是和弦音階對應理論中最重要的概念之一。

### 定義

避免音必須同時滿足兩個條件：

1. **該音階音位於和弦音上方半音處**（即與某個和弦音形成小二度 / ♭9 關係）
2. **該音在弱拍位置持續時，會與和弦產生刺耳的不協和感**

### 為什麼叫「避免音」

它不是「禁止音」——你仍然可以使用它，但需要小心處理：

- 當作**經過音**（passing tone）快速帶過 → 沒問題
- 在**強拍上長時間停留** → 產生不必要的摩擦

### 無避免音的調式最「自由」

| 調式 | 避免音數量 | 即興自由度 |
|------|-----------|-----------|
| Lydian | 0 | 最高——所有音都可以自由使用 |
| Dorian | 0 | 最高——小調型中最好用的即興音階 |
| Ionian | 1（♮4） | 高——只需注意四度音 |
| Mixolydian | 1（♮4） | 高 |
| Aeolian | 1（♭6） | 中——♭6 的衝突較溫和 |
| Phrygian | 2（♭2、♭6） | 低——限制較多 |
| Locrian | 1（♭2） | 最低——和弦本身就不穩定 |

> **這就是為什麼 Dorian 和 Lydian 在爵士即興中特別受歡迎**——沒有避免音，演奏者可以更自由地使用整條音階。

---

## 4. 屬七和弦的多種音階選擇

屬七和弦（dominant 7th）是和弦音階對應中**最靈活的和弦**，因為它可以搭配多種音階，每種帶來不同的色彩與張力程度：

| 音階 | 公式 | 色彩 | 適用場景 |
|------|------|------|----------|
| Mixolydian | 1-2-3-4-5-6-♭7 | 基本、乾淨 | 一般順階屬七（V7） |
| Lydian ♭7 | 1-2-3-#4-5-6-♭7 | 明亮、浮動 | 副屬和弦（V/IV）、三全音代理（♭II7） |
| Altered | 1-♭2-#2-3-♭5-#5-♭7 | 最大張力 | V7 解決到 i 或 I 前的極度緊張 |
| Diminished（H-W） | 1-♭2-#2-3-#4-5-6-♭7 | 對稱、八音音階 | 減和弦經過、爵士即興 |
| Whole Tone | 1-2-3-#4-#5-♭7 | 飄浮、模糊 | 增屬和弦（aug dominant） |

### 選擇邏輯

```
張力低 ──────────────────────────────────→ 張力高

Mixolydian → Lydian ♭7 → Diminished → Altered
  (最安全)    (浮動感)    (對稱色彩)    (最大緊張)
```

- **不確定用哪個？** → 先用 Mixolydian，永遠安全。
- **想要更多色彩？** → 往右移動，張力逐漸增加。
- **V7 要解決到 I？** → Altered 音階提供最大的解決感，因為所有延伸音都是變化音（♭9、#9、♭5、#5）。

> Whole Tone 音階較特殊：它是六音對稱音階（每個音之間都是全音），產生「無方向感」的漂浮效果，Debussy 和 Thelonious Monk 都愛用。

---

## 5. 小調的和弦音階對應

小調系統比大調複雜，因為小調有三種常用音階，各自衍生不同的順階和弦：

### 自然小調（Natural Minor）

和大調的對應邏輯完全相同，只是從第 vi 級開始：

- A 自然小調 = A Aeolian，用的就是 C 大調的音群
- 順階和弦的音階對應和大調是同一套，只是起始級數不同

### 和聲小調（Harmonic Minor）

和聲小調升高了第七音，產生了獨特的音階選項：

- **V7 → 使用和聲小調主音起算的音階**（即 Phrygian Dominant / 西班牙音階 = 1-♭2-3-4-5-♭6-♭7）
- 這條音階有強烈的異國風味（♭2 和大三度的組合），常見於佛朗明哥和中東音樂

### 旋律小調（Melodic Minor）

旋律小調（上行：1-2-♭3-4-5-6-7）是爵士音階的寶庫，衍生出許多重要音階：

| 級數 | 衍生音階 | 用途 |
|------|----------|------|
| I | Melodic Minor | 小大七和弦（mMaj7） |
| II | Dorian ♭2 | sus♭9 和弦 |
| III | Lydian Augmented | maj7#5 和弦 |
| IV | Lydian ♭7（= Lydian Dominant） | 副屬和弦、三全音代理 |
| V | Mixolydian ♭6 | V7 帶 ♭13 |
| VI | Locrian ♮2（= Half-Diminished） | 半減七和弦 |
| VII | Altered（= Super Locrian） | 變化屬七和弦 |

> 注意第 IV 級和第 VII 級——**Lydian ♭7 和 Altered 都來自旋律小調**。這是爵士理論的核心連結。

---

## 6. 實際運用：即興的思考流程

當你拿到一份和弦譜（lead sheet），即興時的思考步驟：

### 步驟

1. **看和弦符號** — 辨認和弦類型（maj7? m7? 7? m7♭5?）
2. **判斷功能** — 這個和弦在調性中扮演什麼角色？
   - 順階和弦？→ 直接用該級的調式
   - 副屬和弦（secondary dominant）？→ Mixolydian 或 Lydian ♭7
   - 三全音代理（tritone substitution）？→ Lydian ♭7
   - V7 解決到小調？→ Altered 或 Phrygian Dominant
3. **選擇對應音階** — 根據功能和你想要的色彩做選擇
4. **演奏時的優先順序** — 強拍用和弦音，弱拍用音階音連接

### 範例：Dm7 – G7 – Cmaj7（ii-V-I in C Major）

```
Dm7        →  D Dorian（D E F G A B C）
G7         →  G Mixolydian（G A B C D E F）
               或 G Altered（G A♭ B♭ B D♭ E♭ F）想要更多張力時
Cmaj7      →  C Ionian（C D E F G A B），注意 F 是避免音
```

---

## 7. 口訣

記住這三條，足以應付大部分情況：

> **順階和弦 → 直接用該級的調式**
> **屬七 → Mixolydian 是預設，想要更多張力就往 Altered 方向走**
> **不確定？→ 先用和弦琶音（chord tones），最安全**

和弦琶音永遠是你的安全網——當你不確定要用什麼音階時，只彈和弦的組成音（1-3-5-7），絕對不會出錯。音階是在這個基礎上的延伸。

---

## 8. 常見誤解

| 誤解 | 澄清 |
|------|------|
| 「每個和弦只能用一種音階」 | 不對。尤其屬七和弦可搭配多種音階，選擇取決於你想要的色彩。 |
| 「避免音絕對不能彈」 | 避免音不是禁止音，快速帶過或當作張力源都可以。 |
| 「和弦音階理論是唯一的即興方法」 | 它只是工具之一。許多偉大的即興演奏者更依賴耳朵、動機發展、和弦琶音等方法。 |
| 「學了音階就會即興」 | 音階是素材，不是音樂。真正的即興還需要節奏感、樂句邏輯和大量聆聽。 |

---

## 9. 小測驗

試著回答以下問題（答案在下方）：

1. 和弦音階對應理論的核心觀念是什麼？用一句話說明。
2. C 大調中，ii 級和弦 Dm7 對應哪條音階？該音階有幾個避免音？
3. 為什麼 Lydian 和 Dorian 被認為是即興中最「自由」的調式？
4. C Ionian 的避免音是哪個音？為什麼它會造成衝突？
5. 列出屬七和弦可搭配的五種音階，並依張力從低到高排列。
6. V7 要解決到小調主和弦時，最常用哪條音階？
7. 旋律小調的第 VII 級衍生出什麼音階？它用在什麼場景？
8. 看到 ii-V-I 進行（Dm7 – G7 – Cmaj7），請寫出每個和弦最基本的對應音階。
9. 和聲小調中的 V7 使用什麼音階？這條音階有什麼特殊的聽感？
10. 即興時，如果不確定要用什麼音階，最安全的策略是什麼？

---

### 答案

1. **每個和弦都暗示一條音階**——和弦音提供骨架，音階補上剩餘的音作為可用的張力音（available tensions）。
2. **D Dorian（D E F G A B C）。零個避免音**——Dorian 是小調型中最自由的即興音階，所有音階音都可以放心使用。
3. **因為它們沒有避免音**——Lydian 的 #4 和 Dorian 的 ♮6 都不會與和弦音形成小二度衝突，所有音階音都可以自由使用。
4. **F（♮4）**——F 與三音 E 只差半音（小二度），在強拍上長時間停留會讓和弦聽起來像 sus4，模糊大和弦的性格。
5. **Mixolydian（最低）→ Lydian ♭7 → Diminished（H-W）→ Altered（最高）**。Whole Tone 較特殊，張力介於 Lydian ♭7 和 Altered 之間。
6. **Altered 音階（= Super Locrian）**——所有延伸音都是變化音（♭9、#9、♭5、#5），提供最大的緊張感，解決到主和弦時對比最強烈。
7. **Altered 音階（Super Locrian）**——用在變化屬七和弦上，特別是 V7 解決前需要最大張力的場景。
8. **Dm7 → D Dorian（D E F G A B C），G7 → G Mixolydian（G A B C D E F），Cmaj7 → C Ionian（C D E F G A B）**。三條音階其實用的是同一組音！
9. **Phrygian Dominant（西班牙音階，1-♭2-3-4-5-♭6-♭7）**——♭2 和大三度的結合產生強烈的異國風味，常見於佛朗明哥和中東音樂。
10. **先用和弦琶音（chord tones：1-3-5-7）**——只彈和弦的組成音絕對不會出錯，音階是在和弦琶音基礎上的延伸。

---

## 下一步

即興分支至此完成。以下頁面可交叉參考：

- [concept_tritone_substitution — 三全音代理](concept_tritone_substitution.md) — ♭II7 代理上的音階選擇（Lydian ♭7）
- [concept_symmetric_scales — 對稱音階](concept_symmetric_scales.md) — 減音階、全音音階的和弦對應

## 延伸參考

- [concept_modes — 教會調式](concept_modes.md) — 和弦音階對應的調式基礎
- [concept_pentatonic_blues — 五聲音階與藍調](concept_pentatonic_blues.md) — 五聲音階在即興中的萬用性
- [concept_non_functional_harmony — 非功能和聲](concept_non_functional_harmony.md) — 調式和聲中的和弦選擇思維
- [concept_seventh_chord — 七和弦](concept_seventh_chord.md) — 和弦音階對應以七和弦為基本單位
- [concept_overtone_series — 泛音列與聲學](concept_overtone_series.md) — 和弦音階選擇背後的聲學基礎：頻率比與協和度（§3）
