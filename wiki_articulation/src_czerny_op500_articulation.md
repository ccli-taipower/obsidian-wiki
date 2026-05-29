# Source: Czerny《Op.500 Vollständige theoretisch-practische Pianoforte-Schule》

> Carl Czerny (1791-1857), *Op.500* (1839, Vienna: Diabelli)，共 4 卷；英譯散見不同編輯，Vol.III 涉及 articulation
> 引用方：[concept_legato_substitution](concept_legato_substitution.md) §2, [concept_articulation_overview](concept_articulation_overview.md) §1, [concept_non_legato_baroque](concept_non_legato_baroque.md) §2

## 1. 作者背景

Carl Czerny 是 Beethoven 的學生（1801-1809 學徒期）+ Liszt 的老師（1819-1822），扮演 18-19 世紀鋼琴教學「**Beethoven 派 → 19 世紀 virtuoso 派**」的關鍵橋樑。

*Op.500* 是其晚期教學理論集大成之作，4 卷涵蓋從入門到 virtuoso 全部技術 + 詮釋 + 即興 + 教學法。是 19 世紀中葉**最被廣泛採用的鋼琴教材系統**，影響後續 Liszt、Leschetizky、Theodor Leschetizky 學派。

## 2. Op.500 的 4 卷結構 ⚠

⚠ Training-data verification needed:
- **Vol.I**：基礎技術 / 指法練習
- **Vol.II**：擴展技術 / scales / arpeggios / 八度
- **Vol.III**：表情 / articulation / 詮釋（**本 wiki 主要參考卷**）
- **Vol.IV**：即興 / 改編 / 風格

本 wiki 主要參考 Vol.III 的 articulation 與觸鍵章節。

## 3. 對 articulation 的核心主張

### 3.1 Articulation 的階段分類 ⚠

⚠ Training-data verification needed: Czerny 在 Vol.III 提出 articulation 的「**漸層分類**」，從最連到最斷：
- Legatissimo（極連）
- Legato（連奏）
- Mezzo legato / portato（半連）
- Non legato（不連，Baroque default）
- Mezzo staccato（半斷）
- Staccato（斷奏）
- Staccatissimo（極斷）

這個 7 階段分類是 [concept_articulation_overview](concept_articulation_overview.md) §2 11 種 taxonomy 的歷史基礎之一。

### 3.2 Substitution 的兩類分法 ⚠

⚠ Training-data verification needed:
> 「Legato 段中，凡是同音重複，應使用 finger change（同音換指）；凡是接續長線條，應預備性地用 substitution 為下個 hand-position 鋪路。」

Czerny 把 finger substitution 明確分為兩類：
1. **同音換指 (same-pitch substitution)**：對重複音；保持 legato 連續性
2. **預備性換指 (preparatory substitution)**：為下個 hand position 鋪路；幫助 thumb cross 或 hand reposition

詳見 [concept_legato_substitution](concept_legato_substitution.md) §2.3, §4 引用。

### 3.3 Scale 與 arpeggio 的標準 fingering

Czerny 在 Vol.I/II 給出大量標準指法表：
- C major scale 8 指：1-2-3-1-2-3-4-5（標準至今）
- 各調 scale 指法（依黑鍵分佈調整）
- 標準 arpeggio fingerings (root position, inversions)

→ 這些**指法陣列傳統**是 19 世紀後鋼琴教學的基石。score-claude DP 透過 `_in_scale_segment` + long_scale_thumb_under rule 部分復現此傳統。

### 3.4 Touch 與 dynamic 的關係

Czerny 區分 articulation（time-axis：音與音間連接）vs touch（force-axis：每音強度）：
- Articulation：legato / staccato / etc.
- Touch：weight, percussion, pressure 等手感類別

兩者獨立但常配合：例如「dolce legato」= 連奏 + 柔和觸鍵；「marcato staccato」= 斷奏 + 強重觸鍵。

## 4. Czerny 對教學派系的影響

Czerny 學派的延續：
- Liszt（直接學生）→ Liszt 學派 → 20 世紀眾多大師
- Theodor Leschetizky 間接受影響 → Schnabel, Paderewski, Friedman
- 維也納古典派傳統

→ Czerny 派「**結構化指法表 + 標準觸鍵分類**」是 19 世紀教學主流，比 Neuhaus 重量哲學更早，比 Matthay 物理分析更系統化（但較少抽象原則）。

## 5. 對指法系統的具體影響

| Czerny 教學 | 對 score-claude DP 的對應 |
|---|---|
| Substitution 兩類分法 | [concept_legato_substitution](concept_legato_substitution.md) §3-4 操作型定義 + 預備性換指 |
| 標準 scale fingering | `concept_long_scale_thumb_under` rule（part of wiki_piano）|
| Articulation 漸層分類 | [concept_articulation_overview](concept_articulation_overview.md) §2 taxonomy 的歷史基礎 |
| 黑鍵 scale 指法調整 | `BLACK_KEY_PCS` + `PINKY_BLACK_KEY_PENALTY` rules |

## 6. 文章未涵蓋

- **個性化指法**：Czerny 偏「standard fingering 表」，較少討論個人差異（手大 / 手小、生物力學差異）
- **演奏者選擇權**：較少明確說「這是可選的，可改」（19 世紀教學偏 prescriptive）
- **作品 specific 分析**：偏練習曲（自己寫的 Op.299 / Op.740 等），少談大師作品具體段落

## 7. 與其他 wiki 頁面的關係

- [concept_legato_substitution](concept_legato_substitution.md) §2.3 — Czerny 兩類 substitution 引述
- [concept_articulation_overview](concept_articulation_overview.md) §2 — Czerny 漸層分類為 taxonomy 基礎
- [concept_non_legato_baroque](concept_non_legato_baroque.md) §2 — Czerny 對 Baroque non-legato 的時代-context 處理
- [src_neuhaus_art_of_piano](src_neuhaus_art_of_piano.md) / [src_matthay_visible_inaudible](src_matthay_visible_inaudible.md) — 對比 19 世紀 vs 20 世紀派系
- [../wiki_piano/concept_finger_span_table](../wiki_piano/concept_finger_span_table.md) — Czerny 標準指法表是 span table 的歷史依據

## 8. ⚠ Training-data verification queue

以下基於 training-data，需 cross-check Op.500 原文 / 英譯：
- §2 Op.500 4 卷結構（章節標題）
- §3.1 articulation 7 階段分類（具體章節 / 名稱對應）
- §3.2 substitution 兩類分法引述（章節 / 頁碼）
- §3.3 是否有提到「黑鍵 scale 指法」具體案例
