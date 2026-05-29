# Source: C.P.E. Bach《Versuch über die wahre Art das Clavier zu spielen》(1753)

> Carl Philipp Emanuel Bach (1714-1788), *Versuch über die wahre Art das Clavier zu spielen*（《論鍵盤演奏的真實藝術》）, Part I (1753, Berlin), Part II (1762, Berlin)；英譯 *Essay on the True Art of Playing Keyboard Instruments* (William J. Mitchell 譯, 1949, W.W. Norton)
> 引用方：[concept_non_legato_baroque](concept_non_legato_baroque.md) §2, [src_turk_klavierschule](src_turk_klavierschule.md) §對應, [concept_ornament_articulation](concept_ornament_articulation.md) §5

## 1. 作者背景

C.P.E. Bach 是 J.S. Bach 的次子，在 18 世紀中葉**比父親更出名** — 任職於普魯士腓特烈大帝宮廷（Berlin, 1738-1768），後於漢堡（Hamburg, 1768-1788）擔任 Kantor。

C.P.E. Bach 是「**Empfindsamer Stil**」（敏感風格）的代表作曲家，作品介於 Baroque 末期與 Classical 早期之間，影響 Haydn、Mozart、Beethoven 早期創作。

*Versuch* 是其畢生教學經驗的系統化呈現，**18 世紀中葉最權威的鍵盤演奏教材**，至今仍是 HIP（historically informed performance）研究 Baroque/Classical 過渡期演奏實踐的核心一手文獻。

## 2. *Versuch* 兩 Parts 的內容區分

| Part | 出版 | 主題 |
|---|---|---|
| **Part I** (1753) | Berlin | 技術 / fingering / ornament / articulation / dynamics |
| **Part II** (1762) | Berlin | Continuo / 即興 / accompaniment / 樂句結構 |

本 wiki 主要參考 Part I 的 articulation + ornament 章節。

## 3. 對 articulation 的核心主張

### 3.1 「ordentliches Fortgehen」(規矩的繼續) 的早期定義 ⚠

⚠ Training-data verification needed: C.P.E. Bach 在 Part I §觸鍵章節定義：

> 「音符的持續時間應大約是其書寫值的一半，除非在抒情段（chantant）或標有 legato 的段落。」

→ 這個「**約一半**」(half value) 的論述比 Türk 1789 的「~75-85%」更短（更 detache）。可能反映：
- 鍵盤從 harpsichord → clavichord → fortepiano 過渡期的不同樂器需求
- C.P.E. Bach 個人風格偏向更 articulated
- 「default 應該更 short」的歷史傳統

對指法的意涵：C.P.E. Bach 比 Türk 更強調 detache default，啟示 score-claude DP 對更早 Baroque 作品（J.S. Bach 時代）應假設更 detache 的 articulation default。

### 3.2 Legato 的明確定義 ⚠

⚠ Training-data verification needed:
> 「Legato（連奏）= 一個音的釋放與後一個音的進入發生在同一瞬間。需要主動的手指控制。」

C.P.E. Bach 強調 legato 是**特殊技術**，不是默認 — 與 Romantic 後傳統把 legato 當默認形成鮮明對比。

→ 強化 [concept_non_legato_baroque](concept_non_legato_baroque.md) § Baroque 主張：**Baroque legato 是例外，需要明確標記**。

### 3.3 各種觸鍵分類

⚠ Training-data verification needed: C.P.E. Bach 在 Part I 提到的觸鍵分類：
- **Legato** — 完全連奏
- **Ordentliches Fortgehen** — 默認 (~50% per CPE, 後人調整為 ~85%)
- **Staccato** — 短音（具體百分比視情境）
- **Tragend** (carrying) — 介於 legato / staccato，類似後來的 portato

此分類影響後續 Türk 1789, Czerny Op.500, 並延續至現代 articulation taxonomy。

### 3.4 Articulation 與 dynamics 的關係

