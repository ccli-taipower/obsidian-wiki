# Analysis: Chopin Nocturne Op.9 No.2 in E♭ major

> PIG: 023 (4 annotators)
> 來源：通用 Chopin Nocturne 分析 + Eigeldinger《Chopin Pianist and Teacher》+ Rosen《The Romantic Generation》
> 狀態：第三個 per-piece analysis，2026-05-26
> 引用方：[[composer_chopin_phrasing]] §3.1、[[concept_chopin_lyrical_phrase]] §6、[[concept_phrase_elision]] §5

## 1. 為什麼挑這首

Op.9 No.2 是 Chopin 最知名的 Nocturne，pedagogically 也是最常被分析的浪漫派 lyrical 範例。對 wiki 的價值：

- 驗證 [[concept_chopin_lyrical_phrase]] 的「禁用 4-bar fallback」「LH pattern reset 為樂句訊號」是否實際適用
- 驗證 [[concept_phrase_elision]] 對浪漫派的應用（Op.9-2 中段華彩後常見 elision）
- 與 [[analysis_mozart_k283_first_mov]] 對比：古典 cadence-driven vs 浪漫 texture-driven

## 2. 曲目基本資訊

- **Op.9 No.2** (1830-1832, Chopin 約 22 歲)
- **E♭ major**, 12/8 拍（slow waltz-like）, **Andante**
- 長度：~34 小節 + Coda
- 形式：strophic with variations (主題 + 兩次變奏 + Coda)

## 3. 主題結構

主題為 12 小節 ABA-like 內部結構：

```
A1 (bb. 1-4)   — Antecedent 4-bar phrase (主題首次呈現)
A2 (bb. 5-8)   — Consequent 4-bar phrase (變化反覆)
B  (bb. 9-12)  — Contrasting 4-bar phrase (新材料 + 回 tonic)
```

之後是 variation 1 (bb. 13-24) 與 variation 2 (bb. 25-34) + Coda。

## 4. 兩個 voice 的樂句結構

### 4.1 RH (旋律)
- Long-breathed bel canto line
- 每 4-bar 一個 sub-phrase, 三個 sub-phrase 組成 12-bar period
- 變奏中加 fioritura (華彩, ~bar 16 周邊、bar 24 周邊、Coda)
- **避免**：把 fioritura 切為獨立樂句 — 它是前 sub-phrase 的延伸

### 4.2 LH (伴奏)
- Slow waltz pattern: 1 (bass) + 5 (chord) + 1 (mid)
- 每 4-bar 內含一個和聲循環 (I-V-I 或 I-IV-V-I)
- **強訊號**：LH harmonic 循環 reset 點 = 強樂句邊界
- LH pattern 在 variation 段大致不變（只 melodic 上方變化），所以 LH 不是 variation 內部樂句訊號

## 5. 預期樂句邊界

| 位置 | 類型 | 偵測訊號 |
|---|---|---|
| bar 1 | 開頭 | 必然 |
| bar 5 | A2 antecedent → consequent | LH 和聲循環 reset (I-V → IV-V-I) |
| bar 9 | A2 → B (contrasting) | LH key/harmony 切換 + 旋律材料新 |
| **bar 13** | 主題 → variation 1 | **strong reset** (texture density 增加 + RH 開始 fioritura) |
| **bar 25** | variation 1 → variation 2 | strong reset |
| **Coda 開始** | last section | tempo / dynamic 切換 |

## 6. 五類偵測器預期表現

| 偵測器 | 預期 | 信心度 |
|---|---|---|
| **Pass 3 (4-bar fallback)** | 對主題 12-bar 結構**剛好對齊**（bar 5, 9, 13）| ⭐⭐⭐ 適用！|
| **Pass 6 (PAC cadence)** | bar 4 / 8 / 12 結尾的 V-I 可能 fire | ⭐⭐ (擴張和聲可能不命中) |
| **Pass 4 (figural)** | variation 中的 fioritura 可能誤觸發內部邊界 | ⚠ 風險 |
| **thumb-reservation** | 對 LH waltz pattern 起手不適用 (chord, 不是單音 melodic run) | ⭐ low fire rate |
| **Pass 5 (subject imitation)** | A1 → A2 重複可能 fire (TI 內主題重述) | ⭐⭐ |

**特殊發現**：Chopin Op.9-2 是「主題每 4-bar 結構規律 + 整體不規律 (variation 段)」的混合 — Pass 3 對 12-bar 主題剛好有效但對 variation 段可能誤切。

## 7. Fioritura 處理

Variation 1 (bar 13-14, 21-22) 與 variation 2 (bar 24) 與 Coda (bar 33-35) 有 fioritura — 連續 16 音符 / 32 音符的快速裝飾。對偵測：

- **不應**視為樂句邊界 — fioritura 是前一個 melodic note 的 expressive prolongation
- **應**：fioritura 結束後的下個 strong-beat melodic note 是 phrase continuation（不是新樂句）
- 對 [[concept_figural_boundary_detection]]：fioritura 滿足 figural 條件 (連續 stepwise, monotonic), Pass 4 會誤觸發

