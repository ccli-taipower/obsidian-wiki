---
question: "建立病人 4 次住院的完整時間軸，整合既有 wiki 框架（IDH / CAD / iatrogenic / prognosis）。"
date: 2026-05-20
tags: [hospitalization_timeline, ADPKD, TAE, renal_embolization, LCX_stent, PTX, dialysis_history, transplant_waitlist, medication_history]
---

# 分析：住院病歷時間軸（4 次住院 + 既有框架整合）

## 來源

89 張健康存摺截圖（IMG_0923-1013，PNG）OCR 萃取。原始影像保存於 `raw/hospitalization/`（含 PII，已 `.gitignore` 不上 GitHub）。本 markdown 摘要層**僅保留結構化臨床資訊**、無身分證號 / 病歷號等敏感欄位。

## 病人脈絡（更精確版）

之前 wiki 寫「HD 11 年」其實混淆透析方式。實際時間軸：

| 時期 | 透析方式 | 持續時間 |
|------|---------|---------|
| 2015/03 - 2019/10 | **腹膜透析（PD）** Tenckhoff catheter | 4.5 年 |
| 2019/10/22 起 | **血液透析（HD）** Equistream perm-cath → AVG | 6.5 年（至 2026/05）|
| **合計透析年資** | | **11 年**（總計 11 年，HD 6.5 年）|

**移植等待**：2015 年起在 NTUH 移植門診評估、登記移植 waiting list → **已等 11 年**。

## 四次住院 summary table

| # | 日期 | 天數 | 醫院 | 主診斷 | 主要處置 |
|---|------|------|------|--------|---------|
| 1 | 2019/10/15-24 | 10 天 | NTUH 外科 | ADPKD 右腎囊腫出血 + PD 改 HD | 右腎 TAE + Permcath 植入 |
| 2 | 2019/12/04-09 | 6 天 | NTUH 外科 | ADPKD 左腎囊腫出血 | 左腎 TAE |
| 3 | 2023/03/10 | (短) | **東元綜合醫院**（新竹） | CAD triple vessel disease | LCX PCI + DES |
| 4 | 2023/10/11-16 | 6 天 | NTUH 外科 | Secondary hyperparathyroidism | Subtotal PTX + right forearm autoimplant |

---

## 住院 #1：右腎 TAE + PD 改 HD（2019/10/15-24，NTUH）

### 入院主訴
血尿、腹脹（右腎 ADPKD 囊腫出血、囊腫持續增大）

### 病史脈絡
- 41 歲男性（1978 生），ADPKD + ESRD
- **2015 開始 PD**（腹腔內 Tenckhoff catheter）
- **2015 起於 NTUH 移植門診評估、登記移植 waiting list**
- 但 polycystic kidney 持續長大、PD 效率下降 + 出現血尿

### 主要處置
| 日期 | 處置 |
|------|------|
| 2019/10/15 | Abdominal MRI（評估腎臟大小、出血部位）|
| 2019/10/17 | **右腎 TAE**（trans-arterial embolization）：右腎動脈 + capsular artery，多 coils embolization → "Nearly stasis of right renal artery" |
| 2019/10/22 | PD 停用 |
| 2019/10/23 | **Permcath 植入**（Equistream 14.5Fr long-term HD catheter）→ HD 啟動 |

### 為什麼做 TAE
ADPKD 患者 TAE 有雙重目的：
1. **止血**（cyst hemorrhage 急性處理）
2. **腎臟縮小**（為將來移植做空間預備）→ 對應 [analysis_prognosis_without_transplant](analysis_prognosis_without_transplant.md) 的解剖關卡

### 跨頁意涵
- 確認 ADPKD 巨腎是長期持續的解剖障礙
- 透析方式從 PD → HD 的關鍵節點
- 與 5/19 下肢動脈超音波（移植解剖關卡 vascular face）一脈相承——**移植準備已持續 11 年**

---

## 住院 #2：左腎 TAE（2019/12/04-09，NTUH）

### 入院主訴
左腎囊腫出血（右腎 TAE 後 1.5 個月，左腎也出現類似問題）

### 主要處置
| 日期 | 處置 |
|------|------|
| 2019/12/04 | 入院 + 入院前 lab |
| 2019/12/05 | **左腎 TAE**：左腎動脈 multiple coils → "Nearly stasis of left renal artery" |

### 建議追蹤
"please follow up at Dr. 影像醫學科 OPD, abdomen and pelvis CT scan 3-6 months later"

