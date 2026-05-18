---
question: "盤點 48 歲 ADPKD 透析病人的完整藥單（保栓通 75 + 伯基 100 + 冠脂妥 10 + 沛暢 75）——有沒有可調整的醫源性 IDH 加重因子？"
date: 2026-05-11
last_revised: 2026-05-11
tags: [refractory_IDH, medication_review, iatrogenic, dipyridamole, triple_antiplatelet, vasodilator, parathyroidectomy, CAD, brain_MRA_negative, hyperkalemia, treatment_plan]
---

# 分析：藥物盤點——醫源性 IDH 加重因子的識別與調整

本分析為前兩篇的第三軸補位，與既有兩篇 analysis 構成完整三軸框架：

| 既有 analysis | 軸 | 介入難度 |
|---------------|------|---------|
| [analysis_refractory_idh_treatment_plan](analysis_refractory_idh_treatment_plan.md) | 血管 / PTH 軸 | 中（需數週調整 vit D/cinacalcet） |
| [analysis_cad_contribution_to_refractory_idh](analysis_cad_contribution_to_refractory_idh.md) | 心臟 / CAD 軸 | 高（chronic disease） |
| **本篇** | **藥物 / 醫源性軸** | **低（停藥即時生效）** |

本軸雖然 conceptually 是最後想到的，但**介入成本最低、效果可能最快**。

## 病人用藥現況

| 中文藥名 | 學名 | 類別 | 劑量 |
|----------|------|------|------|
| 保栓通 | Clopidogrel | P2Y12 抗血小板 | 75 mg QD |
| 伯基 | Aspirin（腸溶錠） | COX-1 抗血小板 | 100 mg QD |
| 冠脂妥 | Rosuvastatin | Statin | 10 mg QD |
| **沛暢** | **Dipyridamole** | **PDE 抑制（抗血小板 + 血管擴張）** | **75 mg QD（劑量可能為 TID）** |
| Midodrine | Midodrine | α-agonist | 洗前 5 mg + 中段加 5 mg |
| **佳立鈣錠** | **Calcium carbonate** | **磷結合劑 + 鈣補充** | **500 mg × 2/餐 × 3 餐 = 6 顆/日（1,200 mg elemental Ca/日）** |

未列出但臨床上重要的觀察：**沒有 β-blocker、沒有 ACE/ARB、沒有非鈣型 phosphate binder**。

### ⚠️ 重要：藥單需要 reconciliation

病人個人醫療摘要（2026/05）的「目前用藥」段**只列了 midodrine + 碳酸鈣**，並標註「需向醫師確認是否還有其他用藥（活性維生素 D、擬鈣劑、其他）」。

→ 上述 4 個藥（含沛暢/dipyridamole）是病人另行告知本 wiki 的內容，**摘要文件未確認**。建議：
- 與藥局做正式 medication reconciliation
- 確認上述 4 個藥是否仍在用、實際劑量、是否有其他未列藥物（特別是活性維生素 D、cinacalcet/calcimimetic、phosphate binder、止痛藥）
- 確認過去是否用過 β-blocker / ACE/ARB 而停藥

## 核心發現：Dipyridamole 是可調整的醫源性 vasodilator

Dipyridamole 不是純抗血小板，是**雙機轉**：

| 機轉 | 細節 | 對 IDH 的方向 |
|------|------|--------------|
| PDE 抑制 → cAMP 累積 | 血小板抑制 + **血管平滑肌舒張** | **🔥 加重** |
| 抑制 adenosine 重吸收 | 細胞外 adenosine ↑ → **強血管擴張作用** | **🔥 加重** |

→ Dipyridamole 副作用最常見就是「**頭痛、頭暈、低血壓**」（藥廠仿單明列）；CTH 仿單直接寫「**避免同時使用其他降血壓藥**」。

### 為什麼這個發現對「PTX 後 PTH 撤除」病人特別重要

