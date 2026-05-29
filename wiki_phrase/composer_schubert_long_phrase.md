# Composer: Schubert 樂句 — 長線條 + Lied 結構 + 頻繁轉調

> 來源：通用音樂理論 + 標準 Schubert 研究 (Cone, Newbould, Rosen《The Romantic Generation》)
> 涵蓋 PIG：Schubert 5 曲
> 狀態：種子頁，第一版 2026-05-26
> 驗證樣本：PIG 111 Impromptu Op.90 No.3

## 1. Schubert 樂句 = 古典模板 + Lied 旋律 + 浪漫式轉調

Schubert 處在古典 (學徒於 Beethoven 風格) 與浪漫 (Lied 之父) 的接縫上：

- **形式上**：仍依古典 period / sentence（早期作品尤其）
- **旋律上**：受 Lied (藝術歌曲) 影響，melodic line 長且 vocal-style
- **和聲上**：浪漫派式的**遠系轉調**（如 C major → A♭ major），轉調點往往就是樂句邊界
- **節奏上**：常用三連音、附點節奏推動長樂句

對指法系統的意涵：**古典規則 + 浪漫派 cadence 弱化 + 額外的轉調訊號**。

## 2. Schubert 樂句的四大特徵

### 2.1 Lied-style Long Melodic Line

Schubert 600+ 首藝術歌曲塑造了他的旋律習慣 — 即使在純器樂作品（如 Impromptus、Sonatas、Moments Musicaux），主旋律仍以「能唱出來」為設計原則。

**特徵**：
- 樂句長度典型 8-16 bar，少有 4-bar 短句
- 旋律弧線清晰（上升 → 高點 → 下降解決）
- 樂句結尾常有「呼吸」（休止半拍-1 拍）

**操作型偵測**：
- 連續無休止的長旋律段落（≥ 8 bar） → 整段為一個樂句
- 高點後的下行 + 休止 → 樂句結束訊號

### 2.2 三連音 / 附點節奏推動

Schubert 鋼琴作品 (尤其 Impromptus, 11 Moments Musicaux) 大量使用：
- LH 三連音（如 Op.90 No.3）— 連續流動的伴奏紋理
- RH 附點節奏 + 大跳 — 抒情主題的標誌

**對樂句偵測**：LH 三連音 pattern 連續不變時，**不切樂句**；pattern 改變（如三連音→八分音符）才是樂句邊界。

### 2.3 遠系轉調 (Modulation to Distant Keys)

Schubert 的標誌性手法是突然轉到**遠系調**（mediant, submediant, flat side）：
- C major → E major (chromatic mediant)
- A♭ major → E major (enharmonic)
- 小三度關係的調性切換

**樂句意涵**：轉調點幾乎必為樂句邊界（情緒切換）。

**操作型偵測**：偵測 key signature 變化（Audiveris 可抽 `<key>` 元素），或 chord 分析發現遠系和弦突然出現。

### 2.4 形式仍偏古典

不像 Chopin 那麼自由 — Schubert Sonatas / Impromptus 多為 ternary (ABA), sonata-allegro, theme + variations 等古典形式。**段落邊界**清楚。

## 3. PIG 5 首 Schubert 曲

從 label 推測：
- 111 Impromptu Op.90 No.3 (G♭ major) — 長 lyrical, LH 三連音
- 112 Impromptu Op.90 No.4 (A♭ major)
- 113 Wanderer Fantasy (C major, D.760)
- 114, 115 待 PIG 確認

## 4. Schubert 樂句邊界偵測啟發式（草案）

```
schubert_phrase_detector(groups, hand):

1. 用 [concept_classical_period_sentence](concept_classical_period_sentence.md) 基底（仍偏古典）

2. 改寫 fallback：
   - 禁用 4-bar 週期 → 改用 8-bar (Schubert 偏長樂句)
   - 若連續 ≥ 16 bar 無樂句邊界，啟用 8-bar fallback

3. 加 Schubert-specific 訊號：
   a. Key signature 變化 → 強樂句邊界 ⭐⭐⭐
   b. LH pattern 變化（如三連音 → 八分） → 強邊界 ⭐⭐⭐
   c. 連續長音 (≥ 2 bar 上方聲部) → 樂句結尾 ⭐⭐
   d. 大段休止 (≥ 1 bar) → 強邊界 ⭐⭐⭐ (Beethoven 共享)

4. Cadence 偵測：
   - PAC / IAC 仍可用（古典殘留）
   - 但接受「PAC 後 1-2 bar 延展」(cadential extension) 為同樂句
```

## 5. PIG 驗證樣本

### 111 Impromptu Op.90 No.3 (G♭ major)
- 長 lyrical 主題，RH 高音域長線條
- LH 持續三連音 arpeggio (waltz-like)
- 結構：A-B-A-Coda
- A 段：~16 bar，含一個內部 PAC 在 bar 8
- B 段：轉到 e♭ minor (小三度遠系)，texture 變密集
- **預期收穫**：(1) A 段內部 bar 8 是次要邊界、bar 16 才是強樂句結束；(2) A→B 轉調點是強邊界

### 113 Wanderer Fantasy (C major)
- 大型四樂章相連 fantasia
- 樂章間無明確休止 → 跨段樂句邊界要靠 tempo / key / texture
- **預期收穫**：樂章邊界是 strong reset；樂章內依 sonata-allegro 規則切

## 6. 與其他 wiki 頁面的關係

- 主要繼承 [concept_classical_period_sentence](concept_classical_period_sentence.md) 基底
- 借用 [concept_chopin_lyrical_phrase](concept_chopin_lyrical_phrase.md) 的「不規律長度」與「LH pattern 切換」訊號
- 不同於 [composer_beethoven_phrasing](composer_beethoven_phrasing.md)：Schubert 較少 phrase expansion / compression
- 待寫：
  - [concept_modulation_as_phrase_signal](concept_modulation_as_phrase_signal.md) (轉調作為樂句訊號的細化)

