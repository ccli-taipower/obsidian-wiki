# Concept: Running Passage 中 Thumb Reservation — 長階串聯指法的起手策略

> 來源：通用對位 / Bach 演奏實踐 + Czerny《Theoretisch-praktische Pianoforte-Schule》Op.500、Hanon 50 練習、Tim Stein 影片 (見 [[../wiki_piano/concept_thumb_technique]])
> 引用方：[[concept_fugue]] (episode 段)、[[analysis_bach_inv_4_d_minor]] (target case)、[[../wiki_piano/concept_thumb_technique]]
> 狀態：第一版 2026-05-26
> 觸發 case：mvt4 RH m50 pos2 — user override f2，但 DP 即使有 phrase reset 仍選 f1

## 1. 為什麼這頁是 phrase wiki 與 piano wiki 的橋樑

[[analysis_bach_inv_4_d_minor]] 揭露：mvt4 m50 RH 即使加上正確的 phrase boundary，DP 仍選 f1 (thumb on C#4)，與 user override f2 不符。

根因 **不是樂句切錯**（[[concept_figural_boundary_detection]] 機制 OK），而是 DP 的 cost function **缺少「啟動長階串聯時保留 thumb」的策略**。這是個跨工具的問題：

- **樂句 wiki** (這頁起源)：phrase 起始位置的指法選擇應該為整個樂句服務
- **生物力學 wiki** ([[../wiki_piano/concept_thumb_technique]])：thumb-under (拇指穿越) 是覆蓋 > 5 半音範圍的必要技巧

## 2. 觀察：5 指 vs > 5 半音範圍

人類只有 5 指。當一段運行音 (running passage) 跨度 > 5 半音時，**必須使用 substitution / thumb-under** 才能完成。

**RH 上行運行音範例**：C4 → A4 (8 半音, 5 音)
- 純 1-2-3-4-5：到第 5 音正好到 G4，下一音 A4 需要 thumb-under
- 純 2-3-4-5-...：到第 4 音 F4 後手指用完，**強制** thumb-under
- 1-2-1-2-3-... 或 2-1-2-3-4：thumb-under 已內建，更平滑

**判定條件**：phrase 內預期跨度 > 5 半音 → **thumb-under 必要** → 起手指法需配合

## 3. mvt4 m50 case 重新檢視

m50 pos2-6 + m51 pos1：C#4-D4-E4-F4-G4-A4，6 音上行覆蓋 8 半音。

| 起手 finger | 純 5-指可達 | 是否需 thumb-under | 自然延伸 |
|---|---|---|---|
| **f1** (DP local optimum) | C#4 + 4 ascending fingers = 到 F4 | ✓ 必須在 G4 處 thumb-under | 1-2-3-4-1-2 (awkward 在 G4 補 thumb) |
| **f2** (user override) | C#4-D4-E4-F4-G4 = 5 fingers 到 G4 | ✓ A4 時 thumb-under 接 | **2-1-2-3-4-5** (thumb-under 在 D4 早期完成) |
| **f3** | C#4-D4-E4-F4 = 4 fingers 到 F4 | ✓ G4 thumb-under | 3-?-... awkward 起手 |

user 選 f2 不只是個人偏好 — 它是這個音型最自然的 thumb-under 起手選擇。

## 4. 一般化原則

### 4.1 偵測 running passage

**定義**：phrase 內滿足以下所有條件即為 running passage：
- 連續 ≥ 4 音
- 方向一致 (上行 / 下行)
- 整體跨度 > 5 半音
- Stepwise (interval magnitude ≤ 4 半音，與 [[concept_figural_boundary_detection]] 一致)

### 4.2 起手 finger 選擇原則

| 手 + 方向 | 跨度 ≤ 5 半音 | 跨度 > 5 半音 |
|---|---|---|
| RH 上行 | 任意 (f1/f2/f3) | **避免 f1 起手**，prefer f2/f3 (留 thumb 給 thumb-under) |
| RH 下行 | 任意 | **避免 f5 起手**，prefer f3/f4 (留 pinky 給接力) |
| LH 上行 | 任意 | **避免 f5 起手**，prefer f3/f4 |
| LH 下行 | 任意 | **避免 f1 起手**，prefer f2/f3 |

「**最外側 finger** (RH-up: thumb / RH-down: pinky / LH-up: pinky / LH-down: thumb) **不應**作為長階串聯的起手」— 因為起手用掉最外側 finger 後，方向相同的下幾個音無法用相同 finger group 延伸，必然在中途強制 substitution / thumb-under。

### 4.3 為什麼 DP 沒自然導出

當前 `_assignment_cost` 是 **per-chord** local — 不看 phrase 後續。
當前 `_transition_cost` 是 **per-pair** local — 看相鄰兩 chord，不看 N 步後。

長階運行音的「起手」是一個 **look-ahead 問題**：當前 finger 的代價要視「後面 4-5 音是否能順流」決定。Local DP 無法看到。

## 5. 兩條實作路線

### 5.1 路線 A — Look-ahead local cost (簡單)

在 `_assignment_cost` 計算當下 chord 時，**peek 後面 K=4 音**（如果在同 phrase 內）：
- 若 K 音同方向 stepwise 且跨度 > 5 半音 → 加 thumb-reservation 罰
- 罰公式：若當前 finger ∈ {最外側方向 finger}，加 `RUNNING_PASSAGE_OUTER_START_PENALTY` (試 0.5-1.0)

**優點**：實作簡單，不動 DP 架構
**缺點**：違反 DP 的「per-step 局部性」紀律；無法評估更複雜的長視野（如連續兩個 running passage 需協同）

### 5.2 路線 B — Phrase-aware optimization (架構性)

在 `_run_phrase_dp` 入口，先分析 phrase 整體形狀（上行 / 下行 / 山型 / 谷型 + 整體跨度），對 phrase 第一個 chord 的 anchor 預測加入「形狀導向的 finger preference」。

**優點**：對齊「樂句 = 整體 plan」的概念
**缺點**：需動 DP 初始化邏輯

## 6. 路線 A 的具體 cost 公式（草案）

```python
def _running_passage_thumb_reservation_cost(
    chord_idx, finger_choice, hand, groups, phrase_end_idx,
    look_ahead=4,
    penalty=0.5,
):
    """If this position is phrase-start AND next look_ahead notes form a
    running passage > 5 semitones in the outer direction, penalize the
    outer-most finger choice (saves it for thumb-under)."""

    # 1. 確認當前位置是 phrase-start (caller 傳入)
    # 2. 看後面 look_ahead 個 group
    look = groups[chord_idx + 1 : min(chord_idx + 1 + look_ahead, phrase_end_idx + 1)]
    if len(look) < 3:
        return 0.0

    # 3. 計算 stepwise + monotonic 條件
    intervals = [look[i+1][0]["midi"] - look[i][0]["midi"] for i in range(len(look) - 1)]
    same_dir = all(x > 0 for x in intervals) or all(x < 0 for x in intervals)
    stepwise = all(abs(x) <= 4 for x in intervals)
    if not (same_dir and stepwise):
        return 0.0

    # 4. 跨度檢查
    span_semitones = abs(look[-1][0]["midi"] - groups[chord_idx][0]["midi"])
    if span_semitones <= 5:
        return 0.0

    # 5. 判斷是 ascending 還是 descending
    ascending = intervals[0] > 0

    # 6. 找出該方向的 outer finger，加罰
    outer_finger_map = {
        ("right", True):  1,   # RH 上行 → 避免 thumb
        ("right", False): 5,   # RH 下行 → 避免 pinky
        ("left",  True):  5,   # LH 上行 → 避免 pinky
        ("left",  False): 1,   # LH 下行 → 避免 thumb
    }
    forbidden = outer_finger_map.get((hand, ascending))
    if finger_choice == forbidden:
        return penalty
    return 0.0
```

整合到 DP：在 `_run_phrase_dp` 處理每個 phrase 第一個 chord 時呼叫此函式，把回傳值加到 `entry`。

## 7. 預期影響 (mvt4 m50)

加 penalty 後：
- m50 pos2 phrase start, C#4
- 後面 4 音：D4, E4, F4, G4 (全上行 stepwise，跨度 from C#4 to G4 = 6 半音 > 5)
- → 觸發 thumb-reservation rule
- RH 上行 → 罰 f1 起手 (+0.5)
- DP 重算：f1 cost +0.5；f2 cost 不變
- 若原本 f1 與 f2 cost 差距 < 0.5 → f2 勝出 ✓

**預期 mvt4 m50 pos2 改 f2**（與 override 一致）。

## 8. 調參考量

**Penalty 大小的權衡**：
- 太大 → 短 phrase（4-5 音）也會被誤罰
- 太小 → 無法翻轉 DP 在 phrase-start 的自然偏好

**Penalty 為何可能需要顯著大於其他 cost 常數**：

`_run_phrase_dp` 對 phrase 第一個 chord 計算 cost 時，「外側 finger」(如 RH 上行的 thumb) 可能同時得到兩個自然優勢：
1. `W_PHRASE_ANCHOR × 0` ≈ 0 cost（thumb 落在 anchor target）
2. `PHRASE_SEAM_TC_SCALE × _transition_cost(prev → thumb)` 較便宜，因為大跨度 finger pair 的 comfort span 較寬

要翻轉這個累積偏好，penalty 必須 > 兩者之和。在實務上這意味著本規則的 penalty **不是 micro-tuning** 而是「結構性修正」— 修正一個 over-applied 的 anchor 原則 — 因此 magnitude 與一般 cost 常數（0.4-1.5）的 scale 不同。

**look_ahead 過大**：
- 看太遠 → phrase 內 figure 變化會被當成 monotonic（過度觸發）
- look_ahead=4 是一個 reasonable cap：只看接下來 4 音

**與 [[concept_figural_boundary_detection]] 的關係**：
- 部分重疊（都基於「stepwise monotonic > 5 半音」結構）
- Figural boundary 偵測「figure 結束」；本頁偵測「figure 開始時的起手」
- 兩者**互補不互斥** — 用在不同 cost 維度

## 9. 與其他 wiki 頁面的關係

- 對應 [[../wiki_piano/concept_thumb_technique]] §thumb-under — 提供啟動的指法選擇支援
- 對應 [[../wiki_piano/concept_finger_span_table]] — 限制 5-指範圍假設的數理基礎
- 對應 [[concept_fugue]] §episode — episode 段大量 running passage
- 對應 [[analysis_bach_inv_4_d_minor]] §5 — 直接解釋 m50 user override 的選擇
