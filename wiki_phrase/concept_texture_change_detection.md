# Concept: Texture Change Detection — 紋理變化作為樂句邊界

> 來源：通用音樂分析 + Howat《Debussy in Proportion》 + standard texture analysis
> 引用方：[concept_impressionist_phrasing](concept_impressionist_phrasing.md) (核心需求)、[composer_debussy_phrasing](composer_debussy_phrasing.md)、[concept_chopin_lyrical_phrase](concept_chopin_lyrical_phrase.md) (浪漫派部分需要)
> 狀態：工具頁，第一版 2026-05-26

## 1. 為什麼這頁是印象派 / 浪漫派的核心工具

[concept_impressionist_phrasing](concept_impressionist_phrasing.md) §1 已建立原則：**Debussy 的樂句邊界不靠 cadence**，靠 texture 變化。但「什麼算 texture 變化」需要這頁定義操作型偵測規則，否則只是概念無法實作。

[concept_chopin_lyrical_phrase](concept_chopin_lyrical_phrase.md) §3.5 也提到 LH pattern / accompaniment 切換是浪漫派的樂句訊號。同樣需要此頁支援。

## 2. Texture 的四個可測維度

| 維度 | 操作型 | 對應感知 |
|---|---|---|
| **Chord density** | 平均 note count per chord group | 「厚」vs「薄」 |
| **Registral range** | (max midi − min midi) per chord group | 「廣」vs「窄」 |
| **Registral center** | average midi per chord group | 「高」vs「低」 |
| **Dynamic level** | dynamic marking (pp/p/mp/mf/f/ff) | 「強」vs「弱」 |
| **Pedal state** | sostenuto / damper pedal on/off | 「混響」vs「乾淨」 |

每個維度在連續 N chord 內的**顯著變化** = 樂句邊界候選。

## 3. 偵測演算法

### 3.1 Chord density change
```python
def detect_density_changes(groups, window=4, min_delta=2):
    """偵測連續 4 chord 內平均 note count 跳變 ≥ 2."""
    changes = []
    for i in range(window, len(groups) - window):
        before = sum(len(g) for g in groups[i-window:i]) / window
        after  = sum(len(g) for g in groups[i:i+window]) / window
        if abs(after - before) >= min_delta:
            changes.append(i)
    return changes
```

**信心度**：⭐⭐⭐ — chord density 是 OMR 直接可測 (note count per group)

### 3.2 Registral shift
```python
def detect_registral_shifts(groups, window=4, min_shift_semitones=7):
    """連續 4 chord 平均 midi center 移動 ≥ 7 半音 (perfect 5th)."""
    changes = []
    for i in range(window, len(groups) - window):
        before_mids = [g[0]['midi'] for g in groups[i-window:i]]
        after_mids  = [g[0]['midi'] for g in groups[i:i+window]]
        before_c = sum(before_mids) / window
        after_c  = sum(after_mids)  / window
        if abs(after_c - before_c) >= min_shift_semitones:
            changes.append(i)
    return changes
```

**信心度**：⭐⭐ — 與現有 `PHRASE_BREAK_THRESHOLD=13` 部分重疊，但本規則對更小幅 (7-12 半音) 也偵測

### 3.3 Range / spread change
```python
def detect_range_changes(groups, window=4, min_delta=5):
    """連續 4 chord 的 spread (max-min midi) 跳變 ≥ 5 半音."""
    changes = []
    for i in range(window, len(groups) - window):
        before_spread = max([n['midi'] for g in groups[i-window:i] for n in g]) - \
                        min([n['midi'] for g in groups[i-window:i] for n in g])
        after_spread  = max([n['midi'] for g in groups[i:i+window] for n in g]) - \
                        min([n['midi'] for g in groups[i:i+window] for n in g])
        if abs(after_spread - before_spread) >= min_delta:
            changes.append(i)
    return changes
```

**信心度**：⭐⭐ — 偵測「窄旋律 → 寬和聲」或反之

### 3.4 Dynamic shift (需 OMR 抽 dynamic markings)
```python
def detect_dynamic_changes(score, min_steps=2):
    """從 music21 抽 dynamic markings, 偵測跨越 ≥ 2 steps 的變化."""
    levels = {'pp': 0, 'p': 1, 'mp': 2, 'mf': 3, 'f': 4, 'ff': 5, 'fff': 6}
    import music21
    dynamics = list(score.flat.getElementsByClass('Dynamic'))
    changes = []
    for i in range(1, len(dynamics)):
        prev_val = levels.get(dynamics[i-1].value, 3)
        curr_val = levels.get(dynamics[i].value, 3)
        if abs(curr_val - prev_val) >= min_steps:
            # Map dynamic location to group idx (需 caller 對齊)
            changes.append((dynamics[i].measureNumber, dynamics[i].offset))
    return changes
```

