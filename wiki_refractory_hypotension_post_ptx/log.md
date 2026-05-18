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

## [2026-05-12] update | 補上透析液 Ca 3.0 mEq/L + Ca 收支總帳 + sequencing 邏輯

病人補充：**透析液 Ca = 3.0 mEq/L（= 1.5 mmol/L，中等濃度，IDH 保護偏好設定）**。

每日 Ca 收支算出：
- 佳立鈣 binder：~1,200 mg elemental Ca/日
- 飲食：~400-800 mg/日
- 透析液淨流入（1.5 mmol/L vs ionized Ca ~1.1）：~65-170 mg/日 平均
- **總計 ~1,600-2,000 mg/日，遠超 KDIGO 1,500 mg/日上限**

關鍵 sequencing 邏輯：透析液 3.0 mEq/L 本身**不是錯**——IDH 保護偏好需要。問題是**疊加鈣型 binder 後總量過高**。正確順序：
1. 先換 binder（佳立鈣 → ferric citrate）：移除 1,200 mg/日 Ca 來源，**不影響 IDH**
2. Dialysate Ca 3.0 mEq/L 暫維持不動
3. 換 binder 後重新評估（追蹤 Ca、P、Hb 後再決定 dialysate 是否需要微調）

三份 analysis 補入：
- `analysis_iatrogenic_factors §8`：補上 Ca 收支表 + sequencing 表（先動 binder 不動 dialysate）
- `analysis_refractory_idh_treatment_plan`：病人摘要補透析液 3.0 mEq/L；鈣兩難段加 Ca 收支總帳表 + sequencing 結論
- `analysis_cad_contribution`：病人摘要補用藥 + 透析液 Ca；剩餘可動段把「透析液 Ca 2.5」改為「目前 3.0 暫維持，先動 binder」

## [2026-05-12] update | 補上乾體重 + UF rate + IDWG 數據與 volume axis 結論

病人補充：
- 乾體重 72.5 kg（兩年內已上調 10 kg）
- 最近 3 次脫水量 3.6 / 3.8 / 3.6 kg

算出：
- 平均 UF 量 3.67 L/次
- **UF rate = 11.2 mL/kg/hr（intermediate 區，理想 < 10）**
- IDWG = 3.67 / 72.5 = **5.06%（理想 < 4%）**

關鍵結論：volume axis 剩餘空間極小
- 乾體重已從 62.5 → 72.5 兩年加 10 kg、IDH 仍頑固 → volume 不是主軸
- UF rate 11.2 雖在 intermediate 邊緣偏高，但接近理想 < 10
- 可動的選項：減 IDWG（5% → 4%）、延長 HD 時間 +30 min、HDF 提頻、加 4 次/週 HD
- 主軸還是 vascular tone (PTH) + cardiac (HFpEF/CAD) + 醫源性 (dipyridamole)

兩份 analysis 補入：
- `analysis_cad_contribution`：病人摘要補乾體重/脫水/UF rate/IDWG；透析處方段加 UF rate 改善表 + 弔詭觀察（volume 不是主軸）
- `analysis_refractory_idh_treatment_plan`：病人摘要補同上；§5 透析處方微調段補 UF rate 表 + 弔詭觀察

## [2026-05-13] query | PTX 前後乾體重耐受差異分析

Query: 為什麼 PTX 前乾體重可以調到那麼低？術後兩年半已調高 10 公斤仍低血壓，CTR 僅 0.4。

新增臨床追蹤數據（DW+10kg、CTR 0.4），交叉比對 6 篇文獻。結論：排除心因性與單純容量不足，確認問題為 iPTH 17.5 導致的血管阻力不足（low SVR）。與 Leiba 2013 Case I 高度吻合。治療策略修正：不再上調乾體重，最高優先讓 iPTH 回升。

## [2026-05-13] consolidate | 四份 analysis 整併為三份

原有 4 份 analysis 存在大量重複（病人摘要 ×3、ferric citrate ×3、K/anemia ×3、三軸總結 ×3）。

整併：
- `analysis_pre_ptx_dry_weight_tolerance` **刪除**，獨特內容（CTR 0.4 排除心因性 + 術前三機轉對比 + Leiba Case I 對照表）併入 `analysis_refractory_idh_treatment_plan` 問題定位段
- `analysis_refractory_idh_treatment_plan`（#1 血管軸）：保留為 master，新增 CTR/DW 段，K/anemia 精簡為 cross-link → #2，ferric citrate 精簡為 cross-link → #3，Ca 收支精簡為 cross-link → #3
- `analysis_cad_contribution`（#2 心臟軸）：病人摘要精簡為心臟特有數據 + cross-link → #1，UF rate 表精簡為 cross-link → #1，三軸總結移除
- `analysis_iatrogenic_factors`（#3 藥物軸）：ferric citrate §8 保留為 authoritative，三軸總結移除

