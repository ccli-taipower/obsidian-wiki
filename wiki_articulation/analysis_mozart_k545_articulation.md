# Analysis: Mozart K545 — Articulation 詮釋（Classical 平衡 典型案例）

> 來源：Henle Urtext (Ulrich Wilker 編), Bärenreiter NBA、Brendel essays §Mozart、Türk Klavierschule (Mozart 同時代文獻)
> 對應 PIG：023 = Chopin Op.9-2, **K545 PIG 編號 017**（已有 score-claude cache 但 Audiveris MXL 0 slur）
> 引用方：[[concept_articulation_overview]] §3, [[concept_period_defaults]] §4 (Classical default), [[../wiki_phrase/analysis_chopin_op9_no2_nocturne]] 對位案例

## 1. 為什麼挑 K545 作為 Mozart articulation 案例

理由：
- K545 (C major) 是 Mozart 「**Sonata facile**」（簡易奏鳴曲）— Mozart 親自標題暗示 intermediate 適用
- 創作 1788 年（Mozart 晚期），articulation 標記密度已成熟
- 結構標準 sonata form，3 樂章，每樂章 articulation 風格各異
- 屬於 [[../score-claude/memory/project_target_repertoire_intermediate]] 核心曲目

## 2. K545 mvt1 (Allegro, C major) articulation 標記 ⚠

⚠ Training-data verification needed: K545 mvt1 標準 articulation 模式：

**第一主題 (m1-4)**:
- RH alberti-like 對稱 phrase
- Slur 涵蓋整個 4 小節主題
- 結尾音（cadential 解決）有時加 staccato 標記區分

**過渡段 (m5-12)**:
- 16th-note 經過音段
- 部分 slur 標記、部分 detache
- 標準 Czerny 派標準指法 (1-2-3-1-2-3-4-5 scale fingering)

**第二主題 (m13+, G major)**:
- 更 cantabile，slur 範圍變長
- 偶有 staccato 對比段

**Development (m29+)**:
- 16th-note 跑動 + slur 短小變化頻繁
- 是 articulation 對比最密集處

**Recap (m42+)**:
- 重現第一主題，articulation 與 exposition 大致相同

## 3. K545 mvt2 (Andante, G major) articulation 標記 ⚠

⚠ Training-data verification needed:

**A 段主題**:
- 抒情主題，slur 涵蓋整段 melody
- 伴奏左手 alberti，slur 標 8 小節大段
- 是 [[concept_legato_substitution]] 高度適用段

**B 段對比段**:
- 較 detache（部分 staccato）
- 動態 forte → piano 對比

**A' 段重現**:
- 加裝飾音，articulation 略複雜

## 4. K545 mvt3 (Rondo - Allegretto, C major) articulation 標記 ⚠

⚠ Training-data verification needed:

- Rondo theme: 短 slur + staccato 對比，**Classical 平衡** 最典型案例
- Episode 段：更 detache
- 結尾 coda: legato + cadential 強奏

## 5. Mozart articulation 慣例的特點

Mozart 標記比 Beethoven **較疏**（標記密度低）但**極具規範性**：
- 寫了的標記必須 honor
- 沒寫的段落 → 依 Classical 平衡 default（[[concept_period_defaults]] §4）：
  - 短音 (16th, 8th 在 fast tempo) → detache
  - 長音 (quarter 以上) → legato
  - 中音 → 依上下文判斷

對指法的意涵：[[concept_period_defaults]] 「**音長相關平衡**」原則特別適用於 Mozart 無標記段。

## 6. Audiveris MXL 對 K545 的 articulation 抓取

從 score-claude 實測（2026-05-29，[[wiki_articulation/index]] §訊號可用性表）：
- K545 B0-22 Audiveris MXL: **0 slurs, 0 articulations**

可能原因：
1. PIG ScorePDF 是簡化版（B0-22 = 第 1-22 小節 excerpt 而非全曲）
2. Audiveris 對 18 世紀 print 的 slur OMR 辨識率低
3. PIG 的 source PDF 可能本來就少標記

→ 對 score-claude DP 的意涵：
- 目前 K545 cache **不適合啟用 [[concept_legato_substitution]]**（無 slur 訊號）
- 若取得 Henle Urtext digital 的 K545 全曲 MusicXML，預期 slur 豐富，可啟用

## 7. K545 vs Chopin Op.9-2 articulation 對比

從 score-claude 實測：

| 曲目 | Audiveris MXL slur 數 | 預期 articulation 風格 |
|---|---|---|
| K545 B0-22 (Classical) | 0 | 應為 Classical 平衡（音長 default）|
| Op.9-2 full (Romantic) | 74 / 148 notes-in-slur | Romantic legato 為主 |

→ 顯示**訊號可用性問題**：Classical 簡易版 PDF Audiveris OMR 不易抓 articulation；Romantic 浪漫派全曲 MXL 訊號豐富。

對指法系統的意涵：要 fully 啟用 [[concept_legato_substitution]] 在 K545，需重 OMR 一份品質更好的 K545 全曲 PDF（如 Henle Urtext），或使用 Henle 提供的 digital MusicXML（如有）。

## 8. Mozart articulation 詮釋的演奏家差異

⚠ Training-data verification needed:

| 演奏家 | K545 articulation 風格 |
|---|---|
| **Brendel** | 字面派 — slur / staccato 明確遵守 |
| **Schiff** | 同 Brendel，加重結構性對比 |
| **Uchida** | 介於字面 / 自由 — 細膩 articulation 變化 |
| **Pires** | 較柔 / 連續 — 偏向 legato 默認 |
| **Gulda** | 較銳利 / detache — 偏向 staccato 默認 |

→ 即使 Urtext 標記明確，演奏家仍有詮釋空間。但對於 score-claude DP，**信標記 + 信時代 default** 是合理保守策略。

## 9. 對 score-claude DP 的影響預測

當 K545 取得品質佳 MXL 後，預期：
- Slur 訊號充足 → [[concept_legato_substitution]] 適用
- 短音 detache 段（development）→ 未來 [[concept_staccato]] 規則的測試對象
- 整體應啟用：**figural + thumb + cadence + legato_substitution + long_scale**（per K545 已有的 `SINGLE_PDF_PHRASE_FLAGS` config + 新增 legato）

## 10. 與其他 wiki 頁面的關係

- [[concept_articulation_overview]] §3 — K545 是 Classical 平衡 default 的典型案例
- [[concept_period_defaults]] §4 — Mozart 為 Classical 「**音長相關平衡**」原則代言
- [[concept_legato_substitution]] §5 — Mozart slow movement 在「適用情境」表中 Classical *cantabile* 代表
- [[src_brendel_essays]] §2.3 — Brendel 對 Mozart 「**18 世紀說話**」articulation 觀察
- [[src_turk_klavierschule]] — Türk 是 Mozart 同時代文獻，提供 articulation default 操作型百分比
- [[../wiki_phrase/analysis_chopin_op9_no2_nocturne]] — 對比 Romantic articulation 與 Classical 差異
- [[../score-claude/memory/project_target_repertoire_intermediate]] — K545 是 intermediate 目標核心曲目

## 11. ⚠ Training-data verification queue

以下基於 training-data，需 cross-check 原譜 / Henle Urtext：
- §2-4 各樂章 articulation 標記精確分布（measure 數）
- §6 Audiveris 對 K545 印刷品 OMR 失誤率（B0-22 vs 全曲）
- §8 演奏家對比 K545 articulation 詮釋差異（具體 timestamp 或 recording 細節）
