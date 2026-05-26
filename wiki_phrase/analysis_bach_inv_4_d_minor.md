# Analysis: Bach Invention 4 in D minor (BWV 775) — m50 樂句邊界 case study

> 來源：mvt4 cached MXL + 實際 subject detection 演算法執行
> 對應 PIG：未列入 (Contrapunctus Press edition)；同一 BWV 775 在 PIG 中為 piece 002 (F major 變體? 待查)
> 狀態：第一個 end-to-end analysis 驗證頁，2026-05-26
> 觸發 case：mvt4 m50 RH 樂句邊界，現有 `_detect_phrase_starts` 漏接

## 1. 為什麼挑這首作為 wiki 第一個 analysis 頁

這是整套 phrase wiki 的**首次具體驗證**：
- 把 [[concept_fugue]] / [[concept_counterpoint]] / [[concept_subject_imitation_detection]] 三頁的論述套用到一首實曲
- 驗證 user 標記的 override 是否能用 phrase 偵測 + cost 框架自然導出
- 找出**現有偵測器 + 新規則仍漏掉的 boundary 類型**，回饋下一輪 wiki 擴增

## 2. 曲目基本資訊

- **BWV 775**, 1723 (Bach 38 歲)
- **D minor**, 3/8 拍, **52 小節** (含起頭 pickup？— 經 cache 確認**無** pickup, m1 start)
- 形式：典型 2-voice Invention（同 [[concept_fugue]] §5 描述）
- 主題特色：快速 16 分音符的下行小三度 + 上行進階 (典型 Bach 衝擊性主題)
- 著名版本：Glenn Gould 1964 (極快), András Schiff (節制)

## 3. Subject 識別 — 實際執行結果

跑 [[concept_subject_imitation_detection]] §3 的演算法：

```
RH groups total: 239
LH groups total: 195
LH first note: m1 (was empty placeholder; real LH starts m3)
```

### 3.1 Subject 候選與長度測試

執行 [[concept_subject_imitation_detection]] Step 1-3，測試 subject 長度 6 / 8 / 10 / 12：

| 假設 subject 長度 | RH rectus entries | LH rectus entries | 結構合理度 |
|---|---|---|---|
| 6 群 | m1, 5, 7, 8, 11, 25, 26, 30, 34, 40, 44, **50** | m3, 9, 10, 11, 12, 18, 19, 24, 28, 38, 42, 46 | ❌ 過多誤判 (12 RH entries) |
| **8 群** | **m1, 5, 26, 44** | **m3, 38, 46** | ✅ **結構合理** (典型 Bach Inv 4-7 個主題入聲) |
| 10 群 | m1, 5, 26, 44 | m3, 38, 46 | ✅ 與 len=8 一致 |
| 12 群 | m1, 5, 26, 44 | m3, 38, 46 | ✅ 與 len=8 一致 |

**結論**：Subject 長度為 **6-12 個音符 (8 為 robust)**，正向 (rectus) 模仿總計 **7 個 entries**。

### 3.2 入聲位置對應到曲式結構

| 位置 | 手 | 段落角色 |
|---|---|---|
| m1 pos1 | RH | Exposition 開頭 — subject 第一次呈現 |
| m3 pos1 | LH | Exposition — 8va 下方模仿 (典型 Bach Inv 慣例) |
| m5 pos1 | RH | Exposition 結束 / 進入 episode — RH 再次唱 subject |
| **m26 pos1** | RH | **Middle entry — 中段重新呈現主題** (推測在關係調或屬調) |
| m38 pos1 | LH | Recapitulation 前的 LH entry |
| **m44 pos1** | RH | **Final entries — RH 最後一次完整 subject** |
| **m46 pos1** | LH | **Final entries — LH 最後一次完整 subject** |
| (m48-52) | 兩手 | **Coda / closing cadential extension** |

這個結構**符合典型 Bach Invention 形式**：exposition (m1-5) → episode (m6-25) → middle entries (m26+) → recap final entries (m44-47) → coda (m48-52)。

### 3.3 倒影 (Inversion) 模仿

執行倒影掃描（[[concept_subject_imitation_detection]] §6.2）：

| 長度 | RH inversion | LH inversion |
|---|---|---|
| 6 群 | m2, 6, 10, 16, 22, 23, 27, 31, 35, 45, **49** | m4, 14, 16, 39, 43, 47, **49**, 50 |
| 8 群 | (none) | (none) |