**信心度**：⭐⭐⭐ (若 Audiveris 抽得到 dynamic) — 動態突變幾乎一定是樂句邊界

### 3.5 Pedal change
```python
def detect_pedal_changes(score):
    """抽 pedal marking changes."""
    import music21
    pedals = list(score.flat.getElementsByClass('PedalMark'))  # music21 class name 待驗證
    return [(p.measureNumber, p.offset, p.type) for p in pedals]
```

**信心度**：⭐⭐⭐ (若 OMR 抽得到) — pedal release ★ = sound color 結束 = 樂句結束

## 4. 整合：複合 score

不同維度的訊號權重不同：

```python
def detect_texture_phrase_boundaries(groups, mxl_path):
    candidates = {}
    for idx in detect_density_changes(groups):
        candidates[idx] = candidates.get(idx, 0) + 1.0   # density 權重
    for idx in detect_registral_shifts(groups):
        candidates[idx] = candidates.get(idx, 0) + 0.8
    for idx in detect_range_changes(groups):
        candidates[idx] = candidates.get(idx, 0) + 0.6
    # ... 加 dynamic / pedal

    # 多個訊號 vote 同一 idx (或鄰近 ±2) → 強樂句邊界
    boundaries = {idx for idx, score in candidates.items() if score >= 1.5}
    return sorted(boundaries)
```

**Score threshold 1.5** 表示至少兩個訊號同時點，或一個訊號 +一個 cross-check（避免 single-signal false positive）。

## 5. 與其他偵測器整合

```
phrases = union(
    _detect_phrase_starts(...),          # 既有 hard breaks + period fallback
    detect_subject_entries(...),         # 對位作品
    detect_cadence_boundaries(...),       # 主調作品
    detect_figural_boundaries(...),       # episode / coda
    detect_texture_phrase_boundaries(...) # 印象派 / 浪漫派
)
```

**衝突處理**：texture boundary 若落在已有 subject / cadence boundary 旁 ±2 group，去重保留更強訊號。

## 6. 預期失靈情況

| 場景 | 失靈原因 | 補救 |
|---|---|---|
| 對位音樂 (Bach Inv) | texture 持續均一 (16th 流動)，density 不變 | 不適用，靠 subject detection |
| 巴洛克 ornate | trill / mordent 短暫增加 density，誤判 | 過濾 duration < 1/16 拍的 ornament |
| 漸進 crescendo | dynamic 緩慢變化，不觸發 "≥ 2 steps" | 取捨；漸進不算樂句邊界 |
| 連續 alberti bass | density / range 都穩定，texture 不變 | 不需偵測樂句邊界 — 整段為一個 phrase |

## 7. PIG 驗證候選

| ID | 曲目 | 期望偵測 |
|---|---|---|
| **037** Debussy Clair de Lune | A→B (中段 arpeggio wash) | density + range 同時跳 |
| 035 Debussy Arabesque 1 | A→B 段 | tempo + texture |
| 023 Chopin Nocturne Op.9-2 | LH waltz pattern reset (每 4-bar) | density 變化 (連續和弦 → 單音 + arpeggio) |

## 8. 與其他 wiki 頁面的關係

- 核心被 [concept_impressionist_phrasing](concept_impressionist_phrasing.md) 引用
- 被 [composer_debussy_phrasing](composer_debussy_phrasing.md) 部分採用（早期作品 cadence + texture 並用）
- 被 [concept_chopin_lyrical_phrase](concept_chopin_lyrical_phrase.md) §3.5 引用
- 補強 [concept_phrase_elision](concept_phrase_elision.md) 的 elision detection（texture 連續 = elision 訊號）
- 與 [concept_figural_boundary_detection](concept_figural_boundary_detection.md) 互補（figural 看 melodic 形狀，texture 看 vertical 厚度）

## 9. 漸進實作路線

**Phase 1**：density + registral 偵測 (純結構訊號)
- 對 Debussy PIG 037 (Clair de Lune) A/B 驗證

**Phase 2**：加 dynamic + pedal 偵測 (需確認 Audiveris 抽取)
- 對 Préludes 系列驗證

**Phase 3**：複合 voting score + threshold 調參

