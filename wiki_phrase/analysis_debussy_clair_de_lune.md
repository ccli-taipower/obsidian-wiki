# Analysis: Debussy Clair de Lune (Suite Bergamasque No.3)

> PIG: 037 (4 annotators)
> 來源：通用 Debussy 分析 + Howat《Debussy in Proportion》+ Roy Howat 演奏研究
> 狀態：第四個 per-piece analysis，2026-05-26
> 引用方：[[composer_debussy_phrasing]] §3.1、[[concept_impressionist_phrasing]] §6、[[concept_texture_change_detection]] §7

## 1. 為什麼挑這首

Clair de Lune 是 Debussy 最知名的鋼琴作品（也是大眾最熟悉的「印象派」代表）。雖屬於早期 Debussy (1890 草稿、1905 出版)，仍偏古典結構但已展現 texture-driven phrasing 特徵 — 是驗證「印象派偵測器組合」的理想 baseline。對 wiki 的價值：

- 驗證 [[concept_impressionist_phrasing]] 的 texture-driven 邏輯
- 驗證 [[concept_texture_change_detection]] 對 density/registral/dynamic shift 的偵測
- 與古典/浪漫對比，揭示 cadence 偵測退化點

## 2. 曲目基本資訊

- **Suite Bergamasque No.3** (Suite 1890 草稿, 1905 大幅修訂出版)
- **D♭ major**, 9/8 拍, **Andante très expressif**
- 長度：~72 小節
- 形式：**ABA' + Coda** (大型三段體)

## 3. 段落結構

| 段落 | 小節範圍 | 特徵 |
|---|---|---|
| A | bb. 1-26 | Slow melodic theme, sparse texture, RH chord melody + LH sustained bass |
| B (中段) | bb. 27-50 | Arpeggio wash (連續 RH 16th-note 流動), dynamic peak, modal harmonies |
| A' | bb. 51-65 | Theme 再現，texture 較 A 段更精簡 |
| Coda | bb. 66-72 | Decrescendo 收尾, niente (ppp 消失) |

## 4. A 段細節 (bb. 1-26)

### 4.1 內部結構
- 8-bar period-like (bb. 1-8)：antecedent (1-4) + consequent (5-8)
- 然後變奏與擴展到 bar 26

### 4.2 樂句邊界訊號
- **傳統 cadence 弱化**：D♭ major 內含 modal inflections (Mixolydian-tinged), V-I 偶見但常被 extended harmonies 覆蓋
- **動態變化**：A 段內部 pp → mp → pp 細微起伏
- **Texture**：RH 三度/六度平行進行為主 (Debussy 標誌)

### 4.3 預期偵測
- Pass 3 (4-bar) 對前 8 bar 期 OK
- Pass 6 (cadence) 可能偵測 bar 8 末 V-I (若 chordify 結果乾淨)
- Pass 4 (figural) 對 sparse texture 不太 fire

## 5. B 段細節 (bb. 27-50) — 印象派偵測核心測試

### 5.1 戲劇 texture 切換
A→B 邊界是**最強樂句邊界**：
- **Texture 切換**：A 段 slow chord melody → B 段 continuous arpeggio wash
- **Tempo 變化**：常標示加速 (Un poco mosso)
- **Dynamic**：明顯 crescendo to mp
- **LH pattern**：A 段 sustained bass → B 段 broken chord arpeggio

### 5.2 內部 phrase
- B 段內部樂句**長度可達 16 bar**
- 4-bar period 完全不適用
- 動態 climax 在 ~bar 40-44，之後 decrescendo

### 5.3 預期偵測
- **Texture change detection ([[concept_texture_change_detection]])** 應為主訊號 — density + registral 同時跳
- Pass 3 (4-bar) 在 B 段應**禁用** — 會錯切 long arpeggio line
- Pass 6 (cadence) 在 B 段失效 — modal/non-functional harmony
- Pedal marking change 強 signal (Debussy 有明確 pedal 標記)

