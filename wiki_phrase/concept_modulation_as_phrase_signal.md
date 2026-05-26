# Concept: Modulation as Phrase Signal — 轉調作為樂句邊界訊號

> 來源：通用音樂理論 + Schenker analyses of Schubert/Brahms、Caplin《Classical Form》§modulation
> 引用方：[[composer_schubert_long_phrase]]、[[composer_beethoven_phrasing]]、[[composer_chopin_phrasing]]
> 狀態：第一版 2026-05-26

## 1. 一句話定義

**Modulation as phrase signal**：當作品從一個調轉到另一個調，這個轉調點**幾乎一定**是樂句邊界（情緒切換、harmonic landscape 重整）。對指法系統而言，這是**獨立於 cadence / subject / figural** 的第四類強訊號。

## 2. 為什麼這對指法系統很重要

- 轉調點 = 樂句邊界 = phrase reset = 指法 anchor 重新計算
- 不同調的「自然指法」差異大（白鍵調 vs 黑鍵調，scale fingering 差異）
- 轉調後 LH 持續和聲 pattern 通常變化 → 順便給 LH-RH 樂句邊界對齊的訊號
- OMR (Audiveris) 通常**抽得到** `<key>` element，比 cadence 偵測**更可靠**

## 3. 轉調的類型與樂句邊界強度

### 3.1 Closely related modulation (近系轉調)
- C major → G major (V), F major (IV), a minor (vi), d minor (ii), e minor (iii)
- **樂句邊界強度**：⭐⭐⭐ — 通常為 sonata-allegro 第一主題→第二主題的標準
- **典型場景**：古典時期 sonata exposition

### 3.2 Chromatic mediant modulation (色彩三度轉調)
- C major → E major / A♭ major / E♭ major (跨大小三度關係)
- **樂句邊界強度**：⭐⭐⭐ — Schubert / Chopin / Brahms 標誌性手法
- **典型場景**：浪漫派中段轉調 (Schubert Op.90-3 G♭ → e♭ minor)
- **指法影響**：常從白鍵調轉到黑鍵調（或反之），五指 position 完全重置

### 3.3 Enharmonic modulation (異名轉調)
- 透過異名同音和弦（如德國增六 → V7）跨遠系
- **樂句邊界強度**：⭐⭐⭐
- **典型場景**：浪漫派戲劇性轉折 (Beethoven Op.27-2 中段)

### 3.4 Modulating sequence (轉調模進)
- 主題在連續不同調上重複（each occurrence = mini-modulation）
- **樂句邊界強度**：⭐⭐ — 模進**內部**可能是同樂句的 sub-units
- **典型場景**：Bach episode (subject 在 V, vi, IV 連續模進)
- **注意**：不要把每個 sequence step 都當成樂句邊界，整段才是一個 unit

### 3.5 Tonicization (短暫離調)
- 1-2 bar 內短暫指向另一個調（含 secondary dominant 等）
- **樂句邊界強度**：⭐ (低) — 太短，不算真正轉調
- **典型場景**：古典時期 development 內部
- **注意**：避免把 tonicization 誤判為轉調

## 4. 偵測演算法

### 4.1 Key signature change (最強訊號)
```python
def detect_keysig_changes(mxl_path):
    """從 MusicXML <key> elements 抽取 key signature changes."""
    import music21
    score = music21.converter.parse(mxl_path)
    changes = []  # list of (measure_num, offset, new_key)
    for part in score.parts:
        for keysig in part.flat.getElementsByClass('KeySignature'):
            changes.append((
                keysig.measureNumber,
                keysig.offset,
                keysig.asKey()
            ))
    return changes
```

**信心度**：⭐⭐⭐ — 樂譜上的 explicit 標記，幾乎 100% 是樂句邊界。

### 4.2 Harmonic key analysis (中等訊號)
```python
def detect_key_changes_by_analysis(mxl_path, window_bars=4):
    """每 window_bars 重算一次 key, 找變化."""
    import music21
    score = music21.converter.parse(mxl_path)
    total_bars = ...
    changes = []
    prev_key = None
    for start_bar in range(0, total_bars, window_bars):
        excerpt = score.measures(start_bar, start_bar + window_bars)
        cur_key = excerpt.analyze('key')
        if prev_key and cur_key.name != prev_key.name:
            changes.append((start_bar, cur_key))
        prev_key = cur_key
    return changes
```

**信心度**：⭐⭐ — music21 key analysis 可能不準（尤其浪漫派擴張和聲）；可作為 key signature 缺漏時的 fallback。

### 4.3 過濾 tonicization
若新 key 持續 ≤ 2 bar 就回到原 key → 是 tonicization，**不**標樂句邊界。

```python
def filter_tonicizations(changes, min_persist_bars=3):
    filtered = []
    for i, (bar, key) in enumerate(changes):
        if i + 1 < len(changes):
            next_bar = changes[i + 1][0]
            if next_bar - bar < min_persist_bars:
                continue  # 太短，跳過
        filtered.append((bar, key))
    return filtered
```

## 5. 整合到 `_detect_phrase_starts`

```python
def _detect_phrase_starts_with_modulation(groups, mxl_path):
    starts = set(_detect_phrase_starts(groups))

    # 1. Key signature changes (strongest)
    keysig_changes = detect_keysig_changes(mxl_path)
    for (m, off, _key) in keysig_changes:
        # 找對應 group idx
        for i, g in enumerate(groups):
            if g[0]['measure'] == m and abs(g[0]['offset'] - off) < 0.5:
                starts.add(i)
                break

    # 2. (Optional) Harmonic key changes (fallback)
    # 只有當 keysig_changes 太稀疏（< 1 / 16 bar）才啟用，避免 over-detection

    return sorted(starts)
```

## 6. 各時期 modulation 為 phrase signal 的重要性

| 時期 | Modulation 頻率 | 信心度 |
|---|---|---|
| 巴洛克 (Bach) | 中（episode 內 sequence） | ⭐⭐ (注意 sequence 不算 modulation) |
| 古典 (Mozart) | 高（sonata-allegro 標準） | ⭐⭐⭐ |
| **早期浪漫 (Schubert)** | **極高**（chromatic mediant 標誌） | **⭐⭐⭐⭐** |
| 浪漫 (Chopin) | 高（中段轉調常見） | ⭐⭐⭐ |
| 印象 (Debussy) | 低（modal 為主，傳統 key 失效） | ⭐ |
| 現代 (Bartok) | 低 / 不適用 | — |

**最有效作曲家**：Schubert > Beethoven (中期) > Chopin > Mozart > 其他

## 7. PIG 驗證候選

| ID | 曲目 | 為何選 |
|---|---|---|
| **111** | Schubert Op.90-3 G♭ | 標誌性 chromatic mediant (G♭ → e♭) |
| 113 | Schubert Wanderer Fantasy | 多次 modulation，連續樂章 |
| 034 | Beethoven Pathétique 1st | sonata-allegro 標準 modulation |
| 021 | Chopin Ballade 2 | 中段戲劇性 key 切換 |

## 8. 與其他 wiki 頁面的關係

- 補完 [[concept_classical_period_sentence]] 的 cadence 訊號
- 與 [[concept_cadence_detection]] 互補（cadence 處理段內，modulation 處理段間）
- 對 [[composer_schubert_long_phrase]] 是**核心**訊號
- 對 [[concept_impressionist_phrasing]] 是**反指標**（Debussy modal 不適用）
- 對 [[concept_fugue]] §3.2 development 段相關

