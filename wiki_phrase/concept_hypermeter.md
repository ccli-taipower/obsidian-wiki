# Concept: Hypermeter — 大週期感

> 來源：Rothstein《Phrase Rhythm in Tonal Music》(1989), Cooper-Meyer《The Rhythmic Structure of Music》(1960), Lerdahl-Jackendoff《A Generative Theory of Tonal Music》(1983)
> 引用方：[[concept_phrase_elision]], [[composer_brahms_phrasing]], [[composer_schumann_phrasing]]

## 1. Hypermeter 是什麼

Hypermeter（**hyper-measure / 大週期**）= 多個 measure 組成的**高層級節奏結構**。最常見：
- **2-bar hypermeter**：兩 bar 為一單位（簡單 dance form）
- **4-bar hypermeter**：四 bar 為一單位（**最常見 Classical / Romantic phrase length**）
- **8-bar hypermeter**：八 bar 為一單位（period form 的標準）

Hypermeter 與 phrase 不同：
- **Measure** = 小節 (3-4 beats)
- **Hypermeter unit** = 多 bar 大週期感
- **Phrase** = 完整音樂語法單位（4-bar / 8-bar 為主）

→ Hypermeter 常與 phrase 重合，但**不一定**等同。

## 2. Hypermeter 的判定

⚠ Training-data verification needed:

判定 hypermeter 的訊號：
| 訊號 | 解釋 |
|---|---|
| **強弱 pattern** | 4-bar hypermeter: bar 1 強, bar 2 弱, bar 3 中, bar 4 弱 |
| **和聲節奏** | 4-bar phrase: bar 1 tonic, bar 4 cadence (PAC / IAC / HC) |
| **Melodic 結構** | 4-bar phrase: bar 1 開始 motif, bar 4 解決 motif |
| **舞蹈節奏** | Waltz 3/4 → 4-bar hypermeter (每 phrase 12 beat); Mazurka 同樣 |

## 3. Hypermeter 與 phrase 的對應

⚠ Training-data verification needed:

| 對應 | 例子 |
|---|---|
| **1:1 (phrase = hypermeter unit)** | Mozart sonata phrase 普遍 4-bar = 4-bar hypermeter |
| **2:1 (phrase = 2 hypermeter units)** | Chopin lyrical melody 常 8-bar phrase = 2 個 4-bar hypermeter |
| **不對應** | Brahms 的 5-bar phrase 在 4-bar hypermeter 上「**錯位**」（結構性張力） |

→ 對 score-claude DP 的對應：phrase boundary 偵測常假設 4-bar fallback（[[../score-claude/run.py]] `_detect_phrase_starts` Pass 2 fallback）— 是 4-bar hypermeter 假設的具體實現。

## 4. Hypermeter 在不同時代

⚠ Training-data verification needed:

| 時代 | Hypermeter 規則性 |
|---|---|
| **Baroque** (Bach / Couperin) | **不規則** — 對位作品 phrase length 變化大 |
| **Classical** (Haydn / Mozart) | **規則 4-bar 為主**，偶有 surprise 不規則 |
| **Romantic early** (Schubert / Schumann) | 規則 4-bar + 偶有末尾延長 |
| **Romantic late** (Brahms) | **不規則為標誌** — 3-bar, 5-bar, 7-bar 並存 |
| **Modernism** (Debussy / Bartók) | 高度不規則 / 自由節奏 |

→ Hypermeter 規則性與時代有強相關。

## 5. Phrase Expansion + Contraction

⚠ Training-data verification needed:

Rothstein 1989 主要貢獻：詳述「**phrase 擴張 + 收縮**」現象：

| 現象 | 描述 |
|---|---|
| **Expansion** | 4-bar phrase 擴展為 5-bar / 6-bar — 透過 sequence / cadential extension |
| **Contraction** | 4-bar phrase 收縮為 3-bar / 2-bar — 透過 elision |
| **Suspension** | Phrase 結束延後 — phrase 同時兼具結束 + 開始 |
| **Imbroglio** | 多種 phrase rhythm 同時進行（罕見複雜）|

→ 對 phrase 偵測的意涵：實際樂句 phrase length 常**不等同**hypermeter 整數倍。

## 6. Hypermeter vs Phrase Elision

[[concept_phrase_elision]] 是「**前 phrase 結束音同時是後 phrase 起首音**」現象。Phrase elision 對 hypermeter 的影響：
- 兩個 4-bar phrase elision → 視角看是 8-bar 還是 7-bar
- Hypermeter 計數可能因 elision 而**錯位**

## 7. 對 score-claude DP 的意涵

DP 處理 hypermeter：
- `_detect_phrase_starts` Pass 2 fallback: 無硬斷點時，4-bar phrase length 假設
- Pass 3 soft breaks: 在 4-bar 倍數位置插 boundary
- 對 Brahms / Bartók 等不規則 hypermeter 段：4-bar fallback 失效

未實作改進方向：
- **作曲家-aware hypermeter**：對 Brahms 不假設 4-bar regularity
- **Adaptive phrase length detection**：依 cadence 自動推測 phrase length
- **Phrase expansion / contraction detection**：偵測 5-bar / 3-bar 變異

## 8. Hypermeter 與舞曲節奏

⚠ Training-data verification needed:

舞蹈 form 對 hypermeter 有強烈規範：
- **Waltz** (3/4): 4-bar hypermeter, 12-beat phrase
- **Mazurka** (3/4): 4-bar hypermeter, 但 accent on beat 2 或 3
- **Polonaise** (3/4): 4-bar hypermeter + 進行曲節奏
- **Gigue** (6/8): 4-bar hypermeter + 12-beat group
- **Minuet** (3/4): 8-bar binary section + 4-bar hypermeter

→ Dance form 是 hypermeter 規則性最強的曲目類別 — 適合 4-bar fallback 假設。

## 9. 與其他 wiki 頁面的關係

- [[concept_phrase_elision]] — Phrase elision 對 hypermeter 計數的影響
- [[concept_classical_period_sentence]] — Period (8-bar) 是 hypermeter 與 phrase 對應典型
- [[composer_brahms_phrasing]] — Brahms 不規則 hypermeter 代表
- [[composer_schumann_phrasing]] — Schumann 規則 4-bar + 末尾延長
- [[composer_mozart_phrasing]] — Mozart 規則 hypermeter 典範
- [[composer_bach_phrasing]] — Bach 對位作品 hypermeter 不規則
- [[src_rothstein_phrase_rhythm]] — Rothstein 1989 hypermeter 系統論述
- [[src_lerdahl_jackendoff_gttm]] — GTTM 對 metrical structure 的論述

## 10. ⚠ Training-data verification queue

- §3 不同 phrase:hypermeter 對應的具體 example
- §4 各時代 hypermeter 規則性的學術考證
- §5 Phrase expansion / contraction 在 Rothstein 1989 的具體章節
- §8 各 dance form hypermeter 規範的學術共識
