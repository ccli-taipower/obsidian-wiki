# Concept: Modal Scale Fingering — Mode 對指法 + 樂句的影響

> 來源：通用音樂理論 + Roy Howat《Debussy in Proportion》、Persichetti《Twentieth-Century Harmony》、五聲音階傳統教學
> 引用方：[composer_debussy_phrasing](composer_debussy_phrasing.md)、[composer_grieg_lyric_pieces](composer_grieg_lyric_pieces.md)、[../wiki_piano/src_chinese_style_piano](../wiki_piano/src_chinese_style_piano.md)
> 狀態：第一版 2026-05-26
> 跨 wiki：與 `wiki_piano/` 的指法系統直接相關

## 1. 為什麼這頁同時屬於 phrase 與 piano wiki

樂句邊界與指法選擇都受 mode 影響：
- 不同 mode 的「終止式」不同（如 Dorian 終止 ≠ Major 終止）→ cadence detection 必須 mode-aware
- 不同 mode 的「自然指法」不同（5 指 group 對應的音不同）→ DP 的 finger group preference 必須 mode-aware
- 部分 mode (whole-tone) 不能用標準 thumb-pass 邏輯

## 2. 七種教會調式 (Church Modes) + 兩種特殊音階

### 2.1 Diatonic modes (基於 7-note diatonic scale)
| Mode | 起音 (C 為主音) | 特徵 interval | 風格 |
|---|---|---|---|
| Ionian (= Major) | C-D-E-F-G-A-B | major 3rd, perfect 5th | 標準大調 |
| Dorian | D-E-F-G-A-B-C | minor 3rd, **major 6th** | melancholy + bright |
| Phrygian | E-F-G-A-B-C-D | minor 3rd, **minor 2nd** | 戲劇/吉普賽 |
| Lydian | F-G-A-B-C-D-E | major 3rd, **augmented 4th** | bright/space |
| Mixolydian | G-A-B-C-D-E-F | major 3rd, **minor 7th** | bluesy/folk |
| Aeolian (= natural minor) | A-B-C-D-E-F-G | minor 3rd, minor 6th | 標準小調 |
| Locrian | B-C-D-E-F-G-A | **diminished 5th** | rare, unstable |

### 2.2 Non-diatonic
- **Pentatonic (5 音)**: C-D-E-G-A (anhemitonic, 無半音) — 中國 / 凱爾特民間
- **Whole-tone (6 音)**: C-D-E-F#-G#-A# (全音階) — Debussy 標誌
- **Octatonic (8 音)**: C-D♭-E♭-E-F#-G-A-B♭ (交替半全音) — Stravinsky / 二十世紀

## 3. 對指法的影響

### 3.1 Pentatonic (5 音 octave)
**5 個音剛好 5 指** — 一隻手可以**不換位置**彈完整 octave 的 pentatonic：

```
RH C pentatonic ascending: C(1) D(2) E(3) G(4) A(5) [C(1) next octave]
                          ─── 5 指剛好覆蓋一個 octave
                              octave 接續才需 thumb-pass
```

**樂句意涵**：pentatonic passages 通常**沒有 thumb-under 需求**（除非跨 octave），所以 [concept_running_passage_thumb_reservation](concept_running_passage_thumb_reservation.md) 規則**不適用**。

**典型場景**：Debussy Pagodes、Grieg Norwegian 民間風段落、Chinese-style 改編曲

### 3.2 Whole-tone (6 音 octave)
**6 個音 octave**，相鄰都是 2 半音（全音）。標準 thumb-pivot at fa/ti（半音位置）**完全不適用**。

**指法慣例**：
- 純全音階：1-2-3-4-5-1-2-... (連續，每 5-6 音 thumb-pass)
- 或不規則 1-2-3-1-2-3 (反覆兩組三指)

**樂句意涵**：whole-tone passages 內部沒有 metric "落點" (因為全音對稱)，phrase 通常依長度切，不依 metric pattern。

**典型場景**：Debussy Voiles, 大部分 Debussy 後期段落

### 3.3 Octatonic (8 音 octave)
**8 個音 octave**，半全交替。一隻手 5 指覆蓋 5 個 octatonic 音 = 約 6 半音範圍。常用 thumb-pass。

**指法慣例**：跟標準大小調 fingering 相近，但 finger group 重新對應。

**典型場景**：Stravinsky Petrushka, Scriabin late period, Bartok

