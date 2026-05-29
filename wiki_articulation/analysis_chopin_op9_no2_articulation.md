# Analysis: Chopin Op.9 No.2 — Articulation 詮釋（Romantic legato 預設 + fioritura 特殊處理）

> 來源：Eigeldinger《Chopin Pianist and Teacher》、Henle Urtext (Ekier 校訂)、National Edition (Ekier)、musetrainer/library MXL（已用於 score-claude 驗證）
> 對應 PIG：023（4 annotators）
> 引用方：[../wiki_phrase/analysis_chopin_op9_no2_nocturne](../wiki_phrase/analysis_chopin_op9_no2_nocturne.md) §7 fioritura, [concept_legato_substitution](concept_legato_substitution.md) §5（Op.9-2 為「適用情境」代表）, [concept_articulation_overview](concept_articulation_overview.md) §3 Romantic default, [concept_period_defaults](concept_period_defaults.md) §4 Romantic

## 1. 為什麼挑 Op.9 No.2 作為 Chopin articulation 案例

理由：
- Op.9 No.2 (Eb major Nocturne, 1830-31) 是 Chopin **最知名 + 教學最常用**的 nocturne
- musetrainer/library 提供高品質全曲 MXL（[../wiki_phrase/analysis_chopin_op9_no2_nocturne](../wiki_phrase/analysis_chopin_op9_no2_nocturne.md) 已用於 fioritura validation）
- Slur 標記豐富（74 slurs / 148 notes-in-slur），是 score-claude 已啟用 [concept_legato_substitution](concept_legato_substitution.md) 的對象
- 同曲已在 score-claude 多項驗證（texture phase 2 / fioritura filter / legato substitution）— articulation 分析可整合所有觀察

## 2. Op.9 No.2 articulation 標記統計（musetrainer MXL 實測）

從 score-claude 2026-05-29 驗證：

| Articulation | RH 計數 | LH 計數 |
|---|---|---|
| Slur (notes-in-slur) | 95+ | 53+ |
| Accent (`>`) | 9 | 0 |
| Staccato | 29 | 0 |
| StrongAccent (`^` marcato) | 2 | 0 |
| Staccatissimo (`▼`) | 3 | 0 |
| Fingering (editorial 指法) | 96 | 0 |

→ Op.9-2 是 score-claude 所有測試曲目中 articulation 訊號最豐富的。Chopin 浪漫派的特性：**Slur 大量 + accent / staccato 精選**。

## 3. Op.9 No.2 articulation 結構特徵

### 3.1 主題段 (m1-m12) — 純 legato 主導

- RH melody 完全在 slur 內，沒有 staccato
- LH waltz 三連音 broken-chord 伴奏 — duration ≥ 0.25 QN，自然非 slur 段
- 對 [concept_legato_substitution](concept_legato_substitution.md): m9 + m17 F5 「同音重複 sustained」是經典 substitution 案例（score-claude 已啟用此 rule）

### 3.2 Variation 1 段 (m13-m20) — Fioritura 起點

- Melody 加裝飾音、加速 32nd-note 經過
- m13-14 有 fioritura（連續 32nd-note）— 雖在 slur 內但**duration < 0.5 QN 不適合 substitution**
- score-claude [concept_legato_substitution](concept_legato_substitution.md) §6 + LEGATO_MIN_DURATION gate 正確跳過此段

### 3.3 Variation 1 重現 (m21-m22) — 同 m13-14 pattern

- 結構性重複 fioritura
- 同樣 fioritura filter 跳過

### 3.4 Variation 2 段 (m24, m26, m29) — 32nd-note variation

- 大量 staccato 標記（29 個）— 對比抒情主題
- accent (>) 出現於 sf 強拍
- 對未來 [concept_staccato](concept_staccato.md) DP rule 是高度適用對象

### 3.5 Coda (m33-m35) — 64-note 大型 fioritura + 結尾 cadence

- 連續 64 個 32nd-note ornamental run
- score-claude fioritura filter 已 cover 此段
- 結尾 PAC 解決 + StrongAccent (marcato) 標記

## 4. Chopin articulation 慣例的特點

### 4.1 Slur 即 phrase 結構

⚠ Training-data verification needed: Chopin slur 的長度不只表 legato，常**等同 phrase 範圍**：
- 4-bar phrase = 4-bar slur
- Sub-phrase 用更短 slur 標
- Phrase elision 處（Op.9-2 m12 末 / m13 起）有 slur 重疊 / 銜接

→ 對應 [concept_articulation_overview](concept_articulation_overview.md) §6 提到的「**例外：超長 slur 等同 phrase boundary**」。Op.9-2 部分 long slur 屬此類。

### 4.2 Accent + staccato 是 expressive contrast 工具

Chopin 在 lyrical 主題中**少**用 accent / staccato — 它們的出現本身是「**戲劇性對比**」標記：
- m24 staccato 段 = 變化區段的 articulation 標誌
- m29 accent = 32nd-note 高潮強拍
- m34 StrongAccent = coda 高點戲劇宣告

