# wiki_harmony Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a 24-page Obsidian wiki (`wiki_harmony/`) covering chord theory from intervals to modulation, with 13 dictionary-style chord reference pages, targeting piano beginners.

**Architecture:** Two page types — concept pages (learning path, `concept_` prefix) and chord reference pages (dictionary lookup, `chord_` prefix). Concept pages link to chord pages via `[[chord_*]]`. All pages use Obsidian-flavoured markdown with YAML frontmatter. 中英混用 language style matching existing `wiki_piano`.

**Tech Stack:** Obsidian markdown, Wikilinks (`[[]]`), YAML frontmatter

**Spec:** `docs/superpowers/specs/2026-06-16-wiki-harmony-design.md`

---

## Conventions

**Frontmatter template** for every page:

```yaml
---
concept: "概念中文名（English Name）"   # concept pages
# or
chord_type: "和弦中文名（English Name）"  # chord pages
date_created: 2026-06-16
tags: [harmony, ...]
---
```

**Chord reference page template** — every `chord_*.md` follows this structure:

```markdown
# 和弦中文名（English Name）

## 組成

- 結構公式：1-3-5
- 音程堆疊：大三度 + 小三度

## 12 調列表

| 根音 | 組成音 | 鍵盤位置 |
|------|--------|----------|
| C    | C-E-G  | `●··●··●·····` |

（鍵盤示意用 13 字元代表 C 到 B 的 12 個半音 + 高八度 C，● = 按下，· = 不按。
  位置對應：C C# D D# E F F# G G# A A# B C'
  例：C major = ●··· ●·· ●··· ●  → 簡化為 ●···●··●·····）

## 轉位

## 常見用法

## 鍵盤應用

→ 指法詳見 [[../wiki_piano/concept_chord_fingering|和弦指法]]

## 聽覺特徵
```

**Cross-wiki links** use relative paths: `[[../wiki_piano/concept_chord_fingering|和弦指法]]`

---

## Task 1: 目錄建立 + concept_interval.md（音程）

**Files:**
- Create: `wiki_harmony/` directory
- Create: `wiki_harmony/concept_interval.md`

- [ ] **Step 1: Create directory**

```bash
mkdir -p wiki_harmony
```

- [ ] **Step 2: Write concept_interval.md**

完整內容。涵蓋：

1. **半音與全音** — 鍵盤上相鄰兩鍵 = 半音（semitone），兩個半音 = 全音（whole tone）。用 C-C# 和 C-D 舉例，配鍵盤示意。
2. **音程度數** — 度（度數 = 音名距離 + 1）：一度到八度，每個附鍵盤上的距離（半音數）。
3. **音程性質** — 完全（P1/P4/P5/P8）、大/小（M2/m2, M3/m3, M6/m6, M7/m7）、增/減。用表格列出所有基本音程的半音數。
4. **協和與不協和** — 完全協和（P1/P5/P8）、不完全協和（M3/m3/M6/m6）、不協和（M2/m2/M7/m7/tritone）。
5. **音程轉位** — 翻轉後度數相加 = 9，性質互換（大↔小、增↔減、完全→完全）。
6. **為什麼學音程** — 它是和弦的積木，每個和弦 = 音程的堆疊。預告 [[concept_triad]]。

語言：中英混用，所有術語首次出現附英文。面向初學者，用鍵盤距離解釋，避免五線譜。

- [ ] **Step 3: Commit**

```bash
git add wiki_harmony/concept_interval.md
git commit -m "wiki_harmony: concept_interval — 音程基礎（半音/全音、度數、性質、協和）"
```

---

## Task 2: concept_triad.md（三和弦）

**Files:**
- Create: `wiki_harmony/concept_triad.md`

- [ ] **Step 1: Write concept_triad.md**

涵蓋：

1. **三和弦定義** — 三個音、以三度堆疊。根音（root）、三音（third）、五音（fifth）。
2. **四種三和弦** — 每種列出音程公式 + 聽感 + 鍵盤示意（以 C 為例）：
   - 大三和弦（Major）：大三度 + 小三度 = 1-3-5。連結 [[chord_major]]
   - 小三和弦（Minor）：小三度 + 大三度 = 1-♭3-5。連結 [[chord_minor]]
   - 減三和弦（Diminished）：小三度 + 小三度 = 1-♭3-♭5。連結 [[chord_diminished]]
   - 增三和弦（Augmented）：大三度 + 大三度 = 1-3-#5。連結 [[chord_augmented]]
