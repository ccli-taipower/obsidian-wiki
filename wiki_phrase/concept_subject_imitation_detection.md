# Concept: Subject Imitation Detection — Fugue / Invention 主題重入聲偵測

> 來源：通用對位理論 + [[concept_fugue]] §7 草案延伸；[[../wiki_piano/src_voice_separation]] 提供 voice 分離前置
> 引用方：[[concept_fugue]]、[[concept_counterpoint]]、[[analysis_bach_inv_4_d_minor]]
> 狀態：工具頁，第一版 2026-05-26

## 1. 為什麼這個工具對對位作品的樂句偵測是關鍵

對位作品（Bach Inventions / Sinfonias / WTC / Art of Fugue）的樂句邊界**幾乎全部**對應於「主題在某聲部再次出現」的時刻。沒有這個偵測，現有的 hard-break / 週期偵測對 Bach 系統性出錯（見 [[analysis_bach_inv_4_d_minor]]）。

這頁定義：給一首對位作品，如何 (1) 識別主題 (subject)、(2) 在後續曲段找出所有主題重入聲位置、(3) 把這些位置變成樂句邊界。

## 2. 演算法 overview

```
Input:  per-hand groups (notes with measure/offset/midi/duration)
Output: list of (hand, group_idx) 為樂句起點

Step 1: subject identification (從曲首)
Step 2: signature extraction (轉位不變表示)
Step 3: scan-and-match (對曲子後續位置做 substring match)
Step 4: 各種模仿形式 (inversion, retrograde, augmentation) 變體匹配
Step 5: 過濾與輸出
```

## 3. Step 1: Subject Identification

對 fugue / Invention，subject 一定在**曲首**呈現。識別策略：

### 3.1 Bach Invention (2-voice) 慣例
- RH 從 bar 1 / 1.5 開始唱 subject（無 pickup 或 pickup 1 拍）
- LH 在 bar 2-3 開始唱 subject 的 imitation（通常 8va 下方或 5 度下方）
- Subject 長度典型 1-2 bar (6-16 個音符)

**偵測規則**：
```
subject_candidate = RH 的第 1 個音到第 1 個 cadence-like 結束點，
                    或第 1 個 LH 入聲前的所有 RH 音
```

### 3.2 Fugue 慣例
- Subject 在 voice 1 (任何聲部) 從 bar 1 開始
- 通常持續到 1 個 cadence / breath（多為 2-4 bar）
- 後續 voice 2/3/4 在 V (dominant) 或 I (tonic) 加入

**偵測規則**：
```
subject_candidate = voice 1 從開頭到第 1 個明顯收束點 (cadence / 長音 / 休止)
```

### 3.3 邊界情況
- 若 RH 從 pickup 開始：subject 包含 pickup 嗎？依 Bach 慣例**包含**
- Countersubject 與 subject 區分：subject 是**第一次出現**的 motif，countersubject 是 subject 唱完後的對位旋律
- 主題長度判斷：若 1-2 bar 內找不到明確收束 → 嘗試 3-4 bar；最多到 8 bar

## 4. Step 2: Signature Extraction (轉位不變)

為了讓「主題在不同調出現」也能 match，把 subject 表示為**音程序列**而非絕對音高：

```python
def extract_signature(notes):
    """notes: list of dict with 'midi' key
    return: tuple of interval semitones (length n-1)
    """
    return tuple(notes[i+1]['midi'] - notes[i]['midi'] for i in range(len(notes) - 1))

# Example: subject = D5-C5-Bb4-A4
# midis = [74, 72, 70, 69]
# signature = (-2, -2, -1)   # 二度下、二度下、半音下
```

這個 signature 對轉位不變 — 同樣的 figure 在 G major 出現會有完全相同的 signature。

## 5. Step 3: Scan-and-Match

對每隻手的後續 group 序列，掃描每個位置是否與 subject signature 匹配：

```python
def find_subject_entries(subject_sig, hand_groups, tolerance=0.8):
    """
    subject_sig: tuple of intervals (length n-1)
    hand_groups: list of groups (each group is a list of notes)
    tolerance: 多少比例的 interval 一致即視為匹配（容許單音變奏）
    return: list of group_idx where subject starts
    """
    entries = []
    n = len(subject_sig) + 1  # subject 音符數
    note_seq = [g[0]['midi'] for g in hand_groups]  # 取每 group 第一個音

    for i in range(len(note_seq) - n + 1):
        window = note_seq[i:i+n]
        window_sig = tuple(window[j+1] - window[j] for j in range(n - 1))
        match_count = sum(1 for a, b in zip(subject_sig, window_sig) if a == b)
        if match_count / len(subject_sig) >= tolerance:
            entries.append(i)
    return entries
```

**Tolerance 設定**：
- 0.8 (預設)：容許 1-2 個音變奏（5-6 音 subject 可有 1 個 interval 不一致）
- 1.0 (嚴格)：要求所有 interval 一致
- 0.6 (寬鬆)：容許更多變奏（適用 sequence 內部的部分匹配）

## 6. Step 4: 變體匹配

Bach / Counterpoint 使用四種模仿形式，需各別處理：

### 6.1 正向 (Rectus)
```python
subject_sig  # 直接用
```

### 6.2 倒影 (Inversion)
```python
inverted_sig = tuple(-x for x in subject_sig)
# 每個 interval 反向（上行→下行，下行→上行）
```

