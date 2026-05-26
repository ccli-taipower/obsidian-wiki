# Concept: Figural Boundary Detection — episode / coda 內 figure 切換偵測

> 來源：通用音樂分析 + Schoenberg《Fundamentals of Musical Composition》motif/figure 章節、Bach 演奏實踐
> 引用方：[[concept_fugue]] (episode 段)、[[composer_beethoven_phrasing]] (中段)、[[concept_chopin_lyrical_phrase]] (figural etudes)、[[analysis_bach_inv_4_d_minor]]
> 狀態：工具頁，第一版 2026-05-26
> 觸發 case：[[analysis_bach_inv_4_d_minor]] §4 m50 邊界揭露 subject + cadence 不足

## 1. 為什麼需要第三類樂句邊界

對位作品的 episode 段、coda 段、ensemble 風的浪漫 etude — 樂句邊界既不是 subject re-entry 也不是 cadence，是 **figure 之間的切換**。

「Figure」這詞在音樂分析有兩個層次：
- **Motif (動機)**：有 melodic identity 的小單位（subject head, 主題碎片）
- **Figure (音型)**：純粹的織度 / 形狀單位（descending sextuplet、broken chord arpeggio、scale run），無獨立 melodic 意義

本頁專注**第二類**（音型 figure）的邊界偵測 — 第一類由 [[concept_subject_imitation_detection]] 處理。

## 2. Figure 的操作型定義

連續一組音符滿足以下**全部**條件即為一個 figure：

| 條件 | 操作型 |
|---|---|
| **方向一致** | 連續 ≥ 3 音 interval 同號（全 + 或全 −） |
| **節奏一致** | 連續音符 duration 相同（容許 1 個例外） |
| **音域範圍小** | 整個 figure 內 (max_midi − min_midi) ≤ 1 octave (12 半音) |
| **無內部休止** | 連續音符 offset 差 = duration（無 rest 插入） |

例：mvt4 m49 RH = D5-C5-B♭4-A4-G4-F4 (全下行小二度，全 16th-note，跨 9 半音) → 是一個 figure。

## 3. Figural boundary 的定義

兩個 figure 之間的接合點 = figural boundary。具體事件類型：

### 3.1 Direction reversal (方向反轉)
最常見：下行 figure 接上行 figure，或反之。
- 反轉前的最後一音 = 前 figure 結束
- 反轉後的第一個與下個音方向相反的音 = 新 figure 起點

例：mvt4 m49-m50 RH:
- m49: D5-C5-B♭4-A4-G4-F4 (下行 6 音 figure)
- m50 pos1: B♭4 (從 F4 上跳 4 度，**反轉但只 1 音** → 不算新 figure，是「neighbor closure」)
- m50 pos2 起: C#4-D4-E4-F4-G4 (上行 5 音 figure)

→ 邊界在 **m50 pos1 與 pos2 之間**（B♭4 屬於前 figure 的 closure，C#4 起是新 figure）

### 3.2 Pattern change (音型變化)
- 16th-note sextuplet → 8th-note pattern
- Scale run → arpeggio
- Single line → 雙重停留 (double-stop)

### 3.3 Register reset (音域重置)
新 figure 起點在 ≥ 1 octave 之外的位置，且方向與前 figure 一致 — 仍視為新 figure（因為手位必須移動）。

例：上行 figure 結束在 G5 → 下個音是 C4 (低 1 octave+) → 即使下個 figure 也上行，邊界仍存在（手移動）。

### 3.4 Closure + Restart pattern
前 figure 以 neighbor / appoggiatura / 簡短 closing 結束（1-2 音），新 figure 從不同起點開始。mvt4 m50 是典型例子。

## 4. 偵測演算法

```python
def detect_figural_boundaries(groups, hand,
                              min_figure_len=3,
                              max_figure_octave=12,
                              closure_tol=2):
    """
    groups: list of groups (each is list of notes)
    return: list of group_idx where new figure starts
    """
    n = len(groups)
    boundaries = set()

    # Step 1: Build directional segments
    # 對每對相鄰 group，標 direction = sign(midi_curr − midi_prev)
    directions = []
    for i in range(1, n):
        diff = groups[i][0]['midi'] - groups[i-1][0]['midi']
        directions.append(1 if diff > 0 else (-1 if diff < 0 else 0))

    # Step 2: Find maximal runs of same direction
    runs = []  # list of (start_idx, end_idx, direction)
    cur_start = 0
    cur_dir = directions[0] if directions else 0
    for i in range(1, len(directions)):
        if directions[i] != cur_dir:
            runs.append((cur_start, i, cur_dir))
            cur_start = i
            cur_dir = directions[i]
    runs.append((cur_start, len(directions), cur_dir))

    # Step 3: Each run becomes a figure if it meets all conditions
    figures = []
    for (start, end, direction) in runs:
        if end - start < min_figure_len - 1:  # 太短，跳過
            continue
        # 對應 group indices
        gstart, gend = start, end + 1
        figure_midis = [groups[k][0]['midi'] for k in range(gstart, gend)]
        if max(figure_midis) - min(figure_midis) > max_figure_octave:
            continue  # 跨度太大，不算 figure
        # 節奏一致性
        durs = [max(n.get('duration', 1.0) for n in groups[k]) for k in range(gstart, gend)]
        if len(set(durs)) > 2:  # 超過 1 種 duration，跳過
            continue
        figures.append((gstart, gend, direction))

    # Step 4: Boundaries between consecutive figures
    for k in range(len(figures) - 1):
        prev_end = figures[k][1]
        next_start = figures[k+1][0]
        gap = next_start - prev_end

        if gap == 0:
            # 緊接：邊界在 next_start
            boundaries.add(next_start)
        elif gap <= closure_tol:
            # 短 closure (1-2 音間距)：邊界在 next_start (closure 屬前 figure)
            boundaries.add(next_start)
        else:
            # 大間距：可能有獨立過渡段，邊界在 next_start
            boundaries.add(next_start)

    # Step 5: Register reset 額外掃描（即使 direction 相同）
    for i in range(1, n):
        if abs(groups[i][0]['midi'] - groups[i-1][0]['midi']) >= 12:
            # 跨 octave 跳躍 → 邊界候選
            boundaries.add(i)

    return sorted(boundaries)
```