3. **轉位** — 原位/第一轉位/第二轉位，用 C major 舉例（C-E-G → E-G-C → G-C-E），說明最低音改變但根音不變。
4. **如何判斷根音** — 把音排成三度堆疊，最底下就是根音。
5. **大調音階上的三和弦** — I(maj) ii(min) iii(min) IV(maj) V(maj) vi(min) vii°(dim)，用 C 大調列表。預告 [[concept_chord_function]]。

- [ ] **Step 2: Commit**

```bash
git add wiki_harmony/concept_triad.md
git commit -m "wiki_harmony: concept_triad — 四種三和弦、轉位、根音判斷"
```

---

## Task 3: chord_major.md + chord_minor.md + chord_diminished.md + chord_augmented.md（三和弦參考頁 ×4）

**Files:**
- Create: `wiki_harmony/chord_major.md`
- Create: `wiki_harmony/chord_minor.md`
- Create: `wiki_harmony/chord_diminished.md`
- Create: `wiki_harmony/chord_augmented.md`

- [ ] **Step 1: Write chord_major.md**

按統一模板。12 調列表（C/C#/D/D#/E/F/F#/G/G#/A/A#/B），每調列組成音 + 鍵盤示意。轉位（原位/一轉/二轉）。常見用法（調性中 I/IV/V 級）。聽覺特徵（明亮、穩定、開放）。鍵盤應用連結 `wiki_piano/concept_chord_fingering`。

- [ ] **Step 2: Write chord_minor.md**

同模板。公式 1-♭3-5。12 調列表。聽覺特徵（柔和、暗淡、內省）。常見用法（ii/iii/vi 級）。

- [ ] **Step 3: Write chord_diminished.md**

同模板。公式 1-♭3-♭5。12 調列表。聽覺特徵（緊張、不穩定、需要解決）。常見用法（vii° 級、經過和弦）。

- [ ] **Step 4: Write chord_augmented.md**

同模板。公式 1-3-#5。12 調列表。聽覺特徵（懸浮、夢幻、不安定）。常見用法（V+ → I 解決、印象派色彩）。注意增三和弦的對稱性（只有 4 種不同的增三和弦）。

- [ ] **Step 5: Commit**

```bash
git add wiki_harmony/chord_major.md wiki_harmony/chord_minor.md wiki_harmony/chord_diminished.md wiki_harmony/chord_augmented.md
git commit -m "wiki_harmony: 4 triad reference pages — major/minor/dim/aug × 12 keys"
```

---

## Task 4: concept_seventh_chord.md（七和弦）

**Files:**
- Create: `wiki_harmony/concept_seventh_chord.md`

- [ ] **Step 1: Write concept_seventh_chord.md**

涵蓋：

1. **七和弦定義** — 三和弦上再疊一個三度 = 四個音。根音 + 三音 + 五音 + 七音。
2. **五種常見七和弦**（每種列公式 + 三和弦基礎 + 鍵盤示意 C 為例）：
   - 大七和弦（Major 7th）：大三和弦 + 大七度 = 1-3-5-7。連結 [[chord_major7]]
   - 小七和弦（Minor 7th）：小三和弦 + 小七度 = 1-♭3-5-♭7。連結 [[chord_minor7]]
   - 屬七和弦（Dominant 7th）：大三和弦 + 小七度 = 1-3-5-♭7。連結 [[chord_dominant7]]
   - 減七和弦（Diminished 7th）：減三和弦 + 減七度 = 1-♭3-♭5-𝄫7。連結 [[chord_dim7]]
   - 半減七和弦（Half-diminished 7th）：減三和弦 + 小七度 = 1-♭3-♭5-♭7。連結 [[chord_half_dim7]]
3. **七和弦轉位** — 原位/一轉/二轉/三轉，數字低音標記（7/6-5/4-3/4-2 或 2）。
4. **屬七的特殊地位** — 含 tritone（3-♭7），產生強烈解決傾向 → V7→I。預告 [[concept_chord_function]]。
5. **大調音階上的七和弦** — Imaj7 / ii7 / iii7 / IVmaj7 / V7 / vi7 / viiø7。

- [ ] **Step 2: Commit**

```bash
git add wiki_harmony/concept_seventh_chord.md
git commit -m "wiki_harmony: concept_seventh_chord — 五種七和弦、轉位、屬七解決"
```

---

## Task 5: chord_dominant7.md + chord_major7.md + chord_minor7.md + chord_dim7.md + chord_half_dim7.md（七和弦參考頁 ×5）

