# Composer: J.S. Bach 樂句分段

> 來源：Schiff Bach lectures, Tovey *Companion to Bach's Art of Fugue*, Williams *J.S. Bach* (2007), Donington *Baroque Music*
> 引用方：[[concept_fugue]], [[concept_counterpoint]], [[analysis_bach_inv_1_c_major]] 等 8 個 Bach Inv 分析頁, [[src_bach_inventions_pedagogy]]

## 1. 為什麼 Bach 樂句分段值得獨立頁面

J.S. Bach (1685-1750) 是鋼琴指法系統的**主要測試對象**：
- score-claude 主流程涵蓋 Bach 15 Two-Part Inventions（mvts 1-15, 已啟用 12 mvts）
- 對位 texture (2-voice / 3-voice fugue / sinfonia) 樂句分段是獨特挑戰
- Baroque non-legato default 對 articulation / fingering 策略有根本影響

Bach 樂句分段不能套用後續 Classical / Romantic 邏輯 — 對位作品的「樂句」概念與 homophonic melody-and-accompaniment 不同。

## 2. Bach 樂句的特殊性

⚠ Training-data verification needed:

### 2.1 對位作品的「樂句」是各聲部獨立

對位作品中，**每聲部都有自己的樂句結構**：
- Subject (主題)：完整 motivic 單位，獨立樂句
- Counter-subject：對位伴奏，獨立樂句
- Episode：兩聲部都從 subject 解放，獨立 phrase 邏輯

→ 不存在「整曲統一樂句」 — 樂句是 per-voice 的。

對 score-claude 的對應：per-hand DP 處理 + [[concept_subject_imitation_detection]] 偵測各聲部 subject re-entry。

### 2.2 Phrase boundary 訊號來源

Bach 對位作品的 phrase boundary 主要訊號：
- **Cadence** ([[concept_cadence_detection]]): half-cadence / authentic cadence / deceptive cadence
- **Subject re-entry** ([[concept_subject_imitation_detection]]): subject 在不同聲部重現
- **Modulation** ([[concept_modulation_as_phrase_signal]]): 調性轉折常伴隨樂句段落
- **Episode 進入 / 結束**: subject-based texture → 自由 development texture 切換

Bach 較少 rely 純 articulation 切樂句（rest / pitch jump 等樂句 default 訊號）。

### 2.3 Hypermeter 對 Bach 較少適用

⚠ Training-data verification needed: [[concept_hypermeter]] (4-bar / 8-bar 大週期感) 主要適用 Classical / Romantic homophonic 音樂。Bach 對位作品的 phrase length **更不規則**：
- 2 bar / 3 bar / 5 bar phrase 並存
- 對位線各自 phrase length 不一致
- Hypermeter 概念在 Bach 適用度有限

## 3. Two-Part Inventions (BWV 772-786) 樂句結構

⚠ Training-data verification needed:

| Inv | Key | Phrase 主要結構 | score-claude 啟用 |
|---|---|---|---|
| 1 | C | Subject (m1) → answer (m3) → episode → ... 標準 2-voice exposition | ✓ fig+thumb |
| 2 | C minor | 同上模式 + minor 半音變化 | ✓ fig+thumb |
| 3 | D | Sequence-rich | ✓ fig only |
| 4 | D minor | 3/8 拍 + sigh motifs | ✓ fig+thumb+cadence |
| 5 | E♭ | Lyrical (chromatic-subject) | ✓ fig+thumb+subject@0.7 |
| 6 | E | **嚴格 canon at octave** — phrase 邏輯特殊 | ✓ fig+thumb+subject@0.7 (surprise win) |
| 7 | E minor | Chromatic LH subject | ✓ fig+subject@0.7 (no thumb) |
| 8 | F | Figural-dominated | ✓ fig+thumb+subject |
| 9 | F minor | ✗ 未啟用 (all axes breach) |
| 10 | G | ✗ 未啟用 |
| 11 | G minor | ✓ fig only (chromatic 段) |
| 12 | A | ✓ fig+thumb+subject@0.7 |
| 13 | A minor | ✗ 未啟用 |
| 14 | B♭ | ✓ fig+thumb+subject@0.7 (big wins) |
| 15 | B minor | ✓ fig only |

→ 12 of 15 mvts enabled (per score-claude `BACH_INV_PHRASE_FLAGS`)。

## 4. Three-Part Sinfonias (BWV 787-801)

