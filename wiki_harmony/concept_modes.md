---
concept: "教會調式（Church Modes）"
date_created: 2026-06-18
tags: [harmony, modes, scale, music_theory]
---

# 教會調式（Church Modes）

> 前置知識：[concept_scale_and_key — 音階與調性](concept_scale_and_key.md)（大調/小調音階、全音半音排列）
> 建議先讀：[concept_interval — 音程基礎](concept_interval.md)

大調和小調是最常見的兩種音階，但它們只是七種調式中的兩種。調式（mode）的概念源自中世紀教會音樂，至今在爵士、電影配樂、遊戲音樂、流行樂中廣泛使用。

---

## 1. 什麼是調式（Mode）

用 C 大調的七個白鍵（C D E F G A B）來解釋：

- 從 **C** 開始彈到 C → C 大調（Ionian）
- 從 **D** 開始彈到 D → 聽感完全不同，雖然用的是同一組白鍵

**同樣七個音，起始音不同 → 全音/半音的排列順序改變 → 音階的「味道」不同。**

這就是調式的核心：七個音有七種排列方式，每種就是一個調式。

---

## 2. 七種調式一覽

以下用 C 大調白鍵為例，展示七種調式的全半音排列。**這只是為了方便觀察——每種調式都能移到任何根音上（見 §4.5）。**

| # | 調式名 | 起始音 | 音階 | 全半音公式 |
|---|--------|--------|------|-----------|
| I | Ionian（伊奧尼安） | C | C D E F G A B | W-W-H-W-W-W-H |
| II | Dorian（多利安） | D | D E F G A B C | W-H-W-W-W-H-W |
| III | Phrygian（弗里吉亞） | E | E F G A B C D | H-W-W-W-H-W-W |
| IV | Lydian（利底亞） | F | F G A B C D E | W-W-W-H-W-W-H |
| V | Mixolydian（混合利底亞） | G | G A B C D E F | W-W-H-W-W-H-W |
| VI | Aeolian（艾奧利安） | A | A B C D E F G | W-H-W-W-H-W-W |
| VII | Locrian（洛克里安） | B | B C D E F G A | H-W-W-H-W-W-W |

> **Ionian = 大調，Aeolian = 自然小調。** 你已經學過兩種了！

---

## 3. 記憶法：大調的「旋轉」

七種調式的公式，其實就是大調公式 **W-W-H-W-W-W-H** 的旋轉：

```
Ionian:     W-W-H-W-W-W-H    ← 大調原型
Dorian:     W-H-W-W-W-H-W    ← 從第 2 個開始讀
Phrygian:   H-W-W-W-H-W-W    ← 從第 3 個開始讀
Lydian:     W-W-W-H-W-W-H    ← 從第 4 個開始讀
Mixolydian: W-W-H-W-W-H-W    ← 從第 5 個開始讀
Aeolian:    W-H-W-W-H-W-W    ← 從第 6 個開始讀（自然小調）
Locrian:    H-W-W-H-W-W-W    ← 從第 7 個開始讀
```

不需要背七條公式——**只要記住大調公式，從不同位置開始讀就好。**

---

## 4. 兩種思考方式：相對法 vs 平行法

### 相對法（Relative）

「D Dorian 用的是 C 大調的音」——找到母調（parent key），借用它的音。

| 調式 | 找母調的方法 |
|------|------------|
| Dorian | 根音下方大二度的大調（D Dorian → C 大調） |
| Phrygian | 根音下方大三度的大調（E Phrygian → C 大調） |
| Lydian | 根音下方完全四度的大調（F Lydian → C 大調） |
| Mixolydian | 根音下方完全五度的大調（G Mixolydian → C 大調） |
| Aeolian | 根音上方小三度的大調（A Aeolian → C 大調） |
| Locrian | 根音上方半音的大調（B Locrian → C 大調） |

### 平行法（Parallel）——推薦！

把每種調式和**同根音的大調或自然小調**比較，只看差了哪些音。

> 此處「小調」皆指**自然小調（Aeolian）**，不是和聲小調。和聲小調的升第 7 音是為了 V→i 解決力而做的改動，不屬於調式系統。

| 調式 | 與大調比較 | 特徵音 | 聽感關鍵字 |
|------|----------|--------|-----------|
| Ionian | = 大調 | （無差異） | 明亮、標準 |
| Dorian | 自然小調 + ♮6 | **升六度**（比自然小調亮） | 柔和、帶希望的小調 |
| Phrygian | 自然小調 + ♭2 | **降二度**（開頭就暗） | 西班牙、阿拉伯、緊張 |
| Lydian | 大調 + #4 | **升四度**（夢幻飄浮） | 幻想、太空、電影開場 |
| Mixolydian | 大調 + ♭7 | **降七度**（少了導音張力） | 藍調、搖滾、鄉村 |
| Aeolian | = 自然小調 | （無差異） | 憂鬱、暗沉 |
| Locrian | 自然小調 + ♭2 + ♭5 | **減五度**（不穩定的根基） | 極度不安、幾乎不單獨使用 |

