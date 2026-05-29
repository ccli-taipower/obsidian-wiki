# Concept: Grouping Preference Rules (GPR) — GTTM 樂句分組規則

> 來源：Lerdahl-Jackendoff《A Generative Theory of Tonal Music》(GTTM, 1983), MIT Press
> 引用方：[src_lerdahl_jackendoff_gttm](src_lerdahl_jackendoff_gttm.md), [concept_figural_boundary_detection](concept_figural_boundary_detection.md), [concept_phrase_elision](concept_phrase_elision.md)

## 1. GTTM 框架簡介

*A Generative Theory of Tonal Music* (1983) 是 Fred Lerdahl + Ray Jackendoff 的合著，將 Chomsky 生成語法理論套用到調性音樂分析。書提出**四個分析層**：
1. **Grouping Structure** (分組結構): 音樂如何切分為 phrase / motif / section
2. **Metrical Structure** (節拍結構): 強弱 + hypermeter
3. **Time-Span Reduction** (時間段化簡): 多層級重要性 hierarchy
4. **Prolongational Reduction** (延展化簡): 和聲張力 + 解決

本頁聚焦 **Grouping Structure** 的 **Preference Rules (GPR)**。

## 2. Grouping Preference Rules (GPR) 七條 ⚠

⚠ Training-data verification needed:

| GPR | 描述 |
|---|---|
| **GPR 1** | Avoid degenerate grouping（避免單音分組）|
| **GPR 2a** (slur/rest) | Slur 結束 / rest 後 → 分組邊界 |
| **GPR 2b** (attack-point) | Attack-point 間隔大 → 分組邊界 |
| **GPR 3a** (register) | 音域大跳 → 分組邊界 |
| **GPR 3b** (dynamics) | 動態變化 → 分組邊界 |
| **GPR 3c** (articulation) | Articulation 變化 → 分組邊界 |
| **GPR 3d** (length) | Note length 變化 → 分組邊界 |
| **GPR 4** | 結構性 parallelism → 重複結構暗示分組邊界 |
| **GPR 5** | Symmetry → 對稱分組偏好 |
| **GPR 6** | 偏好局部小 grouping 嵌套於大 grouping |
| **GPR 7** | Time-span reduction 一致性 |

→ 多條規則**可能衝突** — 系統需 weight 或 ranking 決定優先順。

## 3. GPR 與 score-claude DP 對應

⚠ Training-data verification needed: score-claude `_detect_phrase_starts` 是 GPR 啟發的具體實現：

| GPR | score-claude 對應 cost rule |
|---|---|
| GPR 2a (rest/slur) | Pass 1 hard break: rest gap > REST_THRESHOLD_BEATS, slur 結束 |
| GPR 2b (attack-point) | Pass 1 hard break: measure number gap |
| GPR 3a (register) | Pass 1 hard break: pitch jump > PHRASE_BREAK_THRESHOLD |
| GPR 3b (dynamics) | Texture phase 2: dynamic 變化 ([concept_texture_change_detection](concept_texture_change_detection.md)) |
| GPR 3c (articulation) | Articulation 訊號（slur boundary）— 但未直接切 phrase |
| GPR 3d (length) | Cadential pause: long note 標誌 |
| GPR 4 (parallelism) | Subject re-entry ([concept_subject_imitation_detection](concept_subject_imitation_detection.md)) |
| GPR 5 (symmetry) | Hypermeter 4-bar fallback ([concept_hypermeter](concept_hypermeter.md)) |

→ score-claude DP 約 70% 對應 GPR 框架，部分擴展（cadence detection, fioritura filter）。

## 4. GPR 與其他 phrase 理論的對比

⚠ Training-data verification needed:

| 理論 | 主要差異 |
|---|---|
| **GTTM (Lerdahl-Jackendoff 1983)** | Preference rules + 多層 hierarchy + 跨時代適用 |
| **Schenker** | Reduction tree + 和聲 prolongation 為主，較不重 surface 分組 |
| **Riemann** | Function 理論 + cadence-driven phrasing |
| **Caplin (Classical Form)** | Sentence/period 結構為主，限 Classical |
| **Cooper-Meyer (Rhythmic Structure)** | 節奏分組 + 大小單位嵌套 |

GTTM 是 20 世紀後**最系統化 + 跨時代適用**的 phrase 理論。

## 5. GPR 規則的衝突解決

⚠ Training-data verification needed:

GPR 規則經常衝突，例如：
- GPR 3a (register jump) 暗示分組
- GPR 5 (symmetry) 暗示**不**分組 (打破對稱)

GTTM 不給 hard ranking — 留給聽者 / 分析者主觀判斷。對演算法的意涵：
- 需要 weighted 整合多 GPR 訊號
- score-claude DP 用 cost-based 加權處理

## 6. GPR 在不同時代的適用

⚠ Training-data verification needed:

| 時代 | GPR 適用度 |
|---|---|
| **Baroque (Bach)** | 中 — 對位作品 GPR 4 (parallelism) 特別重要 |
| **Classical (Mozart/Haydn)** | 高 — GPR 5 (symmetry) 強烈適用 |
| **Romantic (Chopin/Brahms)** | 高 — GPR 3b, 3c (動態 + articulation) 重要 |
| **Modernism (Debussy/Bartók)** | 中 — 部分 GPR (3a, 3b) 仍適用，部分（4, 5）失效 |

## 7. GPR 對 score-claude DP 的未來改進方向

⚠ 未實作 ideas:

1. **GPR 3c (articulation) explicit hook**: 把 slur boundary 加入 phrase boundary 訊號（特別 Romantic 段）
2. **GPR 4 (parallelism) 擴展**: 不只 subject re-entry，加 phrase-level parallelism 偵測
3. **GPR weight tuning**: per-時代調整 GPR 各規則 weight
4. **GPR conflict resolution**: 當多 GPR 訊號衝突時的具體 cost integration 機制

## 8. 與其他 wiki 頁面的關係

- [src_lerdahl_jackendoff_gttm](src_lerdahl_jackendoff_gttm.md) — GTTM 原書詳細介紹
- [concept_figural_boundary_detection](concept_figural_boundary_detection.md) — Pass 4 figural 偵測對應 GPR 3a/3d
- [concept_phrase_elision](concept_phrase_elision.md) — GTTM 對 phrase elision 的處理
- [concept_cadence_detection](concept_cadence_detection.md) — Cadence 偵測對應 GPR 4 結構性
- [concept_subject_imitation_detection](concept_subject_imitation_detection.md) — Subject 偵測對應 GPR 4 (parallelism)
- [concept_texture_change_detection](concept_texture_change_detection.md) — Texture 偵測對應 GPR 3b
- [concept_hypermeter](concept_hypermeter.md) — Hypermeter 對應 GPR 5 (symmetry)

## 9. ⚠ Training-data verification queue

- §2 GPR 七條的精確德文 / 英文原文（從 1983 原書）
- §3 score-claude DP 對 GPR 對應的精確驗證
- §4 各 phrase 理論對比的學術文獻
- §6 各時代 GPR 適用度的學術考證