[concept_post_ptx_hemodynamic_changes](concept_post_ptx_hemodynamic_changes.md) 的雙路徑模型：

- 路徑 1（細胞外鈣 ↓）→ 血管舒張
- 路徑 2（PTH 撤除 → 失去 cAMP 促鈣內流訊號）→ 血管舒張

**Dipyridamole 的 PDE 抑制就是讓 cAMP 留得更久** → 直接加重路徑 2 已經造成的損傷。這位病人在血管平滑肌已經失去 PTH 訊號的情況下，又被人為加上一個 cAMP-elevating 藥 → **雙重 cAMP 加重血管舒張**。

[Kawashima 1990](src_kawashima1990_pth_intracellular_calcium_vsmc.md) 的 cAMP 路徑研究是這個推論的機轉基礎：PTH 透過 cAMP → L-type Ca channel 增強鈣內流。Dipyridamole 升高 cAMP 但**沒有 PTH 受體的下游分流訊號**，所以淨效果是血管擴張（不像 PTH 在 cAMP 之外還能 fine-tune 鈣內流）。

## 完整藥物 → IDH 影響評分

| 藥物 | 直接 IDH 加重 | 反射代償抑制 | 淨影響 | 可否停 / 調整 |
|------|--------------|------------|--------|-------------|
| Clopidogrel | 0 | 0 | 中性 | 不能停（PCI 保護） |
| Aspirin | 0 | 0 | 中性 | 不能停（PCI 保護） |
| **Dipyridamole** | **+++（vasodilation）** | 0 | **🔥 強加重** | **可重新評估** |
| Rosuvastatin | 0 | 0 | 中性 | 不能停（CV 保護） |

→ **單一最大可調整因子 = Dipyridamole**。

## 為什麼 Triple antiplatelet 不是 PCI 標準療法

PCI 後標準是 **DAPT（aspirin + P2Y12）**：6-12 個月，之後 aspirin 單藥終身。**三抗（加 dipyridamole）不是 routine**。

合理加 dipyridamole 的場景：

1. **腦中風 / TIA 二次預防**（Aggrenox = aspirin + dipyridamole 200 mg ER BID，是 ESPS-2、ESPRIT 試驗驗證的方案）
2. **冠脈微血管功能障礙 / angina with non-obstructive coronaries**（anti-anginal 角色，少見）
3. **PCI 後 high thrombotic risk + 醫師個人偏好加第三線**（缺乏 RCT 支持）
4. **ADPKD 顱內動脈瘤 + 中風史**（特殊族群）
5. **AV graft 保護**：**Aggrenox ER 200 mg + aspirin 25 mg BID** 在 DAC trial（Dixon 2009, NEJM）顯示 modest 效果（1 年 primary unassisted patency 28% vs 23%, p=0.03），KDOQI Vascular Access guideline 列為 Grade 2B（可選擇）；詳細 RCT 分析見下方

### 🔑 關鍵資訊更新：MRA 陰性 + 醫師說明 indication = AVG 保護

**腦部 MRI/MRA 2023/12**：
- 顱內動脈瘤陰性（威利氏環無異常）✅
- 無微出血（SWI）、無急性缺血（DWI/ADC）
- 僅輕微 WMH（可能 IDH 累積）

→ **場景 1（中風二次預防）和場景 4（ADPKD 動脈瘤）皆被影像排除**

**醫師回覆當初加 dipyridamole 的 indication = AVG 保護（場景 5）**

→ 這是有 RCT 證據的 indication，**不是隨意 off-label 加藥**——前面「dipyridamole 沒有強 indication」的判斷需要修正。

### 🔑 Dipyridamole 對 AVG 的保護——RCT 證據其實 marginal

病人有左前臂 Loop AVG、反覆狹窄（2026/02 PTA, 90%）。停沛暢會不會增加 AVG 風險？最大型 RCT 數據其實**比直覺薄弱**：

