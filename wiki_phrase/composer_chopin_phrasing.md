# Composer: Chopin 樂句 — 按 genre 細分

> 來源：[[concept_chopin_lyrical_phrase]] 基底 + Rosen《The Romantic Generation》Chopin 章節、Eigeldinger《Chopin Pianist and Teacher》、標準 Chopin 演奏文獻
> 涵蓋 PIG：Chopin 23 曲（最大 composer bloc）
> 狀態：第一版 2026-05-26
> 引用方：[[concept_chopin_lyrical_phrase]] (反向引用 — 細分版本)

## 1. 為什麼 Chopin 要按 genre 細分

[[concept_chopin_lyrical_phrase]] 涵蓋通則（不規律長度、禁用 4-bar fallback、texture 訊號），但 Chopin **每個 genre 的樂句邏輯不同**：
- Nocturne 與 Ballade 的 lyrical 句子長度截然不同
- Etude 的 figural unit 與 Mazurka 的舞曲節奏完全不可比
- Polonaise 的 march-like 規律 vs Scherzo 的對比性切換

→ 必須 per-genre 處理。

## 2. PIG 23 首 Chopin 大致分類（待逐曲確認）

從 label 推測：

| Genre | 預期數 | 代表 PIG ID |
|---|---|---|
| Nocturne | 4-5 | 023 (Op.9-2), 其他待查 |
| Etude | 5-7 | 022 (Op.10-3 Tristesse), 024 (Op.10-4) |
| Ballade | 2-3 | 021 (Ballade No.2) |
| Mazurka | 2-3 | 待查 |
| Waltz | 2-3 | 075 (Op.64-2 c# minor) |
| Prelude | 2-3 | 待查 |
| Polonaise / Scherzo / Impromptu | 1-2 | 待查 |

## 3. 各 genre 樂句特徵

### 3.1 Nocturne (夜曲)
- **樂句單位**：典型 4-bar 或 8-bar 內含長 bel canto 旋律線
- **特色**：RH melodic 主導，LH 持續分解和弦伴奏（waltz-like 1+2+3）
- **邊界訊號**：
  - LH harmonic 循環的 reset 點（每 4-8 bar）= 強樂句邊界
  - RH 旋律到 高點/低點後接休止 = 樂句結尾
  - 中段華彩 (fioritura) 後的 strong 音 = 新樂句起點
- **避免**：把 fioritura（裝飾華彩）切成獨立樂句 — 它屬於前句尾
- **代表**：023 Op.9-2 Eb major (12-bar 主題 = 兩個 4-bar phrase + 4-bar 結尾變奏)

### 3.2 Etude (練習曲)
- **樂句單位**：technical pattern 變奏，常 8-16 bar 一個 figural unit
- **特色**：以單一 figural pattern (arpeggio / scale / double-note / etc) 變奏發展
- **邊界訊號**：
  - **Pattern change** = 樂句邊界（如 arpeggio → octave、ascending → descending）
  - **Register shift** ≥ 1 octave = 邊界
  - 中段 contrasting episode (對比段) = 大段落邊界
- **避免**：盲套 melodic 樂句邏輯 — etude 沒有 melodic 中心，是 figural
- **代表**：
  - 022 Op.10-3 "Tristesse" — 例外！這首是 lyrical etude，套 Nocturne 邏輯
  - 024 Op.10-4 — 標準 figural etude

### 3.3 Ballade (敘事曲)
- **樂句單位**：大型 narrative arc，內含多個 subsection
- **特色**：sonata-like 結構但更自由；常含 storytelling tempo / texture 切換
- **邊界訊號**：
  - 大段落 tempo 切換（如 Andantino → Presto）= strong reset
  - Key 變化（特別轉到關係調 / 平行調）= 邊界
  - Texture 主導變化（如 melodic chord → octave passage）= 邊界
- **避免**：把長 narrative 段強分成 4-bar phrases
- **代表**：021 Ballade No.2 F major

### 3.4 Mazurka (馬祖卡)
- **樂句單位**：3/4 拍 dance phrase, typically 4 + 4 bar
- **特色**：強拍常落在第 2 或 3 拍（不在第 1 拍）— 與標準古典 metric 不同
- **邊界訊號**：
  - 4-bar period 結構（更規律於其他 genre）
  - 重音模式 reset = 邊界
- **避免**：用標準 metric accent 推斷邊界 — mazurka 重音特殊

### 3.5 Waltz (圓舞曲)
- **樂句單位**：3/4 拍 dance phrase, typically 8-bar period
- **特色**：LH 1+2+3 oom-pah-pah pattern 持續穩定
- **邊界訊號**：
  - LH pattern 持續時 = 同樂句
  - LH harmonic 循環結尾 = 樂句邊界
  - Tempo / character 切換（如 valse triste → contrasting trio）= 大段落
- **代表**：075 Op.64-2 c# minor (slow waltz, 內含 contrasting middle section)

### 3.6 Prelude (前奏曲)
- **樂句單位**：高度變化 — 從 16-bar miniature 到 80+ bar 大型
- **特色**：Op.28 24 首各曲 character 完全不同（從風暴的 Op.28-16 到 lyrical 的 Op.28-15）
- **邊界訊號**：完全 per-prelude 處理；無通則
- **建議**：每首 prelude 單獨 `analysis_chopin_prelude_op28_N.md`

### 3.7 Polonaise / Scherzo / Impromptu (其他)
- Polonaise：march-like 規律 ~8-bar phrase + 持續 polonaise rhythm
- Scherzo：強對比段落切換（A-B-A-Trio-A）；段落內常 sentence-like
- Impromptu：表面即興、內部仍有 ABA' 或 sonata-like 框架

## 4. Chopin 樂句邊界訊號優先序（總結）

| 訊號 | 適用 genre | 信心度 |
|---|---|---|
| LH pattern / harmonic change | Nocturne, Waltz, Ballade | ⭐⭐⭐ |
| Pattern (figural) change | Etude | ⭐⭐⭐ |
| Tempo marking 變化 | Ballade, Scherzo, Impromptu | ⭐⭐⭐ |
| Key signature 變化 | All | ⭐⭐⭐ |
| Register reset ≥ 1 octave | All | ⭐⭐ |
| Fioritura 後的 strong 音 | Nocturne, Ballade | ⭐⭐ |
| Mazurka strong-beat shift | Mazurka only | ⭐ (genre-specific) |
| 4-bar 週期 | **僅 Mazurka / Waltz**；其他禁用 | ⭐ |

## 5. 為何「禁用 4-bar fallback」對 Chopin 特別重要

Chopin 樂句長度統計分佈（合成估計）：
- Nocturne：6, 8, 10, 12, 16 bar 都常見
- Etude：8, 16, 24, 32 bar (圖案變奏導向，長度遠超 4)
- Ballade：narrative segments 可達 40-80 bar
- Waltz / Mazurka：4-8 bar 較規律（**4-bar fallback 可用**）

`_detect_phrase_starts` Pass 3 的 4-bar 週期 fallback 對 Nocturne / Ballade / Etude **系統性錯**。對 Waltz / Mazurka 可用。

→ 實作上需要 **per-genre dispatcher**，這牽涉「曲目 metadata」（從 label 或 file path 推 genre）。

## 6. PIG 驗證候選清單

按 ROI（PIG 影響 × 概念覆蓋度）排：

1. **023 Op.9-2 Nocturne** — Nocturne 代表
2. **024 Op.10-4 Etude** — figural etude 代表
3. **021 Ballade No.2** — 大型 narrative 代表
4. **075 Op.64-2 Waltz** — Waltz 代表
5. 其他 Chopin PIG 待逐一研究

## 7. 與其他 wiki 頁面的關係

- 父頁 [[concept_chopin_lyrical_phrase]]：通則
- 對應 [[concept_classical_period_sentence]]：Chopin **不**套此模板（過於規律）
- 工具頁 [[concept_cadence_detection]]：Chopin 用 weakened cadence variants
- 工具頁 [[concept_subject_imitation_detection]]：Chopin **不**適用（非對位）
- 待寫：
  - [[analysis_chopin_op9_no2_nocturne]]
  - [[analysis_chopin_ballade_no2]]
  - [[concept_dance_metric_accent]] — Mazurka / Waltz / Polonaise 節奏共通

