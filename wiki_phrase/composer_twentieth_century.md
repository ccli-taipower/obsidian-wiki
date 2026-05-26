# Composer: 二十世紀 / 現代 — Scriabin + Bartok

> 來源：通用音樂理論 + Persichetti《Twentieth-Century Harmony》、Salzman《Twentieth-Century Music: An Introduction》、Scriabin 與 Bartok 各自研究文獻
> 涵蓋 PIG：Scriabin 2 (144, 145) + Bartok 1 (147) = 3 曲
> 狀態：第一版 2026-05-26

## 1. 為什麼把 Scriabin + Bartok 合一頁

兩者在 PIG 數量都少 (Scriabin 2, Bartok 1) 但風格差異大。合一頁是因為共通**音樂分析挑戰**：

- 傳統 V-I cadence 退化 (Scriabin) 或不存在 (Bartok)
- modal / atonal / synthetic scale 為主，標準 finger grouping 不適用
- Phrase 結構不規律，依**和聲色彩**或**節奏 cell** 而非 melodic line

兩者一起處理可以建立「post-tonal phrasing」一般原則。

## 2. PIG 3 首細節

| ID | 曲目 | 作曲家時期 | 特徵 |
|---|---|---|---|
| 144 | Scriabin Piano Sonata No.2 1st mov | 晚期浪漫 (1897) | tonal but extended chromaticism |
| 145 | Scriabin Piano Sonata No.5 | 過渡期 (1907) | mystic chord introduction |
| 147 | Bartok Romanian Dance No.1 | 二十世紀 (1909) | folk-derived, modal, asymmetric |

## 3. Scriabin (1872-1915)

### 3.1 風格演變
- 早期 (Op.1-30, ~1890-1900)：Chopin 影響強，extended tonality
- 中期 (Op.30-50, 1900-1907)：和聲愈漸複雜，dominant chord 變形
- **晚期 (Op.50+, 1907-1915)**：mystic chord (C-F♯-B♭-E-A-D)，**完全脫離 functional harmony**

### 3.2 PIG 144 (Sonata No.2, 1897)
- 早期作品，仍 tonal
- Lyrical 樂句，類似 Chopin
- → 可套 [[concept_chopin_lyrical_phrase]] 規則

### 3.3 PIG 145 (Sonata No.5, 1907)
- 過渡期，mystic chord 開始出現
- Cadence 訊號弱化（傳統 V-I 仍偶見但被擴張和聲掩蓋）
- 樂句邊界靠 texture + dynamic + tempo marking（類似印象派）
- → 部分套 [[concept_impressionist_phrasing]] 規則

### 3.4 樂句邊界訊號 (Scriabin)
| 訊號 | 早期 (Op.1-30) | 中後期 (Op.30+) |
|---|---|---|
| Cadence (V-I) | ⭐⭐⭐ | ⭐ |
| Tempo marking | ⭐⭐⭐ | ⭐⭐⭐ |
| Dynamic shift (Scriabin 大量用) | ⭐⭐⭐ | ⭐⭐⭐ |
| Texture change | ⭐⭐ | ⭐⭐⭐ |
| Theme-based (motif repeats) | ⭐⭐ | ⭐⭐ |

## 4. Bartok (1881-1945)

### 4.1 風格
- Folk-derived modal melodies (Hungarian, Romanian, Slovak 民間音樂研究)
- **Asymmetric meter** (5/8, 7/8, 9/8 不等分節奏)
- Bi-modality (同時兩個 tonal centers)
- Percussive piano writing
- Mikrokosmos 系列為教學標準

### 4.2 PIG 147 (Romanian Dance No.1, 1909)
- 早期作品，仍可辨 tonal centers
- Modal (常 Dorian / Mixolydian)
- 節奏為 phrase 主軸 — **節奏 cell 重複** = phrase 單位
- 樂句邊界 = 節奏 cell 結束 或 tempo / dynamic 切換

### 4.3 樂句邊界訊號 (Bartok)
| 訊號 | 信心度 | 備註 |
|---|---|---|
| **Rhythmic cell 結束** | ⭐⭐⭐ | 一個 N-beat unit 重複 K 次後切換 |
| **Tempo marking 變化** | ⭐⭐⭐ | Bartok 大量用 |
| **Modal final stop** | ⭐⭐ | 停在 modal 主音長音 |
| **Meter change** (5/8 → 7/8 等) | ⭐⭐⭐ | 偶見，是 strong 邊界 |
| Cadence (傳統 V-I) | ❌ | 不適用 |
| 4-bar 週期 | **禁用** | Bartok 節奏不規律 |

## 5. 二十世紀通則

從 Scriabin 晚期 + Bartok 中期開始，phrase 邊界依賴：

1. **Tempo / dynamic marking** — 樂譜直接標示，最可靠
2. **Texture / rhythm cell 變化** — 結構性訊號
3. **Motivic repetition** — 即使 atonal 也常用 motif 連貫
4. **Meter change** — strong reset
5. **Performer / 編者 phrase mark** — 二十世紀作曲家常用 explicit phrase markings

**不再可靠**：cadence 偵測、key signature change（modal/atonal context）

## 6. 對指法系統的影響

- DP 的 W_PHRASE_ANCHOR 仍有效（手位中央化是通則）
- thumb-reservation 規則：需 mode-aware（pentatonic Bartok 段落不適用 — 見 [[concept_modal_scale_fingering]]）
- 節奏 cell 偵測尚未有概念頁 — 是未來 wiki 缺口

## 7. PIG 驗證候選

對 3 首 PIG 都應該獨立 analysis：
- **144** Scriabin Sonata 2-i: lyrical, 套 Chopin rules
- **145** Scriabin Sonata 5: 過渡期，部分 impressionist + 部分 chromatic
- **147** Bartok Romanian Dance 1: 節奏為主，dance phrase 邏輯

## 8. 與其他 wiki 頁面的關係

- 借用 [[concept_chopin_lyrical_phrase]] (Scriabin 早期)
- 借用 [[concept_impressionist_phrasing]] (Scriabin 晚期)
- 借用 [[concept_modal_scale_fingering]] (Bartok modal scales)
- 待寫：
  - [[concept_rhythmic_cell_detection]] (Bartok / Stravinsky 節奏 cell)
  - [[concept_asymmetric_meter]] (5/8, 7/8 對 phrase 的影響)

## 變更日誌
- 2026-05-26: 創立。Scriabin + Bartok 合一頁。PIG 覆蓋從 ~92% 推到 ~94%。
