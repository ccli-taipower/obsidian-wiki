# Articulation Wiki Log

> Pure ingest log — 記錄每次新增 / 修改 wiki 內容。
> Project status / implementation 進度不在此 — 見 [[_implementation_status]]。

## [2026-05-29] revision — 知識頁清理 + 補齊 6 個 concept 頁

把原本 index / overview / legato_substitution 三頁混雜的 spec / todo / 實作狀態移到新建 `_implementation_status.md`（per wiki_phrase 慣例：底線開頭 meta 頁）。

Pages revised:
- `index.md` — 改純 TOC，移除 "Open questions"、"src 待 ingest"、"analysis 待寫" 等 roadmap 內容
- `concept_articulation_overview.md` — 移除 §7 "對既有 cost rule 的 retrofit 影響評估"、§8 "未解 questions / 待 ingest" 等 meta 段；§4 cost-rule mapping 簡化為「主要影響 + 詳細頁連結」
- `concept_legato_substitution.md` — 移除 §3.2 DP 修改提案、§4 預期 cost 改變、§7 A/B 驗證計畫 等 spec/未跑 內容；保留純知識（rationale / sources / 操作型定義 / 適用情境 / 失效情境）

Pages created (6 new concept):
- `concept_staccato.md` (90 行) — 斷奏 / staccatissimo / mezzo-staccato spectrum，對 hand jump / thumb cross / substitution / 同指連續 的反向約束
- `concept_tenuto.md` (78 行) — 持音的「禁止換指」+ 強指偏好（1/2/3）+ 與其他 articulation 疊加處理
- `concept_accent_marcato.md` (87 行) — accent (`>`) / marcato (`^`) / sforzando (`sfz`) 三符號區別，強指偏好物理基礎，與 dynamic 標記的區別
- `concept_portato_mezzo_staccato.md` (76 行) — 半連半斷中間值，為何指法保守選 legato 端
- `concept_non_legato_baroque.md` (95 行) — Baroque 默認 articulation 的歷史依據（C.P.E. Bach / Türk / Couperin），對指法策略的意涵，例外情境（chantant 段）
- `concept_period_defaults.md` (108 行) — 四時代 default 對應表（Baroque / Classical / Romantic / Modernism），編輯者 articulation 與時代 default 的衝突，對指法系統的實作意涵

Pages created (1 new meta):
- `_implementation_status.md` (75 行) — DP 落地狀態表 + source ingest queue + analysis 頁 queue + open design questions + v3 candidates

Total: 3 revised + 7 new pages = 10 active pages（之前 3 → 現在 10），約 700 行純知識內容。

對應 [[../score-claude/memory/feedback_wiki_knowledge_vs_project_separation]] 原則：concept 頁全為純音樂知識，無「spec'd」/「待實作」/「待 ingest」/「A/B 預期」雜訊。

## [2026-05-29] init — articulation track seed

新建 wiki_articulation/ 作為第三條獨立 discipline（parallel to wiki_piano + wiki_phrase）。

初版 pages:
- `index.md`、`log.md`、`concept_articulation_overview.md`、`concept_legato_substitution.md`

詳細 init 內容見 obsidian-wiki commit `9984996`。
