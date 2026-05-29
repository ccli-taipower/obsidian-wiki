# Analysis: Beethoven Op.49 No.1 / No.2 — Articulation 詮釋（intermediate 教學主力）

> 來源：Brendel essays、Henle Urtext (Sieghard Brandenburg 編), Bärenreiter NBA、Czerny Op.500 § Beethoven 章節
> 對應 PIG：未列入（input/ MXL 待取得）
> 引用方：[[concept_articulation_overview]] §3 (Classical period)，[[concept_period_defaults]] §4 Classical 平衡, [[concept_tenuto]] §5 Beethoven 持音

## 1. 為什麼挑 Op.49 作為 Beethoven articulation 案例

理由：
- Op.49 No.1 (G minor) + No.2 (G major) 是 Beethoven「**easy sonatas**」，初中階學生最常入門 Beethoven 奏鳴曲（[[../score-claude/memory/project_target_repertoire_intermediate]]）
- 創作於 Beethoven 早期（c. 1795-1797），articulation 寫法接近 Classical 風格（mid-period 才開始大量 tenuto / sf 標記）
- 兩首都 ≤ 8 分鐘，2 樂章結構簡單，是分析 Beethoven articulation 慣例的最小單元

## 2. Op.49 articulation 標記密度（vs 後期作品對比）⚠

⚠ Training-data verification needed:

| 作品 | 創作年份 | Slur 密度 | Staccato dot 密度 | Tenuto 密度 | Accent 密度 |
|---|---|---|---|---|---|
| **Op.49 No.1 (G minor)** | 1795-97 | 中等 | 中等 | 接近 0 | 少 |
| **Op.49 No.2 (G major)** | 1795-97 | 中等 | 中等 | 接近 0 | 少 |
| Op.27/2 (月光) | 1801 | 大量（連續 slur）| 少 | 開始出現 | 中等 |
| Op.57 (熱情) | 1804-05 | 大量 | 大量 | 中等 | 大量 sf |
| Op.106 (Hammerklavier) | 1817-19 | 大量 | 大量 | 大量 | 極多 sf / sfp |
| Op.111 | 1821-22 | 中等（更精細）| 大量 | 大量（結構性）| 極多 |

→ Op.49 articulation 標記比後期少很多，但**精確程度仍高於 Mozart 同時代作品** — 屬於「Beethoven 風格的 Classical 平衡」。

## 3. Op.49 No.1 (G minor) 樂章 articulation 特徵 ⚠

⚠ Training-data verification needed:

**mvt1 Andante (G minor)**:
- 抒情主題（cantabile 性格）→ 默認 legato，但 Beethoven 標明確 slur 範圍
- 對位段（subject + accompaniment）→ 主題 legato（slur 內），伴奏 detache（無 slur）
- Cadential 強奏段 → sf 標記出現於 V-I 解決強拍前

對指法的意涵：
- Slur 內主題段 → [[concept_legato_substitution]] 適用
- 伴奏 alberti / 8 分音符 detache 段 → [[concept_staccato]] 鬆綁適用
- sf 強拍 → [[concept_accent_marcato]] 強指偏好

**mvt2 Rondo - Allegro (G major 結尾)**:
- Rondo theme 用 slur 標連奏；對比段（B, C theme）用 staccato dot
- 八度跳躍段 detache（無 slur）
- 結尾 coda 加 sf 強拍

對指法的意涵：明顯的 articulation 結構性對比 — 連奏主題 vs 斷奏對比段。

## 4. Op.49 No.2 (G major) 樂章 articulation 特徵 ⚠

⚠ Training-data verification needed:

**mvt1 Allegro ma non troppo (G major)**:
- Sonata form 結構 — exposition / development / recapitulation 各段 articulation 鮮明
- 第一主題 detache + 跳躍；第二主題 legato + cantabile
- Development 段交替 detache + legato，articulation 對比即是結構標記

對指法的意涵：articulation 與樂段結構強相關 — Brendel 字面派立場 ([[src_brendel_essays]] §2.1) 在此例特別有效。

**mvt2 Tempo di Menuetto (G major)**:
- Minuet & Trio 結構 — 兩段 articulation 風格差異明顯
- Minuet 段：對稱 phrase，每 phrase 結尾 slur 收尾 + 跳到下個 phrase
- Trio 段：較 cantabile 連續 slur，少 staccato

## 5. Beethoven articulation 的「結構標記」性質

Beethoven 標記不是純表情，常是**結構轉折標誌**：
- Slur 結束的位置 = phrase 結束的位置（與 wiki_phrase phrase boundary 重合）
- sf 的位置 = development 段戲劇高點或 recapitulation 強烈宣告
- Tenuto 的位置 = inner voice 結構性強調

→ Brendel essays（[[src_brendel_essays]] §2.1）強烈主張這些標記應**字面 honor**，因為它們承載結構信息，不只是表情。

## 6. 對 score-claude DP 的影響預測

當 Op.49 MXL 取得後，預期：
- Slur 數量充足（Classical 標記比 Baroque 多得多）→ [[concept_legato_substitution]] 有效啟用對象
- Staccato 標記充足 → 未來 [[concept_staccato]] DP rule 落地後的測試對象
- sf 標記少但具結構意義 → 未來 [[concept_accent_marcato]] DP rule 的測試對象
- 整體應**啟用 figural + thumb + legato_substitution**（per 初中階 Classical 慣例）

啟用順序建議：
1. 先取得 Op.49 No.2 mvt2 (Tempo di Menuetto) MXL（最 lyrical，slur 標記最豐富）
2. 啟用 legato_substitution + 驗證 cost red-line
3. 啟用 figural + thumb（標準 Classical config）

## 7. 與其他 wiki 頁面的關係

- [[concept_articulation_overview]] §3 — Op.49 是 Classical period 平衡 default 的典型案例
- [[concept_legato_substitution]] §5 — Op.49 cantabile 段是「適用情境」表中 Classical *cantabile* 代表
- [[concept_period_defaults]] §4 — Beethoven 早期接近 Classical 平衡（vs 後期更自由）
- [[concept_tenuto]] §5 — Op.49 tenuto 標記少，但比較對象（後期 Op.110-111）大量
- [[concept_accent_marcato]] §1, §4 — Op.49 sf 標記少但具結構意義
- [[src_brendel_essays]] §2 — Brendel 對 Beethoven articulation 字面派立場
- [[src_czerny_op500_articulation]] — Czerny 作為 Beethoven 學生，對 Beethoven articulation 的詮釋傳承
- [[../score-claude/memory/project_target_repertoire_intermediate]] — Op.49 是 intermediate 目標的核心曲目

## 8. ⚠ Training-data verification queue

以下基於 training-data，需 cross-check 原譜 / 學術文獻：
- §2 各時期 Beethoven 作品 articulation 標記密度對比表
- §3-4 Op.49 各樂章 articulation 特徵描述（精確段落、measure 數）
- §5 Beethoven 標記「結構標記」性質的學術共識
- §6 Op.49 MXL 取得（musetrainer / IMSLP / Henle digital）後驗證實際 slur 統計