→ Op.9-2 case 顯示 figural detection 對浪漫派 lyrical 段需要 **fioritura 過濾**。

### 7.1 演算法實測（2026-05-29 full piece validation）

以 musetrainer/library MXL 全曲 (m0-m37, 38 measures) 跑 `_detect_fioritura_ranges` (min_run=6, max_dur=0.25 QN)：

**RH — 11 個 fioritura 範圍**：

| Bars | Notes | First-note dur | 對應 wiki 角色 |
|---|---|---|---|
| m4 | 6 | 0.25 QN | 主題內 ornamental (wiki §7 原版未列) |
| m5 | 6 | 0.25 | 主題內 |
| m5-6 | 18 | 0.25 | 主題收束 ornamental |
| m13 | 6 | 0.25 | **var 1 起手** |
| **m13-14** | **18** | **0.25** | **var 1 核心 fioritura (wiki §7 原本說「bar 16 周邊」實為 m13-14)** |
| m21 | 6 | 0.25 | var 1 重現起手 |
| m21-22 | 18 | 0.25 | **var 1 重現 fioritura** |
| **m24** | **14** | **0.25** | **var 2 fioritura ✓ wiki 預測命中** |
| m26 | 6 | 0.25 | var 2 收束 |
| m29 | 8 | 0.1875 | var 2 內 32-note run |
| **m33-35** | **64** | **0.125** | **Coda 大型 32-note fioritura ✓ wiki 預測命中** |

**LH — 0 範圍**：waltz 三連音伴奏，每組 duration ≥ 0.25 QN → 全 break runs。符合 fioritura filter 設計 (避免誤觸發 accompaniment)。

**Filter 效果**：RH 9 個 figural boundaries 落在 fioritura 範圍內 (m4 / m6 / m13 / m14 / m21 / m22 / m24×2 / m35)，啟用 `USE_FIORITURA_FILTER` 後 Pass 4 不會在這 9 處誤切樂句。

### 7.2 Wiki §7 原預測校正記錄

- 「bar 16 周邊」實際為 **m13-14** (var 1 fioritura 中心) — Op.9 No.2 var 1 從 m13 起跑而非 m16
- 「bar 24」✓ 預測準確
- 「Coda」實際為 **m33-35** (64 連 32-note run) — 符合預期
- 演算法另發現 m4 / m5-6 / m26 / m29 多處 ornamental fioritura，wiki §7 原本未列舉但確實是 fioritura filter 該保護的位置

詳見診斷腳本 `tmp/diag_fioritura_op9_no2_full.py` 與 memory `project_fioritura_filter_2026-05-28.md` 後續更新。

## 8. Elision 觀察

Op.9-2 中段（variation 1, ~bar 14）常有 elision：
- 主題段 bar 12 末 V-I (E♭) 解決
- variation 1 立即從 bar 13 (E♭ tonic) 起跑
- bar 13 的 E♭ 音同時是「主題收尾」與「variation 起手」

→ [[concept_phrase_elision]] 「歸前」原則：bar 12 末歸主題、bar 13 起算 variation。Boundary idx 應在 bar 13 第 1 拍**之前**的 transition 點。

## 9. PIG 4 annotators 預期 disagreement

Chopin 浪漫派指法比 Mozart classical 變異更大（個人風格 + 大手前提）。預期 PIG 023 annotators 間：

- Big leaps 處 finger 多選 (f4 vs f5 為 octave)
- LH waltz bass 用 f5 vs f4 取決於手張
- Fioritura 指法 5-finger group 不同分組
- Substitution (同音換指) 標記頻率與位置

→ majority-vote ground truth 在某些位置可能很弱（≤ 50% agreement）。

## 10. 對指法系統的測試重點

| 場景 | 預期挑戰 |
|---|---|
| RH 長 lyrical line | DP 是否能保持手位連續、避免亂跳指 |
| LH waltz pattern stretch (10度) | DP 對寬 (1,5) chord 的 cost 設定 |
| Fioritura 段 | 5-finger group 不重新洗牌（連續 thumb-pass 避免）|
| 同音換指 (sub_from) | 多個 annotators 標記點位置一致性 |

## 11. 與其他 wiki 頁面的關係

- 父頁 [[composer_chopin_phrasing]]：通則 (per-genre, 本曲 = Nocturne)
- 父頁 [[concept_chopin_lyrical_phrase]]：通則 (浪漫派 lyrical)
- 工具頁 [[concept_phrase_elision]]：Op.9-2 為主要驗證 case
- 反向：[[concept_figural_boundary_detection]] 對 fioritura 的處理
- 兄弟頁 [[analysis_mozart_k283_first_mov]]：古典 vs 浪漫對比
  - [[analysis_chopin_ballade_2]] — 大型 narrative

