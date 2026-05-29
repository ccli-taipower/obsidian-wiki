# Analysis: Mozart K283 (G major) — Articulation 詮釋（Classical 平衡 標準案例）

> 來源：Henle Urtext (Ulrich Wilker 編), Bärenreiter NBA, Brendel essays §Mozart sonata
> 對應 PIG：011 (K283 mvt1 B0-22)
> 引用方：*project_target_repertoire_intermediate* §Mozart, [concept_period_defaults](concept_period_defaults.md) §4 Classical

## 1. 為什麼挑 K283 作為 Classical 平衡 範例

Mozart Piano Sonata No.5 in G major K283 (1774, Salzburg)。理由：
- score-claude 已有 K283 mvt1 cache（PIG 011 B0-22 excerpt）
- 創作於 Mozart 18 歲，**早期 sonata** — articulation 標記相對精簡（vs 後期 K576, K545 之後標記更精細）
- Sonata form 標準 3 樂章，是分析 Mozart Classical 平衡 articulation 的良好範本
- 已在 score-claude 啟用 `cadence + long_scale` rules（per `SINGLE_PDF_PHRASE_FLAGS`）

## 2. K283 mvt1 (Allegro, G major) articulation 結構 ⚠

⚠ Training-data verification needed:

| 段落 | 小節 | Articulation 特徵 |
|---|---|---|
| Exposition 主題 1 | m1-10 | 跳躍 staccato + 偶 slur 主題 |
| Bridge | m11-22 | 16th-note 經過音段 (large_long_scale enable 對象) |
| Exposition 主題 2 | m23+ | 較 cantabile, slur 範圍變長 |
| Development | m54+ | 對比 articulation 變化頻繁 |
| Recap | m72+ | 重現主題 |

對指法的意涵：
- m1-10 主題：classical staccato + slur 對比模式
- m11-22 16th-note: long-scale thumb-under rule 適用（*project_long_scale_thumb_under*）— 已啟用
- m23+ cantabile：[concept_legato_substitution](concept_legato_substitution.md) 適用對象（未啟用，因為 cache MXL 0 slur）

## 3. K283 mvt2 (Andante, C major) — 慢板 cantabile

⚠ Training-data verification needed:
- 抒情主題，slur 涵蓋長 phrase
- LH 較靜止伴奏
- 結構清晰 3-part form

對指法的意涵：高度 [concept_legato_substitution](concept_legato_substitution.md) 適用 — 但同樣受限於 cache MXL articulation 訊號不足。

## 4. K283 mvt3 (Presto, G major) — 快速 finale

⚠ Training-data verification needed:
- Rondo 結構 + 快速 16th/32nd-note 跑動
- Articulation 對比明顯 — 跳躍主題 vs cantabile 中段

對指法的意涵：[concept_articulation_and_tempo](concept_articulation_and_tempo.md) 強烈適用 — 快速段不可 substitution，需 hand-position-stable 處理。

## 5. score-claude 對 K283 的啟用狀況

從 `SINGLE_PDF_PHRASE_FLAGS["011_Mozart_PSon_K283_G_i_B0-22"]`:

```python
{
    "figural": False, "thumb": False, "subject": False,
    "cadence": True, "texture": False, "long_scale": True,
}
```

- ✓ cadence 偵測 — K283 主要 cadence 邊界（m9 IAC, m22 PAC 等）
- ✓ long_scale_thumb_under — m11-22 16th-note 經過音段適用
- ✗ figural / thumb / subject / legato — 未啟用

未啟用 legato_substitution 原因：cache MXL **0 slur** (Audiveris OMR 對 K283 PIG ScorePDF 抓取失敗)。

## 6. K283 vs K545 vs Op.49 對比

| 屬性 | K283 (1774) | K545 (1788) | Op.49 (1795-97) |
|---|---|---|---|
| 創作年份 | Mozart 18 歲 | Mozart 32 歲 | Beethoven 25 歲 |
| Articulation 標記 | 中等精細 | 精簡明確 | 精細 |
| Cantabile 段 | mvt2 為主 | mvt2 為主 | 部分 mvt2 |
| 快速段 | mvt1 + mvt3 | mvt1 主題段 | mvt2 + mvt1 過渡 |
| 適合 intermediate | 略偏難（mvt1, mvt3） | 經典 facile | 經典 intermediate |
| score-claude 啟用程度 | 中（cadence+long_scale）| 中（同 K283） | 0（MXL 待取得） |

→ K283 是「**Mozart sonata articulation 教學早期 sample**」的良好代表。

## 7. 對 score-claude DP 的未來方向

要充分啟用 K283 articulation rules，需要：

1. **取得品質佳的 MXL** — Henle digital 或 Musescore 高品質版（per Op.9 No.2 musetrainer 經驗）
2. **驗證 slur 訊號數** — 預期 30-50 slurs（Mozart sonata 典型密度）
3. **啟用 legato_substitution** — 對 mvt2 Andante 高度適用
4. **加 figural** — 對 mvt1 / mvt3 跳躍 + 16th-note 段適用
5. **加 thumb**（保守）— K283 LH 較傳統 alberti，thumb 限制不易踩 breach

## 8. 演奏家對 K283 articulation 詮釋

⚠ Training-data verification needed:

| 演奏家 | K283 風格 |
|---|---|
| **Mitsuko Uchida** | 細膩 articulation，每 motif 精雕 |
| **András Schiff** | Classical 平衡 + 略 cantabile |
| **Daniel Barenboim** | 較大開大合，articulation 對比鮮明 |
| **Robert Levin** | HIP 派 — 用 fortepiano 演奏，articulation 接近時代實踐 |

## 9. 與其他 wiki 頁面的關係

- *project_target_repertoire_intermediate* §Mozart — K283 為 intermediate 推薦曲目
- [concept_period_defaults](concept_period_defaults.md) §4 — K283 為 Classical 平衡 default 案例
- [concept_legato_substitution](concept_legato_substitution.md) §5 — K283 mvt2 為「適用情境」表中 Classical 慢板代表
- [concept_articulation_and_tempo](concept_articulation_and_tempo.md) — K283 mvt3 Presto 為快速段 substitution gate 適用例
- [analysis_mozart_k545_articulation](analysis_mozart_k545_articulation.md) — Mozart 兄弟曲目對比
- *project_cadence_phase_2* — K283 cadence 偵測啟用

## 10. ⚠ Training-data verification queue

- §2-4 各樂章 articulation 結構（精確段落分布）
- §3 K283 mvt2 cantabile 段具體小節
- §8 演奏家風格差異具體 timestamps
