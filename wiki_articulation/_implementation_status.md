# Articulation Wiki — Implementation Status (meta)

> Project-level status / ingest queue / DP 落地進度，不是給人讀的音樂知識。
> 純知識內容在 `concept_*.md` 與（未來）`src_*.md` / `analysis_*.md`。
> Wiki 知識 / project 分離原則見 [[../score-claude/memory/feedback_wiki_knowledge_vs_project_separation]]。

## DP 落地狀態（per cost rule）

| Cost rule | Wiki spec | DP 實作 | 啟用 piece | 詳見 |
|---|---|---|---|---|
| **Legato substitution** (same-pitch + slur → 換指 bonus) | [[concept_legato_substitution]] | ✓ (score-claude `7d5241a` v1 + `7203d27` v2 加 duration gate) | Chopin Op.9 No.2 (`023_..._full`) | [[../score-claude/memory/project_legato_substitution_v1_2026-05-29]] |
| Staccato hand-jump 鬆綁 | [[concept_staccato]] | (未實作) | – | – |
| Tenuto 強制 hold | [[concept_tenuto]] | (未實作) | – | – |
| Accent / marcato / sfz 偏強指 | [[concept_accent_marcato]] | (未實作) | – | – |
| Portato 中間值 | [[concept_portato_mezzo_staccato]] | (未實作) | – | – |
| Non-legato Baroque default | [[concept_non_legato_baroque]] | （即現行 DP 預設行為） | (所有 Bach Inv 對應) | – |
| Period-default 推論（無標記時）| [[concept_period_defaults]] | (未實作；目前 DP 一視同仁) | – | – |

## Source ingest queue（待補 src_* 頁）

以下文獻是 concept 頁面引用基礎，按優先序：

1. **Neuhaus《The Art of Piano Playing》§觸鍵章** — 連奏 / 觸鍵理論最常被引用源
2. **Matthay《The Visible and Invisible in Pianoforte Technique》** — 觸鍵物理分析最系統的單一來源
3. **Czerny Op.500《Vollständige theoretisch-practische Pianoforte-Schule》Vol.III** — 19 世紀教學派系基準
4. **Kullak《Die Ästhetik des Klavierspiels》** — 19 世紀理論，articulation 美學
5. **Brendel essays**（特別 Beethoven articulation 詮釋章節）
6. **Türk《Klavierschule》(1789)** — articulation pedagogical history 早期文獻
7. **Donington《Baroque Music: Style and Performance》** — Baroque articulation 與 ornament 互動

## Analysis 頁面 queue（per-piece 分析，待寫）

- `analysis_bach_inv_articulation.md` — Bach 2-voice subject vs counterpoint articulation 不同取法（Bach Inv Audiveris MXL 多數無 slur，需參考 urtext 推斷）
- `analysis_beethoven_op49_articulation.md` — Op.49 明確 articulation 標記 + DP 對應（MXL 待取得）
- `analysis_mozart_k545_articulation.md` — K545 Classical balance 案例（Audiveris MXL 目前 0 slur，可能需 re-OMR 或 Henle urtext MXL）
- `analysis_chopin_op9_no2_articulation.md` — Op.9 No.2 已有 wiki_phrase/analysis_chopin_op9_no2_nocturne.md，可補充 articulation 角度（musetrainer/library MXL 含 74 slur）

## Open design questions

- **Articulation 訊號信任度**：當 MXL slur 與 urtext 不一致時信哪個？傾向 urtext > Audiveris OMR 推斷
- **Edition 標記差異**：Henle / Bärenreiter / Schirmer 同一段標記不同 — wiki 應記載差異但 DP 使用單一來源（傾向 Henle 或當前 MXL 編輯）
- **Articulation 是 per-passage 還是 per-note？** 傾向 per-passage（一個 slur 區段一致），per-note 標記（staccato 單音）獨立處理
- **Period-default 推論**：是否要對無標記 MXL 自動推論時代 default？目前無；引入後 Baroque MXL 不受影響、Romantic MXL 預設 legato → 系統性增加 substitution。風險：時代判定可能錯（user 可能放 Bach 的 modernist editorial 加大量 slur）
- **是否需要 articulation_flags（類似 phrase_flags 機制）以 opt-in？** 目前每條 articulation rule 都進 `_PHRASE_FLAG_MAPPING` 共用 opt-in，是合理設計

## 對既有 cost rule 的 retrofit 影響（articulation 引入後）

| 既有 cost rule | 是否需要 articulation 條件化 | 理由 |
|---|---|---|
| `NOTE_RETENTION_PENALTY` (現 0.0) | 是 | legato 段應 bonus，staccato 段保持 0 — 已部分由 [[concept_legato_substitution]] cover |
| `THUMB_PASS_PHRASE_BUDGET` | 是 | staccato 段加寬 — 待 [[concept_staccato]] DP rule 落地 |
| `WRIST_EXT_PHRASE_BUDGET` | 否 | wrist extension 與 articulation 解耦 |
| `STEP_AGILITY_WEIGHT` | 否 | velocity-driven，與 articulation 不直接相關 |
| `PINKY_BLACK_MELODY_PENALTY` | 可選 | accent 段該音若為 pinky 應加重 penalty |
| `RH_F3F4_EXTRA_COST` | 否 | 解剖學常數 |
| `THUMB_PASS_UPWARD_EXTRA` | 否 | 解剖學常數 |

多數既有 cost rule 是純解剖學，不受 articulation 影響。只有 substitution-friendly / hand-jump-friendly 兩類 rule 是 articulation-sensitive。

## v3 candidates（legato substitution 後續，defer until problem surfaces）

來自 [[../score-claude/memory/project_legato_substitution_v1_2026-05-29]] §v3：

- **Adjacent-finger preference** — 在 substitution 時偏好相鄰指（2↔3 / 3↔4），避免 thumb 隔指換（2↔1 / 5↔1）
- **Slur-boundary-aware** — 只在 slur 起點 / 終點檢查 same-pitch substitution，不是 slur 全程

## 變更日誌

進度時間線 → 看 `log.md`（pure ingest log）。
