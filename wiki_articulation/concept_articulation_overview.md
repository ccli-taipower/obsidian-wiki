# Concept: Articulation Overview — 11 種類型 + 對指法的影響

> 來源：通用 articulation pedagogy + Neuhaus / Matthay / Czerny / Türk / 19 世紀理論家
> 引用方：本 wiki 所有後續 concept 頁的基礎參考

## 1. 為什麼 articulation 對指法重要

兩個音之間怎麼連接（**connection style**），不只是表情問題，**直接決定可用的手指轉換策略**。

當鋼琴家看到「legato」標記時，物理上必須讓前一音的「釋放」與下一音的「彈下」在同一瞬間完成 — 沒有 finger substitution 就無法達成。同理「staccato」要求每音獨立、結束後手指立刻離鍵 — 此時 finger substitution 既無意義也浪費動作；自由的 thumb cross 反而更實用。

所以 articulation 標記不是純粹「演奏效果」的選擇，而是「指法策略」的前置決定。

## 2. 11 種 articulation 完整 taxonomy

依「連接性 → 音長」光譜排序，從最連到最斷：

| # | 名稱 | 符號 | 操作型 (相對音長) | 中文常見譯 |
|---|---|---|---|---|
| 1 | **Legatissimo** | (極致連) | 100% + overlap | 極連 |
| 2 | **Legato** | slur `⌒` | 100% (full duration) | 連奏 |
| 3 | **Portato / Mezzo-staccato** | 點+slur | ~75% | 半連 |
| 4 | **Non-legato** | (無符號 Baroque 默認) | ~85% | 不連 |
| 5 | **Tenuto** | `–` | 100% + 壓重 | 持音 / 保持音 |
| 6 | **Staccato** | `·` | ~50% | 斷奏 |
| 7 | **Staccatissimo** | `▼` | ~25% | 極斷 |
| 8 | **Accent** | `>` | 不變音長，重音 | 重音 |
| 9 | **Marcato** | `^` | ~75% + 強重音 | 強調 |
| 10 | **Sforzando (sfz)** | `sfz` | 不變音長，突重音 | 突強 |
| 11 | **Fermata** | `𝄐` | extend ad lib | 延長 |

註：1-7 是 connection 光譜；8-10 是 dynamic accent overlay；11 是 duration 修飾。可疊加，例如 `sfp` + tenuto 同一個音。

每類詳細指法影響見對應 concept 頁（見 [index](index.md) 索引）。

## 3. 時代 default 差異

當樂譜**沒**有 articulation 標記時，演奏家假設什麼 default：

| 時代 | Default articulation | 對指法的假設影響 |
|---|---|---|
| **Baroque (1600-1750)** | non-legato (~85%) | 不假設 legato bias；目前指法系統的預設行為相對正確（[concept_non_legato_baroque](concept_non_legato_baroque.md)） |
| **Classical (1750-1820)** | 平衡 — 短音 detache，長音 legato | 需以音長分類，短音允許 hand jump、長音偏好 substitution |
| **Romantic (1820-1900)** | legato 為主（除非標記 staccato）| 強烈假設 substitution-friendly；Chopin 浪漫派 melody 段必須觸發 [concept_legato_substitution](concept_legato_substitution.md) |
| **Modernism (1900+)** | 必須有明確標記，無 default | 不適用 default 假設 — 信樂譜原文 |

詳細按時代 default 邏輯見 [concept_period_defaults](concept_period_defaults.md)。

## 4. Articulation 與指法系統的對應關係

每種 articulation 在指法決策中扮演不同角色：

| Articulation | 主要影響 | 詳細頁 |
|---|---|---|
| Legato | 鼓勵 finger substitution、限制 hand jump | [concept_legato_substitution](concept_legato_substitution.md) |
| Staccato / Staccatissimo | 允許 thumb cross、free hand jump | [concept_staccato](concept_staccato.md) |
| Tenuto | 禁用同音換指、強制 hold | [concept_tenuto](concept_tenuto.md) |
| Accent / Marcato / Sforzando | 偏好強指（1/2/3 而非 4/5）| [concept_accent_marcato](concept_accent_marcato.md) |
| Portato | 介於 legato 與 staccato（保守選 legato）| [concept_portato_mezzo_staccato](concept_portato_mezzo_staccato.md) |
| Non-legato (Baroque) | 不假設特殊處理 — 預設行為合理 | [concept_non_legato_baroque](concept_non_legato_baroque.md) |
| Fermata | duration override（指法不受影響）| (無單獨頁) |

## 5. Articulation 訊號從哪來

| 訊號源 | 可靠度 | 取得方式 |
|---|---|---|
| **MXL `<slur>` element** | 高（編輯者明確標記）| music21 `note.spannerSites` → 過濾 Slur |
| **MXL `<articulation>` element** | 高 | music21 `note.articulations` (Staccato / Tenuto / Accent 等類) |
| **編輯者推斷 / urtext editorial** | 中（會有 edition 差異）| 同上但需 edition 標記 |
| **音長 + 時代推論**（無明確標記時）| 中（fallback）| 自訂規則：短音 + Classical = staccato 嫌疑、長音 + Romantic = legato 嫌疑 |
| **演奏家詮釋傳統** | 低（不入指法系統）| 不應 hard-code |

## 6. Articulation 與樂句邊界的區別

**Articulation 是 within-phrase 屬性，不是 phrase 切分訊號**。

| 分段類型 | 來自 | 影響 |
|---|---|---|
| **Phrase boundary** | wiki_phrase 五軸 (rest gap / pitch jump / cadence / subject / texture / figural) | 樂句間獨立優化，free hand reposition |
| **Slur boundary** | articulation slur start/end | 不切樂句；只調整指法 cost conditional |
| **Articulation marking start** | 個別音符標記 (staccato / tenuto / accent) | 不切樂句；只調整該音指法偏好 |

→ Slur 結束**通常**不是 phrase 結束：Chopin lyrical 段一個 phrase 可有多個 slur 子分句；Bach 一個 figure 可橫跨 slur 邊界。

例外：超長 slur（Wagner / Liszt 整段持續 slur）等同 phrase boundary 標記 — 屬罕見浪漫派情境，初中階目標曲目不太遇到。

## 7. 與其他 wiki 頁面的關係

- [index](index.md) — 本 wiki 入口
- 每種 articulation 的詳細指法影響 → 各 `concept_*.md`
- [../wiki_phrase/concept_figural_boundary_detection](../wiki_phrase/concept_figural_boundary_detection.md) — figure 邊界與 slur 邊界的區分
- [../wiki_piano/concept_thumb_technique](../wiki_piano/concept_thumb_technique.md) — staccato 段 thumb-cross 放鬆與 thumb 解剖學的對位
- [../wiki_piano/concept_finger_span_table](../wiki_piano/concept_finger_span_table.md) — substitution 改變了「下一步」的 hand position
