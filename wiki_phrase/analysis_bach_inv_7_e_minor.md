# Analysis: Bach Invention 7 in E minor (BWV 778) — Chromatic descent + leading-rest challenges

> 來源：musicology 文獻 + 教學傳統共識（Schiff, Hewitt, Czerny editions）
> 對應 PIG：未列入 / 對照需另行查核
> 狀態：第三個 Bach Invention analysis 頁；algorithmic claims **多為 musicology 預測，待跑 `_detect_subject_entries` / phrase pipeline 驗證**（⚠ 標記處）
> 觸發 case：chromatic subject 對 subject detection / modulation signal 的混淆風險；leading-rest 結構對 OMR / phrase boundary 的影響

## 1. 為什麼挑這首作為 wiki 第三個 Bach analysis 頁

BWV 778 與已有兩頁 ([[analysis_bach_inv_1_c_major]], [[analysis_bach_inv_4_d_minor]]) 構成**三角對照**：

| 維度 | Inv 1 (C major) | Inv 4 (D minor) | **Inv 7 (E minor)** |
|---|---|---|---|
| 調性語言 | 大調 diatonic | 小調 diatonic + 短暫 chromatic | **小調 + 長期 chromatic descent** |
| 主題長度 / 形態 | 1-bar 上行 figure | 6-12 群快速 figure | 1-2 小節 + **sigh motif** (半音下行) |
| 主要邊界類型 | Modulation + cadence | Figural (m50 case) | **半音線條 + leading-rest entries** |
| 對 OMR 的 stress | 低（無譜號 / 調號變動） | 中（密集 figures） | **高（leading-rest 結構觸發 fuzzy-match cascade）** |
| 演算法挑戰 | 直接 | figural boundary 漏接 | **chromatic ≠ modulation 的 disambiguation** |

→ Inv 7 是 wiki 框架對「**演算法假設與 musicology 現實的不對齊**」的最強壓力測試。

## 2. 曲目基本資訊

- **BWV 778**, 約 1723 (Bach 38 歲, Köthen)
- **E minor**, 1 # 調號, 4/4 拍, **23 小節**（無反覆，through-composed）
- 形式：典型 2-voice Invention；exposition / development / recap 三段論
- 主題特色：**chromatic descent + countersubject** — Bach 對「**小調 + 半音**」聲響的著名運用；主題明顯含 **sigh motif** (半音下行 appoggiatura) 重複出現
- 教學定位：*Two-Part Inventions* 第 7 首；是該集中**第一首充分發揮 chromatic voice-leading** 的 Invention
- 著名版本：András Schiff (*lamentoso* character emphasis), Angela Hewitt (sigh motif articulation), Glenn Gould (anti-romantic dryness 例外)
- 與 [[composer_other_pig_pieces]] 的關係：BWV 778 在現有 PIG dataset 中未列入；對照另需自建

## 3. Subject 識別 — chromatic subject 的演算法挑戰

### 3.1 Subject 範圍的教學共識

關於 BWV 778 subject 長度，教學傳統較統一（不像 Inv 1 的 1-bar / 2-bar 之爭）：

- **Subject ≈ 1-2 小節**：m1 RH 起，含 chromatic descent figure + 結尾 sigh motif
- LH 答句約在 **m3**，採標準 8va 下方模仿（與 Inv 1 / Inv 4 慣例一致）

但 Inv 7 的特殊性在於 **subject 的音程組成包含 chromatic intervals**：相鄰音之間出現 Δ=1（半音）與 Δ=2（全音）並存，且半音不只是裝飾性 passing tone，**是 subject 結構的本質特徵**。

### 3.2 對 `_detect_subject_entries` 的影響（演算法層次）

[[concept_subject_imitation_detection]] §3 的 algorithm 用 **interval signature** 作為 subject 匹配 key。對 Inv 7：

| 演算法假設 | Inv 1 / Inv 4 情況 | **Inv 7 情況** |
|---|---|---|
| Subject signature 用半音差序列 | ✅ 直接適用 | ✅ 直接適用，但... |
| Diatonic subject → entry detection robust | ✅ | ⚠ 若 signature 包含 (1, 1, 1) 連續半音，**轉位 / 移調 entry 的容差設定**需重新檢視 |
| Inversion detection 用 sign-flip | Inv 4 有 strict inversion 例證 | ⚠ **Inv 7 是否使用 strict inversion 待驗證** — Bach 在小調 + chromatic 時偏好對位變體 |
| Stretto / overlap 容差 | Inv 1 / 4 中 entries 較稀疏 | ⚠ Inv 7 的 sigh motif 重複密集，**可能誤判為多次 subject entry** |

→ **演算法待驗證項**：
- ⚠ 跑 `_detect_subject_entries` 對 BWV 778 cached MXL，記錄 entries 數與位置，校對 musicology 預期
- ⚠ 若 entries 過多（如 > 8），檢查是否被 sigh motif 內部 chromatic 子序列誤觸

### 3.3 預期 subject entries (musicology 預測)

