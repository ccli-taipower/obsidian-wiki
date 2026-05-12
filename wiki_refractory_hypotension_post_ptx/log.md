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

## [2026-05-11] lint | wiki 健康檢查 — 17 頁、2 處不對稱修復

掃描 17 個頁面建立連結圖。檢查結果：
- ✅ 無 orphan page（每頁皆有 inbound link）
- ✅ 無 broken link
- ✅ 無內部矛盾陳述（dialysate Ca 1.75 mmol/L 用於圍術期 HBS vs 慢性 adynamic bone 場景避免——是情境分流不是矛盾）
- ✅ 無強制需新增的概念專頁

修復：2 處不對稱的 concept-concept 連結
- `concept_pth_cardiovascular_effects` 加上 → `concept_hypocalcemia_cardiac_effects`
- `concept_baroreflex_sensitivity_ckd` 加上 → `concept_perioperative_calcium_management`

未自動修復的觀察（需內容改寫，僅報告）：
- `analysis_refractory_idh_treatment_plan` 未引用 Shih 2013、Sofronie 2018、Pizzarelli 1993，但這 3 篇與「post-PTX IDH 治療」高度相關。分析寫作時聚焦於 iPTH 過度抑制 + BRS 框架，刻意未涉及這 3 篇的觀點（PTX 整體上減少 IDH、BP 改善 meta-analysis、長期 BP 趨勢）。未來若擴充分析可考慮納入。

## [2026-05-11] query | CAD 對 PTX 後頑固性 IDH 的貢獻

Query: 同一位 48 歲男性 ADPKD 透析 11 年、PTX 後 iPTH 過度抑制（17.5）、頑固性 IDH，新增資訊 RCA 完全阻塞 + LCX 於 2023/03 安裝支架——心血管疾病是否是 IDH 的原因？如何改善？

產生 `analysis_cad_contribution_to_refractory_idh`，定位 CAD 為「慢性 substrate」、PTH 過度抑制為「acute trigger」的協同模型。改善策略涵蓋冠脈評估、cardiac-protective HD（UF rate < 10-13 mL/kg/h、cool dialysate、HDF）、β-blocker 優化（cardioselective 最低劑量取代 carvedilol）、乾體重保守設定、Shih 2013 補進引用。引用 8 篇 src，與既有 `analysis_refractory_idh_treatment_plan` 互補（後者血管軸，本篇心臟軸）。

## [2026-05-11] query | 藥物盤點識別醫源性 IDH 加重因子

Query: 同一位 48 歲 ADPKD HD 病人完整藥單——保栓通 75 + 伯基 100 + 冠脂妥 10 + 沛暢 75，有沒有可調整的醫源性 IDH 加重因子？

確認沛暢 = Peysan = Dipyridamole（透過 CTH 仿單頁面）。產生 `analysis_iatrogenic_factors_in_refractory_idh`，識別 Dipyridamole 為最大可調整因子：PDE 抑制 → cAMP 累積 → 血管擴張，且 adenosine 重吸收抑制再強化擴張作用。在 PTX 後 PTH 撤除已造成血管路徑 2 失能的情境下，cAMP-elevating drug 是雪上加霜。

構成三軸框架：血管軸（既有）+ 心臟軸（既有）+ 藥物軸（本篇）。本軸介入成本最低、effect 最快，建議從這軸先試（停或減 dipyridamole 1-2 週評估 IDH 改善）。

註記：缺少 β-blocker 與 ACE/ARB 的觀察可能反映「已試過但因 IDH 停掉」——若如此，停 dipyridamole 比停 β-blocker 更該被優先考慮。

## [2026-05-11] update | 全面修訂三份 analysis — 整合病人個人醫療摘要 PDF（13 頁）

來源：病人提供 `/Users/ccli/Documents/病歷/個人醫療摘要.pdf` (整理日期 2026/05)。含心超 2026/04、核醫 2025/08、腦部 MRI/MRA 2023/12、腹部 MRI 2025/12、抽血 2026/04 完整數據與已嘗試介入清單。

