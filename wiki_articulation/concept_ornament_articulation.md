# Concept: Ornament 與 Articulation 的互動

> 來源：Donington《Baroque Music: Style and Performance》§ornaments, C.P.E. Bach *Versuch* §ornament 章節, Henle Urtext §ornament 詮釋指南
> 引用方：[concept_legato_substitution](concept_legato_substitution.md) §6 (失效情境), [analysis_bach_inv_articulation](analysis_bach_inv_articulation.md) §例外 legato 段

## 1. Ornament 是 articulation 系統的「特殊區段」

Ornament（trill, mordent, turn, appoggiatura, acciaccatura 等裝飾音）在 articulation 框架中是**特殊區段**：
- 內部音通常**非常短**（小於主音時值）
- 通常**不**屬於主旋律的 articulation 規則（不算入 slur / staccato 計算）
- 自有獨立的演奏實踐慣例

→ 對指法系統來說，ornament 區段應該**跳過一般 articulation rule**，由獨立規則處理。

## 2. 主要 ornament 類型 + articulation 默認

⚠ Training-data verification needed:

| Ornament | 符號 | 內部 articulation | 框架音的 articulation |
|---|---|---|---|
| **Trill (顫音)** | `tr` 或 `~~~` | non-legato 內部（每音清晰）| 結束音常 legato 接 resolution |
| **Mordent** | `⤬` | non-legato 內部 | 同上 |
| **Appoggiatura** | 小音符 | 內部 legato 接主音 | Appoggiatura 與主音 legato，主音與後續可 detache |
| **Acciaccatura** | 小音符 + 斜線 | 非常快 + 略 detache | 與主音 connection 緊湊但不一定 legato |
| **Turn (回轉)** | `∾` | 內部 legato 流動 | 結束音常 legato 接後續 |
| **Tremolo (顫指)** | 雙線 | non-legato（兩音交替）| 結束接後續可 legato 或 detache |

## 3. 為何 ornament 通常不適用 legato substitution

[concept_legato_substitution](concept_legato_substitution.md) §6 列「Ornament 內部」為失效情境，理由：

1. **Ornament 內部音極短**（通常 < 0.25 QN，小於 [concept_legato_substitution](concept_legato_substitution.md) §3 操作型定義 0.5 QN 閾值）
2. **Ornament 由獨立指法慣例規定**（標準 trill 指法、標準 mordent 指法），不應被 substitution rule 干擾
3. **演奏者把 ornament 視為整體單位**，不在內部做 substitution 決策

→ score-claude DP 對 ornament 區段的處理：
- 目前無明確 ornament 識別（MXL ornament marking 未進入 DP cost 計算）
- 但 [concept_legato_substitution](concept_legato_substitution.md) v2 duration gate (LEGATO_MIN_DURATION = 0.5 QN) **自然跳過** ornament 內部的快音
- 結果：ornament 內部音不被 substitution rule 干擾 — 是設計上的自然防護

## 4. Ornament 與框架音的銜接 articulation

Ornament 內部處理一回事，**ornament 與框架音的銜接**是另一回事：

### 4.1 Ornament → 主音

- Trill / mordent 結束音與主音通常 **legato 連接**（resolution）
- Appoggiatura → 主音 一定 legato（這是 appoggiatura 的本意）

對指法的意涵：trill 結束指與主音指應該方便 substitution 或自然 legato 銜接。實作上 ornament fingering 通常已考慮此銜接。

### 4.2 前一框架音 → Ornament 起首

- 通常 detache 或 non-legato 銜接（讓 ornament 起頭清晰）
- 例外：grace note 群組（appoggiatura cluster）需 legato 銜接前後

### 4.3 對未來 score-claude 的影響

若實作 ornament-aware rule（未實作），應：
- Ornament 內部完全跳過 articulation rule
- Ornament 結束與後續主音之間應啟用 legato substitution（resolution 連接）
- Ornament 起首與前一音之間 default non-legato

## 5. Baroque ornament 詮釋的歷史背景

⚠ Training-data verification needed: C.P.E. Bach *Versuch* (1753) 大量論述 Baroque ornament 詮釋：
- Trill 是 Baroque 最重要的單一 ornament（每個 cadence 幾乎都用）
- Mordent 用於 stepwise descending 線條
- Appoggiatura 用於 dissonance-to-consonance resolution

對指法的意涵：演奏 Baroque 時 ornament 比 Romantic 密集得多 — Bach Inventions 大量隱含 ornament（雖未必明確標記），現代 edition 加標記常與 Bach 原意有差異（[src_donington_baroque_music](src_donington_baroque_music.md)）。

## 6. Romantic ornament 的演變

⚠ Training-data verification needed:
- Romantic 時代 ornament 標記**較少**（作曲家直接寫出全部音，不用簡寫）
- 但 fioritura（cadenza-like 自由裝飾段）成為新分類 — Chopin Op.9-2 §7 是典型
- Fioritura 不適用一般 ornament 規則（更長、更自由）

對應 [../wiki_phrase/analysis_chopin_op9_no2_nocturne](../wiki_phrase/analysis_chopin_op9_no2_nocturne.md) §7 + score-claude *project_fioritura_filter_2026-05-28* — fioritura 是 ornament 的浪漫派擴展，需獨立規則處理。

## 7. 與其他 wiki 頁面的關係

- [concept_legato_substitution](concept_legato_substitution.md) §6 — ornament 為 substitution 失效情境
- [concept_non_legato_baroque](concept_non_legato_baroque.md) §例外 — Bach ornament 段的 articulation
- [analysis_bach_inv_articulation](analysis_bach_inv_articulation.md) §4 — Bach Inv 內 sigh motif / ornament 處理
- [analysis_chopin_op9_no2_articulation](analysis_chopin_op9_no2_articulation.md) §3.2-3.5 — Chopin fioritura 處理
- [../wiki_phrase/concept_figural_boundary_detection](../wiki_phrase/concept_figural_boundary_detection.md) — figural pattern 偵測
- [src_donington_baroque_music](src_donington_baroque_music.md) §2.4 — Donington 對 ornament 內部 articulation 的論述

## 8. ⚠ Training-data verification queue

- §2 各 ornament 類型內部 articulation 默認的歷史考證
- §5 C.P.E. Bach Versuch ornament 章節具體頁碼
- §6 Romantic ornament 標記減少 + fioritura 興起的學術論述
