# Concept: Articulation 與 Tempo 的互動

> 來源：Matthay《The Visible and Invisible》§速度與觸鍵, Brendel essays §tempo flexibility, Czerny *Op.500* §速度與表情
> 引用方：[concept_legato_substitution](concept_legato_substitution.md) §6 (失效情境：快速 passage), [concept_staccato](concept_staccato.md) §1（物理動作與速度的關係）

## 1. 為什麼 tempo 影響 articulation 詮釋

同一個 articulation 標記在不同 tempo 下**物理上**是不同行為：

| 標記 | Adagio (慢) | Allegro (快) | Presto (極快) |
|---|---|---|---|
| **Slur (legato)** | 重量觸鍵 + finger substitution 充分時間 | 仍 legato，但 substitution 限速 | 物理難 substitution；改用 hand-position 穩定 |
| **Staccato** | 較長停頓感的短斷 | 較尖銳的點狀 attack | 接近「**手指 staccato**」（最快、最輕的變體）|
| **Tenuto** | 持滿值 + 壓重 | 持滿值，但壓重感弱 | 接近一般 detache（持滿時間有限）|
| **Accent** | 顯著重音 | 重音仍清楚 | 重音減弱（速度限制）|

→ Tempo 不只是「**演奏速度**」，更影響 articulation 是否**物理可行**。

## 2. Matthay 的「速度-重量觸鍵不相容」原則

[src_matthay_visible_inaudible](src_matthay_visible_inaudible.md) §2.3:

⚠ Training-data verification needed:
> 「重量觸鍵與快速度不相容 — 快速段（≥ Allegro 16 分音符）必須用手指 staccato，重量觸鍵會跟不上；慢速段（≤ Andante 八分音符）重量 legato 才有時間建立。」

對指法的意涵：
- 快速段 substitution 來不及執行 → [concept_legato_substitution](concept_legato_substitution.md) §6 失效情境 + LEGATO_MIN_DURATION gate
- 慢速段重量 legato 必要 → substitution rule 強烈適用
- 中速段（八分音符 in Moderato）→ 介於兩者

## 3. 同一段不同 tempo 的具體例子

⚠ Training-data verification needed: 假設一段 16th-note RH passage 標 slur (legato):

| Tempo | 演奏實踐 | 是否可 substitution |
|---|---|---|
| **♩=60 (Andante)** | 每音 ~0.25 秒，substitution 有時間 | 適用 |
| **♩=100 (Moderato)** | 每音 ~0.15 秒，substitution 急促但仍可 | 邊緣可用 |
| **♩=140 (Allegro)** | 每音 ~0.1 秒，substitution 物理困難 | 失效 |
| **♩=180 (Vivace)** | 每音 ~0.08 秒，幾乎不可能 substitution | 失效 |

→ score-claude DP 的 LEGATO_MIN_DURATION = 0.5 QN 大致對應 Andante 範圍。Allegro 16th-note (duration 0.25 QN) 自然被 gate 跳過。

## 4. Tempo 對 thumb-cross 的影響

⚠ Training-data verification needed:
- **慢速段**：thumb-cross 物理寬鬆，可花時間 reposition
- **快速段**：thumb-cross 需預備（提前 prepare），無法「臨時」cross
- **極快段**：thumb-cross 風險高（focal dystonia 風險，Altenmüller 2005）

對指法的意涵：score-claude 的 `THUMB_PASS_PHRASE_BUDGET` rule 對快速段段應該**緊縮**（少許免罰 thumb-pass）。目前 DP 未根據 tempo 調整此 budget — 是 known 限制。

## 5. Tempo 標記如何進入指法系統

理論上，MXL 的 `<metronome>` element 提供 tempo 信息。但 score-claude DP 目前**完全不看 tempo**：
- LEGATO_MIN_DURATION = 0.5 QN 是 tempo-independent 閾值
- THUMB_PASS_PHRASE_BUDGET = 3 是 tempo-independent

未來改進方向：
1. **Tempo-aware LEGATO_MIN_DURATION**：在 Allegro 段提高閾值（如 0.75），在 Adagio 段降低（如 0.25）
2. **Tempo-aware THUMB_PASS_BUDGET**：快速段更緊
3. **Tempo-aware STEP_AGILITY_WEIGHT**：快速段更寬鬆（弱指允許更多使用）

是 wiki_articulation 提出的 future direction，未實作。

## 6. 演奏家對「tempo 標記」的態度

不同學派對 tempo 標記嚴格性的差異：

| 學派 | 對作曲家 tempo 標記的態度 |
|---|---|
| **HIP / Urtext** | 嚴格遵守（如 Beethoven 標 metronome 必須照彈）|
| **浪漫派傳統** | 較自由，rubato 廣泛使用 |
| **20 世紀大師** | 折衷 — 信標記但允許 micro 變化 |

對指法系統的意涵：tempo 變化（rubato）會影響 articulation 物理可行性。但這是演奏層面，不應強求 DP 模型化。

## 7. 對 score-claude DP 的影響預測

目前不看 tempo，未來引入 tempo-aware rule 後預期：

| 曲目 / 段落 | 預期變化 |
|---|---|
| Bach Inv Allegro 段 (16th-note runs) | substitution rule 自動跳過（已透過 duration gate 達到） |
| Mozart Andante (slow movement) | 更廣泛 substitution 啟用 |
| Chopin Op.9-2 lyrical melody (slow) | 強烈 substitution（目前已啟用）|
| Chopin Etude Op.10 No.4 (Presto) | substitution 完全跳過、thumb-pass 嚴格限制 |

## 8. 與其他 wiki 頁面的關係

- [concept_legato_substitution](concept_legato_substitution.md) §6 — duration gate 是 tempo-aware 的隱含實作
- [concept_staccato](concept_staccato.md) §1 — 速度與 staccato 變體的物理對應
- [src_matthay_visible_inaudible](src_matthay_visible_inaudible.md) §2.3 — 速度-重量觸鍵不相容的物理基礎
- [../wiki_piano/concept_thumb_technique](../wiki_piano/concept_thumb_technique.md) — thumb-pass 與速度的關係
- [../wiki_piano/analysis_common_fingering_injuries](../wiki_piano/analysis_common_fingering_injuries.md) — 快速段 thumb-pass 與 focal dystonia 風險

## 9. ⚠ Training-data verification queue

- §2 Matthay 速度-重量不相容原則的具體章節引述
- §3 各 tempo 下 substitution 物理時間限制的具體 study
- §4 thumb-cross 在快速段的 focal dystonia 學術論述（Altenmüller 之外的支持）
