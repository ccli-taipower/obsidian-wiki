# Composer: Grieg 樂句 — Lyric Pieces 系列為主

> 來源：通用音樂理論 + 標準 Grieg 研究 (Benestad & Schjelderup-Ebbe)
> 涵蓋 PIG：Grieg 10 曲（推測多為 Lyric Pieces 系列）
> 狀態：種子頁，第一版 2026-05-26
> 驗證樣本：待 PIG label 確認

## 1. Grieg 樂句 = 規律 4-8 bar + 北歐 modal + 微型結構

Grieg (1843-1907) 屬北歐民族樂派，鋼琴作品以 *Lyric Pieces* (Op.12 起到 Op.71，10 冊共 66 首) 為核心。風格特徵：

- **短小精煉**：每首 lyric piece 多為 1-5 分鐘
- **規律樂句**：4-bar 或 8-bar period 結構為主
- **北歐 modal 元素**：Lydian #4、Dorian raised 6 等教會調式 + 民間音階
- **明確 ternary / binary 形式**：A-B-A 或 A-B 段落清楚
- **persistent ostinato bass**：模擬北歐民俗樂器 (hardingfele 等)

對指法系統的意涵：**樂句偵測相對容易** — 古典規則 + 4-bar 週期大致可用。新挑戰是 modal scale 對指法選擇的影響。

## 2. Grieg 樂句的四大特徵

### 2.1 規律 4 / 8-bar Period 結構

Lyric Pieces 多採用對稱 period（antecedent + consequent），長度典型 4+4 或 8+8。

**操作型偵測**：現有 `_detect_phrase_starts` Pass 3 的 4-bar 週期 fallback 對 Grieg **大致正確**。

### 2.2 Modal Inflections (調式色彩)

Grieg 不嚴格遵守大小調 — 常使用：
- **Lydian raised 4**：F# 在 C major 環境
- **Dorian raised 6**：B♮ 在 D minor 環境
- **Pentatonic** 片段（北歐民歌風）

**對樂句影響**：modal 不像大小調有明確 V-I cadence；樂句結尾常停在 modal final 而非 tonic。Cadence 偵測需放寬。

### 2.3 LH Drone / Ostinato Bass

很多 Lyric Pieces 的 LH 是持續 drone (五度音程持續) 或 ostinato pattern（反覆 4-8 bar 不變）。

**對樂句偵測**：
- LH 不變 → **不**作為樂句訊號（古典規則中 LH pattern change 是訊號，這裡反例）
- RH 自由發展 → 樂句邊界全靠 RH melodic 結構
- Pattern 結束 / 切換到新 pattern → 段落邊界（A→B 切換）

### 2.4 Ternary / Binary 形式為主

A-B-A 結構主導，**段落切換**清楚（中段常完全停頓或 tempo 切換）。Sonata-allegro 等大型結構少見。

**操作型**：段落邊界用 tempo / dynamic / texture 訊號偵測，內部樂句用 4-8 bar 規律。

## 3. PIG 10 首 Grieg 曲

從 label 推測多為 Lyric Pieces 集（待 PIG 細看確認）：
- 081-090 範圍待 PIG label 確認
- 著名 Lyric Pieces 候選：Wedding Day at Troldhaugen Op.65/6、Notturno Op.54/4、March of the Dwarfs Op.54/3、Arietta Op.12/1、Butterfly Op.43/1 等

## 4. Grieg 樂句邊界偵測啟發式（草案）

```
grieg_phrase_detector(groups, hand):

1. 套用 [[concept_classical_period_sentence]] 基底：
   - 啟用 4-bar 週期 Pass 3 fallback（適合 Grieg）
   - period (4+4 / 8+8) 為主結構

2. Grieg-specific 調整：
   a. LH 若是 drone / ostinato (連續 ≥ 8 chord 同 pattern)：
      → LH 不參與樂句訊號
      → 樂句邊界全靠 RH melodic 結構
   b. Modal cadence (停在非 tonic 的 modal final)：
      → 接受為樂句結尾（弱化 V-I 偏好）
   c. 段落邊界：tempo / dynamic / pattern 切換 → strong boundary

3. Lyric Pieces 形式判斷：
   - A 段：第 1 個段落，4-32 bar
   - B 段：中段，常與 A 對比 (tempo / mode / texture)
   - A' 段：A 再現，常簡化
   - 每段內部依 1+2 規則切樂句
```

## 5. PIG 驗證樣本

待 PIG 10 首 Grieg label 細看後選 1-2 首作為代表。候選優先：
- **Wedding Day at Troldhaugen** (若有)：A-B-A-Coda，A 段 march-like 規律、B 段 lyrical
- **Arietta Op.12/1**：最早期 Lyric Pieces，最簡潔的 period 結構

## 6. 與其他 wiki 頁面的關係

- 主要繼承 [[concept_classical_period_sentence]] 基底
- 借用 [[../wiki_piano/src_chinese_style_piano]] 的五聲音階指法（Grieg pentatonic 段落共用）
- 不同於 [[concept_chopin_lyrical_phrase]]：Grieg 樂句**較規律**，不需要禁用 4-bar fallback
- 待寫：
  - [[concept_modal_cadence_detection]] (modal final 而非 tonic 的 cadence 處理)
  - [[concept_drone_bass_pattern]] (drone / ostinato 對樂句偵測的影響)

## 變更日誌
- 2026-05-26: 創立。Grieg Lyric Pieces 特化頁。規律結構 + modal 色彩 + drone bass。