### 意涵
雙腎 TAE 完成（2019/10 右側 + 2019/12 左側）→ **雙腎血流大幅減少**、囊腫不再增長
- 這也部分解釋為何病人**沒繼續輸血、Hb 仍 12.3 自維持**（如 [analysis_iatrogenic_factors §7](analysis_iatrogenic_factors_in_refractory_idh.md) 所述，ADPKD 囊腫壁仍分泌 EPO）——雙腎 TAE 後 EPO 分泌大致仍存在（沒有完全梗塞），是 ADPKD 病人的特殊優勢

---

## 住院 #3：LCX PCI + DES（2023/03/10，東元綜合醫院）

### ⚠️ 注意：這次住院在**東元綜合醫院（新竹）**，不是 NTUH

→ 這代表病人**部分照護分散在多家醫院**——心臟科介入在東元、移植 + PTX + 一般追蹤在 NTUH。雙院系統可能造成藥物 / 紀錄整合問題。

### 入院主訴
胸悶 + 喘 1-2 個月（dyspnea on exertion）

### 病史 at admission
- 45 歲，ESRD HD M/W/F、HTN regular control 於東元
- 已接種 COVID-19 疫苗 5 劑（含 AZ × 2、Medigen × 2、Novavax × 1）

### 心導管結果 + 處置
| 發現 | 處置 |
|------|------|
| **Coronary artery disease with triple vessel disease**（三血管病變）| **LCX PCI + DES × 1**（drug-eluting stent，成功）|
| RCA 病變（後續確認為 CTO）| 未處理 |
| LAD 病變 | 未處理 |

### 出院用藥
- **Plavix 75 mg** QD × 4 天，其餘門診續用