C.P.E. Bach 強調 articulation + dynamics + tempo 是「**表情三要素**」，共同構成 musical character：
- 同樣音符序列，articulation / dynamics 不同 → 不同 character
- 演奏家**詮釋自由**主要展現於這三要素的細節變化

對指法的意涵：fingering 選擇影響 articulation 執行品質 → 間接影響表情 character。

## 4. 對 ornament 的權威論述

⚠ *Versuch* Part I 中**ornament 章節**極長且詳盡，是 Baroque ornament 理解的核心一手文獻：

- **Trill**：標準 main-note start, upper-note start 變體, resolution turn
- **Mordent**：short / long 變體, prall-triller (pincé)
- **Appoggiatura**：accented / unaccented, short / long, rules for length
- **Turn**：placement before / after note, speed
- **Tremolo / Bebung** (clavichord-specific)

對指法的意涵：[concept_ornament_articulation](concept_ornament_articulation.md) 的多數 ornament 規則可追溯至 *Versuch*。

## 5. *Versuch* 對後世的影響

| 後代影響 | 內容 |
|---|---|
| **Mozart** | 自稱看過 *Versuch* 並推崇 — Mozart sonata 中 ornament 處理符合 C.P.E. Bach 規則 |
| **Beethoven** | 透過老師 Christian Gottlob Neefe（C.P.E. Bach 學生）間接受影響 |
| **Türk** | *Klavierschule* (1789) 大量引用 C.P.E. Bach |
| **Czerny** | Op.500 雖較系統化，articulation 框架可追溯 |
| **20 世紀 HIP 運動** | *Versuch* 是 Baroque/Classical 演奏實踐核心文獻 |

## 6. 對指法系統的具體影響

| C.P.E. Bach 主張 | 對 score-claude DP 的對應 |
|---|---|
| Default 非 legato (~50%) | 強化 [concept_non_legato_baroque](concept_non_legato_baroque.md) §2 對 Baroque MXL 處理 |
| Legato 是特殊技術 | [concept_legato_substitution](concept_legato_substitution.md) 啟用應 per-piece opt-in 而非 default |
| Articulation 分類 | [concept_articulation_overview](concept_articulation_overview.md) §2 taxonomy 歷史基礎 |
| Ornament 詮釋細則 | [concept_ornament_articulation](concept_ornament_articulation.md) §2-5 規則的一手依據 |

## 7. 文章未涵蓋

- **大型 sonata 分析**：教材性質，少分析具體作品段落
- **20 世紀演奏實踐爭議**：18 世紀文獻不涉及後續傳統演變
- **harpsichord / clavichord 之外的樂器**：modern piano 未及（時代限制）

## 8. 與其他 wiki 頁面的關係

- [concept_non_legato_baroque](concept_non_legato_baroque.md) §2 — C.P.E. Bach 對 Baroque non-legato default 的核心論證
- [concept_articulation_overview](concept_articulation_overview.md) §3 — Baroque default 操作型百分比
- [concept_ornament_articulation](concept_ornament_articulation.md) §5 — Baroque ornament 詮釋一手文獻
- [src_turk_klavierschule](src_turk_klavierschule.md) §對應 — Türk 多次引用 C.P.E. Bach
- [src_donington_baroque_music](src_donington_baroque_music.md) — Donington 20 世紀 HIP 視角對 *Versuch* 的回顧
- [../wiki_phrase/concept_fugue](../wiki_phrase/concept_fugue.md) / [../wiki_phrase/concept_counterpoint](../wiki_phrase/concept_counterpoint.md) — 對位作品 articulation 處理

## 9. ⚠ Training-data verification queue

以下基於 training-data + Mitchell 1949 英譯間接知識：
- §3.1 「half value」default 引述具體章節 / 頁碼
- §3.2 Legato 定義引述
- §3.3 觸鍵分類完整對應表（德文原名）
- §4 Ornament 章節具體結構（subsection 數 / 頁碼）
