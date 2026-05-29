# Concept: Legato Substitution — 連奏段的同音換指偏好

> 來源：Neuhaus *The Art of Piano Playing* §觸鍵章、Matthay *The Visible and Invisible* §legato chapter、Czerny Op.500 Vol.III §legato touch、Türk *Klavierschule* (1789)、Kullak *Die Ästhetik des Klavierspiels*
> 引用方：[[concept_articulation_overview]] §4、[[index]]

## 1. 為什麼 legato 段要 favor finger substitution

物理上 legato = 「前指還按 → 後指彈下 → 前指鬆」**重疊期 ≥ 1 ms**。當旋律線需要在同一音上維持 legato，**沒有 finger substitution 就無法達成**：

- 旋律從 C5 → C5（同音）→ B4
- 不換指：f5 彈 C5 → 鬆 → f5 再彈 C5 → 無 overlap，audibly broken
- 換指：f5 彈 C5 → f4 接住 C5 → f5 鬆 → f4 鬆 + f3 彈 B4 → 全 legato ✓

→ 在 legato 段，**同音換指不只是允許，是必要**。

對於非同音的 legato 段，substitution 也常用於「reset 手位」維持連續性 — 例如八度跨越時用 4-3 substitution 為 thumb-pass 準備手位。

## 2. Pedagogical 文獻共識

### Neuhaus《The Art of Piano Playing》§連奏觸鍵
> 「legato 的真實意義不是『不分開』，而是『前一個音的釋放與後一個音的進入發生在同一瞬間』。為達此目的，finger substitution 是不可或缺的技術。」

Neuhaus 明確把 substitution 列為 legato 的「**技術基礎之一**」，不是可選技巧。

### Matthay《The Visible and Invisible》§legato touch
> 「在持續 melody line 中，同一根手指不能既彈下又釋放給後續音，因為釋放動作本身會中斷聲音持續。Substitution 是樂手的解決方案。」

Matthay 從觸鍵物理（不可同時兼任「彈下」與「釋放」）論證 substitution 必要性。

### Czerny《Op.500》Vol.III §legato touch
> 「Legato 段中，凡是同音重複，應使用 finger change（同音換指）；凡是接續長線條，應預備性地用 substitution 為下個 hand-position 鋪路。」

Czerny 把 substitution 分為兩類：
1. **同音換指 (same-pitch substitution)** — 對重複音；本頁主題
2. **預備性換指 (preparatory substitution)** — 為下個 hand position 鋪路；見 §6

### 18-19 世紀理論共識
- Türk *Klavierschule* (1789) — 已提到 substitution 是「成熟演奏者必備」
- Kullak《Die Ästhetik des Klavierspiels》§連奏 — 同 Neuhaus 觀點

→ 自 18 世紀末以來 substitution 在 legato 段是**標準教學**，不是個人風格選擇。

## 3. 操作型定義

對於指法決策，legato substitution 的判斷條件：

| 條件 | 操作型 |
|---|---|
| **訊號** | 兩個相鄰音都在同一個 slur 範圍內（或都有 legato 標記）|
| **同音** | MIDI pitch 完全相同 |
| **足夠時長** | 兩音的 duration 都 ≥ eighth note (≥ 0.5 QN)。快速 16 分 / 32 分音符物理上不允許 substitution（見 §6）|

滿足全部三條件，下個音應使用**不同於前音**的手指（即 substitution）。

## 4. 預備性換指 (preparatory substitution)

Czerny 提到的第二類 substitution：為下個 hand position 鋪路。

例：上行 octave scale C → D → E → F → G → A → B → C：
- 標準指法 1-2-3-1-2-3-4-5 (with thumb cross at F)
- 在 F 那個 thumb cross 之前，若上一句末是 C5(f3)，可以**預備性** substitution 把 f3 換成 f4 給下一段更好 hand position

這類換指不限於同音，可以發生在任何 hand-position 轉換點。它的目標是「下個 hand position 的 readiness」，而不是「保持 legato 連續性」。

## 5. 適用情境

| 情境 | 適用 |
|---|---|
| 浪漫派 lyrical melody（Chopin Nocturne / Schumann *Träumerei* 等）| ✓ 高度適用 |
| Classical *cantabile* 段（Beethoven Op.49 No.2 mvt2 / Mozart slow movements）| ✓ 適用 |
| Baroque suite slow movement（Bach French Suite *Sarabande* 等）| 部分適用（看 edition slur 標記）|
| Bach 2-voice Inventions（fast 對位）| ✗ 通常不適用（Baroque default 是 non-legato）|

## 6. 失效情境 / 不適用 case

| 情境 | 為何不適用 |
|---|---|
| **快速 passage**（≥ Allegro tempo 的 16th-note runs）| Substitution 來不及執行，反而要 hand-position-stable |
| **Baroque non-legato 段** | 預設不應觸發 substitution；過度套用會誘導 unnecessary finger changes |
| **Trill / mordent / ornament** | Ornament 內部 fingering 由獨立規則處理，substitution rule 不適用 |
| **Chordal texture** | 和弦 voicing 由單獨 cost 處理，substitution 不適用於 simultaneous attack 的和弦 |

## 7. 與其他 wiki 頁面的關係

- [[concept_articulation_overview]] — 本頁的 parent 概覽
- [[concept_staccato]] — 互補頁，staccato 段做的事相反（鼓勵 hand jump、無 substitution 需要）
- [[concept_non_legato_baroque]] — 為何 Baroque 不應該預設啟用此規則
- [[../wiki_piano/concept_thumb_technique]] — substitution 與 thumb cross 的互動
- [[../wiki_piano/concept_finger_span_table]] — substitution 改變了「下一步」的 hand position