| Entry | 手 | 段落角色 |
|---|---|---|
| m1 pos1 | RH | Exposition — subject 第一次呈現 |
| m3 附近 | LH | Exposition — **8va 下方模仿** (典型答句) |
| m7-m8 附近 | LH or RH | Modulation 起點 — 主題可能移至 G 大調 (III, 關係大調) 或 b 小調 (v) |
| m11-m14 附近 | 兩手交替 | Development middle entries — chromatic sequence 區段 |
| m17-m20 附近 | RH 主導 | Recap / final entries 前準備 |

⚠ **以上為 musicology 預測，演算法輸出待補入 `_implementation_status.md`**。

### 3.4 Inversion 可能性

Bach 在小調 + chromatic subject 時**常用 strict inversion** 作為對位手法（[[analysis_bach_inv_4_d_minor]] 已示範）。對 Inv 7：

- ⚠ **未經驗證**：Inv 7 是否同樣大量使用 inversion
- 教學版本（Schiff, Hewitt 樂譜註）對此**少有明確標示**，多以 *imitation* 通稱
- 若演算法 inversion detection 在 Inv 7 返回稀疏結果（< 2 entries），與 Inv 4 對照可推斷「**Inv 7 偏好 sequence + 移調 over inversion**」

## 4. 三段曲式對應到 form

| 段落 | 小節 | 調性 | 角色 |
|---|---|---|---|
| **Exposition** | m1–m6 | e 小調 → 過渡 | RH subject (m1) → LH 8va 模仿 (m3) → 開始發展 |
| **Modulation / development** | m7–m16 | G major (III) / b minor (v) / 各短暫 tonicization | Chromatic sequence + voice exchange + sigh motif 密集區 |
| **Return + final cadence** | m17–m23 | e minor (回主) | Final entries + cadential extension；**末和弦可能為 Picardy 3rd (E major chord)** |

→ m6–m7、m16–m17 是兩個主要 **form 段落邊界**；末小節的 Picardy 3rd（若有）構成獨立的**音色 / 音響**邊界，與和聲結構同步但表達層次不同。

## 5. Case A — Chromatic descent 對 modulation signal 的混淆

### 5.1 問題陳述

[[concept_modulation_as_phrase_signal]] 的核心 heuristic 包含：
- Key signature 變動偵測
- Tonicization (短暫離調) 偵測

**Inv 7 的 chromatic descent 是 risk**：半音下行（如 B → A# → A → G# → G）會讓 tonicization detector 看到「**多個非 diatonic accidentals 短時間出現**」，這與真實的 modulation 訊號**表面上一樣**，但意義完全不同：

| 現象 | Modulation | Chromatic voice-leading (Inv 7) |
|---|---|---|
| Accidentals 出現 | ✅ 是 | ✅ 是 |
| 持續時間 | 通常 ≥ 4 小節 | **單一線條內，1-2 小節即解決回 diatonic** |
| 和聲功能 | 建立新 tonic | **單純 voice-leading**（接 dominant 或 cadential ii-V） |
| 樂句邊界意義 | ✅ 有 | ❌ **無** — chromatic 不應觸發 phrase boundary |

### 5.2 對 tonicization filter 的設計意涵

→ [[concept_modulation_as_phrase_signal]] 的 tonicization filter **必須能區分 chromatic line vs key change**。可能 heuristics：

- **Duration filter**：accidentals 在 < N beats 內解決 → 視為 chromatic，不觸發
- **Direction filter**：連續半音同向（如全降）→ 視為 chromatic line，不觸發
- **Cadence anchor**：若該段落結束**不是**新 key 的 V→I，則拒絕 modulation 判定

⚠ **演算法待驗證**：跑 BWV 778 的 phrase detection，記錄 m1-m23 是否有**錯誤觸發**的 modulation boundaries（理論上應只有 m6-m7、m16-m17 兩處）。

### 5.3 與 [[concept_subject_imitation_detection]] 的交叉影響

Chromatic subject 同時影響 subject detection 的 **interval tolerance**：
- 若演算法用嚴格 signature matching（要求每個 interval 完全一致），entries 會抓到太少（chromatic 變體會被視為不同 subject）
- 若放寬到 ±1 半音容差，entries 會抓到太多（任何 chromatic 局部都被誤判）

→ Inv 7 是**tolerance 調整 case study 的最佳載體**；與 Inv 1（diatonic, robust）對照，可以反推合理的容差參數區間。

## 6. Case B — Leading-rest 結構與 phrase boundary

### 6.1 Leading-rest 在 Bach Invention 的角色

Bach 在 voice entry 之前**常用休止符讓另一聲部 lead in**：
- LH 沉默幾拍 → RH 結束 phrase → LH 在沉默後**新樂句起點**進入
- 這是 [[concept_counterpoint]] §模仿規則的標準呈現方式：**voice entry 與 phrase boundary 同步**

### 6.2 對 phrase boundary 的明確訊號

Leading-rest **不是 [[concept_phrase_elision]] case** — 反而是 elision 的反例：

| 模式 | 樂句關係 |
|---|---|
| **Phrase elision** | 樂句重疊 — 同一拍同時是前句結束 + 後句起點 |
| **Leading-rest entry (Inv 7)** | **無重疊** — 前句結束 → 短暫休止 → 後句獨立起點，邊界清晰 |