## 4. 對 cadence detection 的影響

[concept_cadence_detection](concept_cadence_detection.md) 假設 V-I 為主要 cadence。對 modal 音樂：

| Mode | 主要 cadence | V-I 適用 |
|---|---|---|
| Ionian / Aeolian | V-I / V-i | ✓ |
| **Dorian** | **♭VII-i** 或 **IV-i** (plagal) | ✗ V is minor |
| **Mixolydian** | **♭VII-I** | ✗ V is minor |
| **Lydian** | I-IV-I (#4 features) | ✗ |
| **Phrygian** | **♭II-I** (Phrygian cadence) | ✗ V awkward |
| Pentatonic / Whole-tone | 不適用 cadence 概念 | ✗ |

→ **如果偵測到曲目是 modal**（從 key signature + scale analysis），`detect_cadence_boundaries` 應**啟用 mode-specific cadence patterns** 而非標準 V-I。

## 5. 偵測 mode 的演算法

```python
def detect_mode(score, segment_bars=8):
    """Per-section 偵測 mode."""
    import music21
    notes_in_segment = [...]  # extract notes per 8-bar window
    pcs = set(n.pitchClass for n in notes_in_segment)

    # Pentatonic check (5 distinct pcs, anhemitonic)
    if len(pcs) == 5 and not any_semitones(pcs):
        return "pentatonic"

    # Whole-tone check (6 distinct pcs, all whole tones)
    if len(pcs) == 6 and all_whole_tones(pcs):
        return "whole-tone"

    # Diatonic mode check
    if len(pcs) == 7:
        # Identify modal final + compare interval pattern to known modes
        return identify_diatonic_mode(pcs, segment_root)

    return "chromatic"  # 12+ pcs, fully chromatic
```

**信心度**：⭐⭐ — 對短段（< 8 bar）不夠準；對長段且 mode-pure 段（如 Debussy entire piece in Lydian）可靠

## 6. 整合到指法系統

```python
def assign_fingering_v6_modal_aware(matched, hand):
    """V6 DP with mode-aware adjustments."""
    mode_per_segment = detect_mode_per_section(matched)

    for segment in matched_segments:
        mode = mode_per_segment[segment.id]
        if mode == "pentatonic":
            # Disable thumb-reservation (pentatonic 不需 thumb-under)
            # Enable pentatonic finger group preference (C-D-E-G-A = 1-2-3-4-5)
            ...
        elif mode == "whole-tone":
            # Use modified thumb-pass rule (every 5-6 notes)
            ...
        elif mode in diatonic_modes:
            # Use mode-specific cadence detection
            ...
        # Run DP on segment with adjusted rules
```

實作上**複雜度高**，建議漸進：
1. **Phase 1**：純粹偵測 mode，當作 metadata，不影響 DP
2. **Phase 2**：對 pentatonic 段落停用 thumb-reservation
3. **Phase 3**：mode-specific cadence detection
4. **Phase 4**：whole-tone thumb-pass override

## 7. PIG 驗證候選

| ID | 曲目 | 預期 mode |
|---|---|---|
| Debussy Pagodes (若在 PIG) | 035-040 範圍 | pentatonic |
| Debussy Voiles (若在 PIG) | 035-040 範圍 | whole-tone |
| Grieg Lyric Pieces | 081-090 範圍 | Lydian / Dorian inflections |
| **037** Clair de Lune | 037 | major (modally inflected, 不是純 modal) |

## 8. 與其他 wiki 頁面的關係

- 跨 wiki：與 [../wiki_piano/src_chinese_style_piano](../wiki_piano/src_chinese_style_piano.md) 五聲音階指法重疊
- 影響 [concept_cadence_detection](concept_cadence_detection.md)：modal cadence patterns 補充
- 影響 [concept_running_passage_thumb_reservation](concept_running_passage_thumb_reservation.md)：pentatonic 段不適用
- 引用方 [composer_debussy_phrasing](composer_debussy_phrasing.md) (whole-tone / pentatonic / octatonic)、[composer_grieg_lyric_pieces](composer_grieg_lyric_pieces.md) (modal inflections)
- 待寫：
  - [concept_modal_cadence_patterns](concept_modal_cadence_patterns.md) (mode-specific cadence)
  - [../wiki_piano/concept_pentatonic_finger_groups](../wiki_piano/concept_pentatonic_finger_groups.md) (跨 wiki 新頁)