## 5. Closure 音的歸屬問題

對 mvt4 m50：
- m49 figure 結束於 m49 pos6 F4 (idx 在 RH groups 中的某 i)
- m50 pos1 B♭4 是「closure 音」（neighbor 上跳）
- m50 pos2 C#4 起是新 figure

**問題**：B♭4 屬於前 figure 還是後 figure？

**答案（依 user override 與生物力學）**：
- B♭4 屬於**前 figure** (closure)
- 邊界 idx = m50 pos2 的 group index (不是 m50 pos1)

**實作上**：上面演算法的 `closure_tol` 控制這個 — 如果 prev_end 到 next_start 中間 ≤ 2 音，那些中間音歸**前 figure**。

```python
# 細化 step 4:
if gap <= closure_tol:
    # closure 音歸前 figure，邊界在 closure 音之後
    boundaries.add(prev_end + gap)
```

## 6. 與 subject detection / cadence detection 的整合

三類偵測器互補，**不互斥**：

```
boundaries = (
    subject_imitation_boundaries(groups)  # 對對位作品
    | cadence_boundaries(groups, mxl)     # 對主調作品
    | figural_boundaries(groups)          # 對 episode / coda / etude
    | _detect_phrase_starts(groups)       # 現有 hard breaks fallback
)
```

**衝突處理**：
- Subject entry 邊界優先（最強訊號）
- Cadence (PAC) 與 figural boundary 若衝突（不同 group），保留 cadence
- Figural boundary 若落在 subject entry 後 ≤ 2 group 內，去重

## 7. 預期失靈情況

| 場景 | 失靈原因 | 補救 |
|---|---|---|
| 長 melodic line (Chopin Nocturne) | 整段都是「figure」但無內部邊界 | 設 max_figure_length 限制，超過則允許內部邊界 |
| Arpeggio 連續變奏 | direction 反轉頻繁但都是同一個 figure 的內部變化 | 用 pattern detection 排除（同 arpeggio pattern 不算邊界）|
| Trills / ornament | 微小方向反轉誤判 | 過濾 duration < 8th-note 的快速反轉 |
| 二十世紀 atonal | 無清晰 figural 結構 | 不啟用此偵測，回到 hard break |

## 8. PIG 驗證樣本

### Bach Invention 4 (mvt4 m50) [target case]
- 主要驗證點：m50 pos2 應被偵測為新樂句邊界
- 期望結果：figural detector 抓到 m50 pos1→pos2 的方向反轉 (下行 → 上行 + closure pattern)

### Chopin Etude Op.10 No.1 (C major, "Waterfall")
- 整曲 RH 是廣音域 arpeggio 不斷變化
- 每個 arpeggio = 一個 figure，pattern 切換 = 邊界
- 期望：figural detector 在 chord-change 位置抓邊界

### Mozart K283 1st mov (Sonata)
- 主題段：melodic line，少 figure
- Bridge / 副題：常見 scale run + arpeggio = figure
- 期望：主題段邊界由 cadence detection 抓、bridge 段由 figural detection 補

## 9. 實作風險與漸進路線

**Phase 1**（最小）：
- 只實作 direction reversal 偵測
- min_figure_len=3, closure_tol=2
- 對 mvt4 m50 case 驗證

**Phase 2**：
- 加 pattern (rhythm) change 偵測
- 加 register reset 偵測

**Phase 3**：
- Trill / ornament 過濾
- Long-line 內部分割（Chopin Nocturne 等）

## 10. 與其他 wiki 頁面的關係

- 與 [[concept_subject_imitation_detection]] 互補：subject 處理對位 motif，本頁處理無 motif 的純 figure
- 與 [[concept_cadence_detection]] 互補：cadence 處理和聲收束，本頁處理 melodic 形狀切換
- 觸發頁：[[analysis_bach_inv_4_d_minor]] §4 揭露此 concept 缺失

## 變更日誌
- 2026-05-26: 創立。第三類樂句邊界工具頁。Phase 1 (direction reversal) 為下一步實作目標。
