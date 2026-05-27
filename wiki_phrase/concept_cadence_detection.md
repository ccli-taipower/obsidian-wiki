# Concept: Cadence Detection — PAC / IAC / HC / DC 偵測演算法

> 來源：通用音樂理論 + music21 API、Aldwell & Schachter《Harmony and Voice Leading》、Caplin《Classical Form》cadence chapter
> 引用方：[[concept_classical_period_sentence]]、[[concept_chopin_lyrical_phrase]]、[[composer_beethoven_phrasing]]、[[composer_schubert_long_phrase]]、[[composer_grieg_lyric_pieces]]
> 狀態：工具頁，第一版 2026-05-26

## 1. 為什麼 cadence 偵測是樂句分析的工具頁

四種 cadence 是古典 / 浪漫派**樂句邊界最強的訊號**。所有 era / composer 概念頁都引用此頁，所以這頁定義一次、全部適用：

| Cadence | 對樂句邊界的意義 |
|---|---|
| **PAC** Perfect Authentic | **強樂句結束**（period / sentence 的主要終點） |
| **IAC** Imperfect Authentic | 中等樂句結束（antecedent 常用） |
| **HC** Half Cadence | **樂句中點**（period antecedent 結尾） |
| **DC** Deceptive Cadence | **不**是樂句邊界 — 預期 PAC 被替代，真正邊界在後面 |

## 2. 四種 cadence 的判定條件

### 2.1 PAC (Perfect Authentic Cadence)
```
和聲：V (或 V7) → I (或 i)
條件：
  - V 和 I 都在 root position (bass = root)
  - I 和弦上方聲部 (soprano) 落在 tonic 音 (do)
  - 落點在 strong beat (downbeat 或次強拍)
強度：⭐⭐⭐
```

### 2.2 IAC (Imperfect Authentic Cadence)
```
和聲：V (或 V7) → I (或 i)
條件：以下任一造成「不完美」：
  - V 或 I 不在 root position (inverted)
  - I 上方聲部不落在 tonic (落在 mi 或 sol)
  - 或落點在弱拍
強度：⭐⭐
```

### 2.3 HC (Half Cadence)
```
和聲：任何和弦 → V (停在 V 不解決)
條件：
  - 結束於 V（常是 V，也可 V7）
  - V 持續 ≥ 1 拍 (給聽者「停頓」感)
  - 或後面接 rest / breath mark
強度：⭐⭐
```

### 2.4 DC (Deceptive Cadence)
```
和聲：V → vi (大調) 或 V → VI (小調)
條件：
  - V 後預期接 I 卻接 vi/VI（替代 tonic）
  - 常見於 sentence continuation 末段，延後真正的 PAC
重要：DC 後面 1-4 bar 內常有 cadential extension + 真正 PAC
強度：對樂句邊界 = ⭐ (DC 本身不是邊界，後面的 PAC 才是)
```

## 3. music21 實作

### 3.1 基本和聲分析
```python
import music21
score = music21.converter.parse(mxl_path)
key = score.analyze('key')  # 推測調性

# 把整首切成 beat 級的 chord 流
chordified = score.chordify()
chords = list(chordified.flat.getElementsByClass('Chord'))

for ch in chords:
    rn = music21.roman.romanNumeralFromChord(ch, key)
    # rn.romanNumeral : "V", "I", "vi" 等
    # rn.inversion()  : 0=根位, 1=第一轉位, ...
    # rn.figure       : 完整 figure (e.g. "V7", "I6")
```

### 3.2 PAC 偵測（核心）
```python
def detect_pac(chords, key, idx):
    """idx 處是否為 PAC (chords[idx-1] 是 V, chords[idx] 是 I)"""
    if idx < 1:
        return False
    prev_rn = music21.roman.romanNumeralFromChord(chords[idx-1], key)
    curr_rn = music21.roman.romanNumeralFromChord(chords[idx], key)

    # V → I (含 V7→I, V→i)
    is_v_to_i = (
        prev_rn.romanNumeral in ("V", "V7", "V9") and
        curr_rn.romanNumeral in ("I", "i")
    )
    if not is_v_to_i:
        return False

    # 兩和弦都根位
    if prev_rn.inversion() != 0 or curr_rn.inversion() != 0:
        return False  # 退化為 IAC

    # I 上方聲部 = tonic
    soprano = max(p.midi for p in chords[idx].pitches)
    tonic_pcs = {key.tonic.pitchClass}
    if soprano % 12 not in tonic_pcs:
        return False  # 退化為 IAC

    # 強拍
    offset_in_bar = chords[idx].offset % chords[idx].beatDurationCount
    if offset_in_bar > 1.0:  # 非次強拍以上
        return False

    return True
```

