# Concept: Phrase Elision 樂句重疊 — 邊界歸屬問題

> 來源：通用音樂理論 + Rothstein《Phrase Rhythm in Tonal Music》Ch.3 elision、Caplin《Classical Form》§phrase combination
> 引用方：[[concept_classical_period_sentence]]、[[concept_chopin_lyrical_phrase]]、[[composer_beethoven_phrasing]]
> 狀態：第一版 2026-05-26

## 1. 一句話定義

**Phrase elision (樂句重疊)**：一句的 cadential 結尾音同時是下一句的開始音。表面看像兩句連接，實際上是「同一個音兩個身份」 — 對指法系統而言，這個音應該屬於**哪一句**？

例：
```
A 句：…… V → I  ⟶ B 句：I → …… (B 句從 A 句的 PAC 落點起跑)
                ↑
              同一個 I 和弦 = A 句的結尾 + B 句的開頭
```

## 2. 為什麼這對指法系統很重要

`_run_phrase_dp` 用 `INTER_PHRASE_SCALE = 0.0`，phrases 獨立優化。一個 elision 音被歸到哪個 phrase 影響：
- A 句的 DP 範圍 (groups[start_A..elision_idx] vs ..elision_idx-1)
- B 句的 DP 範圍 (groups[elision_idx..end_B] vs elision_idx+1..)
- 那個 elision 音的 finger 由哪個 phrase 的 DP 決定

歸錯了會導致：
- elision 音的指法跟前句尾矛盾（前句要結尾、新句要開新位置）
- B 句少了起手 anchor 音、anchor 計算偏
- 或 A 句多了一個離原 phrase center 太遠的「異物」音，破壞 phrase shape

## 3. Elision 的兩種觀點

### 3.1 「歸前」(elision-as-overlap-end)
elision 音 = A 句的最後一個音 + B 句**從下一個音**起算。
- A 句指法在這音收尾
- B 句獨立優化，第一個音是 elision 音的後一個

### 3.2 「歸後」(elision-as-overlap-start)
elision 音 = B 句的第一個音 + A 句**到上一個音**為止。
- A 句指法在 elision 音前收尾
- B 句包含 elision 音作為起手

### 3.3 操作型選擇：歸前

理由（與 user override 行為一致）：
- elision 音通常是 cadential 解決（V→I 的 I），手部處於收束姿態 — 屬於前句的「呼吸出」
- 新句的「呼吸入」是下一個音 — 是新句真正的起點
- 對 thumb-reservation 等 phrase-start 規則的 anchor 計算更準確

→ `_detect_phrase_starts` 應返回 elision **後一個** group 的 idx 作為 phrase boundary。

## 4. 偵測 elision 的訊號

| 訊號 | 操作型 | 信心度 |
|---|---|---|
| **PAC 落點同時是 motif 開頭** | 在偵測到 PAC 的 group，下一 group 也是 subject head | ⭐⭐⭐ |
| **PAC + 短時值** | PAC 解決音 duration < typical phrase ending duration | ⭐⭐ |
| **明確 phrase mark 重疊** | 樂譜上 phrase slur 結尾落在下一個 phrase 開頭音之前 | ⭐⭐⭐ (若 OMR 抽得到) |
| **Texture 連續** | A 句 cadence 後 B 句立即開始，無休止 | ⭐⭐ |

## 5. 各時期 elision 常見度

| 時期 | Elision 頻率 | 典型場景 |
|---|---|---|
| 巴洛克 (Bach) | 少（subject entry 通常後接 episode，明確分段） | Final entries → coda 偶有 |
| 古典 (Mozart) | 中等（sentence continuation 內常見） | Sentence's cadence elides with codetta |
| **浪漫 (Chopin)** | **高**（連續 lyrical 線條的標誌） | Nocturne 中段 |
| **晚期浪漫 (Brahms / Rachmaninoff)** | **高** | 連續長 phrases 串連 |
| 印象派 (Debussy) | 中等（texture 主導，邊界本來就模糊） | — |
| 現代 (Bartok / Scriabin) | 低（節奏結構更突兀） | — |

## 6. 演算法整合到 `_detect_phrase_starts`

```python
def _detect_phrase_starts_with_elision(groups, mxl_path):
    # 1. 跑現有偵測
    starts = _detect_phrase_starts(groups)

    # 2. 對每個偵測到的 cadence (PAC) 位置，檢查是否 elision
    cadences = detect_cadences(groups, mxl_path)
    for cad_idx, cad_type in cadences:
        if cad_type != "PAC": continue
        # 若下一 group 立刻有新 phrase 起點 (motif start / texture change),
        # 則 elision = True，邊界放下一 group
        if cad_idx + 1 < len(groups):
            next_g = groups[cad_idx + 1]
            if is_phrase_start_signal(next_g):
                # Boundary at cad_idx + 1 (B 句從 cad_idx + 1 起)
                starts.add(cad_idx + 1)
                # 注意：cad_idx 本身應屬 A 句，不另立邊界
                continue
        # 非 elision：standard PAC boundary at cad_idx + 1
        starts.add(cad_idx + 1)

    return sorted(starts)
```

實作上的主要差別 = **如何識別「elision 訊號」**。最簡單：偵測 PAC + 下一音是 strong-beat motif start。

## 7. 對 motif consistency 的影響

[[../score-claude/memory/feedback_personal_biomechanics]] 要求同 motif 同指法。Elision 場景下：
- B 句的開頭 motif 與其他 occurrences 比對時，應該從 **B 句真正的開頭** 起算（即 elision 音的後一個，若採「歸前」）
- 不應把 elision 的 cadential 音當作 motif head

→ Motif detection ([[concept_subject_imitation_detection]]) 應在 elision-aware phrase boundary 之後跑。

## 8. 與其他 wiki 頁面的關係

- 依賴 [[concept_cadence_detection]] (PAC 偵測為前置)
- 影響 [[concept_subject_imitation_detection]] (motif 起算點)
- 主要使用於 [[concept_chopin_lyrical_phrase]] (浪漫派 elision 頻繁)、[[composer_beethoven_phrasing]] (中期常用)
- 待寫：
  - [[analysis_chopin_op9_no2_nocturne]] 應該有 elision 範例

## 變更日誌
- 2026-05-26: 創立。Phrase elision 概念頁，含「歸前」操作型決定 + 整合到 `_detect_phrase_starts` 的方案。
