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

## Source 頁狀態（已全 ingest，2026-05-29）

| 來源 | 頁面 | 狀態 |
|---|---|---|
| Neuhaus *The Art of Piano Playing* (1958) | [[src_neuhaus_art_of_piano]] | ✓ ingest（含 ⚠ verification queue）|
| Matthay *The Visible and Invisible* (1932) | [[src_matthay_visible_inaudible]] | ✓ ingest |
| Czerny *Op.500* (1839) | [[src_czerny_op500_articulation]] | ✓ ingest |
| Kullak *Die Ästhetik des Klavierspiels* (1860) | [[src_kullak_aesthetics_pianoforte]] | ✓ ingest |
| Brendel essays (1990s+) | [[src_brendel_essays]] | ✓ ingest |
| Türk *Klavierschule* (1789) | [[src_turk_klavierschule]] | ✓ ingest |
| Donington *Baroque Music* (1982) | [[src_donington_baroque_music]] | ✓ ingest |

每頁底部都有 `⚠ Training-data verification queue` 列出需要 cross-check 原書的具體引述。

## Analysis 頁狀態（已全寫，2026-05-29）

| 曲目 | 頁面 | 狀態 |
|---|---|---|
| Bach Two-Part Inventions | [[analysis_bach_inv_articulation]] | ✓ 寫（Baroque non-legato default + 例外段）|
| Beethoven Op.49 No.1 / No.2 | [[analysis_beethoven_op49_articulation]] | ✓ 寫（intermediate 教學主力, MXL 待取得）|
| Mozart K545 | [[analysis_mozart_k545_articulation]] | ✓ 寫（K545 Audiveris MXL 0 slur, 需更好 MXL）|
| Chopin Op.9 No.2 | [[analysis_chopin_op9_no2_articulation]] | ✓ 寫（已有 musetrainer MXL，整合 score-claude 啟用狀況）|

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