### 3.3 HC 偵測
```python
def detect_hc(chords, key, idx):
    """idx 處 V 持續且後面有停頓 → HC"""
    rn = music21.roman.romanNumeralFromChord(chords[idx], key)
    if rn.romanNumeral not in ("V", "V7"):
        return False

    # V 持續或後面有 rest
    if chords[idx].quarterLength >= 1.0:
        return True
    if idx + 1 < len(chords):
        gap = chords[idx+1].offset - (chords[idx].offset + chords[idx].quarterLength)
        if gap >= 0.5:  # 後面 ≥ 半拍休止
            return True
    return False
```

### 3.4 DC 偵測（反訊號）
```python
def detect_dc(chords, key, idx):
    """idx 處是否為 DC (V → vi)"""
    if idx < 1:
        return False
    prev_rn = music21.roman.romanNumeralFromChord(chords[idx-1], key)
    curr_rn = music21.roman.romanNumeralFromChord(chords[idx], key)
    return (
        prev_rn.romanNumeral in ("V", "V7") and
        curr_rn.romanNumeral in ("vi", "VI")
    )
```

## 4. 整合到 `_detect_phrase_starts`

```
def _detect_phrase_starts_with_cadence(groups, mxl_path):
    """擴增現有偵測器，加 cadence 訊號"""

    # 1. 跑現有 hard breaks / 週期偵測
    starts = set(_detect_phrase_starts(groups))

    # 2. 跑 music21 chord 分析（cache 結果）
    score = music21.converter.parse(mxl_path)
    key = score.analyze('key')
    chordified = score.chordify().flat.getElementsByClass('Chord')

    # 3. 對每個 group 找對應的 chord (時間對齊)
    for gi, g in enumerate(groups):
        chord_at = find_chord_at_offset(chordified, g[0]['measure'], g[0]['offset'])
        if chord_at is None:
            continue
        idx_in_chords = chord_at.idx

        # 4. 偵測 cadence
        if detect_pac(chordified, key, idx_in_chords):
            starts.add(gi + 1)  # PAC 後一個 group 是新樂句起點
        elif detect_hc(chordified, key, idx_in_chords):
            # HC 後一個 group 是樂句中點 (secondary boundary)
            starts.add(gi + 1)
        elif detect_dc(chordified, key, idx_in_chords):
            # DC = 反訊號 — 確保接下來 4 bar 內**不**加邊界
            # 等真正 PAC 再切
            pass

    return sorted(starts)
```

## 5. 預期失靈情況

| 場景 | 失靈原因 | 補救 |
|---|---|---|
| 對位音樂 (fugue) | 多聲部，chordify 把多旋律混成和弦，cadence 不準 | 用 [[concept_subject_imitation_detection]] 取代 |
| 浪漫派 (Chopin) | 擴張和聲 (V9/13/altered)，music21 RomanNumeral 不準 | 弱化權重；以 [[concept_chopin_lyrical_phrase]] 的 texture 訊號為主 |
| 印象派 (Debussy) | 非功能和聲，cadence 概念不適用 | **禁用** cadence 偵測；用 [[concept_impressionist_phrasing]] texture 偵測 |
| 二十世紀 / 無調 | 同上 | 同上 |
| 音樂節奏複雜 | chord 對齊 offset 計算困難 | 給 ±0.25 拍容差 |
| Modulation | key 推測錯誤 → 整段 cadence 誤判 | 用 windowed key analysis (每 8 bar 重算 key) |

## 6. 信心度評分

不同訊號信心不同，DP 整合時可加 weight：

