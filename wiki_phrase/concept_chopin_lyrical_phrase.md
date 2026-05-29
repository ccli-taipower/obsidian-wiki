# Concept: 浪漫派抒情樂句 — Chopin 為核心

> 來源：通用音樂理論知識 + Rothstein《Phrase Rhythm in Tonal Music》(1989) 為標準參考、Schenker analyses of Chopin
> 涵蓋 PIG：Chopin 23 + Schumann 6 + Liszt 3 + Brahms 3 + Mendelssohn 3 + Tchaikovsky 1 = **39 曲 (26%)**
> 狀態：種子頁，第一版 2026-05-26
> 驗證樣本：PIG 023 Chopin Nocturne Op.9 No.2

## 1. 為什麼這頁對指法系統重要

浪漫派樂句**最容易讓現有偵測器系統性出錯**：

- ❌ 樂句長度**不規律**：5、6、7、9、11 bar 常見，4-bar 週期假設**錯**
- ❌ 樂句邊界常**不在小節線**上：旋律延伸跨小節線，rubato 呼吸點在弱拍
- ❌ Phrase elision 比古典時期**更常見**：一句的 PAC 落點同時是下句的開頭音
- ❌ Cadence 訊號**減弱**：擴張和聲、半音進行、避免根位 V-I 為美學
- ✅ 但有新訊號：texture / accompaniment pattern 變化、dynamic 收束、register reset、明確的 *respira* 或 comma 記號

當前 `_detect_phrase_starts` 的 Pass 3 (4-bar 週期) 對 Chopin 是**反指標** — 強行 4-bar 切會把長線抒情樂句腰斬，導致該樂句內的指法被切成兩半最佳化。

## 2. 浪漫派樂句的五大特徵

### 2.1 長線條 (Long-Breathed Melodic Line)

Chopin、Schumann、Brahms 都繼承 bel canto 聲樂傳統 — 樂句以「一口氣能唱完」為自然單位，長度可達 8、12、16 bar。

**操作型偵測**：
- 連續無休止符 / 無長音 (≥ 1 拍以上靜止) 的旋律段落
- 動態 marking（如 `<` crescendo, `>` decrescendo）作為樂句弧線指示
- 主聲部 (soprano) 連續移動 ≥ 8 bar 而無明確收束 → 暗示這是一個長樂句

### 2.2 樂句長度不規律 (Irregular Phrase Lengths)

Rothstein 統計浪漫派常見樂句：5、6、7、9、11 bar 都不少於 4 / 8 bar。常見原因：
- **Phrase expansion**：標準 4 bar 透過 sequence、 deceptive cadence 延長
- **Phrase compression**：兩個樂句的 elision 使聯合長度 < 期待
- **Free fantasia 風格**：完全無規律，依和聲與旋律邏輯走（如 Chopin Ballade 中段）

**操作型對應**：禁用 `_detect_phrase_starts` Pass 3 的 4-bar fallback；改為依「下一個 strong cadence 或 strong texture change」決定樂句邊界。

### 2.3 Phrase Elision (樂句重疊)

一句結尾的下行解決音 = 下句起始音。例如：
- A 句 V→I (PAC) 落在 bar 8 第 1 拍的 C 音
- B 句 ALSO 從 bar 8 第 1 拍的 C 音起跑

對指法系統：這個 C 音**屬於哪一句**？答案：兩句都屬於。實務上應視為「A 句的 phrase boundary 在 bar 8 第 1 拍**前**」、「B 句從 bar 8 第 1 拍起」— 即邊界 idx 落在該音之前的 transition 點。

### 2.4 Rubato Breath Marks (呼吸記號)

部分浪漫派樂譜直接標 *respira* (Italian) 或 `,` (comma) 表示樂句呼吸點。對 OMR 抽取：
- Audiveris 是否抽取 textual marking? **目前未確認** — 需要驗證
- 若可抽取，這是 phrase boundary 的 **ground truth** 級別訊號
- 若不可抽取，仍可從動態 marking 與 fermata 推斷

### 2.5 Texture / Accompaniment Change

伴奏音型變化常常標示樂句邊界。例如：
- Alberti bass → 厚和弦（古典→浪漫風格切換點）
- Arpeggio 上行 → 持續八度
- Single line → 雙重旋律
- LH 音域突然下移 / 上移

對指法系統：**LH texture change 是 RH 樂句邊界的 secondary 訊號**（兩手協同變化）。

## 3. Cadence 偵測在浪漫派的退化

古典派 cadence 訊號（V-I 根位）在浪漫派被刻意削弱：