### 跨頁意涵
- **三血管病變從 2023/03 就被診斷**——不是 2025/08 核醫才發現！
- 2023/03 只處理了 LCX，**RCA CTO + LAD 已知存在但未介入**
- 對應 5/19 心臟科門診 [Q1](file:///Users/ccli/Documents/病歷/心臟內科門診清單_2026-05-19.pdf) RCA CTO 開通議題：**這個議題其實已經拖了 3 年**

### 對 IDH / CAD 軸的重要校正

之前 wiki 寫「核醫 2025/08 才發現缺血擴及 LAD/LCX」——其實 **2023/03 心導管就已經知道 triple vessel disease**。校正：核醫不是「發現」，是「**證實之前心導管所見的 LAD/LCX 區域仍在持續缺血**」（沒有自癒、沒被當時的 PCI 解決）。

→ 更新 [analysis_cad_contribution](analysis_cad_contribution_to_refractory_idh.md) 病人摘要：CAD 已知 triple vessel 的時間從「核醫 2025/08」前提到「**2023/03 心導管確認**」。

---

## 住院 #4：Subtotal PTX（2023/10/11-16，NTUH）

### 入院主訴
Secondary hyperparathyroidism, ESRD related — 高 PTH 控制不佳

### 入院時 vital signs（IMG_0996）
- BH 168 cm, BW **65.9 kg**（vs 2026 目前 72.5 kg → 2.5 年加 6.6 kg）
- **BP 158/99 mmHg**（**HTN 明顯**——這對應後續 PTH 撤除後血壓崩潰的 baseline）
- HR 87 bpm, T 36.8°C

### 🔥 入院時的完整用藥清單（IMG_0994）

| 藥物 | 學名 | 類別 | 目前狀態 |
|------|------|------|---------|
| Bokey | Aspirin 100 mg | COX-1 抗血小板 | ✅ 仍在用 |
| Peysan | Dipyridamole | PDE 抑制（抗血小板 + vasodilator）| **2026/05/19 停藥** |
| **Norvasc** | **Amlodipine 鈣離子阻斷劑** | **降壓藥** | **❌ 已停**（PTX 後血壓崩潰停藥）|
| Crestor 10 mg | Rosuvastatin | Statin | ✅ 仍在用 |
| **Ezetrol** | **Ezetimibe** | **腸道膽固醇吸收抑制劑** | **❌ 已停（原因不明）**|
| Plavix | Clopidogrel | P2Y12 抗血小板 | ✅ 仍在用 |

### 🔥 重要發現：Ezetrol 為何停？

PTX 前曾有 **Crestor + Ezetrol 雙重 LDL 控制**。Ezetrol 不是降壓藥、跟 PTX 沒有機轉關聯——**為什麼會被停掉沒有明確理由**。

可能原因：
1. PTX 後簡化用藥的副作用（簡化得太多）
2. 健保限制 / 自費考量
3. 雙院系統溝通失誤（東元 vs NTUH 用藥差異）
4. 出院摘要漏列、實際從沒停過？

→ **對應 5/19 [Q4 LDL 100 議題](file:///Users/ccli/Documents/病歷/心臟內科門診清單_2026-05-19.pdf)**：可能不需要把 Crestor 從 10 → 20 mg，**只要加回 Ezetrol 10 mg QD 就能直接拉下 LDL 25-30 mg/dL**（典型 ezetimibe 效果）→ 達到 < 70 目標。

**明天 / 下次門診的關鍵問題**（更新版）：
> 「我 PTX 前是 Crestor + Ezetrol，PTX 後 Ezetrol 不知為何被停了。能不能直接加回 Ezetrol 10 mg QD？這可能比上調 Crestor 更有效率、且不會增加 statin 相關副作用（肌肉、肝臟）。」

### 手術細節（IMG_1001）
**Total parathyroidectomy + right forearm autoimplantation 2023/10/12**

切除的副甲狀腺重量：
| 位置 | 重量 |
|------|------|
| Left lower | 0.979 g |
| Right superior | 0.179 g |
| Right inferior | **2.612 g**（最大）|
| Right upper（部分保留）| 0.80 g → 右前臂 autoimplantation |

→ 病人摘要寫「subtotal PTX」是準確的（保留 0.80g 作 autoimplant）。

### 術後追蹤建議
照會腎臟科透析（兼 Cr > 4 + 血漿置換術 indication）→ 後續 IDH 由腎臟科主管

---

## 跟現有 wiki 三軸 + 預後的整合

| 既有 analysis | 本住院時間軸提供的新校正 |
|--------------|----------------------|
| [analysis_refractory_idh_treatment_plan](analysis_refractory_idh_treatment_plan.md)（血管/PTH 軸）| PTX 前 BW 65.9 kg + BP 158/99 → PTX 後乾體重 +10 kg、BP 80-90，巨大轉變的 baseline 確認 |
| [analysis_cad_contribution](analysis_cad_contribution_to_refractory_idh.md)（心臟/CAD 軸）| **CAD triple vessel 從 2023/03 就確認**，不是 2025/08 才知道；RCA CTO + LAD 拖了 3 年未處理 |
| [analysis_iatrogenic_factors](analysis_iatrogenic_factors_in_refractory_idh.md)（藥物軸）| **Ezetrol 被不明原因停藥**——對應 LDL 100 高的可能元兇；加回 Ezetrol 是 Q4 的低成本解法 |
| [analysis_prognosis_without_transplant](analysis_prognosis_without_transplant.md)（預後）| 雙腎 TAE（2019）+ 移植等候 11 年——免疫關卡的時間累積；解剖關卡的長期準備 |

## 觀察到的「兩院系統」議題

- **NTUH**：移植、PTX、一般追蹤
- **東元綜合醫院（新竹）**：心臟科、PCI、原發 HTN 追蹤
- 5/19 心臟科門診是 NTUH 還是東元？需確認（建議下次門診直接問醫師：哪一邊是主管心臟科？）

→ **建議建立統一 medication reconciliation list**，跨兩家醫院核對，避免類似 Ezetrol 這種藥物不知為何被停掉的事情。

## 對 5/19 心臟科門診清單的後續更新

| 原 Q | 更新後（基於住院記錄）|
|------|------|
| Q1 RCA CTO 開通 | **已拖 3 年**——2023/03 心導管就已知 triple vessel，更該推 |
| Q4 LDL 100 | **不需要先上調 Crestor**，**先加回 Ezetrol** 就可能達標 |
| 額外議題：兩院系統 | 確認哪邊主管 cardiac care，避免處方衝突 |

## 相關頁面

- [analysis_refractory_idh_treatment_plan](analysis_refractory_idh_treatment_plan.md)
- [analysis_cad_contribution_to_refractory_idh](analysis_cad_contribution_to_refractory_idh.md)
- [analysis_iatrogenic_factors_in_refractory_idh](analysis_iatrogenic_factors_in_refractory_idh.md)
- [analysis_prognosis_without_transplant](analysis_prognosis_without_transplant.md)
