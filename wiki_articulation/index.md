# Wiki: Articulation — 連結 / 斷奏 / 觸鍵 對指法的影響

> 第三條 wiki track，平行於 [[../wiki_piano/index|wiki_piano]] (生物力學) + [[../wiki_phrase/index|wiki_phrase]] (樂句分段)
> 起始 2026-05-29
> 目標曲目：初中階（[[../score-claude/memory/project_target_repertoire_intermediate]]）
> 對 score-claude DP 的影響面：cost rule 加 articulation-conditional 修飾項，不新增 phrase boundary

## 為什麼開這條獨立 wiki

Articulation（連結 / 斷奏 / 觸鍵類型）不屬於既有兩條 wiki：
- 不是「樂句邊界」— articulation 不會切樂句（slur 結束 ≠ 樂句結束）
- 不是「生物力學常數」— articulation 是 notation 詮釋層，per-piece / per-段 變動

但 articulation 直接決定多條 DP cost rule：
- **legato 段** → favor finger substitution，鬆綁 `NOTE_RETENTION_PENALTY`
- **staccato 段** → relax `INTRA_PHRASE_TRANSITION_SCALE`，允許 hand jump / thumb cross
- **accent / agogic** → 偏好強指（1/2/3 而非 4/5）
- **tenuto** → 強制 hold（同音換指禁用）

目前 DP 完全沒看 MXL 的 `slur` / `articulation` / `dynamic` elements — 此 wiki 把 articulation 文獻 + 對應 cost rule 對齊起來。

## 索引 (TOC)

### Concept 頁
- [[concept_articulation_overview]] — 完整 taxonomy（legato / non-legato / staccato / portato / tenuto / accent / marcato / sforzando）+ 各條對應 cost rule 表
- [[concept_legato_substitution]] — 最大衝擊條目：legato 段 finger substitution 偏好，pedagogical 文獻 + DP 修改提案

### Source 頁 (待 ingest)
- src_neuhaus_art_of_piano.md — Heinrich Neuhaus *The Art of Piano Playing*（觸鍵原則章節）
- src_matthay_visible_inaudible.md — Tobias Matthay *The Visible and Invisible in Pianoforte Technique*
- src_czerny_op500_articulation.md — Czerny Op.500 articulation 段
- src_brendel_essays.md — Alfred Brendel 散文（Beethoven articulation 案例集）
- src_kullak_aesthetics_pianoforte.md — Kullak *Die Ästhetik des Klavierspiels*（19 世紀 articulation 理論）

### Analysis 頁 (待寫，per-piece)
- analysis_bach_inv_articulation.md — Bach 2-voice subject vs counterpoint articulation 不同取法
- analysis_beethoven_op49_articulation.md — Op.49 明確 articulation 標記 + DP 對應
- analysis_mozart_k545_articulation.md — K545 Classical balance（既不全 legato 也不全 detache）

### Meta
- `_implementation_status.md` — 各 concept 對應 DP cost rule 落地狀態 / A/B 結果（待開）

## 與其他 wiki 的對位

| 訊號 | wiki_piano | wiki_phrase | wiki_articulation |
|---|---|---|---|
| 來源 | 解剖學 + 個人生物力學 | 樂理 + 作曲家分析 | notation 詮釋 + 觸鍵傳統 |
| 改 DP 哪裡 | cost terms (span/transition/thumb-pass) | phrase boundary 加 | cost rule conditional 修飾 |
| 變化頻率 | 個人常數 (per-user) | per-piece 樂句結構 | per-段 / per-articulation marking |
| 訊號 hook | wiki concept → cost rule | wiki concept → _detect_phrase_starts | wiki concept → conditional rule (待實作) |

## Open questions（記錄供未來決定）

- Articulation 是 per-passage (per-段) 還是 per-note? 我傾向 per-段（一個 slur 區段一致 articulation）
- 不同 edition 同一段 articulation 標記不同 — 信哪本？（傾向 Henle Urtext > Schirmer / Bärenreiter）
- 演奏家 articulation 詮釋 vs 樂譜標記 — 系統信樂譜還是信「典型詮釋」？傾向信樂譜（avoid second-guessing the score）
- 是否需要 per-piece articulation_flags（類似 phrase_flags 機制）以 opt-in？— 應該需要
