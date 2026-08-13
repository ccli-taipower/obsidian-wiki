---
concept: 音階指法 (Scale Fingering)
date_created: 2026-04-08
tags: [piano_fingering, scales, finger_groups, thumb_under, technique]
---

# 音階指法 (Scale Fingering)

音階是鋼琴演奏的基礎，熟記音階指法能大幅加速視譜與學習。

## 指群法 (Finger Groups)

音階指法由**短組（3 指）和長組（4 指）交替**組成（Tim Stein / Graham Fitch）：

- **C 大調右手**：1-2-3 | 1-2-3-4 | （短組 + 長組）
- **C 大調左手**：5-4-3-2-1 | 3-2-1 | （長組 + 短組）
- 練習法：先分組練再連起來

指群結構的直接推論：**同一組內每個音用不同手指**，換組靠拇指穿越。
跑動中途重複同一手指等於把指群切斷——手必須在原地滑動或抬起重放，
既破壞圓滑也打亂下一次穿越的落點。此推論與手指強弱無關，
是幾何性質而非負荷性質。

**DP 對應（2026-08-13）**：`SCALE_REPEAT_FINGER_PENALTY` 對 scale segment 內的
同指異音收固定罰（與 `FINGER_AGILITY` 無關，區別於 `SAME_FINGER_WEAK_PENALTY`）。

## 指法家族

同一套指法適用於多個調：

| 家族 | 適用調（大小調均適用）|
|------|-------------------|
| C 大調指法 | C, D, E, G, A |
| B♭ 家族（LH 3-4 開頭）| B♭, E♭, A♭, D♭ |
| F 大調指法 | F |
| B 大調指法 | B |

## 非傳統音階指法

### 極簡主義觀點（Cory Hall）
- 傳統 C 大調指法（123-12345）不是唯一選擇
- F 大調指法（1234-1234）更均等，可作為「預設」
- 至少 8 種有效替代指法
- 詳見 [concept_minimalist_fingering](concept_minimalist_fingering.md)

### 人體工學觀點（Graham Fitch）
- F 小調和聲左手替代指法：長指上黑鍵、短指上白鍵
- 符合手的自然形狀，呼應 [Chopin 教學法](concept_chopin_method.md)

## 半音階指法

| 類型 | 指法 | 適用 |
|------|------|------|
| 基礎 | 1-3-1-3（白鍵對用 2）| 慢速 |
| 進階 | 1-2-3-4 四指組（遇拇指上黑鍵改 3 指組）| 快速 |

**DP 對應（2026-06-15）**：基礎 1-3 指法已實作為 `USE_CHROMATIC_FINGERING`（opt-in flag, default OFF）。DP 的 `_detect_scale_segments` 把半音階排除（`SCALE_MAX_CHROMATIC_RUN`），故 base DP 對半音階無規則（診斷：標 1-2-3-4-5 循環、黑鍵 37/40 非 f3）。新規則 `_detect_chromatic_segments`（≥5 音全半音同向 run）+ `_chromatic_segment_fingers`（**黑→3、白→拇指、白-白橋 E-F/B-C 第二音→2**）在 phrase DP 內把 segment 單音 filter 成 rule finger。harness：flag-ON 後拇指 0 次落黑鍵、黑鍵 100% f3。進階四指組未實作（偏 advanced）。branch feat-chromatic-fingering。

## 雙音音階

- 同樣短組+長組原則（雙拇指：2-1 / 3-1）
- 完全連奏不可能 → 至少一音連奏，創造**連奏錯覺**
- 參考 Moskovsky《School of Double Notes》

## 拇指穿越練習

音階的核心技巧。練習法（Tim Stein）：
- 三音反覆練習拇指轉位
- 保持手腕放鬆，不要把拇指強推到手下方
- 詳見 [concept_thumb_technique](concept_thumb_technique.md)

## 白鍵錨定 (White-Key Anchoring, 2026-06-15)

**基本原則**：音階中拇指只能落在白鍵上。這是無爭議的演奏傳統，任何調的音階指法皆遵循此原則。

### 貪心 3-or-4 算法的侷限

`_compute_scale_pivots` 的貪心演算法（每隔 3 或 4 鍵切換拇指）在 C / G / D / A / E 等白鍵多的調上成立，因為這些調的白鍵恰好落在 3–4 鍵間距。然而在黑鍵密集調（C♯、E♭、A♭、D♭）上，貪心切割點可能落在黑鍵，違反基本原則。

### 白鍵錨定修復

`_white_key_anchored_pivots(seg, groups, hand)` 在貪心結果含黑鍵 pivot 時介入，重新搜尋各 pivot 附近最近的白鍵作為替代落點（engaged only when greedy lands on black）。`SCALE_THUMB_BLACK_PENALTY = 5.0` 在 `_run_phrase_dp` 的初始化迴圈與內層迴圈中對首音 thumb 落黑鍵施加 scale-local 懲罰，補強非 pivot 起始音的約束。兩者合力使長音階 DP 在所有調上都符合「拇指只落白鍵」的基本原則。

**DP 對應**：`_compute_scale_pivots` / `_white_key_anchored_pivots` / `SCALE_THUMB_BLACK_PENALTY`（`program/run.py`，`USE_LONG_SCALE_THUMB_UNDER` flag）。

## 來源

- [src_graham_fitch_video_series](src_graham_fitch_video_series.md)
- [src_piano_fingering_articles](src_piano_fingering_articles.md)
- [src_piano_fingering_articles_batch2](src_piano_fingering_articles_batch2.md)
- [concept_piano_fingering_principles](concept_piano_fingering_principles.md)