> **每種調式只差一個音！** Dorian 就是「自然小調但第 6 音不降」，Lydian 就是「大調但第 4 音升半音」。這是最快的記法。

---

## 4.5 調式不限於白鍵——移調到任何根音

前面的例子都用 C 大調白鍵，是為了讓「旋轉」的概念最直觀。但調式可以建立在**任意根音**上，包含黑鍵調。方法有兩種：

### 方法一：平行法（推薦）

從同根音的大調或小調出發，改一個音：

| 目標調式 | 步驟 | 結果 |
|---------|------|------|
| **E♭ Dorian** | E♭ 自然小調（E♭ F G♭ A♭ B♭ C♭ D♭）→ 第 6 音升半音（C♭ → C♮） | E♭ F G♭ A♭ B♭ **C** D♭ |
| **B♭ Lydian** | B♭ 大調（B♭ C D E♭ F G A）→ 第 4 音升半音（E♭ → E♮） | B♭ C D **E** F G A |
| **A Mixolydian** | A 大調（A B C# D E F# G#）→ 第 7 音降半音（G# → G♮） | A B C# D E F# **G** |
| **F# Phrygian** | F# 自然小調（F# G# A B C# D E）→ 第 2 音降半音（G# → G♮） | F# **G** A B C# D E |

### 方法二：相對法

找到母調，借用它的全部音：

| 目標調式 | 母調 | 驗證 |
|---------|------|------|
| **E♭ Dorian** | 根音下方大二度 → D♭ 大調（D♭ E♭ F G♭ A♭ B♭ C） | 從 E♭ 開始讀 ✓ |
| **B♭ Lydian** | 根音下方完全四度 → F 大調（F G A B♭ C D E） | 從 B♭ 開始讀 ✓ |
| **A Mixolydian** | 根音下方完全五度 → D 大調（D E F# G A B C#） | 從 A 開始讀 ✓ |

> **兩種方法得出的結果永遠一樣。** 平行法適合即時思考（「小調改一個音」），相對法適合看譜分析（「這些升降記號是哪個大調的？」）。

---

## 5. 各調式的順階和弦

以 C 為根音的平行調式，各級順階三和弦：

### 大調型（根音上方是大三度）

| 級數 | C Ionian（大調） | C Lydian（#4） | C Mixolydian（♭7） |
|------|-----------------|---------------|-------------------|
| I | **C**（大） | **C**（大） | **C**（大） |
| ii | Dm（小） | Dm（小） | Dm（小） |
| iii | Em（小） | Em（小） | Em（小）→ E♭（大）* |
| IV | F（大） | **F#dim**（減）★ | F（大） |
| V | G（大） | G（大） | Gm（小）★ |
| vi | Am（小） | Am（小） | Am（小）→ A♭（大）* |
| vii° | Bdim（減） | Bm（小）★ | **B♭**（大）★ |

★ = 與 Ionian 不同的和弦（特徵音造成的差異）

### 小調型（根音上方是小三度）

| 級數 | C Aeolian（自然小調） | C Dorian（♮6） | C Phrygian（♭2） |
|------|---------------------|---------------|-----------------|
| i | Cm（小） | Cm（小） | Cm（小） |
| ii° / ii | Ddim（減） | Dm（小）★ | D♭（大）★ |
| III | E♭（大） | E♭（大） | E♭（大） |
| iv | Fm（小） | Fm（小） | Fm（小） |
| v | Gm（小） | Gm（小） | Gm（小） |
| VI | A♭（大） | **A**（大）★ | A♭（大） |
| VII | B♭（大） | B♭（大） | B♭（大） |

★ = 與 Aeolian 不同的和弦

> **Locrian** 因為 I 級本身就是減三和弦（不穩定），幾乎不被當作獨立調式使用，這裡省略。

---

## 6. 各調式的代表曲風與範例

| 調式 | 常見場景 | 知名範例 |
|------|---------|---------|
| Ionian | 古典、流行、兒歌 | 大部分流行歌曲 |
| Dorian | 爵士、放克、遊戲 | *So What*（Miles Davis）、*Scarborough Fair* |
| Phrygian | 佛朗明哥、金屬、中東風 | 西班牙吉他即興 |
| Lydian | 電影配樂、夢幻場景 | *E.T.* 主題（John Williams） |
| Mixolydian | 藍調搖滾、鄉村、凱爾特 | *Norwegian Wood*（Beatles） |
| Aeolian | 抒情、悲傷、史詩 | 大部分小調抒情曲 |
| Locrian | 重金屬 riff（短暫使用） | 極少單獨使用 |

---

## 7. 如何判斷一段音樂的調式

