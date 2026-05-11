# Wiki Log

## [2026-05-07] init | Wiki 建立

建立 wiki_refractory_hypotension_post_ptx，主題為副甲狀腺部分切除後的頑固性低血壓。初始 ingest 11 篇文獻，產生 11 個 src_ 頁面、3 個 concept 頁面及 index。

Sources ingested:
1. Leiba 2013 — 嚴重持久低血壓 case series
2. Shinoda 1992 — 低血鈣誘發心衰竭
3. Sofronie 2018 — 高血壓正常化 + systematic review
4. Pizzarelli 1993 — PTX 後血壓長期追蹤
5. Shih 2013 — PTX 減少透析中低血壓
6. Kawashima 1990 — PTH 與血管平滑肌細胞內鈣
7. Campese 1989 — 鈣、PTH 與血壓綜述
8. Chesterton 2005 — BRS 與 CKD 血管運動不穩定
9. Chesterton 2010 — BRS 分類透析血流動力學
10. Petraki 2008 — 運動改善 BRS
11. Martinez-Alanis 2023 — 延遲序列法測量 BRS

Concepts created:
- concept_pth_cardiovascular_effects
- concept_post_ptx_hemodynamic_changes
- concept_baroreflex_sensitivity_ckd

## [2026-05-07] query | PTX 後 iPTH 過度抑制合併頑固性 IDH 治療策略

Query: 48 歲男性 ADPKD 透析 11 年，PTX 後 iPTH 過度抑制（17.5），頑固性透析中低血壓，該如何改善？

產生 analysis_refractory_idh_treatment_plan，交叉比對 8 篇文獻，提出 5 項治療策略及鈣的兩難整合方案。同步輸出 PDF 至 /Users/ccli/Documents/病歷/wiki_treatment_analysis.pdf。

## [2026-05-11] update | 新增 2 個 concept + 重構 hemodynamic_changes

從「低血鈣症」角度補強現有 wiki（曾短暫嘗試獨立 wiki_hypocalcemia/，發現與本 wiki 機轉內容重疊嚴重，改為合併）。

新增 concept：
- `concept_hypocalcemia_cardiac_effects` — 心肌收縮力依賴鈣的機轉、揭露潛伏性心衰竭、與血管路徑的臨床區辨表
- `concept_perioperative_calcium_management` — ionized vs total Ca、dialysate Ca 策略、輸注劑量、HBS 時序、術前準備

重構 `concept_post_ptx_hemodynamic_changes`：
- 機轉假說段改為顯式「雙路徑模型」（路徑 1：細胞外鈣下降；路徑 2：PTH 訊號撤除——後者解釋為何鈣補回血壓仍持續低）
- 三個 reset 假說從機轉段獨立出來
- 新增 RAAS 抑制 + McCarron 悖論 + 治療對策表
- 心肌路徑改為短段 + cross-link 到新的 hypocalcemia_cardiac_effects