**Files:**
- Create: `wiki_harmony/chord_dominant7.md`
- Create: `wiki_harmony/chord_major7.md`
- Create: `wiki_harmony/chord_minor7.md`
- Create: `wiki_harmony/chord_dim7.md`
- Create: `wiki_harmony/chord_half_dim7.md`

- [ ] **Step 1: Write chord_dominant7.md**

按統一模板。公式 1-3-5-♭7。12 調列表含組成音 + 鍵盤示意。三種轉位。常見用法（V7→I 解決、blues 中每個和弦都用 dom7）。聽覺特徵（緊張但帶推進感、藍調味）。

- [ ] **Step 2: Write chord_major7.md**

公式 1-3-5-7。聽覺特徵（溫暖、夢幻、爵士感）。常見用法（Imaj7/IVmaj7，流行/bossa nova）。

- [ ] **Step 3: Write chord_minor7.md**

公式 1-♭3-5-♭7。聽覺特徵（柔和、流動、帶藍調色彩）。常見用法（ii7 在 ii-V-I 中）。

- [ ] **Step 4: Write chord_dim7.md**

公式 1-♭3-♭5-𝄫7（enharmonic = 大六度）。12 調列表。注意減七和弦的對稱性（只有 3 種不同的減七和弦，每隔小三度 = 同一組轉位）。聽覺特徵（極度緊張、戲劇性、電影配樂感）。常見用法（經過減七、vii°7/V）。

- [ ] **Step 5: Write chord_half_dim7.md**

公式 1-♭3-♭5-♭7。符號 ø。聽覺特徵（憂鬱、不安但較減七柔和）。常見用法（viiø7 in major、iiø7 in minor ii-V-i）。

- [ ] **Step 6: Commit**

```bash
git add wiki_harmony/chord_dominant7.md wiki_harmony/chord_major7.md wiki_harmony/chord_minor7.md wiki_harmony/chord_dim7.md wiki_harmony/chord_half_dim7.md
git commit -m "wiki_harmony: 5 seventh chord reference pages — dom7/maj7/m7/dim7/half-dim7 × 12 keys"
```

---

## Task 6: concept_extended_chord.md + concept_sus_add_chord.md + chord_9th.md + chord_sus.md + chord_add.md + chord_6th.md

**Files:**
- Create: `wiki_harmony/concept_extended_chord.md`
- Create: `wiki_harmony/concept_sus_add_chord.md`
- Create: `wiki_harmony/chord_9th.md`
- Create: `wiki_harmony/chord_sus.md`
- Create: `wiki_harmony/chord_add.md`
- Create: `wiki_harmony/chord_6th.md`

- [ ] **Step 1: Write concept_extended_chord.md**

涵蓋：
1. **疊加邏輯** — 七和弦上再疊三度 = 九和弦，再疊 = 十一，再疊 = 十三。最多疊到十三（= 七個音 = 全音階所有音）。
2. **九和弦** — dom9 (1-3-5-♭7-9)、Maj9 (1-3-5-7-9)、m9 (1-♭3-5-♭7-9)。連結 [[chord_9th]]。
3. **十一和弦** — 通常省略三音（與十一度衝突）。
4. **十三和弦** — 通常省略九度和十一度。
5. **省略音原則** — 實際彈奏時，五音最常省略，根音次之（有 bass 代勞）。鍵盤上的 voicing 通常 4-5 音。

- [ ] **Step 2: Write concept_sus_add_chord.md**

涵蓋：
1. **sus 和弦** — sus4 (1-4-5) 和 sus2 (1-2-5)，「suspended」= 三音被掛起（替換），不含三度 → 無大小之分。
2. **add 和弦** — add9 (1-3-5-9)、add11 等，三和弦 + 直接加一個音，不經過七度。
3. **sus/add 與延伸和弦的區別** — dom9 有 ♭7，add9 沒有。sus4 替換三音，dom11 保留三音（理論上）。

- [ ] **Step 3: Write chord_9th.md**

統一模板。列出 dom9/Maj9/m9 三種，每種 12 調。公式、鍵盤示意、常見省略音 voicing。

- [ ] **Step 4: Write chord_sus.md**

統一模板。sus4 和 sus2 分兩節。12 調列表。聽覺特徵（開放、懸浮、解決期待）。常見用法（sus4→大三和弦解決、流行音樂 intro/outro）。

- [ ] **Step 5: Write chord_add.md**