1. **找到調號**：確定用了哪七個音（= 哪個大調的音群）
2. **找到主音**（tonal center）：旋律不斷回到、結束在哪個音？和聲不斷解決到哪個和弦？
3. **主音 + 音群 → 調式**：例如用 C 大調的音群，但主音是 D → D Dorian

> **關鍵不在你用了哪些音，而在哪個音聽起來像「家」。**

---

## 8. 調式與大/小調的關係總結

```
亮 ←──────────────────────────────→ 暗

Lydian  Ionian  Mixolydian  Dorian  Aeolian  Phrygian  Locrian
  #4     大調      ♭7        ♮6      小調      ♭2      ♭2♭5
         ===                                    ===
       最常見                                 最常見
```

- 左邊三個是「大調型」（根音到三音 = 大三度）
- 右邊四個是「小調型」（根音到三音 = 小三度）
- 從左到右，聽感從最亮到最暗
- 每往右一步，就多降一個音

---

## 9. 小測驗

試著回答以下問題（答案在下方）：

1. D Dorian 調式使用哪個大調的音群？寫出 D Dorian 的七個音。
2. Lydian 調式與大調只差一個音，是哪個音？它讓聽感產生什麼變化？
3. G Mixolydian 的音階是什麼？它和 G 大調差在哪裡？
4. 七種調式中，哪兩種等同於我們已經學過的大調和自然小調？
5. 一段旋律用了 B♭大調的音群（B♭ C D E♭ F G A），但主音聽起來是 G。這是什麼調式？
6. 從亮到暗排列，Dorian 排在 Mixolydian 的哪一邊（更亮還是更暗）？
7. Phrygian 調式的特徵音是什麼？它常見於哪種音樂風格？
8. C Lydian 的第 IV 級順階三和弦是什麼？為什麼和 C 大調不同？
9. Locrian 調式幾乎不單獨使用，原因是什麼？
10. A Dorian 和 A Aeolian（自然小調）只差一個音。是哪個音？寫出兩種音階做比較。

---

### 答案

1. **C 大調的音群。D E F G A B C** — Dorian 從大調的第 II 級開始，D 的母調是 C 大調。
2. **第 4 音升半音（#4）** — 例如 C Lydian 的 F 變成 F#。升四度消除了完全四度的「重力感」，產生漂浮、夢幻的效果。
3. **G A B C D E F G** — 和 G 大調（G A B C D E F# G）相比，第 7 音從 F# 降為 F（♭7）。少了導音 F#→G 的半音張力，聽感更放鬆、帶藍調味。
4. **Ionian = 大調，Aeolian = 自然小調** — 它們分別是調式系統的第 I 和第 VI 調式。
5. **G Aeolian（G 自然小調）** — B♭大調的音群從 G 開始 = G Aeolian。G 自然小調的關係大調就是 B♭大調。
6. **更暗** — 亮到暗排列：Lydian → Ionian → Mixolydian → **Dorian** → Aeolian → Phrygian → Locrian。Dorian 是小調型，Mixolydian 是大調型，所以 Dorian 在右邊（更暗）。
7. **降二度（♭2）** — 音階一開始就是半音（E→F），帶有強烈的西班牙/阿拉伯色彩，常見於佛朗明哥和金屬樂。
8. **F#dim（減三和弦）** — C Lydian 的第 4 音是 F#（不是 F），所以 IV 級 = F#-A-C = 減三和弦，而 C 大調的 IV 級 = F-A-C = 大三和弦。特徵音 #4 直接改變了這個和弦的性質。
9. **I 級和弦是減三和弦（不穩定）** — 例如 B Locrian 的 I 級 = B-D-F = Bdim。減三和弦聽起來不像「家」，無法建立穩定的主和弦感，所以幾乎不能作為獨立調式使用。
10. **第 6 音：A Dorian 有 F#，A Aeolian 有 F** — A Dorian = A B C D E **F#** G，A Aeolian = A B C D E **F** G。Dorian 的升六度讓它比普通小調多一分溫暖和希望感。

---

## 下一步

- [concept_pentatonic_blues — 五聲音階與藍調](concept_pentatonic_blues.md) — 另一種「不是大調也不是小調」的音階系統
- [concept_chord_scale — 和弦音階對應](concept_chord_scale.md) — 每個順階和弦對應哪個調式？即興的起點
- [concept_non_functional_harmony — 非功能和聲](concept_non_functional_harmony.md) — 調式和聲：不靠 V→I 驅動的和弦用法

## 延伸參考

- [concept_triad — 三和弦](concept_triad.md) — 各調式順階和弦的基礎結構
- [concept_symmetric_scales — 對稱音階](concept_symmetric_scales.md) — 全音、減音階等超越七聲框架的特殊音階
- [concept_scale_and_key — 音階與調性](concept_scale_and_key.md) — 回顧大調 / 小調基礎
