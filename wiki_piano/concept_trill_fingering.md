# Concept: Trill Fingering — 顫音指法

> 來源：C.P.E. Bach *Versuch* §trills, Czerny *Op.500* §trills, Hanon §finger independence
> 引用方：[concept_finger_substitution](concept_finger_substitution.md), [concept_hand_anatomy](concept_hand_anatomy.md)（4-5 弱指）, [../wiki_articulation/concept_ornament_articulation](../wiki_articulation/concept_ornament_articulation.md)

## 1. Trill 是什麼

Trill（顫音）= 兩個相鄰音（通常 1 音差 = 半音 / 全音）快速交替。標準 trill：
- **Main note + upper neighbor** (Baroque + Classical 派)
- **Upper neighbor + main note** (現代多用，從上音開始)
- 持續時長視音樂內容，通常 1-2 拍至整小節

Trill 是 ornament 中**最常見**的一種，每個 cadence 幾乎都用。

## 2. 標準 trill 指法

⚠ Training-data verification needed:

| 演奏層級 | 指法選項 | 場合 |
|---|---|---|
| **入門** | 2-3 | 短 trill、白鍵 |
| **進階** | 3-4 | 中速 trill、各種音域 |
| **高難** | 4-5 | 上音為 4/5 可達到處（rare）|
| **避免** | 1-2 | thumb 在 trill 中不靈活（除非必要）|

→ **2-3** 是最通用標準。**3-4** 訓練手指獨立性。**4-5** 是高難挑戰（4-5 之間 juncturae tendinum 限制獨立性）。

## 3. 為何 trill 需要 finger independence

物理上 trill = 兩根手指**極高速度交替**：
- 慢 trill: 每秒 ~5-6 音（即每指 ~3 次/秒）
- 中速 trill: 每秒 ~8-10 音
- 快速 trill: 每秒 ~12+ 音（接近 motor 控制極限）

對手指要求：
- **彈下動作**: 主動快速
- **釋放動作**: 同樣快速（不能因 release 慢拖累下個 attack）
- **不互相干擾**: 一手指動作不能拉動另一手指

→ Trill 的 fingering 選擇直接影響可達速度 + 持續性。

## 4. 4-5 trill 的特殊挑戰

⚠ Training-data verification needed:

4-5 trill 是鋼琴技術中**最難的單一動作**之一：
- **解剖學**: 4-5 有 juncturae tendinum 連接，獨立性最差
- **訓練**: Hanon / Czerny 大量 4-5 練習為此設計
- **替代**: 演奏家常用 3-5 或 4-5-4-5 變體繞過純 4-5 trill
- **失敗訊號**: 5 開始無法及時 release → trill 逐漸減速 → "**trill 拖死**"

對應 [analysis_common_fingering_injuries](analysis_common_fingering_injuries.md)：強迫 4-5 trill 持續是 focal dystonia / strain 高風險。

## 5. Trill resolution 處理

Trill 通常接 resolution 音（cadence 解決音）：
- 標準 trill: 主音-上音-主音-上音-...-結束音
- Resolution 通常 legato 連接到後續 melodic 音
- 結束指應方便接後續 fingering

⚠ Training-data verification needed: Czerny 主張：trill 結束音應**用適合接後續 fingering 的指**，可能需要 trill 內部 substitution（中段切換 trill 用指）。

## 6. Compound trill (trill + ornament)

⚠ Training-data verification needed:

Trill 可結合其他 ornament：
- **Trill + turn**: trill 結束加 turn 修飾
- **Trill + termination**: trill 結尾加 2-3 額外音
- **Double trill** (兩聲部同時 trill): rare 但存在於 advanced 曲目

複合 trill 對 fingering 更複雜 — 通常需 advanced 演奏家自選 fingering。

## 7. Trill 速度與 fingering 對應

⚠ Training-data verification needed:

| Trill 速度 | 推薦 fingering |
|---|---|
| 慢 (♩=60 trill 每秒 4-5 音) | 任何 fingering 都可（2-3 / 3-4 / 4-5）|
| 中速 (♩=100 trill 每秒 7-8 音) | 2-3 / 3-4 為主 |
| 快速 (♩=140+ trill 每秒 10+ 音) | 2-3 強烈偏好（最獨立 + 最強）|
| 極快 (presto) | 2-3 唯一可靠 |

→ 速度越快越偏 2-3。4-5 trill 在快速段幾乎無法 sustain。

## 8. 對 score-claude DP 的影響

DP 對 trill 的處理：
- 識別 trill marker (`tr` 或 `~~~`)
- Trill 內部音通常**極短** (duration < 0.125 QN)，由 [../wiki_articulation/concept_legato_substitution](../wiki_articulation/concept_legato_substitution.md) §6 LEGATO_MIN_DURATION gate 自動跳過 substitution rule
- 但對 trill 兩音 fingering 選擇，DP 目前無 special-case — 看 cost 自然產生

未來 v3 candidate：**trill-aware fingering rule** — 偵測 trill 段強制偏好 2-3 fingering。是 future direction，未實作。

## 9. 適用作曲家 / 曲目

| 作曲家 | Trill 使用頻率 |
|---|---|
| **Bach** | 中高 — Inventions / Sinfonias / Suite 偶見；Goldberg Variations 大量 |
| **Mozart** | 高 — 每個 cadence 幾乎都用 trill |
| **Beethoven** | 高 — Op.111 mvt2 高難度 long trill |
| **Chopin** | 中 — 較少純 trill，多 cadence-style |
| **Liszt** | 高 — *La Campanella* 大量複合 trill |

## 10. 與其他 wiki 頁面的關係

- [concept_finger_substitution](concept_finger_substitution.md) — Trill 中段 substitution 處理
- [concept_hand_anatomy](concept_hand_anatomy.md) — 4-5 juncturae tendinum 物理基礎
- [analysis_common_fingering_injuries](analysis_common_fingering_injuries.md) — Trill 強迫 4-5 的 strain 風險
- [../wiki_articulation/concept_ornament_articulation](../wiki_articulation/concept_ornament_articulation.md) — Trill 作為 ornament 的 articulation 處理
- [../wiki_articulation/src_cpe_bach_versuch](../wiki_articulation/src_cpe_bach_versuch.md) — C.P.E. Bach 對 trill 的權威論述