結果：19 頁（-1），三份 analysis 各有清晰焦點，重複內容統一歸屬。

## [2026-05-14] update | Dipyridamole 對 AVG 保護的 RCT 證據

Query: 停沛暢以改善 IDH，但沛暢是否對人工血管（AVG）有保護作用？

在 `analysis_iatrogenic_factors` 新增 AVG patency 段落。DAC Trial（Dixon 2009, AJKD）為最大型 RCT，結果陰性——dipyridamole + aspirin 未顯著改善 AVG primary unassisted patency。AVG 反覆狹窄主因為新生內膜增生非血栓，DAPT 已提供足夠抗血小板覆蓋。停沛暢不增加 AVG 風險，反而可能透過改善 IDH 間接保護 AVG。

## [2026-05-14] update | ADPKD 保留 EPO 分泌 + ferric citrate 五重效益 + PRA 穩定

病人補充：目前不用 EPO 也不輸血，Hb 12.3 自維持。ADPKD 囊腫壁細胞仍能分泌 EPO（ADPKD 特殊優勢）。三份 analysis 更新：
- `analysis_prognosis_without_transplant`：有利因子新增 ADPKD 保留 EPO 分泌；免疫段補入 PRA 不會繼續升高的保護意義
- `analysis_cad_contribution`：貧血段加入 EPO 獨立、補鐵預期效果更好、不輸血保護 PRA
- `analysis_iatrogenic_factors`：ferric citrate 從三重效益升級為五重效益（新增 IDH tolerance + 保護移植 PRA）

## [2026-05-14] update | 移植三道關卡完整框架（心臟 + 免疫 + 解剖）

在 `analysis_prognosis_without_transplant` 補入 ADPKD 巨腎解剖障礙段：原生腎佔據腹腔空間→移植腎放置困難、三種切除時機比較（移植前/同時/移植後）、TKV 評估建議。移植關卡表從兩道擴充為三道（心臟 SSS=16 + 免疫 PRA 44% + 解剖 ADPKD 巨腎）。

## [2026-05-14] update | FlowPRA 移植免疫數據補入預後分析

來源：健康存摺截圖（115/03/02 移植門診抽血）。FlowPRA Class I 44%（MFI 563）、Class II 11%（MFI 355）。在 `analysis_prognosis_without_transplant` 新增移植免疫障礙段：中度致敏（Class I 44%）為配對障礙，但 MFI 偏低是緩衝。移植有兩道關卡（心臟 SSS=16 + 免疫 PRA 44%），均需主動處理。對策含 SAB 細分、acceptable mismatch、desensitization、活體評估、減少未來致敏。風險分層表新增 PRA 44% 為不利因子。

## [2026-05-14] update | HFpEF 治療策略完整段落補入 CAD analysis

在 `analysis_cad_contribution_to_refractory_idh` 新增「HFpEF 的治療策略——搬開壓在上面的四座山」段。涵蓋：已完成介入盤點（5 項 ✅）、剩餘 5 層優先序（CAD 處理 → BB → 透析微調 → iPTH 回升 → 貧血糾正）、禁忌清單、現實期望框架（四因子疊加 → 目標剩 HFpEF 本身）。核心訊息：HFpEF 無特效藥，策略是移除加重因子。

## [2026-05-14] update | 病人自我管理建議（工作安全、猝死預警、飲食、運動）

在 `analysis_prognosis_without_transplant` 新增病人自我管理建議段。涵蓋：工作安全（透析隔天為最脆弱時段、緊急聯絡卡）、心臟猝死預警症狀辨識、K 6.0 飲食管理（楊桃禁忌、高鉀水果、低鈉鹽陷阱）、運動建議（Petraki 2008 透析中運動改善 BRS +23%）、推動心臟科再評估為最重要單一行動。

## [2026-05-14] update | Bisoprolol 處方建議補入 CAD analysis

在 `analysis_cad_contribution_to_refractory_idh` β-blocker 段新增具體處方建議：Concor（康肯）1.25 mg QD 起步、非透析日開始、滴定至 5 mg 目標。說明 bisoprolol 選擇理由（高 β1 選擇性、無 α-block、有 1.25 mg 最小劑型）與應避免的 BB（carvedilol、propranolol、labetalol）。

