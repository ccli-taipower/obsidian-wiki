# Concept: Baroque Phrasing — 巴洛克樂句邏輯

> 來源：Donington《Baroque Music: Style and Performance》, C.P.E. Bach *Versuch*, Mattheson *Der vollkommene Capellmeister* (1739)
> 引用方：[composer_bach_phrasing](composer_bach_phrasing.md), [composer_scarlatti_phrasing](composer_scarlatti_phrasing.md), [concept_fugue](concept_fugue.md), [concept_counterpoint](concept_counterpoint.md)

## 1. Baroque 樂句不能套用 Classical 邏輯

Baroque（1600-1750）樂句結構與後續 Classical / Romantic **根本不同**：
- **對位主導**：每聲部獨立 phrase，無「**整曲統一 phrase**」
- **動機 + 序列為主**：不是 antecedent + consequent period 結構
- **Hypermeter 弱化**：較少 4-bar 規則
- **舞曲 form 主導**：suite 各舞曲 form 決定 phrase length
- **Fortspinnung (繼續展開)**：phrase 不結束 — 持續展開到段尾

→ 套用 Mozart / Chopin 樂句邏輯到 Bach 會錯。

## 2. Baroque 主要 phrase 結構類型

⚠ Training-data verification needed:

### 2.1 Fortspinnung 結構

**Fortspinnung** (繼續展開) 是 Baroque 最常見 phrase 邏輯：
- Vordersatz (前段)：主題陳述
- Fortspinnung (繼續展開)：序列發展、persistent motion
- Epilog (結尾)：cadential 收結

→ 比 Classical period (4+4 對稱) 更**單向流動**。

### 2.2 對位 phrase

對位作品（fugue, invention, sinfonia）：
- 每聲部獨立 phrase，多聲部 phrase 不重合
- Subject + counter-subject + episode 結構決定 phrase
- 詳見 [concept_fugue](concept_fugue.md) + [concept_counterpoint](concept_counterpoint.md)

### 2.3 舞曲 form

Baroque suite 各 dance 對 phrase 有特定規範：
- **Allemande**: 不規則 phrase, often 從 anacrusis 開始
- **Courante**: 3/2 或 6/4, 流動 phrase
- **Sarabande**: 3/4, 強拍在 beat 2, slow + cadential
- **Gigue**: 6/8 / 12/8, 對位 + fast tempo
- **Minuet** (Baroque 末): 3/4, 4-bar phrase 開始規則化

→ Dance form 對 phrase 規範不同於 Classical sonata form。

### 2.4 Aria + Recitative (Opera 影響)

Baroque opera aria 結構影響 keyboard:
- **Da capo aria** (ABA): 兩段對比 + 再現
- **Ground bass / Chaconne / Passacaglia**: 持續 bass + 上聲部變奏
- 對應 keyboard variations

## 3. Cadence 在 Baroque 的特殊性

⚠ Training-data verification needed:

Baroque cadence types：
| Cadence | 描述 |
|---|---|
| **Authentic cadence (V-I)** | 主要 cadence，類似後續時代 |
| **Half cadence (V)** | 段中 phrase 收結 |
| **Plagal cadence (IV-I)** | 「Amen」cadence，在 prelude / chorale 用 |
| **Deceptive cadence (V-vi)** | 戲劇性意外 |
| **Phrygian cadence (iv6-V)** | 模式性 cadence，特別在 minor 段 |

→ Baroque cadence 多元 — 是 phrase 偵測主要訊號 ([concept_cadence_detection](concept_cadence_detection.md))。

## 4. Hemiola — Baroque 特殊 phrase 訊號

⚠ Training-data verification needed:

**Hemiola** = 3/4 拍中**兩 bar 視為一個 6/4 大 bar**（2 個 dotted half-note）：
- 常見於 Sarabande、Allemande 末尾
- 是 phrase 結束的**結構性標記**
- 對指法的意涵：hemiola 段 hand-position 需 stability 維持

→ Hemiola 是 Baroque-specific phrase signal，後續 Classical 罕見。

## 5. Baroque vs Classical phrase 對比

⚠ Training-data verification needed:

| 屬性 | Baroque | Classical |
|---|---|---|
| 主導 phrase 結構 | Fortspinnung + 對位 | Period / Sentence |
| Hypermeter 規則性 | 弱 | 強（4-bar 為主）|
| 對稱性 | 弱 — phrase 自由發展 | 強 — antecedent + consequent |
| 主題重複 | 序列為主（變化重複）| 對稱重複（identical 或近似）|
| Cadence 在 phrase 中的位置 | Phrase 末 + 偶見段中 | 嚴格 phrase 末 |
| 樂句長度 | 不規則 — 5-bar, 7-bar, 13-bar 都常見 | 規則 — 多 4-bar / 8-bar |

## 6. Baroque keyboard 主要作曲家 phrase 風格

⚠ Training-data verification needed:

| 作曲家 | Phrase 風格 |
|---|---|
| **J.S. Bach** | 對位主導 + Fortspinnung + 序列；fugue / invention 為主 (參 [composer_bach_phrasing](composer_bach_phrasing.md)) |
| **G.F. Handel** | 對位 + opera 影響；suite + concerto grosso |
| **D. Scarlatti** | Binary form, 不規則 phrase, Iberian 影響 (參 [composer_scarlatti_phrasing](composer_scarlatti_phrasing.md)) |
| **F. Couperin** | Ordres (suite) 各 movement；ornament 密集 + agréments |
| **J.-P. Rameau** | French ordres；harmony 理論家 (Traité de l'harmonie) |
| **C.P.E. Bach** | 過渡期 — Baroque 對位 + Empfindsamer Stil 抒情 |

## 7. 對 score-claude DP 的意涵

DP 對 Baroque phrase 處理：
- [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 是 Baroque 對位作品的主要 phrase 偵測軸
- [concept_cadence_detection](concept_cadence_detection.md) 適用 Baroque cadence
- **不適合** 4-bar fallback (Pass 2)：Baroque phrase 規則性弱
- [../wiki_articulation/concept_non_legato_baroque](../wiki_articulation/concept_non_legato_baroque.md) default 對 articulation 處理

對 Bach 12/15 mvts 啟用實證（*project_bach_inv_subject_detection_validation_2026-05-28*）：subject detection + figural + thumb 配合是 Baroque 主軸。

## 8. Baroque 樂句邏輯與 fingering 慣例

⚠ Training-data verification needed:

Baroque fingering 慣例（pre-Bach 5-finger system）：
- **不一定**用 thumb（pre-Bach 傳統）
- Bach 引入 thumb-pass 變革
- Paired fingering (3-4, 2-3) 為 ornament 標準
- 詳見 [../wiki_articulation/src_couperin_lart_de_toucher](../wiki_articulation/src_couperin_lart_de_toucher.md)（法國派）+ [../wiki_articulation/src_cpe_bach_versuch](../wiki_articulation/src_cpe_bach_versuch.md)（德國派）

## 9. 與其他 wiki 頁面的關係

- [composer_bach_phrasing](composer_bach_phrasing.md) — Bach 是 Baroque 對位主要代表
- [composer_scarlatti_phrasing](composer_scarlatti_phrasing.md) — Scarlatti 是 Iberian Baroque 對比
- [concept_fugue](concept_fugue.md) / [concept_counterpoint](concept_counterpoint.md) — 對位作品結構詳述
- [concept_cadence_detection](concept_cadence_detection.md) — Baroque cadence 偵測
- [concept_subject_imitation_detection](concept_subject_imitation_detection.md) — Subject re-entry 為主要 phrase 訊號
- [concept_hypermeter](concept_hypermeter.md) §4 — Hypermeter 規則性對 Baroque 弱
- [../wiki_articulation/concept_non_legato_baroque](../wiki_articulation/concept_non_legato_baroque.md) — Baroque articulation default
- [../wiki_articulation/src_cpe_bach_versuch](../wiki_articulation/src_cpe_bach_versuch.md) / [../wiki_articulation/src_couperin_lart_de_toucher](../wiki_articulation/src_couperin_lart_de_toucher.md) — Baroque pedagogy 一手文獻
- [../wiki_articulation/src_donington_baroque_music](../wiki_articulation/src_donington_baroque_music.md) — HIP 派 Baroque 演奏實踐回顧

## 10. ⚠ Training-data verification queue

- §2.1 Fortspinnung 結構的具體 Baroque 案例
- §4 Hemiola 在 Baroque 各 dance form 的精確使用
- §6 各 Baroque 作曲家 phrase 風格的學術考證
- §8 Pre-Bach paired fingering 的具體歷史