### 6.3 逆行 (Retrograde)
```python
retrograde_sig = tuple(-x for x in reversed(subject_sig))
# 從後往前讀，並反向 interval (因為方向也要反)
```

### 6.4 逆行倒影 (Retrograde Inversion)
```python
ri_sig = tuple(x for x in reversed(subject_sig))
# 從後往前讀，但 interval 不反向（雙重否定）
```

### 6.5 時值變化 (Augmentation / Diminution)
- Augmentation：所有時值 ×2 (或 ×4)
- Diminution：所有時值 ×0.5
- 對 signature **沒影響**（signature 是 interval 序列，不含時值）
- 影響的是「subject 在 group 序列中占多少 group」 — 變大或變小

**操作型**：先以原始 signature 匹配；額外掃時值 ×2 / ×0.5 的版本作補充候選

## 7. Step 5: 過濾與輸出

掃描可能產出大量候選 entries，過濾以避免 over-segmentation：

### 7.1 最小間距過濾
連續兩個 entry 太近（< subject 長度的 50%）→ 視為偽匹配，保留信心高者

### 7.2 跨手對位
若某 entry 在 RH 對應位置 LH 也有 entry → 雙重 entry，**兩隻手同時**標 phrase boundary

### 7.3 信心評分
```python
def entry_confidence(window_sig, subject_sig):
    exact_match = sum(1 for a, b in zip(subject_sig, window_sig) if a == b) / len(subject_sig)
    sign_match = sum(1 for a, b in zip(subject_sig, window_sig) if (a > 0) == (b > 0)) / len(subject_sig)
    return 0.7 * exact_match + 0.3 * sign_match
```

過濾條件：confidence < 0.6 丟棄

## 8. 與 `_detect_phrase_starts` 的整合

```python
def _detect_phrase_starts_with_subject(groups, hand, all_hand_groups):
    """擴增現有偵測器，加 fugue subject 訊號"""

    # 1. 跑現有 hard breaks / 週期偵測
    starts = set(_detect_phrase_starts(groups))

    # 2. 從 RH 開頭抓 subject candidate
    if hand == "right" or starts_only_in_rh:
        rh_groups = all_hand_groups["right"]
        subject_groups = extract_subject(rh_groups)
        subject_sig = extract_signature(
            [g[0] for g in subject_groups]
        )

        # 3. 在當前 hand 掃 subject entries (含變體)
        for variant_sig in [subject_sig, invert(subject_sig)]:
            entries = find_subject_entries(variant_sig, groups, tolerance=0.8)
            for e in entries:
                starts.add(e)  # entry 起點 = 新樂句起點

    return sorted(starts)
```

## 9. Voice Separation 前置

對位作品中，**每隻手可能不只一條聲部**（Bach Sinfonias 3 聲部，常 RH 含 2 條）。

- Bach Inventions (2-voice)：RH = voice 1, LH = voice 2，**不需** voice separation
- Bach Sinfonias / WTC Fugues：需要先把每隻手分成聲部，對每條聲部跑 subject detection
- 工具：[[../wiki_piano/src_voice_separation]] 列舉 Karystinaios GNN (F1=0.97) 等方法

Phase 1 實作只處理 2-voice 情況；Sinfonias / Fugues 為 Phase 2。

## 10. 預期失靈情況

| 場景 | 失靈原因 | 補救 |
|---|---|---|
| Stretto 段（subject 重疊） | 多個 entry 在近距離出現 | 不過濾「近距 entry」，全部保留 |
| 主題在 sequence 內變奏 | signature 不嚴格匹配 | 降低 tolerance 到 0.6 |
| 主題碎片 (countersubject 用 subject head) | 部分匹配誤判為完整 entry | 要求至少 4 個 interval 連續匹配 |
| 自由 fantasia 段（無 subject） | 找不到 entry，回到 hard break / 週期 | 兼容現有 fallback |

## 11. 與其他 wiki 頁面的關係

- 工具頁，被 [[concept_fugue]] 與 [[concept_counterpoint]] 引用
- 與 [[concept_cadence_detection]] 互補：cadence 適用古典 / 浪漫主調作品，subject detection 適用對位作品
- 兩者**可以並存**：對位作品偶有 cadence 結尾段（如 fugue 結束部），cadence 偵測仍有用

## 12. 演算法的範疇與已知限制

Subject detection 是「曲式正確性」工具：捕捉作曲家結構性的主題重述（exposition / middle entries / recapitulation），這些位置通常與 cadence-aware 或 figural-aware 偵測**互補**。

**範疇**：
- 對 2-voice 對位作品（Bach Inventions）per-hand self-extraction 即足，TI signature 對 transposition imitation 天然對齊
- 對 3+ voice 作品（Bach Sinfonias / Fugues）需先做 voice separation（見 [[../wiki_piano/src_voice_separation]]）
- 對主調作品（Mozart / Chopin / etc）主題重述較自由，匹配率較低 — 改用 cadence + texture 偵測為主

**已知限制**：
- 自由 fantasia 段（無 subject）回退到 hard break / 週期 fallback
- Stretto 段內多個 entries 在近距離出現 — 需避免過度去重
- Subject 在 sequence 內變奏 — 降低 tolerance（0.6）可捕捉但增加 false positives
- 主題碎片（countersubject 用 subject head）— 需要求至少 4 個連續 interval 匹配避免誤判