## [2026-05-14] query | 無移植情境下的預後推估

Query: 綜合所有臨床資料，假設無腎臟移植，能否預測這位病人的壽命？

新增 `analysis_prognosis_without_transplant`。基線 48 歲 HD 中位存活 5-7 年，但 SSS=16 嚴重可逆缺血為最大單一威脅（年心臟事件率 10-15%）。三情境推估：不處理 3-5 年、處理可調因子但不處理 CAD 5-7 年、積極處理 CAD + 可調因子 7-10+ 年。有利因子包括年輕、ADPKD 病因（優於 DM）、Alb 4.2、EF 73.7%、仍正常上班。核心訊息：可調空間不小，但 SSS=16 的時間窗口有限。

## [2026-05-15] update | Dipyridamole indication 確認 = AVG 保護 → reframe 為 N=1 trial-off + Aggrenox ER upgrade option

病人補充：**醫師回覆當初開沛暢是為了保護人工血管（AVG）**——確認了 5/14 上游已預先推測的 AVG 保護 indication。

整合兩個視角（rebased onto 5/14 upstream）：

| 來源 | 主要論點 |
|------|---------|
| 5/14 上游 | DAC trial 結果 marginal、AVG 狹窄機轉是 neointimal hyperplasia 而非血栓、低 BP 反而是 AVG 血栓風險（停藥可能間接保護 AVG）|
| 本次補充 | DAC trial 用 Aggrenox ER 200/25 mg BID，病人是沛暢 75 mg IR — formulation 不一致；N=1 trial-off 8 週 + access flow 監測 decision tree；若需重啟建議升級到 Aggrenox ER 而非回到 IR |

合併後 §1-§5 重寫：
- §indication 場景 #5 AVG 保護描述補上 DAC trial 絕對數字（28% vs 23%, p=0.03）+ KDOQI Grade 2B
- 「RCT 證據其實 marginal」段保留上游 3 個論點（狹窄機轉、formulation 不一致、已有 DAPT）+ 反向思考（停藥可能保護 AVG）
- §2 新增 N=1 trial-off 8 週 + access flow 監測方案 + decision tree
- §3 替代方案首選改為 Aggrenox ER（升級 formulation）
- §4 β-blocker 段整合為「為何沒在用 + 是否該重啟」雙重評估
- §5-§7 編號精簡（移除重複的 BB 段）

教訓：「沒有 indication」的強斷論在 5/12 已被 5/14 上游修正，本次再被病人 ground truth 確認 → 維持「需 indication 確認 + 客觀 N=1 trial 測量 net effect」的開放態度比較穩健。

## [2026-05-15] update | 兩難不對稱框架 — sym vs asym dilemma 的決策邏輯區分

延續 dipyridamole 的問題：「停或不停都觸到 AVG，這算兩難嗎？」答：**算，但是不對稱兩難**。

`analysis_iatrogenic_factors` 新增「🧠 兩難不對稱框架」段，明確區分：

| 維度 | 鈣的兩難（symmetric）| 沛暢的兩難（asymmetric）|
|------|---------------------|-----------------------|
| 兩個方向 | 高 vs 低（反向）| 停 vs 繼續（同一變數開關）|
| 兩個 outcome 強度 | 相當 | 不對稱 |
| 可實測嗎 | 難（要看數年血管鈣化進展）| 可（8 週 access flow Doppler）|
| 有逃脫路徑 | 無（妥協中等）| 有（trial-off + Aggrenox ER 備案）|
| 決策邏輯 | 妥協中等 + 動其他維度 | trial-off + 監測 + decision tree |

雙箭頭分析：「繼續沛暢」= 弱正 + 中負（IDH 持續傷 AVG）；「停沛暢」= 弱負 + 中正（IDH 改善反保護 AVG）→ stop 的 EV 較高。

2×2 結果矩陣：stop 的兩格 = 最佳 + 中等且有救；continue 的兩格 = 現狀爛 + 全爆。

一般化教訓：遇到「停藥 vs 繼續」兩難先檢核三條件（箭頭對稱？可實測？有 fallback？）。三條件都滿足 → trial-off 是高 EV 低風險選擇而非賭注。

跨頁 cross-link：iatrogenic 新段連到 refractory_idh_treatment_plan 鈣兩難段做對比參照。