| 古典 cadence | 浪漫等價物 | 偵測信心 |
|---|---|---|
| V-I PAC | V7-I（含七和弦張力） | 仍可偵測，⭐⭐⭐ |
| V-vi DC | V-VI / V-iv 各種替代 | ⭐⭐ |
| HC (V) | V9, V13 擴張和聲，常無解決 | ⭐ |
| (新) Half-step descent | 半音下行至 root | ⭐⭐ (浪漫獨有) |
| (新) Plagal IV-I | 教堂風 "amen" 收束 | ⭐⭐ (浪漫 nocturne 常見) |
| (新) Chromatic 進行 | Tritone substitution 等 | ⭐ (Chopin 已用) |

**實務原則**：浪漫派 cadence 偵測**不要靠和聲分析**（不準），改靠**旋律收束**（長音 + 動態收束 + 跟在後面的休止）。

## 4. Chopin 特定的樂句語法

Chopin 風格的樂句訊號比一般浪漫派更具體：

| 訊號 | 描述 | PIG 例 |
|---|---|---|
| **左手分解和弦循環** | LH 持續 4-5 音 arpeggio 循環，循環的 reset 點常是樂句邊界 | 023 Nocturne Op.9 No.2 (waltz-like LH) |
| **裝飾音華彩 (fioritura)** | 在樂句末加長串裝飾音，視為前一樂句的 prolongation；下一個 strong 音才是新樂句 | 023, 多數 Nocturnes |
| **轉調作為樂句訊號** | 中段轉到關係調，調性切換點 = 樂句邊界 | Mazurka, Polonaise, Ballade |
| **Ballade A-B-A 結構** | 大型 ABA 段落切換是 strong reset | Ballade 1-4 |
| **Etude 圖案重複** | Etude 通常是單一 figural pattern 變奏，pattern 切換點 = 樂句邊界 | Op.10 / Op.25 各曲 |

## 5. 浪漫派樂句邊界偵測啟發式（草案）

按優先序：

| 訊號 | 操作型定義 | 信心度 | 古典比較 |
|---|---|---|---|
| 旋律收束（長音 ≥ 2 拍 + 後面 ≥ 0.5 拍靜止） | 現有 `LONG_NOTE_BEATS` + 後面 rest | ⭐⭐⭐ | 強於古典 |
| LH texture / pattern 切換 | LH 在連續 ≥ 4 chord 內音型一致，然後突然變 | ⭐⭐⭐ | **浪漫特有** |
| Register reset (RH 跳 ≥ 1 octave) | 旋律突然跳到新音域 | ⭐⭐ | 同 |
| 裝飾音 (Audiveris 標 `grace`) 後面的 strong 音 | 跟在裝飾華彩後的下一個 metric 強位音 | ⭐⭐ | **浪漫特有** |
| 4-bar 週期 | **禁用** | — | ❌ 古典適用、浪漫**反指標** |

## 6. PIG 驗證樣本與預期收穫

### 023 Chopin Nocturne Op.9 No.2 (E♭ major)
- 12-bar waltz-like 主題，內含 2 個 4-bar phrase + 1 個 4-bar 變奏結尾
- LH 是穩定 1+2+3 waltz pattern，每 4 bar 一個和聲循環
- **預期收穫**：新偵測器應在 bar 4, 8, 12 立邊界（與現有 Pass 3 部分對齊）；但中段華彩 (fioritura) 後的 strong 音應額外被偵測為新樂句起點，這是現有偵測器看不到的

### 022 Chopin Etude Op.10 No.3 "Tristesse" (E major)
- Slow lyrical etude
- RH 是長線條，LH 同步配合
- **預期收穫**：絕對禁用 4-bar 週期 — 主題樂句長度為 8 bar，中段拓展可達 12 bar

### 024 Chopin Etude Op.10 No.4 (C# minor)
- Fast figural etude
- 樂句以 figural pattern 變化為單位，不是melodic
- **預期收穫**：偵測 pattern 變化（如 16-note descending arpeggio → ascending broken chord）作為樂句訊號

## 7. 與其他 wiki 頁面的關係

- 對比 [concept_classical_period_sentence](concept_classical_period_sentence.md)：浪漫派**禁用** period / sentence 模板，但繼承 cadence 概念（弱化版）
- 對比 [concept_fugue](concept_fugue.md)：兩者都不規律，但浪漫派以**melodic 邏輯**為主、fugue 以**subject 邏輯**為主
- 待寫：
  - [composer_chopin_phrasing](composer_chopin_phrasing.md) — Chopin 特化，按 genre (Nocturne / Ballade / Etude / Mazurka / Waltz / Prelude / Scherzo) 細分
  - [composer_schumann_phrasing](composer_schumann_phrasing.md) — Schumann 的 character pieces 與 cycle 邏輯
  - [concept_rubato_phrasing](concept_rubato_phrasing.md) — rubato 對樂句邊界的影響
  - [concept_phrase_elision](concept_phrase_elision.md) — elision 通用處理