## 6. A' 段 + Coda

- bar 51: B → A' 強樂句邊界 (texture 回到 sparse)
- bar 66 開始 Coda - tempo 慢下、dynamic 漸弱

## 7. 五類偵測器預期表現

| 偵測器 | A 段 | B 段 | A' 段 + Coda | 整體 |
|---|---|---|---|---|
| Pass 3 (4-bar) | ⭐⭐⭐ OK | ❌ **禁用** | ⭐⭐ | 混合 |
| Pass 6 (PAC) | ⭐⭐ 可能 | ❌ failed | ⭐ | 中 |
| Pass 4 (figural) | ⭐ low | ⭐⭐ arpeggio 切換 | ⭐ | 中 |
| **Texture change** ([[concept_texture_change_detection]]) | ⭐ | **⭐⭐⭐ critical** | ⭐⭐ | **核心** |
| thumb-reservation | ⭐ low (slow tempo, sparse) | ⭐⭐ arpeggio runs | ⭐ | low fire |

→ Clair de Lune 是 [[concept_texture_change_detection]] 的**最重要驗證 case**。Phase 1 未實作此偵測器（still TODO），所以 Clair de Lune 目前無法被既有偵測器正確分段。

## 8. Pentatonic / Modal 元素

Debussy 在 A 段大量使用平行三度六度（modal flavoring），但 B 段 arpeggio wash 是 D♭ major 與 a♭ minor 切換（含 b♭ minor + 增六和弦色彩變化）。對指法：

- A 段 RH 三度 chord melody → 五指 group 對位重要
- B 段 arpeggio 跨 2 octaves → thumb-pass 連續使用
- 黑鍵調 (D♭) → fingers 自然落黑鍵組
- 與 [[concept_modal_scale_fingering]] 部分相關（但本曲整體仍 functional, 非純 modal）

## 9. PIG 4 annotators 預期 disagreement

- B 段 arpeggio 指法（5-finger group 對應）— 個人偏好強
- A 段 RH chord voicing — 哪個音給 thumb 取決於手張
- Pedal-dependent 指法（Debussy 預設 pedal）— annotator 對 pedal 假設可能不同

## 10. 待執行驗證

```bash
# 對 PIG 037 跑 compare_pig.py with default flags
# 預期：B 段大量 mismatch (no texture detector available)
# 加 texture detector (Phase 1 待實作) 後比對改善

# 短期可手動寫 SINGLE_PDF_PHRASE_FLAGS["clair"] = {"figural": True} 看 arpeggio
# Pattern change 是否被 figural detector 部分捕捉
```

## 11. 對 wiki 的回饋

Clair de Lune 揭露下一輪實作優先序：

1. **[[concept_texture_change_detection]] Phase 1 實作**：B 段 arpeggio wash 必須偵測
2. **Cadence detection mode awareness**：modal-tinged passages 不能用嚴格 V-I 條件
3. **Pedal marking 偵測**：Audiveris 是否抽取需驗證

## 12. 與其他 wiki 頁面的關係

- 父頁 [[composer_debussy_phrasing]] §3.1 Suite Bergamasque
- 父頁 [[concept_impressionist_phrasing]] §6 驗證樣本
- 工具頁 [[concept_texture_change_detection]] §7 驗證 case (Phase 1 待實作)
- 對比 [[analysis_mozart_k283_first_mov]] (古典 vs 印象派)
- 對比 [[analysis_chopin_op9_no2_nocturne]] (浪漫 lyrical vs 印象派 texture)
- 待寫：
  - [[analysis_debussy_arabesque_1]] (PIG 035, 早期更古典)
  - [[concept_pedal_as_phrase_signal]] (Debussy 系列需要)

## 變更日誌
- 2026-05-26: 創立。第四個 per-piece analysis，印象派 texture-driven 範本，揭露 texture change detection 為下一輪實作優先。