統一模板。add9 為主，附 add11。12 調列表。聽覺特徵（清新、空氣感）。常見用法（流行/ACG 音樂）。

- [ ] **Step 6: Write chord_6th.md**

統一模板。大六和弦 (1-3-5-6) 和小六和弦 (1-♭3-5-6) 分兩節。12 調列表。聽覺特徵（復古、溫馨）。常見用法（爵士結尾、走路低音伴奏）。

- [ ] **Step 7: Commit**

```bash
git add wiki_harmony/concept_extended_chord.md wiki_harmony/concept_sus_add_chord.md wiki_harmony/chord_9th.md wiki_harmony/chord_sus.md wiki_harmony/chord_add.md wiki_harmony/chord_6th.md
git commit -m "wiki_harmony: extended/sus/add/6th — 2 concept + 4 reference pages"
```

---

## Task 7: concept_chord_function.md + concept_cadence.md（功能和聲 + 終止式）

**Files:**
- Create: `wiki_harmony/concept_chord_function.md`
- Create: `wiki_harmony/concept_cadence.md`

- [ ] **Step 1: Write concept_chord_function.md**

涵蓋：
1. **級數標記** — 大寫 I-VII = 大三和弦，小寫 ii-vii = 小三和弦，° = 減。羅馬數字 = 根音在音階上的位置。
2. **三大功能** — Tonic (T)：I, iii, vi → 穩定、回家感。Subdominant (S)：ii, IV → 離家、準備。Dominant (D)：V, vii° → 緊張、要回家。
3. **功能流向** — T → S → D → T（最常見）。不常 D → S（逆行稀少但存在）。
4. **大調 vs 小調** — 小調和弦表：i / ii° / III / iv / V(或 v) / VI / VII(或 vii°)。和聲小音階讓 V 成為大三和弦。
5. **鍵盤應用** — 以 C 大調和 A 小調各彈一次 I-IV-V-I / i-iv-V-i，標鍵盤位置。

- [ ] **Step 2: Write concept_cadence.md**

涵蓋：
1. **終止式定義** — 樂句結尾的和弦公式，像標點符號。
2. **四種基本終止式**：
   - 正格終止（Authentic Cadence）：V→I，「句號」。完全正格（PAC）vs 不完全正格（IAC）。
   - 半終止（Half Cadence）：?→V，「逗號」，停在 dominant 上。
   - 變格終止（Plagal Cadence）：IV→I，「阿門終止」。
   - 欺騙終止（Deceptive Cadence）：V→vi，「驚嘆號」，期待回家但被騙。
3. **鍵盤範例** — 每種終止式用 C 大調 4 小節示範，標和弦與鍵盤位置。
4. **聽辨提示** — 每種終止式的「感覺」描述。

- [ ] **Step 3: Commit**

```bash
git add wiki_harmony/concept_chord_function.md wiki_harmony/concept_cadence.md
git commit -m "wiki_harmony: chord function (T/S/D) + cadence (4 types with keyboard examples)"
```

---

## Task 8: concept_progression.md（和弦進行）

**Files:**
- Create: `wiki_harmony/concept_progression.md`

- [ ] **Step 1: Write concept_progression.md**

涵蓋：
1. **什麼是和弦進行** — 和弦按順序排列形成的 harmonic pattern，是歌曲的骨架。
2. **常用進行**（每個附級數 + C 大調實例 + 鍵盤位置 + 代表曲目 1-2 首）：
   - I-IV-V-I：最基本的古典進行
   - I-V-vi-IV（流行四和弦）：Let It Be, Someone Like You
   - vi-IV-I-V（同上的旋轉）：Despacito
   - I-vi-IV-V（50s 進行 / doo-wop）
   - ii-V-I（爵士最重要進行）
   - I-IV-vi-V（卡農進行變體）
   - 12-bar blues：I-I-I-I / IV-IV-I-I / V-IV-I-V
   - 4536 進行（流行華語）：IV-V-iii-vi
3. **為什麼這些進行好聽** — 功能和聲流向（T→S→D→T）的體現。共同音（common tones）讓轉換平滑。
4. **自己動手** — 鼓勵讀者在鍵盤上試彈每個進行，先用 C 大調，再移到 G 大調。

- [ ] **Step 2: Commit**

```bash
git add wiki_harmony/concept_progression.md
git commit -m "wiki_harmony: concept_progression — 8 common progressions with keyboard examples"
```

---

## Task 9: concept_secondary_dominant.md + concept_modulation.md（離調 + 轉調）