| 研究 | 設計 | 結果 |
|------|------|------|
| **DAC Trial（Dixon 2009, NEJM）** | Aggrenox ER 200/25 mg BID vs 安慰劑，新 AVG | 1 年 primary unassisted patency 28% vs 23%（p=0.03，**統計顯著但臨床 marginal**，NNT ~20）|
| Kaufman 2003 | RCT | Dipyridamole 對 AVG 血栓無顯著保護 |
| KDOQI Vascular Access guideline | Grade 2B | 列為**可選**而非常規用藥 |

**三個削弱「為了 AVG 必須繼續」的論點：**

1. **狹窄機轉錯位**：AVG 反覆狹窄的主因是**新生內膜增生（neointimal hyperplasia）**，不是血栓。抗血小板藥對新生內膜增生效果極有限。這位病人狹窄位置在 in-graft + venous junction（典型 intimal hyperplasia）正符合此情境。
2. **Formulation 不一致**：DAC trial 證據基礎是 **Aggrenox ER 200 mg + aspirin 25 mg BID**，病人吃的是**沛暢 75 mg IR**——IR formulation 的 AVG patency RCT 證據幾乎沒有。
3. **病人已有 DAPT 保護**：aspirin（伯基）+ clopidogrel（保栓通）= DAPT 已提供足夠抗血小板覆蓋。Dipyridamole 作為第三個抗血小板藥，RCT 不支持額外 AVG 保護效益。

**反向思考**：停沛暢 → 改善 IDH → 透析中血壓更穩 → AVG 血流更穩定 → **低血壓本身是 AVG 血栓的風險因子**（低流速 → 易血栓），改善 IDH 反而可能**間接保護** AVG。

**→ 結論：停沛暢的 AVG 風險不大，反而可能透過 IDH 改善間接保護 AVG。但保險起見，建議 N=1 trial-off + 客觀監測（見 §2）。**

## 🧠 兩難不對稱框架：為什麼 N=1 trial-off 而非二選一