**關鍵發現修正既有 analysis：**

1. **心臟病理被誤判**：先前推論 cardiac reserve 受限。實際心超 EF 73.7%（hyperdynamic）+ E/A 0.62（impaired LV relaxation）= **HFpEF physiology**。preload-sensitive 而非 contractility-limited。
2. **CAD 是 active progressing 而非穩定**：核醫 SSS=16、ΔTPD=16% severe reversible ischemia，**缺血擴及 LAD/LCX territory** 不只 RCA 區。
3. **腦部 MRI/MRA 2023/12 顱內動脈瘤陰性**：Dipyridamole 的中風二次預防 indication 已被影像排除——停藥論證更扎實。
4. **大量 cardiac-protective HD 介入已做**：停降壓藥、乾體重 +10 kg、Midodrine、HDF 1/週、4.5 hr、36°C 都已執行。剩 35.5°C、HDF 頻率、客觀乾體重。
5. **K 6.0 上升 + 缺鐵性貧血**：兩個既有 analysis 都漏掉的 modifiable factor。

**全面修訂：**

- `analysis_cad_contribution_to_refractory_idh.md`：心臟框架從「cardiac reserve」改為「HFpEF + active progressive CAD」；更新核醫數據；β-blocker 從「共犯」改為「在 HFpEF + ischemia 雙重 indication 下應重啟」；reality check 已完成介入；加上 transplant 評估作為 organizing principle；補上 anemia、K、AVG access 三個新觀察。
- `analysis_iatrogenic_factors_in_refractory_idh.md`：加 MRI/MRA 陰性段（dipyridamole indication 進一步薄弱）；新增藥物 reconciliation 警示（病人摘要的目前用藥未確認 4 藥）；新增 BB 重啟建議；新增 K 6.0 修飾因子。
- `analysis_refractory_idh_treatment_plan.md`：標註已完成介入 ✅；新增 K 與 anemia 修飾因子段；加結尾三軸整合段；補相關頁面連結。

無 analysis 被刪除——三軸（血管/PTH、心臟/CAD、藥物/iatrogenic）各自獨立未重疊。

## [2026-05-12] update | 補上佳立鈣劑量資訊 + ferric citrate switch 建議

病人補充：**佳立鈣錠 500 mg × 6/日 = 1,200 mg elemental Ca/日**（鈣型 phosphate binder）。

關鍵分析：
- KDIGO 上限警戒（< 1,500 mg/日）：1,200 mg 在上限
- 磷已控制良好（P=4.6）→ 不需這麼強的 binder
- adynamic bone 強烈懷疑（iPTH 17.5 + ALP 61）→ 多餘鈣跑去血管 / 軟組織
- 腹部 MRI 證實主動脈 + 冠脈鈣化 → 直接加重
- 合併缺鐵性貧血（MCV 69.2、RDW 19.3）

→ **理想對策：換成 ferric citrate（鐵爾思 / Auryxia）**——一石二鳥：減少 Ca load + 提供腸吸收鐵改善貧血。

三份 analysis 補入：
- `analysis_iatrogenic_factors`：藥物表加入佳立鈣 + Midodrine（之前漏列）；新增 §8 鈣 binder 換 ferric citrate 完整論述（含三個替代選項比較）；結論段升級為「第一級 dipyridamole + 第二級 ferric citrate switch」雙層
- `analysis_refractory_idh_treatment_plan`：病人摘要段加入 1,200 mg Ca/日 + 主動脈/冠脈鈣化；治療策略 §1 「減少碳酸鈣劑量」具體化為「換 ferric citrate」；鈣的兩難段補上 ferric citrate 是清晰一步
- `analysis_cad_contribution`：anemia 段把 IV iron 改為「首選 ferric citrate switch」；結論加入第 6 點 ferric citrate 三合一解方
