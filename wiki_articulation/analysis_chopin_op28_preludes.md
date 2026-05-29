# Analysis: Chopin Preludes Op.28 — Articulation 詮釋（intermediate Romantic 入門）

> 來源：Henle Urtext (Norbert Müllemann), National Edition (Ekier), Eigeldinger *Chopin Pianist and Teacher*
> 對應 PIG：028 (Op.28 No.17, A♭ major, 1839)
> 引用方：*project_target_repertoire_intermediate* §Chopin, [concept_period_defaults](concept_period_defaults.md) §4 Romantic

## 1. 為什麼挑 Op.28 Preludes 作為 intermediate Romantic 案例

Chopin *24 Preludes* Op.28 (1836-39)，24 首對應 24 個大小調。理由：
- **長度短**：每首 1-3 分鐘，學生短期可掌握
- **難度跨度大**：從**極簡單**（No.4 e minor, No.7 A major）到**極難**（No.16 b♭ minor, No.24 d minor）
- **intermediate 適合 No.4, 6, 7, 20**：典型「簡單 Chopin 入門」選擇
- Chopin **articulation 標記詳細** — 浪漫派 slur + accent + pedal 標記完整

## 2. Intermediate-適合的 Op.28 Preludes 概覽 ⚠

⚠ Training-data verification needed:

| No. | Key | 長度 | Articulation 特性 | 難度 |
|---|---|---|---|---|
| **4** | E minor | 25 bars | 極簡 RH melody + LH 重複和弦 | 入門 |
| **6** | B minor | 26 bars | LH melody + RH 簡單伴奏（cello 風）| 入門-中階 |
| **7** | A major | 16 bars | 4-bar phrase 重複 + 結尾 cadence | 入門 |
| **15** | D♭ major (雨滴) | 89 bars | A-B-A' 結構, A 段 lyrical | 中階 |
| **20** | C minor | 13 bars | 莊嚴 chord progression | 入門-中階 |

→ **No.4, 6, 7, 20** 是 intermediate 教學標準選擇。

## 3. Op.28 No.4 (E minor) — 極簡 Romantic 入門 ⚠

⚠ Training-data verification needed:

結構：
- RH 持續長 phrase melody（slur 涵蓋全曲一大段）
- LH 8th-note 和弦持續伴奏（單一節奏 pattern）
- Tempo Largo — 慢速

對指法的意涵：
- RH melody 高度 [concept_legato_substitution](concept_legato_substitution.md) 適用（slow + slur + 同音重複偶見）
- LH 持續和弦 — voicing 重要，articulation 較單一
- pedal 持續踩 — 增強 legato 聲響但不替代 finger legato

## 4. Op.28 No.6 (B minor) — LH melody 案例

⚠ Training-data verification needed:

結構特殊性：
- **LH 是主旋律**（cello-like 低音線條）
- RH 是伴奏（簡單 8th-note 和弦）
- 對指法：LH 需 cantabile + substitution；RH 需穩定伴奏

對指法的意涵：
- LH 啟用 [concept_legato_substitution](concept_legato_substitution.md) 對主旋律有效
- RH 不需要 substitution（伴奏角色）
- 兩手 articulation 處理不對等 — 是 [concept_articulation_in_polyphony](concept_articulation_in_polyphony.md) §3 範例

## 5. Op.28 No.7 (A major) — 4-bar phrase 標準

⚠ Training-data verification needed:

結構：
- 4-bar phrase × 4 = 16 bars
- Slur 涵蓋每 4-bar phrase 完整
- Cadence 在 m16 PAC

對指法的意涵：
- Slur ≡ phrase（[concept_slur_phrase_overlap](concept_slur_phrase_overlap.md) §2.2 案例）
- 每 4-bar phrase 結束是手位 free reset 點
- [concept_legato_substitution](concept_legato_substitution.md) 在 slur 內適用

## 6. Op.28 No.20 (C minor) — 莊嚴 chord 案例

⚠ Training-data verification needed:

結構：
- 連續 chord progression（funeral-march 風格）
- 短 13 bars, 3 段 (A-A'-A" with pedal differences)
- 大量 tenuto 標記（持音 + 重）

對指法的意涵：
- Chord voicing 重要
- [concept_tenuto](concept_tenuto.md) 強指偏好 — 該段大量 tenuto 標記
- 不適用 [concept_legato_substitution](concept_legato_substitution.md)（單音 melody 罕見，多 chord texture）

## 7. Op.28 完整集中 articulation 標記密度比較

⚠ Training-data verification needed:

| No. | Slur 密度 | Staccato | Tenuto | Accent |
|---|---|---|---|---|
| 4 | 高（連續長 slur）| 0 | 偶見 | 偶見 |
| 6 | 高（LH melody）| 0 | 0 | 0 |
| 7 | 中（4-bar slur）| 0 | 0 | 0 |
| 15 | 高（A 段 long slur）| 中段加 staccato | 高（雨滴強拍）| 中段強 |
| 20 | 中 | 0 | **大量** | 偶見 |

→ Op.28 各 prelude articulation 標記密度差異大，每首是不同 articulation case study。

## 8. Audiveris MXL 對 Op.28 的 articulation 抓取

⚠ 取決於 source PDF 來源。如使用：
- Henle Urtext PDF: 預期 slur 抓取率高
- Mikuli (Schirmer) 19 世紀版: 高（但有 editorial 補加）
- musetrainer Op.28 集合 (如存在): 預期高品質 MXL

對 score-claude DP 的意涵：使用品質 MXL 後可啟用：
- legato_substitution (對 No.4, 6, 7, 15A 等 lyrical 段)
- (未來) staccato (對 No.15 中段)
- (未來) tenuto (對 No.20)
- (未來) accent (對 No.15 雨滴強拍)

## 9. 演奏家對 Op.28 詮釋

⚠ Training-data verification needed:

| 演奏家 | Op.28 風格 |
|---|---|
| **Maurizio Pollini** | 嚴謹 + 字面派詮釋 |
| **Krystian Zimerman** | 結構清晰 + 表情豐富 |
| **Martha Argerich** | 戲劇性對比 + 速度自由 |
| **Daniil Trifonov** | 細膩 articulation + 浪漫流動 |
| **Vladimir Ashkenazy** | 平衡 — 結構 + 浪漫並重 |

## 10. 與其他 wiki 頁面的關係

- *project_target_repertoire_intermediate* §Chopin — Op.28 No.4/7/20 為入門 Chopin 推薦
- [concept_period_defaults](concept_period_defaults.md) §4 Romantic — Op.28 為 Romantic legato default 典型集合
- [concept_legato_substitution](concept_legato_substitution.md) §5 — Op.28 lyrical preludes 為適用代表
- [concept_slur_phrase_overlap](concept_slur_phrase_overlap.md) §2.2 — No.7 為 slur ≡ phrase 案例
- [concept_articulation_in_polyphony](concept_articulation_in_polyphony.md) §3 — No.6 為 LH-as-melody 案例
- [concept_tenuto](concept_tenuto.md) §5 — No.20 為 tenuto 集中使用案例
- [analysis_chopin_op9_no2_articulation](analysis_chopin_op9_no2_articulation.md) — Chopin 大型作品對比

## 11. ⚠ Training-data verification queue

- §3-6 各 prelude 具體 articulation 標記分布
- §7 整體 articulation 密度數據（per Henle Urtext 統計）
- §9 演奏家詮釋風格差異具體 recording 比較