→ 對演算法的意涵：**Leading-rest 後的 voice entry 是 phrase boundary 的高信心訊號**。可作為 [[concept_subject_imitation_detection]] / [[concept_figural_boundary_detection]] 之外的獨立 boundary detector（如「voice silence ≥ N beats 後 re-entry → phrase start」）。

### 6.3 對 OMR / fuzzy-match 的 stress

但 leading-rest 結構同時對 **OMR alignment** 構成壓力。Audiveris 在 voice 沉默小節常產生：
- `quarterLength = 0.0` 的幽靈小節（已由 `_fill_ghost_measures` 處理）
- 整個 voice 在某小節**完全沒有 note element**，導致下一小節的 voice entry **被歸到錯誤小節 index**

當 leading-rest 跨越多個小節（Inv 7 在 development 段較常見），**fuzzy-match 的 skip budget 可能不足**，造成下游 pos 偏移 cascade。

→ 這不是 phrase detection 本身的問題，但**phrase detection 結果會被 OMR 偏移污染**。意涵：

- 解 Inv 7 的 phrase detection 前，必須先解 OMR alignment 信心
- 對 wiki 框架：leading-rest 結構是「**樂句訊號明確但 implementation 困難**」的典型 case，與 chromatic descent 構成 Inv 7 的雙重挑戰

⚠ **OMR-side 處理屬於 implementation 細節**（不屬於 phrase wiki scope），具體狀態見 `[[../score-claude/memory/project_mvt7_m21_pending]]`。本頁僅記錄**musicological 為什麼這結構難**，不記錄 implementation 修復步驟。

## 7. 三類樂句邊界並用的必要性（Inv 7 視角）

對 BWV 778，三類邊界各覆蓋不同 form 位置：

| 邊界類型 | Inv 7 預期觸發點 | 工具 | 風險 |
|---|---|---|---|
| **Subject entry** | 主題 / 答句: m1 RH + m3 LH (在演算法 template 內); 演算法掃描自 template 之後 — 實測 RH @ (len=8: none) 全 miss, LH @ m3 (1 entry) | [[concept_subject_imitation_detection]] | ⚠ RH 全 miss 推測為 chromatic subject + 0.8 tolerance 太緊; 見 [[../score-claude/memory/project_bach_inv_subject_detection_validation_2026-05-28]] |
| **Modulation** | m6-m7, m16-m17 | [[concept_modulation_as_phrase_signal]] | ⚠ Chromatic descent 的 false positive 風險 |
| **Cadence** | m22-m23 final cadence (可能 Picardy 3rd) | [[concept_cadence_detection]] | 末和弦音色變化 (e → E) 是獨立訊號 |
| **Leading-rest entry** | development 段內多處 | （新提議軸，目前 [[concept_subject_imitation_detection]] 部分覆蓋） | OMR alignment cascade |
| **Figural** | sigh motif 段內 figure 切換 | [[concept_figural_boundary_detection]] | sigh motif 高重複度可作為高信心 figural 標記 |

→ Inv 7 與另兩首對照：
  - Inv 1: modulation + cadence 主導
  - Inv 4: figural boundary 主導 (m50 case)
  - **Inv 7: subject + chromatic disambiguation 主導，leading-rest 為輔軸**

三首合看，支持 [[../score-claude/memory/feedback_phrase_analysis_is_its_own_discipline]] 的核心主張：**單一偵測軸無法完整描述 Bach Invention 樂句結構，不同曲目主導軸不同**。

## 8. 與其他 wiki 頁面的關係

- 與 [[analysis_bach_inv_1_c_major]] + [[analysis_bach_inv_4_d_minor]] 構成三角對照（diatonic-major / diatonic-minor / chromatic-minor）
- 應用 [[concept_fugue]] / [[concept_counterpoint]] 對 2-voice Invention 的論述
- 對 [[concept_subject_imitation_detection]] 提供 **chromatic subject + interval tolerance 校準** 的測試 case
- 對 [[concept_modulation_as_phrase_signal]] 提供 **chromatic descent vs modulation disambiguation** 的代表 case
- 對 [[concept_cadence_detection]] 提供 **Picardy 3rd 末和弦** case (待確認)
- 對 [[concept_figural_boundary_detection]] 提供 **sigh motif 重複** 的 high-confidence figural 標記 case
- 對 [[concept_phrase_elision]] 提供**反例** (leading-rest = 無 elision, 清晰邊界)
- 編輯版本與教學脈絡引 [[src_bach_inventions_pedagogy]]
- 對位起源溯至 [[src_fux_gradus_ad_parnassum]]
- Measure 對應依 [[../score-claude/memory/project_bach_inv_measure_mapping]]
- 個人化生物力學原則依 [[../score-claude/memory/feedback_personal_biomechanics]]
- 樂句呼吸原則依 [[../score-claude/memory/feedback_phrase_as_breath]]
- 樂句分析獨立性主張依 [[../score-claude/memory/feedback_phrase_analysis_is_its_own_discipline]]