⚠ Training-data verification needed: 15 Sinfonias 是 Two-Part Inventions 的進階版本：
- 3 聲部 within-hand polyphony — 一手承載兩聲部
- 樂句結構更複雜（[[../wiki_articulation/concept_articulation_in_polyphony]] §對位）
- 是 [[../score-claude/memory/project_target_repertoire_intermediate]] 中「intermediate 深化」對象

score-claude 對 Sinfonias 處理：尚未在 BACH_INV_PHRASE_FLAGS 啟用（cache 還沒 Sinfonias OMR）。

## 5. Well-Tempered Clavier (BWV 846-893) 樂句邏輯

兩本 *Das Wohltemperierte Clavier* (1722, 1742) 各含 24 對 Prelude + Fugue：

| 類型 | 樂句結構特性 |
|---|---|
| **Prelude** | 自由形式 — 從 toccata-like 到 invention-like 都有；樂句邏輯依風格 |
| **Fugue** | Subject + answer + counter-subject + episode + stretto + cadence 標準 fugue 結構 |

對指法系統的意涵：WTC 是 [[concept_fugue]] 的最系統化練習對象，但**不在 intermediate 目標範圍**（多數 WTC fugue 是 advanced）。

## 6. 其他 Bach 鍵盤作品的樂句

⚠ Training-data verification needed:

| 作品集 | 樂句特性 |
|---|---|
| **French Suites** (BWV 812-817) | 6 suite 各含 4-7 dance movements；dance form 決定樂句長度 |
| **English Suites** (BWV 806-811) | 同 French 但加 Prelude；Prelude 較大型 |
| **Partitas** (BWV 825-830) | 6 partita，最 advanced，含 sinfonia / fantasia 等大型開頭樂章 |
| **Goldberg Variations** (BWV 988) | Aria + 30 variations + Aria reprise；variations 各自獨立樂句 |
| **Italian Concerto** (BWV 971) | Italian-style 3 樂章，較 homophonic（適用一般 phrase 邏輯）|

## 7. Bach articulation 處理（與 [[../wiki_articulation/analysis_bach_inv_articulation]] 重疊）

Bach 樂句邊界 vs articulation 是分開的事：
- **樂句邊界**：本頁 §2 列的 cadence / subject / modulation 訊號
- **Articulation**：Baroque non-legato default ([[../wiki_articulation/concept_non_legato_baroque]])

樂句切完之後，articulation 處理是獨立決策。

## 8. 演奏家 Bach 詮釋傳統

⚠ Training-data verification needed:

| 演奏家 | Bach 詮釋風格 |
|---|---|
| **Glenn Gould** | 極度個性化 — articulation 對比鮮明，phrase 結構清晰 |
| **András Schiff** | 學術 + 表情；常以 lecture-recital 形式分析 |
| **Angela Hewitt** | 平衡 — 對位清晰 + 表情兼顧 |
| **Murray Perahia** | 抒情 + 結構並重 |
| **Tatiana Nikolayeva** | 俄羅斯派 — 較重量感 |
| **Wanda Landowska** | Harpsichord 演奏 — HIP 派代表 |

## 9. 與其他 wiki 頁面的關係

- [[concept_fugue]] — Fugue 結構與 Bach 對位作品分析框架
- [[concept_counterpoint]] — 對位 texture 樂句獨立性
- [[concept_subject_imitation_detection]] — Subject re-entry 偵測（Bach 主要 phrase signal）
- [[concept_cadence_detection]] — Cadence 偵測（Bach 段落收結）
- [[analysis_bach_inv_1_c_major]] 等 8 個 Bach Inv 分析頁
- [[src_bach_inventions_pedagogy]] — Bach Inv 多 edition 教學傳統
- [[../wiki_articulation/concept_non_legato_baroque]] — Bach 默認 articulation
- [[../wiki_articulation/analysis_bach_inv_articulation]] — Bach Inv articulation 詮釋
- [[../wiki_articulation/analysis_bach_sinfonias]] — Sinfonias 進階對位
- [[../wiki_articulation/src_cpe_bach_versuch]] — Bach 兒子 C.P.E. Bach 對 Baroque 演奏的權威論述

## 10. ⚠ Training-data verification queue

- §2.3 Hypermeter 在 Bach 適用度的學術文獻
- §3 各 Inv subject 結構的精確 manuscript 比較
- §6 Partitas / Goldberg 樂句結構的具體分析
- §8 演奏家詮釋差異的具體 recording 比較
