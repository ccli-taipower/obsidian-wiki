# Composer: Haydn 樂句分段

> 來源：Caplin《Classical Form》§Haydn, Rosen《The Classical Style》, Brendel essays §Haydn
> 引用方：[[concept_classical_period_sentence]], [[concept_cadence_detection]], [[composer_mozart_phrasing]]

## 1. Haydn 樂句的特殊性

Joseph Haydn (1732-1809) 樂句結構是 Classical 形式的**奠基者**：
- **Sentence + Period 結構** 的早期發明者
- **Wit + 意外**：故意打破預期 phrase length（不在標準 4-bar 結束）
- **Sonata form** 標準化：Haydn 主導 18 世紀晚期 sonata form 形成

→ Haydn 是 Classical phrasing 的「**標準範本**」，但其**個性化「驚喜」打破** rules。

## 2. Haydn 樂句邏輯的核心特色

⚠ Training-data verification needed:

### 2.1 Sentence + Period 兩種樂句結構

[[concept_classical_period_sentence]] 詳述：
- **Period**: 4+4 = antecedent + consequent (詢問 + 回答)
- **Sentence**: 2+2+4 = presentation + presentation' + continuation

Haydn 是兩種結構的**早期典型使用者**。Mozart 後續沿用，Beethoven 擴展。

### 2.2 「Surprise」phrase length 打破

Haydn 的**幽默感**展現於樂句結構：
- 期待 4 bar 結束，實際 3 bar 或 5 bar
- 期待 cadence 解決，實際 deceptive cadence
- 期待 rest，實際突然繼續

→ 對 phrase 偵測的意涵：Haydn 段 **hypermeter 不規則性** 略高於 Mozart（仍低於 Brahms / Schumann）。

### 2.3 Sonata form 的樂句層級

⚠ Training-data verification needed: Haydn 對 sonata form 樂句層級貢獻：
- **Phrase** (4-8 bar): basic 樂句單位
- **Theme group** (8-16 bar): 多 phrase 組合成 theme
- **Section** (32-64 bar): exposition / development / recap 大段
- **Movement** (整樂章): 整 sonata movement

→ 樂句**層級嵌套**是 Classical form 核心。

## 3. Haydn 主要鋼琴作品

⚠ Training-data verification needed:

| 作品集 | 樂句特性 | intermediate 適合 |
|---|---|---|
| **Sonatas Hob.XVI** (62 首) | 標準 sonata form, sentence + period | 部分 intermediate (No.34, 37, 38, 50) |
| *Variations* | Theme + variations form | 部分 intermediate |
| *Andante con Variazioni* Hob.XVII:6 | Cantabile 主題 + variations | intermediate |
| *Fantasia in C* Hob.XVII:4 | 自由 fantasia form | advanced |

→ Haydn intermediate 入門 sonata 推薦：**Hob.XVI:34 (e minor)** 或 **Hob.XVI:37 (D major)** — 都是教學標準。

## 4. Haydn 與 Mozart 樂句對比

⚠ Training-data verification needed:

| 屬性 | Haydn | Mozart |
|---|---|---|
| Phrase 規則性 | 較不規則（surprise）| 較規則（balanced） |
| Texture | 簡潔 + clarity | 較豐富 + chromatic |
| Articulation 標記 | 少（依時代 default）| 中（標記精細）|
| 對位段 | 偶見（particularly 後期 quartet）| 中（晚期 K388 等）|
| 教學優先順 | 入門 Classical | 入門 Classical |

→ Haydn 是 Classical 形式「**raw model**」，Mozart 是 Classical 形式「**完成體**」。

## 5. Haydn articulation 標記特性

⚠ Training-data verification needed:

Haydn 標記比 Mozart **更精簡**：
- Slur 標記範圍**簡單**（短 phrase 為主）
- Staccato dot **較少**
- Tenuto **罕見**
- Accent / sf 標記**極少**

→ 對指法系統：Haydn MXL articulation 訊號**少** — 需依時代 default ([[../wiki_articulation/concept_period_defaults]]) 處理。

## 6. Haydn vs Beethoven 早期樂句對比

⚠ Training-data verification needed:

Beethoven 早期作品（Op.49 等）受 Haydn 直接影響：

| 屬性 | Haydn 晚期 | Beethoven 早期 |
|---|---|---|
| Phrase 結構 | Surprise + 不規則 | Surprise + 戲劇對比 |
| 動態變化 | 中等 | 大（pp 至 ff）|
| 對位融合 | 增加（特別 Op.76 quartet）| 增加（特別 Op.18） |
| 標記精細度 | 較少 | 較多（Beethoven 標記革命）|

## 7. 演奏家 Haydn 詮釋

⚠ Training-data verification needed:

| 演奏家 | Haydn 風格 |
|---|---|
| **Marc-André Hamelin** | 細膩 + virtuoso 詮釋 |
| **András Schiff** | 學術派 + lecture-recital |
| **Alfred Brendel** | 字面派 + 結構性 |
| **Sviatoslav Richter** | 個性化 + 戲劇性 |

## 8. 對 score-claude DP 的意涵

Haydn 對 score-claude DP 的對應：
- **intermediate sonata 範圍**：Hob.XVI:34 / Hob.XVI:37 是潛在 in-scope 對象
- 樂句偵測：可借鑑 [[concept_classical_period_sentence]] sentence/period 結構
- Surprise phrase length：對 hypermeter fallback rule 是 stress test

但 score-claude 目前未啟用 Haydn 曲目（cache 待取得）。

## 9. 與其他 wiki 頁面的關係

- [[concept_classical_period_sentence]] — Haydn 是 sentence/period 結構奠基者
- [[concept_hypermeter]] — Haydn 的 surprise 打破規則
- [[composer_mozart_phrasing]] — 同時代 Classical 對比
- [[composer_beethoven_phrasing]] — 受 Haydn 影響的早期 Beethoven
- [[../wiki_articulation/concept_period_defaults]] — Classical 時代 default
- [[../score-claude/memory/project_target_repertoire_intermediate]] — Hob.XVI:34/37 為 intermediate 候選

## 10. ⚠ Training-data verification queue

- §2.2 Haydn surprise phrase length 經典案例的精確段落
- §3 Haydn sonata 對 intermediate 適用度的學術評估
- §5 Haydn articulation 標記精確密度（per Henle Urtext 統計）
- §7 演奏家詮釋差異具體 recording 比較