**Files:**
- Create: `wiki_harmony/concept_secondary_dominant.md`
- Create: `wiki_harmony/concept_modulation.md`

- [ ] **Step 1: Write concept_secondary_dominant.md**

涵蓋：
1. **離調定義** — 暫時借用另一個調的 dominant 和弦，但不真正轉調。
2. **副屬和弦（Secondary Dominant）** — V/V（五級的五級）、V/ii、V/vi 等。以 C 大調為例：V/V = D7（→ G）、V/ii = A7（→ Dm）。
3. **辨認方法** — 看到調性外的大三或屬七和弦 → 檢查它是否解決到調性內和弦。
4. **常見用法** — V/V → V → I（加強 dominant 前的推力）。流行音樂中 V/vi 常見。
5. **鍵盤範例** — C 大調中 C → A7 → Dm → G7 → C（含 V/ii）。

- [ ] **Step 2: Write concept_modulation.md**

涵蓋：
1. **轉調定義** — 從一個調「搬家」到另一個調，新的 tonic 確立。
2. **近系調與遠系調** — 近系調 = 差一個升降記號（如 C↔G, C↔F, C↔Am）。遠系調 = 差多個。
3. **共同和弦轉調（Pivot Chord Modulation）** — 找兩個調共有的和弦作為橋樑。例：C 大調 → G 大調，Am = C 調 vi = G 調 ii，用它當 pivot。附鍵盤範例。
4. **半音轉調（Chromatic Modulation）** — 直接用半音移動過渡，常見於流行音樂副歌升半音。
5. **直接轉調** — 沒有過渡，突然換調。效果戲劇性。

- [ ] **Step 3: Commit**

```bash
git add wiki_harmony/concept_secondary_dominant.md wiki_harmony/concept_modulation.md
git commit -m "wiki_harmony: secondary dominant + modulation — 離調與轉調基礎"
```

---

## Task 10: index.md + wiki_piano/index.md 互連 + final commit

**Files:**
- Create: `wiki_harmony/index.md`
- Modify: `wiki_piano/index.md` (add cross-wiki link)

- [ ] **Step 1: Write wiki_harmony/index.md**

涵蓋：
1. **標題與統計** — `# Harmony Wiki（和聲樂理）`，頁數統計。
2. **並列 wiki 連結** — wiki_piano, wiki_phrase, wiki_articulation。
3. **學習路線圖** — 概念頁按順序列出，附一句話描述，標前置知識：
   - concept_interval → concept_triad → concept_seventh_chord → concept_extended_chord
   - concept_triad → concept_sus_add_chord（分支）
   - concept_triad → concept_chord_function → concept_cadence → concept_progression → concept_secondary_dominant → concept_modulation
4. **和弦速查索引** — 按類別分組（三和弦/七和弦/延伸/色彩），連結所有 13 個 chord_ 頁。
5. **拼圖照片** — 嵌入 `![[../raw/piano_fingering/IMG_1069 (1).HEIC]]`（Obsidian 支援 HEIC）。

- [ ] **Step 2: Update wiki_piano/index.md**

在 header 的 `並列 wiki` 行加上 `wiki_harmony` 連結：

```markdown
> 並列 wiki：[../wiki_phrase/index](../wiki_phrase/index.md) (樂句分段) + [../wiki_articulation/index](../wiki_articulation/index.md) (連結 / 斷奏 / 觸鍵詮釋) + [../wiki_harmony/index](../wiki_harmony/index.md) (和聲樂理)
```

- [ ] **Step 3: Commit**

```bash
git add wiki_harmony/index.md wiki_piano/index.md
git commit -m "wiki_harmony: index + cross-wiki link from wiki_piano"
```

---

## Summary

| Task | Pages | Description |
|------|-------|-------------|
| 1 | 1 | concept_interval（音程基礎） |
| 2 | 1 | concept_triad（三和弦） |
| 3 | 4 | chord_major/minor/dim/aug（三和弦參考頁） |
| 4 | 1 | concept_seventh_chord（七和弦） |
| 5 | 5 | chord_dom7/maj7/m7/dim7/half-dim7（七和弦參考頁） |
| 6 | 6 | concept_extended + concept_sus_add + chord_9th/sus/add/6th |
| 7 | 2 | concept_chord_function + concept_cadence |
| 8 | 1 | concept_progression（和弦進行） |
| 9 | 2 | concept_secondary_dominant + concept_modulation |
| 10 | 1 | index.md + wiki_piano 互連 |
| **Total** | **24** | |
