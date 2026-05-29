# Analysis: Clementi Sonatina Op.36 — Articulation 詮釋（intermediate 入門 sonata）

> 來源：Henle Urtext (Heinz Schüngeler 編), Wiener Urtext, Czerny *Op.500* §Clementi 引述
> 對應 PIG：未列入
> 引用方：*project_target_repertoire_intermediate* §推薦曲目, [concept_period_defaults](concept_period_defaults.md) §Classical balance

## 1. 為什麼挑 Op.36 作為 intermediate 入門 sonata 範例

Muzio Clementi (1752-1832) Op.36 (1797 出版)，共 6 首 Sonatinas（No.1-6）。理由：
- 整套都是初中階學生「**第一首奏鳴曲**」的標準選擇（Op.36 No.1 in C major 特別常用）
- Clementi 是 Classical 時期 keyboard teacher，作品設計**明確 articulation 標記**，是教學鋼琴 articulation 慣例的理想範本
- 比 Mozart K545 結構更簡單（Sonatina = 簡化 sonata），articulation 變化更可預期

## 2. Op.36 No.1 (C major) — 標準入門案例

### 2.1 mvt1 Allegro 結構與 articulation ⚠

⚠ Training-data verification needed:

| 段落 | 小節 | Articulation 特徵 |
|---|---|---|
| Exposition 主題 1 | m1-8 | RH detache scale + LH alberti bass (no slur) |
| Bridge / 過渡 | m9-12 | 16th-note 經過，部分 slur |
| Exposition 主題 2 | m13-20 | 更 cantabile，slur 涵蓋短 phrase |
| Development | m21-30 | 對比段，articulation 變化頻繁 |
| Recapitulation | m31-end | 重現主題，articulation 對應 exposition |

對指法的意涵：典型 Classical 平衡 — 短音 detache（[concept_period_defaults](concept_period_defaults.md) §4 短音 default）+ 長音 legato。

### 2.2 mvt2 Andante (F major) ⚠

⚠ Training-data verification needed:
- 抒情主題，3-part form (A-B-A')
- A 段：legato melody + 簡單 LH 伴奏
- B 段：較動態，部分 detache
- A' 段：重現 + 微裝飾

對指法的意涵：A 段是 [concept_legato_substitution](concept_legato_substitution.md) 適用對象（slow tempo + slur melody）。

### 2.3 mvt3 Vivace ⚠

⚠ Training-data verification needed:
- 快速 rondo
- 主題 detache + 跳躍
- Refrain 段對比明顯

對指法的意涵：rondo theme detache 段是 [concept_staccato](concept_staccato.md) 適用對象（未實作）。

## 3. Op.36 整體 articulation 特徵

⚠ Training-data verification needed:

| 特徵 | 出現頻率 |
|---|---|
| Slur 標記密度 | 中高 — Clementi 對教學考慮，標記明確 |
| Staccato dot | 中高 — Classical detache 段標明確 |
| Tenuto | 罕見 — Classical 早期較少使用 |
| Accent (`>`) | 偶見 — 主要在強拍 |
| Fermata | 偶見 — 樂章結尾、cadenza 段 |

→ 整體 articulation 訊號比 Bach Inv 豐富很多，比 Mozart K545 更系統化（因為是教學作品）。

## 4. 與其他入門 sonata 的對比

| 曲目 | 難度 | Articulation 系統化程度 | 適合教學什麼 |
|---|---|---|---|
| **Clementi Op.36 No.1** | 入門 | 高 — 標記明確 | 第一首 sonata |
| **Mozart K545** | 入門-中階 | 中 — Mozart 風格較精簡 | Classical 平衡 |
| **Beethoven Op.49 No.1/2** | 入門-中階 | 高 — Beethoven 標記精細 | Beethoven 入門 |
| **Kuhlau Op.20 Sonatinas** | 入門 | 高 — 與 Clementi 同類 | Clementi 替代曲目 |
| **Diabelli Op.151 Sonatinas** | 入門 | 中 | 補充曲目 |

→ Clementi Op.36 No.1 是「**入門 Classical sonata articulation 教學**」的標準選擇。

## 5. 對 score-claude DP 的影響預測

⚠ MXL 待取得（musetrainer / IMSLP / Henle digital）。預期：

- Slur 訊號充足 → [concept_legato_substitution](concept_legato_substitution.md) 可啟用（特別 mvt2 Andante）
- Staccato 標記充足 → 未來 [concept_staccato](concept_staccato.md) DP rule 測試對象
- 整體 config 建議：`figural + thumb + legato_substitution`（per Classical 標準）

啟用順序建議：
1. 取得 Op.36 No.1 mvt2 (Andante) MXL — 最 lyrical，slur 標記最豐富
2. 啟用 figural + thumb（standard Classical config）
3. 加 legato_substitution + 驗證 cost red-line（per Op.9-2 經驗）

## 6. Clementi 教學派系對後續教學的影響

Clementi 是 19 世紀 keyboard teaching 重要人物：
- 倫敦 keyboard scene 領袖（與 Beethoven 同時代）
- 學生包含 John Field (Nocturne 形式發明者)、Cramer（練習曲作者）
- *Gradus ad Parnassum* (Op.44) 是 19 世紀練習曲標準教材
- 影響 Czerny、後續 Russian school

→ Op.36 articulation 標記反映「**Clementi 派教學系統化**」的傳統，比 Mozart 個人風格化標記更可預期、更教學友善。

## 7. 與其他 wiki 頁面的關係

- *project_target_repertoire_intermediate* §推薦曲目 — Op.36 No.1/3 在 in-scope list
- [concept_period_defaults](concept_period_defaults.md) §4 — Classical 平衡 default 典型案例
- [concept_legato_substitution](concept_legato_substitution.md) §5 — mvt2 lyrical 段適用
- [concept_staccato](concept_staccato.md) §4 — mvt3 rondo theme 適用
- [analysis_mozart_k545_articulation](analysis_mozart_k545_articulation.md) — 同時代 sonata 對比
- [analysis_beethoven_op49_articulation](analysis_beethoven_op49_articulation.md) — Clementi vs Beethoven Classical 平衡比較
- [src_czerny_op500_articulation](src_czerny_op500_articulation.md) — Czerny 對 Clementi 教學傳承的提及

## 8. ⚠ Training-data verification queue

- §2 各樂章 articulation 標記精確分布
- §3 整體 articulation 標記密度數據
- §5 MXL 取得後的實際 articulation 統計
