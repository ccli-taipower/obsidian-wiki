# wiki_harmony 設計文件

## 目標

在 Obsidian vault 新建 `wiki_harmony/` 目錄，系統化介紹和弦樂理與鍵盤應用，面向鋼琴初學者。

## 定位

- 與 `wiki_piano`（指法）、`wiki_phrase`（樂句）、`wiki_articulation`（觸鍵）並列
- 和弦指法細節交給 `wiki_piano/concept_chord_fingering.md`，本 wiki 專注樂理與鍵盤位置
- 語言：中英混用，術語附英文原文

## 結構

兩類頁面：**概念頁**（循序學習路線）+ **和弦參考頁**（字典式速查）。概念頁用 `[[chord_*]]` 連結到對應參考頁。

### 概念頁（concept_ prefix）

| 檔案 | 內容 | 前置知識 |
|------|------|----------|
| `concept_interval.md` | 半音/全音、音程度數與性質（大/小/完全/增/減）、協和與不協和 | 無 |
| `concept_triad.md` | 三和弦四種（大/小/增/減）、轉位、根音位置判斷 | interval |
| `concept_seventh_chord.md` | 五種七和弦（Maj7/m7/dom7/dim7/m7♭5）、轉位 | triad |
| `concept_extended_chord.md` | 九和弦、十一和弦、十三和弦、疊加邏輯 | seventh_chord |
| `concept_sus_add_chord.md` | sus2/sus4、add9/add11、與延伸和弦的區別 | triad |
| `concept_chord_function.md` | 調性內和弦級數（I-VII）、T/S/D 功能分組、大調與小調 | triad |
| `concept_cadence.md` | 正格終止（V→I）、半終止、變格終止（IV→I）、欺騙終止（V→vi） | chord_function |
| `concept_progression.md` | I-IV-V-I、ii-V-I、卡農進行、12-bar blues、流行 4536 等 | cadence |
| `concept_secondary_dominant.md` | 副屬和弦（V/V 等）、離調概念、常見用法 | progression |
| `concept_modulation.md` | 共同和弦轉調、半音轉調、近系調與遠系調 | secondary_dominant |

### 和弦參考頁（chord_ prefix）

每頁統一格式：

```markdown
# 和弦名稱（英文名）

## 組成
- 結構公式（如 1-3-5, 1-♭3-5）
- 音程堆疊說明

## 12 調列表
| 根音 | 組成音 | 鍵盤示意 |
|------|--------|----------|
| C    | C-E-G  | ⬜⬛⬜⬛⬜⬜⬛⬜⬛⬜⬛⬜ |
| ...  | ...    | ...      |

## 轉位
- 第一轉位、第二轉位...

## 常見用法
- 在哪些調中出現、典型進行

## 鍵盤應用
- 彈奏提示（指法連結到 wiki_piano）

## 聽覺特徵
- 一句話描述聽感（如「明亮穩定」「暗淡柔和」）
```

參考頁清單（13 頁）：

| 檔案 | 和弦類型 |
|------|----------|
| `chord_major.md` | 大三和弦 Major |
| `chord_minor.md` | 小三和弦 Minor |
| `chord_diminished.md` | 減三和弦 Diminished |
| `chord_augmented.md` | 增三和弦 Augmented |
| `chord_dominant7.md` | 屬七和弦 Dominant 7th |
| `chord_major7.md` | 大七和弦 Major 7th |
| `chord_minor7.md` | 小七和弦 Minor 7th |
| `chord_dim7.md` | 減七和弦 Diminished 7th |
| `chord_half_dim7.md` | 半減七和弦 Half-diminished 7th (m7♭5) |
| `chord_9th.md` | 九和弦（dom9/Maj9/m9） |
| `chord_sus.md` | sus2 / sus4 |
| `chord_add.md` | add9 / add11 |
| `chord_6th.md` | 六和弦 6 / m6 |

### index.md

- 學習路線圖（概念頁順序 + 建議閱讀順序）
- 和弦速查索引（連結所有 chord_ 頁）
- 拼圖照片嵌入（`raw/piano_fingering/IMG_1069 (1).HEIC`）
- 與其他 wiki 的互連（wiki_piano 指法、wiki_articulation 觸鍵）

## 頁面總數

- 概念頁：10 頁
- 參考頁：13 頁
- index：1 頁
- **共 24 頁**

## 鍵盤示意方式

參考頁中的 12 調列表用 ASCII 鍵盤示意，標記被按下的琴鍵。格式待實作時確定（可能用 text block 或簡易 SVG）。

## 與現有 wiki 的關係

- `wiki_piano/concept_chord_fingering.md` — 和弦指法細節，從 chord_ 頁連結過去
- `wiki_piano/concept_chord_voicing_fingering.md` — 和弦聲位指法
- `wiki_piano/concept_standard_scale_arpeggio_fingering.md` — 琶音指法
- `wiki_articulation/` — 和弦的觸鍵詮釋

## 不包含

- 對位法（counterpoint）
- 配器法（orchestration）
- 爵士和聲進階（tritone sub、modal interchange 等）
- MIDI/音訊範例
