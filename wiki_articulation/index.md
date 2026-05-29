# Wiki: Articulation — 連結 / 斷奏 / 觸鍵 對指法的影響

> 第三條 wiki track，平行於 [[../wiki_piano/index|wiki_piano]] (生物力學) + [[../wiki_phrase/index|wiki_phrase]] (樂句分段)。
> 主題：notation 詮釋層（slur、staccato、tenuto、accent...）如何決定指法選擇，特別是同音換指、手位跳轉、強指偏好。
> 目標讀者：鋼琴教師、學生、指法系統設計者。

## 為什麼要獨立一條 wiki

兩個音之間怎麼連接（**connection style**），不只是表情問題，**直接決定可用的手指轉換策略**：

| Articulation | 物理動作 | 對指法的約束 |
|---|---|---|
| **Legato** | 前指還按、後指彈下、前指鬆 | 允許 finger substitution；不允許 hand jump |
| **Staccato** | 每音獨立、鬆指後再彈 | 允許 thumb cross / hand jump；substitution 無意義 |
| **Tenuto** | 持滿值、明顯壓重 | 同音換指禁用；強制 hold 此指 |
| **Accent / Marcato** | 強重音 + 短斷 | 偏好強指（1/2/3）下這個音 |

→ 沒看 articulation = 把所有音當 non-legato 處理 = 對 Baroque 對位 OK（baroque 默認 non-legato）但對 Chopin lyrical 段 / Beethoven *cantabile* 標記段系統性失誤。

## 索引

### Foundation 頁
- [[concept_articulation_overview]] — 完整 articulation taxonomy（11 種類型）+ 時代 default（Baroque/Classical/Romantic/Modern）

### Per-articulation concept 頁
- [[concept_legato_substitution]] — 連奏段 finger substitution 偏好（最常被引用的指法-articulation 介面）
- [[concept_staccato]] — 斷奏 / staccatissimo 對 hand jump 與 thumb cross 的鬆綁
- [[concept_tenuto]] — 持音的「禁止換指」約束
- [[concept_accent_marcato]] — 重音 / marcato / sforzando 的強指偏好
- [[concept_portato_mezzo_staccato]] — 半連半斷的中間地帶
- [[concept_non_legato_baroque]] — Baroque 默認 articulation（為何不應該對 Baroque 過度套用 legato 規則）
- [[concept_period_defaults]] — 無標記時各時代假設什麼 default

### Source 頁（文獻參考）
- [[src_neuhaus_art_of_piano]] — Neuhaus *The Art of Piano Playing* (1958) — 俄羅斯派重量觸鍵理論
- [[src_matthay_visible_inaudible]] — Matthay *The Visible and Invisible in Pianoforte Technique* (1932) — 英國派觸鍵物理分析
- [[src_czerny_op500_articulation]] — Czerny *Op.500 Vollständige theoretisch-practische Pianoforte-Schule* (1839) — 19 世紀教學集大成
- [[src_kullak_aesthetics_pianoforte]] — Kullak *Die Ästhetik des Klavierspiels* (1860) — 19 世紀美學論述
- [[src_brendel_essays]] — Brendel *Music Sounded Out* + 散文集 (1990s+) — Beethoven articulation 字面派詮釋
- [[src_turk_klavierschule]] — Türk *Klavierschule* (1789) — Baroque/Classical 過渡期一手文獻
- [[src_donington_baroque_music]] — Donington *Baroque Music: Style and Performance* (1982) — HIP 運動學者性回顧

### Analysis 頁（per-piece articulation 分析）
- [[analysis_bach_inv_articulation]] — Bach Two-Part Inventions（Baroque non-legato default + 例外 legato 段）
- [[analysis_beethoven_op49_articulation]] — Beethoven Op.49 No.1 / No.2（Classical 平衡, intermediate 教學主力）
- [[analysis_mozart_k545_articulation]] — Mozart K545（Classical 平衡 典型案例）
- [[analysis_chopin_op9_no2_articulation]] — Chopin Op.9 No.2（Romantic legato 預設 + fioritura 特殊處理）

### Meta
- `_implementation_status.md` — DP 落地狀態 / source ingest queue / open design questions
- `log.md` — 變更記錄

## Wiki 內定位

| 訊號軸 | 屬於哪條 wiki | 改 DP 哪裡 | 變化頻率 |
|---|---|---|---|
| 解剖學 + 手部生物力學 | [[../wiki_piano/index|wiki_piano]] | cost terms (span / transition / thumb-pass) | 個人常數 (per-user) |
| 樂句結構 + 對位邏輯 | [[../wiki_phrase/index|wiki_phrase]] | phrase boundary 加 | per-piece 樂句結構 |
| Notation 詮釋 + 觸鍵 | wiki_articulation (本) | cost rule conditional 修飾 | per-段 / per-marking |

**Articulation 是 within-phrase 屬性，不是 phrase 切分訊號**：slur 結束通常不是樂句結束（Chopin lyrical 一個 phrase 可有多 slur 子分句、Bach 一個 figure 可橫跨 slur 邊界）。

## 主要文獻基礎

詳細導覽見上方「Source 頁」索引 — 7 個 `src_*.md` 已完成（2026-05-29 補齊）。

## 目標曲目對應

主要應用：初中階曲目（[[../score-claude/memory/project_target_repertoire_intermediate]]）
- Bach 2-voice Inventions — Baroque non-legato default 為主
- Easy Beethoven sonatas (Op.49) — Classical 平衡：短音 detache、長音 legato
- Mozart sonatinas / 易奏鳴曲 — Classical 同上
- 簡單 Chopin Preludes — Romantic legato 為主
- Chopin Op.9 No.2 — 已有 [[concept_legato_substitution]] 啟用驗證

進階曲目（Pathétique 等）不在目標範圍 — advanced pianists 有個人 articulation 詮釋習慣。