```python
cadence_weight = {
    "PAC":   1.0,
    "HC":    0.5,
    "IAC":   0.4,
    "DC":    0.0,  # DC 不是邊界
    "weak":  0.2,  # cadence-like 但條件不齊
}
```

整合到 DP：`W_PHRASE_ANCHOR` 在 PAC 後比在週期 fallback 後**更強**（手位 reset 信心更高）。可以做 `W_PHRASE_ANCHOR × cadence_weight` 的動態加權。

## 7. Phase 2 (2026-05-27): music21 roman on measure-final chord

Phase 1's per-tick `chordify` + `romanNumeralFromChord` produced 0 PACs on every tonal piece due to bass fragmentation. Phase 2 takes a different approach:

### 7.1 Algorithm
1. **`_aggregate_measure_chords(score)`**: collapse chordify into one chord per measure, exposing the last chord event (the resolution) as `final_chord` (music21 Chord object)
2. **`_classify_cadence_pair(prev_chord, curr_chord, key, soprano_midi)`**: call `music21.roman.romanNumeralFromChord(chord, key)` on each measure-final chord (NOT per-tick). Returns:
   - `"PAC"` if V/V7 root → I root + soprano on tonic
   - `"IAC"` if V→I but missing root-pos OR soprano-on-tonic (e.g. V in inversion, soprano on 3rd)
   - `None` for V→vi (DC), I in 2nd inversion (cadential 6/4), or no V→I
3. Cadence types accepted: V/V7/V9 + lowercase v/v7/v9 (music21's marker for incomplete dominant)
4. I/i case-insensitive
5. Boundary at first group of the measure AFTER the I-chord

### 7.2 Scope (PAC + IAC only)
- **PAC** + **IAC** are detected and both trigger boundaries
- **HC** explicitly NOT detected — over-fires on piano accompaniment textures where many bars end on isolated dominant notes (K545 m1, m2, m4 all classify as `v`); would introduce false boundaries
- **DC** correctly returns `None` from `_classify_cadence_pair` (V→vi is non-resolution)

### 7.3 Pass 3 interaction
- Default `CADENCE_DISABLES_FALLBACK = False` (window mode): remove Pass 3 fallback boundaries within ±1 bar of detected cadence; preserve distant fallbacks
- Originally `=True` (full disable), changed after K283 -1.69pp regression with full disable: classical pieces with multiple sub-phrases benefit from Pass 3's regular structure; just one detected cadence shouldn't void all 4-bar fallbacks

### 7.4 K283 + K545 validation results (T9 + T10)
- K283 (primary): Run B (cadence ON) RH 53.27% → 54.28% (Δ+1.01pp); IAC detected at m10
- K545 (secondary): Run B RH 70.02% → 70.02% (Δ+0.00pp); IAC detected at m8 — boundary structure DID change (Pass 3 m5 boundary suppressed by window mode at m9) but DP fingering result is bit-identical to BASE (K545 m5 problem is texture-driven; the boundary fix is necessary but not sufficient for fingering improvement)
- 26 other PIG val pieces byte-identical to baseline (per-piece flag isolation verified)
- Aggregate Run B RH +0.07pp

### 7.5 Known limits still present
- **K545 m5 problem unsolved by cadence alone**: removing m5 boundary doesn't change DP fingering — K545 m5-m8 scale's "right" fingering (1-2-3-1-2 thumb-under per PIG 6/6) requires DP cost rules beyond phrase boundary management
- **Mid-piece modulation**: single `score.analyze('key')` for whole piece → cadences in new key may be missed (deferred to windowed key analysis)
- **Counterpoint (Bach Inv)**: chordify still vertically squashes multi-voice; use `concept_subject_imitation_detection` instead, leave `USE_CADENCE_DETECTION` OFF per piece
- **HC / DC** not Phase 2 (deferred)
- **Beat-strength filter** not Phase 2 (PAC accepted regardless of which beat the I-chord lands on)

## 8. 與其他 wiki 頁面的關係

- 工具頁，被 [[concept_classical_period_sentence]] 等多頁引用
- 對位作品改用 [[concept_subject_imitation_detection]] 而非 cadence
- 印象派 [[concept_impressionist_phrasing]] 明確說「禁用此頁演算法」