決定停沛暢還是繼續沛暢是個兩難——兩個方向都觸到 AVG。但這**不是對稱兩難**，跟 [analysis_refractory_idh_treatment_plan 的「鈣的兩難」](analysis_refractory_idh_treatment_plan.md#鈣的兩難calcium-dilemma)（true symmetric）性質不同。理解兩者差異有助於選擇正確的決策邏輯。

### 雙箭頭分析

兩個選項都觸到 AVG，但強度不對稱：

| 選項 | 對 AVG 的箭頭 | 強度 |
|------|--------------|------|
| 繼續沛暢 | (+) 微弱抗血小板加碼 | 弱（RCT marginal、formulation 不對、已有 DAPT） |
| 繼續沛暢 | (−) IDH 持續 → 透析中低流速 → endothelial stress → 血栓 | 中等（low flow 是 documented AVG 失能風險） |
| 停沛暢 | (−) 失去（弱的）抗血小板加碼 | 弱 |
| 停沛暢 | (+) IDH 改善 → 透析中血流穩定 → AVG 流量 stable | 中等 |

→「繼續」側：弱正 + 中負；「停藥」側：弱負 + 中正 → **不對稱，停藥 expected value 較高**。

### 2×2 結果矩陣

|  | AVG flow 穩定 | AVG flow 惡化 |
|---|--------------|--------------|
| **繼續沛暢** | 維持現狀（IDH 折磨繼續、AVG 還是 2 月才 PTA 90%）| 最糟（IDH + AVG 都壞，藥沒幫上忙）|
| **停沛暢** | **最佳結局**（IDH 改善 + AVG 因流量穩定反而更好）| IDH 改善但 AVG 惡化 → 升級到 Aggrenox ER（見 §3）|

→「停」的兩格 = 最佳 + 中等且有救；「繼續」的兩格 = 現狀爛 + 全爆。**停的 expected value > continue**。

### 為什麼 N=1 trial-off 是解法（vs. 鈣兩難無法）

| 維度 | 鈣的兩難（真對稱）| 沛暢的兩難（不對稱）|
|------|------------------|-------------------|
| 兩個方向 | 高 vs 低（反向）| 停 vs 繼續（同一變數的開關）|
| 兩個 outcome 強度 | 相當 | 不對稱 |
| 可實測嗎？ | 難（要看數年血管鈣化進展）| **可（8 週 access flow Doppler）** |
| 有逃脫路徑嗎？ | 無（必須選一邊或妥協中等）| **有（trial-off + 升級 Aggrenox ER 備案）** |
| 決策邏輯 | 妥協中等值（dialysate Ca 3.0）+ 動其他維度（換 binder） | **trial-off + 客觀監測 + decision tree** |

→ **沛暢之所以可 trial-off，正是因為兩難不對稱 + 可監測 + 有 fallback**。

→ **鈣兩難之所以只能妥協選中等 dialysate Ca（3.0 mEq/L）+ 動 binder（佳立鈣 → ferric citrate）**，是因為對稱 + 短期內不可測 + 沒有等效替代品。

### 一般化教訓

遇到任何「停藥 vs 繼續」的兩難時，先做這個分類：

1. **箭頭強度對稱嗎？** 不對稱 → 直接選 EV 高的那一邊
2. **可不可以實測？** 可測 → trial-off + 監測；不可測 → 必須事前決策
3. **有沒有 fallback / 備案？** 有 → 試錯成本低，可大膽 trial；無 → 必須保守

沛暢同時滿足三個條件（不對稱 + 可測 + 有 Aggrenox ER 備案）→ **trial-off 是高 EV、低風險的選擇**，而不是「需要勇氣的賭注」。

## 行動建議（依優先序，2026/05 修訂為 AVG-protection-aware 版本）

### 1. ✅ Indication 已確認 = AVG 保護（DAC trial）

不需再追問為什麼開——已知是 AVG 保護用途。轉問題：**這個 indication 在這位病人身上的 net effect 是否仍 positive？**

兩個切角：

| 切角 | 證據 | 對結論的影響 |
|------|------|------------|
| **AVG 真的有被保護嗎？** | 2026/02 PTA 90% 狹窄、反覆 PTA → 不像有效 | 削弱「為了 AVG 必須繼續」的論證 |
| **Formulation 對嗎？** | DAC trial 用 Aggrenox ER 200 mg + aspirin 25 mg BID；病人是沛暢 75 mg IR | IR formulation 缺乏 AVG 保護的 evidence base |

### 2. 🔑 建議：N=1 trial-off 1-2 個月 + 客觀監測

**不是「直接停」也不是「不動」，是「客觀測量 net effect 後再決定」。**

具體方案：

| 階段 | 動作 | 監測 |
|------|------|------|
| Baseline（試停前 2 週）| 紀錄目前 IDH 頻率/深度、access flow rate、AVG bruit/thrill 變化 | 抽血 baseline + Doppler access flow（如可）|
| Trial-off（8 週）| 停 dipyridamole | 每 4 週 access flow + 每次透析 IDH 紀錄 |
| 評估（停藥滿 8 週）| 客觀比較 IDH 改善 vs AVG flow 變化 | 同上 |

**Decision tree（停藥後 8 週）：**

| IDH 變化 | AVG flow 變化 | 結論 |
|----------|--------------|------|
| 明顯改善（BP 不再掉 < 80） | 穩定 | **繼續停藥**——真正 culprit 找到 |
| 明顯改善 | 流量下降明顯 | **討論重啟，但建議換成 Aggrenox ER**（劑量正確的版本） |
| 無改善 | 穩定 | **繼續停藥**——藥本來就無效，IDH 元兇在他處 |
| 無改善 | 流量下降明顯 | **重啟 Aggrenox ER + 加速備用通路規劃**（雙線並行）|

### 3. 替代方案（若 trial-off 後決定仍需抗血栓加強）

- **改 Aggrenox ER（首選）**：DAC trial dose（dipyridamole 200 mg ER + aspirin 25 mg BID），若要承擔 vasodilation 副作用至少拿到 RCT 級療效；注意 aspirin 劑量會跟現有伯基 100 mg QD 不同，需重整
- 改 cilostazol：vasodilation 性質類似，**不會更好**
- 改 NOAC（dabigatran/rivaroxaban）：抗凝而非抗血小板，AVG 證據混雜，出血風險高
- 加 fish oil：DAC trial 也有 fish oil arm（小幅 benefit），可能可同時試
- 改純 DAPT（aspirin + clopidogrel）：已有了，AVG 保護論證最弱（KDOQI 未列）

### 4. β-blocker 雙重評估：為何沒在用 + 是否該重啟

藥單沒列 β-blocker。LCX-stent 後 + HFpEF + SSS=16 標準應該要用。

**第一步：確認過去用藥史**
- 已試過但因 IDH 停掉？
- 從未開（少見）？
- 病人自行停藥？

→ 跟主治確認。**如果是「停藥因 IDH」**，那 dipyridamole 反而**正是被誤留下來**的 culprit——應該優先處理 dipyridamole 而非 β-blocker。

**第二步：重新挑戰 BB（先解決 dipyridamole 後）**
- 心超 E/A 0.62 是 **HFpEF physiology**，BB 減慢 HR 延長 diastolic filling time 對 stiff ventricle 有助益
- 核醫 SSS=16 是 **active reversible ischemia**，BB 抗 ischemia 效益強
- 起始：bisoprolol 1.25 mg QD（cardioselective、無 α-block）；避免 carvedilol（α-block 加重 IDH）
- 詳細處方建議見 [analysis_cad_contribution §β-blocker](analysis_cad_contribution_to_refractory_idh.md#β-blocker-在-hfpef--active-ischemia-的角色)

### 5. 不要為了 IDH 停 aspirin / clopidogrel / statin

這三個都是 LCX-stent 後 mandatory 保護，停藥的 stent thrombosis / re-MI / CV death 風險遠大於 IDH 帶來的不適。

### 6. 高血鉀（K 6.0 上升趨勢）—— 醫源性 IDH 加重的另一面

病人 2026/04 抽血 K 6.0（3/19 為 5.7），上升趨勢。雖然不是直接 BP 機轉，但：
- **加重透析後段抽筋**（病人摘要主訴）
- **在 active ischemia 患者增加心律不整風險**
- 是可調整的：飲食 review、Lokelma（sodium zirconium cyclosilicate）or Patiromer、透析液 K 從 2.0 改 1.5 mEq/L

→ 不直接是 IDH 原因，但是「同 axis 可一起處理」的 modifiable factor。

### 7. 🔥 佳立鈣 1,200 mg/日 + 透析液 Ca 3.0 mEq/L —— 二級可調整因子

實際劑量：**佳立鈣 500 mg × 2 顆/餐 × 3 餐 = 6 顆/日 = 3,000 mg 碳酸鈣 = 約 1,200 mg elemental Ca/日**
透析液 Ca：**3.0 mEq/L = 1.5 mmol/L**（中等濃度，IDH 保護偏好）

**每日 Ca 收支總帳：**

| 來源 | 估算 |
|------|------|
| 佳立鈣（鈣型 binder） | ~1,200 mg elemental Ca/日（adynamic bone 患者吸收率較高） |
| 飲食 | ~400-800 mg/日 |
| 透析液淨流入（1.5 mmol/L vs 患者 ionized Ca ~1.1） | ~65-170 mg/日 平均（450-1,200 mg/週 / 3 次） |
| **總計** | **~1,600-2,000 mg/日 → 遠超 KDIGO 上限 1,500 mg/日** |

**問題定位：**

1. **KDIGO 上限警戒**：CKD-MBD 患者建議 binder 來源 Ca < 1,500 mg/日，**加上透析液 + 飲食總計遠超此值**
2. **磷已控制良好**（P=4.6）→ 不需要這麼強的 binder 壓制
3. **adynamic bone 強烈懷疑**（iPTH 17.5 + ALP 61 偏低）→ 骨頭無法吸收鈣 → **多餘鈣跑到血管 / 軟組織**
4. **腹部 MRI 證實**：主動脈 + 冠狀動脈鈣化 → 雙高設定持續加重這個進展
5. **病人合併缺鐵性貧血**（MCV 69.2、MCH 21.0、RDW 19.3、Hb 12.3）

**Sequencing 關鍵：先換 binder，不要先動透析液**

| Lever | 目前狀態 | 理想方向 | 對 IDH 的影響 |
|-------|---------|---------|--------------|
| **Binder（先動）** | 佳立鈣 1,200 mg/日 | **換 ferric citrate**（移除整個 binder Ca 來源） | **無不利影響** |
| Dialysate Ca（後評估） | 3.0 mEq/L（1.5 mmol/L） | 暫維持 3.0 mEq/L（IDH 保護需要） | 降到 2.5 會加重 IDH |

→ **正確順序：先換 binder（移除最大 Ca 來源、不影響 IDH），再評估 dialysate Ca 是否需要微調**。透析液 3.0 mEq/L 本身不是設定錯誤——它是 IDH 患者的合理選擇（見 [concept_perioperative_calcium_management](concept_perioperative_calcium_management.md)）；問題在於**疊加鈣型 binder 後總量過高**。

**理想對策：換成鐵基 phosphate binder**

| 選項 | 學名 | 機轉 | 對這位病人的雙重效益 |
|------|------|------|--------------------|
| **🥇 鐵爾思 / Auryxia** | Ferric citrate | 鐵基 binder，腸吸收 ~1% 為元素鐵 | **同時解決鈣負擔 + 缺鐵貧血** |
| 福斯靈 / Renvela | Sevelamer | Polymer binder，無金屬 | 解決鈣負擔；LDL ↓ 額外效益 |
| 福斯耐爾 / Fosrenol | Lanthanum carbonate | 稀土金屬 binder | 解決鈣負擔；長期累積疑慮 |

**強烈推薦 ferric citrate（五重效益）**：
1. 移除 1,200 mg/日 Ca load → 減緩血管鈣化進展
2. 口服 elemental iron → 改善缺鐵性貧血（MCV 69.2）
3. 讓 iPTH 回升空間 → 改善 adynamic bone + 血管張力
4. Hb 上升 → 改善 IDH tolerance + 心肌氧供
5. **減少未來輸血需求 → PRA（目前 Class I 44%）不再升高 → 保護移植機會**

附註：病人目前不用 EPO 也不輸血（ADPKD 囊腫壁細胞仍分泌 EPO，Hb 12.3 自維持）。自產 EPO + 補鐵 → Hb 預期可升至 13-14，不需額外 EPO。

實務建議：
- 跟腎臟科 + 健保用藥規範討論轉換（ferric citrate 在台灣有健保但有條件）
- 過渡期可先**減量碳酸鈣**（6 顆 → 4 顆 → 2 顆），同時加 ferric citrate，每月測 P + Ca + Hb
- 目標：P 維持 < 5.5，Ca 維持 8.4-9.5，Hb 拉到 13-14

## 預期效果（2026/05 修訂為 trial-off 框架）

**N=1 trial-off 的時間軸：**

- **2-3 天**：cAMP 積累效應消退（dipyridamole 半衰期 10-12 hr），血管張力部分恢復
- **1-2 週**：透析中血壓掉的深度若有改善應已可見（5-15 mmHg 範圍）
- **4 週**：第一次 access flow 追蹤，看 AVG 是否惡化
- **8 週**：第二次 access flow + 完整 IDH 評估 → 做留 / 停 / 換 Aggrenox ER 的決策
- **長期（若停藥確認）**：搭配 PTH 回升 + cardiac-protective HD，可能進入正向循環

**但這個介入再有效也不夠單獨解決 IDH**——病人有 multiple substrate（CAD、PTH↓、BRS↓、HFpEF、可能無 BB、佳立鈣 1,200 mg），dipyridamole trial-off 是其中**最容易做、最快有 feedback** 的一步，但不是唯一答案。

三軸整合框架與優先序見 [analysis_refractory_idh_treatment_plan 結論段](analysis_refractory_idh_treatment_plan.md)。**藥物軸（本篇）建議先試**——成本最低，效果最快。

## 結論（2026/05 修訂 — AVG-protection-aware 版本）

**第一級可調整因子：Dipyridamole N=1 trial-off + 客觀監測**（不是直接停，是「測量」）
**第二級可調整因子：碳酸鈣換成 ferric citrate**（adynamic bone + 鈣負擔 + 缺鐵三合一）

醫師確認 dipyridamole 用於 AVG 保護（DAC trial indication），但這位病人 AVG 反覆狹窄 + IR 75 mg 不是 DAC trial 的 ER 200 mg formulation → indication 真實但效果可疑。

1. **第一步：藥物 reconciliation** — 病人摘要與另行告知的藥單不完全一致，先確認實際用藥
2. **第二步：跟透析科 / 血管外科 / 心臟科討論 dipyridamole trial-off 方案** — 8 週 trial-off + access flow 監測 + IDH 紀錄；依結果做 decision tree（見 §2）
3. **第三步：與腎臟科討論 ferric citrate 取代碳酸鈣** —— 解決 Ca load + 缺鐵雙問題
4. **不論結果如何，都不要停 aspirin/clopidogrel/statin**
5. **重新評估 BB**：HFpEF + active ischemia 雙重 indication；先解決 dipyridamole trial-off 再考慮重啟
6. **高血鉀（K 6.0）一併處理**：飲食、binder、透析液 K 微調
7. **同時啟動前兩篇 analysis 的血管軸 + 心臟軸介入**
8. **若 trial-off 結果是「需重啟」**：建議升級 formulation 到 Aggrenox ER 200 mg + aspirin 25 mg BID（DAC trial 證實的劑型）而非回到沛暢 75 mg IR

## 引用來源

- [src_kawashima1990_pth_intracellular_calcium_vsmc](src_kawashima1990_pth_intracellular_calcium_vsmc.md)（cAMP-vasculature 機轉基礎）
- [src_campese1989_calcium_pth_blood_pressure](src_campese1989_calcium_pth_blood_pressure.md)（PTH-Ca-BP 框架）
- [src_leiba2013_severe_hypotension_after_ptx](src_leiba2013_severe_hypotension_after_ptx.md)（術後低血壓即使藥物（midodrine, fludrocortisone）也難治的脈絡）

外部資訊來源：
- 藥品仿單（CTH 醫院 Peysan / Dipyridamole 條目）
- 病人個人醫療摘要（2026/05），含腦部 MRI/MRA 2023/12 報告

## 相關頁面

- [analysis_refractory_idh_treatment_plan](analysis_refractory_idh_treatment_plan.md)
- [analysis_cad_contribution_to_refractory_idh](analysis_cad_contribution_to_refractory_idh.md)
- [analysis_prognosis_without_transplant](analysis_prognosis_without_transplant.md) — Dipyridamole trial-off 等本軸介入是改善預後的低成本高效益槓桿
- [concept_post_ptx_hemodynamic_changes](concept_post_ptx_hemodynamic_changes.md)
- [concept_pth_cardiovascular_effects](concept_pth_cardiovascular_effects.md)