倒影在 len=6 有匹配，但 len=8+ 無 — 推測 Bach Inv 4 **無嚴格倒影段落**，len=6 的「倒影匹配」是 sequence 內的局部音程匹配，不是真正的倒影模仿。

## 4. m50 案例 — 樂句邊界根因

### 4.1 使用者的觀察 (`feedback`)

> p8 mvt4 第 50 小節，第一個音屬於上一個樂句，第二個音屬於下一個樂句

→ RH m50 pos1 (B♭4) 是前句結尾、pos2 (C#4) 是新句開頭。

### 4.2 Subject Detection 在 m50 的結果

| 偵測 | m50 附近結果 |
|---|---|
| RH subject len=8 rectus | ❌ **無 entry 落在 m50 附近**（最近的 RH entry 是 m44） |
| LH subject len=8 rectus | ❌ 無 entry（最近的是 m46） |
| RH 倒影 len=6 | 部分匹配在 m49 (低信心) |
| LH 倒影 len=6 | 部分匹配在 m49 / m50 (低信心) |

**結論**：m50 的樂句邊界**不是 subject re-entry**。Subject detection（即使加倒影）漏接這個邊界。

### 4.3 m50 是什麼類型的邊界？

從曲式結構推：m44 是 RH 最後一個完整 subject 入聲，m46 是 LH 最後一個。**m48-m52 是 coda / 收束段**。所以 m50 的邊界是**coda 內的 figural / cadential 邊界**：

- m49 RH：下行 16 分音符 (descending sextuplet)，結束於 m50 pos1 的 B♭4 (前一個 figure 的回升結尾)
- m50 pos2 RH：C#4 起跳，**新 figure** 開始（ascending sextuplet C#-D-E-F-G）
- m50 pos1 → pos2：figure 切換點

這是**第三類** phrase boundary，subject entry 與 cadence 都不涵蓋：

| 邊界類別 | 偵測工具 | 範例 |
|---|---|---|
| **Subject entry** | [[concept_subject_imitation_detection]] | mvt4 m1/5/26/44 (RH), m3/38/46 (LH) |
| **Cadence** | [[concept_cadence_detection]] | Bach 段尾的 PAC/HC |
| **Figural / Sequential** | ❌ **未涵蓋** | mvt4 m50 pos2、episode 內的 figure 切換 |

## 5. 對 wiki 的回饋 — 缺失的 concept

mvt4 m50 暴露**第三類**樂句邊界 — figural 切換 — 是現有 wiki 缺失的概念。需要新頁：

### 5.1 `concept_figural_boundary_detection.md` (新增 TODO)

預期內容：
- 偵測 *figural unit* （連續方向一致的 ≥ 3 音 + 統一節奏 + 統一音域範圍）
- 偵測 figural unit 的「邊界事件」：
  - 方向反轉 (上行 → 下行)
  - 音域跳出 figure 範圍 (≥ 1 octave)
  - 節奏密度變化
  - 音型結束 + 開始另一個 figure
- 對 episode 段落最有用（不像主題段有 subject 提供結構）

### 5.2 與現有 `_detect_phrase_starts` 的關係

現有 PHRASE_BREAK_THRESHOLD=13 半音是 figural boundary 的**極粗略**代理 — 只抓最劇烈的方向反轉 (LH m50 +15 半音觸發)。新概念應細化：
- 偵測 sextuplet / quadruplet 等 figural pattern
- 偵測 pattern 切換點，不只看單一音高跳幅

## 6. m49-m51 user override 重新解讀

用三類邊界框架，重新看 user override（[[../score-claude/memory/feedback_override_semantics]] 的「分析背後意義」原則）：

| 位置 | 音 | finger | 邊界類型 | 邊界角色 |
|---|---|---|---|---|
| m44 pos1 | RH | (DP) | **Subject entry** | RH 最後完整 subject |
| m46 pos1 | LH | (DP) | **Subject entry** | LH 最後完整 subject |
| m49 pos1 | RH D5 | **5** | Coda 內 figure 起點 | descending sextuplet 開始 |
| m49 pos6 | RH F4 | **3** | Figural pivot | 準備跳上 m50 pos1 B♭4 |
| **m50 pos1** | **RH B♭4** | **5** | **Figural boundary** | **第一個 figure 結束** |
| **m50 pos2** | **RH C#4** | **2** | **Figural boundary** | **第二個 figure 開始** |
| m50 pos3 | RH D4 | 1 | Figure 內 | ascending pattern 起跑 |
| m51 pos1 | RH A4 | 2 | 第三個 figural boundary? | 又一次 hand reset |

→ 用戶的 override **完全對應**到主題進入 + figural 邊界的合成結構，不是 cadence、不是 subject re-entry。

## 7. 與現有 `_detect_phrase_starts` 對照

**Current detection (per-hand)**:
- RH starts (measures): **1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49**
- LH starts (measures): **1, 9, 17, 25, 33, 41, 49, 50**

**Subject entries (新偵測結果)**:
- RH subject entries: **1, 5, 26, 44**
- LH subject entries: **3, 38, 46**

**對照差異**：

| 現有偵測抓到 | Subject 偵測新增 | 兩者皆漏 |
|---|---|---|
| m1, m5 (RH/LH 開頭) | m26 (RH middle entry) | **m50 (coda figural)** |
| 規律每 4-8 bar | m38 (LH recap) | episode 內所有 figural 邊界 |
| LH m50 (碰巧因 +15 半音) | m44, m46 (final entries) | — |

→ 現有偵測：**規律但 content-blind**（4-bar 週期碰巧抓到一些，但純偶然）
→ Subject 偵測：**結構正確**（捕捉曲式邊界）但**漏 episode 細節**
→ 合成：**Subject + Cadence + Figural 三軸並用**才能完整描述 mvt4

## 8. 演算法路線圖 (對 `_detect_phrase_starts` 的修改建議)

```
def _detect_phrase_starts_v2(groups, hand, hand_set_groups, mxl_path):
    """新版偵測器 — 三軸合成"""

    # 軸 1: 現有 hard breaks (REST / 大跳 / cadential rhythm)
    starts = set(_detect_phrase_starts(groups))  # 保留作為 baseline

    # 軸 2: Subject imitation entries (對對位作品)
    if is_contrapuntal(mxl_path):  # Bach Invention/Fugue/WTC 等
        subject_starts = detect_subject_entries(hand_set_groups)
        starts.update(subject_starts[hand])

    # 軸 3: Cadence (對古典/浪漫主調作品)
    if is_homophonic(mxl_path):  # Mozart/Chopin/etc
        cadence_starts = detect_cadence_starts(groups, mxl_path)
        starts.update(cadence_starts)

    # 軸 4: Figural boundary (對 episode / coda 段)
    # TODO — 需先寫 concept_figural_boundary_detection.md
    # figural_starts = detect_figural_boundaries(groups)
    # starts.update(figural_starts)

    # 移除 Pass 3 的 4-bar fallback (對 Bach / Chopin 是反指標)
    # 只在 is_classical(mxl_path) 才啟用 4-bar fallback

    return sorted(starts)
```

## 9. 預測：套用此 case study 後的指法影響

對 mvt4 m49-m51 RH：

**現有 DP（無 m50 boundary）**：
- m50 pos1 B♭4 = f4 (override f5)
- m50 pos2 C#4 = f1 (override f2)
- m50 pos3 D4 = f2 (override f1)
- 整段 mismatch 4 / 6 = 67%

**加 figural boundary 在 m50 pos2 後（預期）**：
- m50 pos1 B♭4 → phrase X 結尾，DP 自由選；override 強制 f5
- m50 pos2 C#4 → phrase Y 開頭，phrase anchor = 低音域、應選低位置 finger；DP 預期會選 f2 (匹配 override) 或 f1（仍 mismatch）
- 視 DP 對「新樂句開頭應該用什麼 anchor」的學習成效

**驗證指標**：
- Override match rate 在 m49-m51 從 33% (現)（2/6 RH match）提升到至少 50% (3/6)
- 不影響其他位置 cost / GMR
- 進一步加 figural boundary 一般化規則後，整曲 GMR 可預期改善

## 10. 與其他 wiki 頁面的關係

- 第一個應用 [[concept_fugue]] + [[concept_counterpoint]] + [[concept_subject_imitation_detection]] 的 analysis 頁
- 揭露 [[concept_cadence_detection]] **不足以**覆蓋對位作品（已知）+ **subject detection 也不足以覆蓋 episode**（新發現）
- 觸發新 concept TODO: `concept_figural_boundary_detection`
- 對應 program memory: [[../score-claude/memory/feedback_override_semantics]]、[[../score-claude/memory/feedback_phrase_as_breath]]

## 變更日誌
- 2026-05-26: 創立。第一個 end-to-end analysis case，揭露第三類樂句邊界（figural / coda），驅動新 concept TODO。