對指法的意涵：未來 [concept_accent_marcato](concept_accent_marcato.md) DP rule 落地後，這些位置應**強指偏好**（1/2/3）。

### 4.3 Romantic legato default — 與 Bach 對比

| 項目 | Bach Inv (Baroque) | Chopin Op.9-2 (Romantic) |
|---|---|---|
| 默認 articulation | non-legato | legato |
| Slur 標記密度 | 接近 0 | 大量 |
| 演奏家詮釋空間 | 大（必須補 articulation）| 小（信標記）|

→ 演奏 Chopin = honor slur 標記為主；演奏 Bach = honor 時代 default 為主。

## 5. 不同 edition 的 articulation 編輯差異 ⚠

⚠ Training-data verification needed:

| Edition | Slur 處理 | Fingering 處理 |
|---|---|---|
| **Henle Urtext (Müllemann)** | 接近 Ekier National Edition | 編輯加 fingering 標記 |
| **National Edition (Ekier)** | 最接近 Chopin 手稿 + 第一版 | 學術 fingering |
| **Mikuli (Schirmer 1894)** | Chopin 學生 Mikuli 編輯，加大量 fingering + 個別 slur 變動 | 大量 Mikuli fingering 詮釋 |
| **Wiener Urtext** | 折衷 | 中性 |
| **musetrainer/library MXL** | 接近 Henle/Ekier | 含 96 個 Fingering articulation（編輯預設指法）|

→ score-claude 使用 musetrainer 版本，articulation 訊號可靠度高。

## 6. score-claude DP 對 Op.9-2 的啟用狀況

從 *project_legato_substitution_v1_2026-05-29* 與其他 memory：

| Rule | 啟用 | 效果 |
|---|---|---|
| Figural boundary detection | ✓ | mvt4 m50-style 處理浪漫派 figural 邊界 |
| Texture phase 2 (dynamic + pedal) | ✓ | 8 dynamic + 37 pedal spanner 訊號 |
| Fioritura filter | ✓ | m13-14, m21-22, m24, m33-35 範圍跳過 figural boundary |
| Legato substitution (v2) | ✓ | m9, m17 F5 同音換指 4→3 |
| Cadence detection | (off) | – |
| Subject detection | (off) | Op.9-2 無對位主題重現 |
| Long-scale | (off) | – |

→ Op.9-2 是 score-claude 啟用最多 wiki-traceable rules 的曲目，可作為「**整套 system 在 Romantic intermediate 曲目能達成什麼**」的代表案例。

## 7. 未來 articulation rule 落地對 Op.9-2 的預期影響

### 7.1 Staccato hand-jump 鬆綁（未實作）

Op.9-2 RH 有 29 個 staccato 標記，主要在 m24 / m29 variation 段。未來 [concept_staccato](concept_staccato.md) DP rule 落地後：
- m24 staccato 段：DP 應允許 thumb-cross 較自由、hand-jump penalty 減
- 預期 cost 改善：中等（~5-10 cost units RH）

### 7.2 Accent / sforzando 強指偏好（未實作）

Op.9-2 有 9 個 accent + 2 個 StrongAccent。未來 [concept_accent_marcato](concept_accent_marcato.md) rule 落地後：
- 這 11 個音應強指偏好（1/2/3）
- 預期 cost 改善：小（11 個音 × per-音 cost shift）

### 7.3 Tenuto 規則（Op.9-2 似乎無 tenuto 標記，no-op 預期）

## 8. 與其他 wiki 頁面的關係

- [../wiki_phrase/analysis_chopin_op9_no2_nocturne](../wiki_phrase/analysis_chopin_op9_no2_nocturne.md) §7 — fioritura 結構分析（本頁是 articulation 補充）
- [concept_articulation_overview](concept_articulation_overview.md) §3 — Op.9-2 是 Romantic default 典型案例
- [concept_legato_substitution](concept_legato_substitution.md) §5 — Op.9-2 在「適用情境」表中浪漫派 lyrical melody 代表
- [concept_staccato](concept_staccato.md) §4 — Op.9-2 m24 staccato 段為未來測試對象
- [concept_accent_marcato](concept_accent_marcato.md) §4 — Op.9-2 sf 標記為未來測試對象
- [concept_period_defaults](concept_period_defaults.md) §4 — Chopin 為 Romantic legato default 代言
- *project_legato_substitution_v1_2026-05-29* — Op.9-2 legato substitution 啟用 + v2 duration gate
- *project_fioritura_filter_2026-05-28* — Op.9-2 fioritura filter 啟用 + §7 校正

## 9. ⚠ Training-data verification queue

以下基於 training-data 推測：
- §4.1 Chopin slur = phrase 範圍的學術共識（具體文獻引用）
- §5 各 edition 差異精確比較
- §7.1-7.2 對未來 staccato / accent rule 落地的 cost 影響數字（需實際 A/B 跑）
