# Composer: Debussy 樂句 — texture-driven 細分

> 來源：[[concept_impressionist_phrasing]] 基底 + Howat《Debussy in Proportion》、Jankélévitch《Debussy et le mystère》、Roy Howat 演奏研究
> 涵蓋 PIG：Debussy 9 曲
> 狀態：第一版 2026-05-26
> 引用方：[[concept_impressionist_phrasing]] (反向引用 — composer 細分)

## 1. Debussy 為何要按 collection 細分

Debussy 不同 collection 的樂句邏輯**差異顯著**：

| Collection | 樂句傾向 |
|---|---|
| **Suite Bergamasque** (含 Clair de Lune) | 仍偏古典結構，ABA / ternary，cadence 較可辨 |
| **Préludes Livre I/II** | 每首獨立 character piece，樂句完全因主題而異 |
| **Études** | 重 texture 變奏；樂句單位 ≈ figural pattern unit |
| **Images / Estampes** | 強烈 programmatic（標題引導），樂句邊界對應「場景變化」 |
| **Children's Corner** | 較簡單、ABA 為主、規律性高 |

## 2. PIG 9 首 Debussy 大致分類（待逐曲確認）

從 label 推測：

| 曲目 | Collection | PIG ID | 形式 | 邊界主訊號 |
|---|---|---|---|---|
| Arabesque No.1 | (early) | 035 | ABA, lyrical | Tempo / cadence |
| Arabesque No.2 | (early) | 036 | ABA, scherzando | Pattern change |
| **Clair de Lune** | Suite Bergamasque | 037 | ABA, lyrical | Texture + tempo |
| 其他 6 首 | 待 PIG label 確認 | — | — | — |

## 3. 各 collection 樂句特徵

### 3.1 Suite Bergamasque (含 Clair de Lune)
- **時期**：Debussy 早期 (1890s)，仍受古典/浪漫派影響
- **樂句結構**：ABA / ABACA，內部仍有 period-like 8-bar 段落
- **Cadence 訊號**：較傳統（V-I 仍可偵測），但和聲已 modal-tinged
- **邊界訊號**：
  - A→B 段落切換：tempo / dynamic 變化 = strong
  - A 段內部 8-bar period 仍有效
  - B 段（中段）常 modulation + texture change

### 3.2 Préludes Livre I/II
- **時期**：Debussy 成熟期 (1909-1913)
- **樂句結構**：每首獨立 character piece，**無通則**
- **特點**：每首有副標題（La cathédrale engloutie / Voiles / etc）暗示 programmatic 結構
- **邊界訊號**：
  - **Tempo marking 變化**（Modéré → Animé → Calmato）= strong
  - **Dynamic level 切換**（pp 段 → ff 段）= strong
  - **Texture 切換**（single line → arpeggio wash → block chord）= strong
  - **明確 phrase mark / breath mark**（若 Audiveris 抽得到）= strongest
- **建議**：每首單獨 `analysis_debussy_prelude_*.md`

### 3.3 Études (12 首, 1915)
- **時期**：Debussy 晚期
- **樂句結構**：表面 etude form（一個 technical idea 變奏），但內部和聲色彩變化頻繁
- **邊界訊號**：
  - **Pattern change** = 邊界（同 Chopin Etude，但 Debussy 的 pattern 更 abstract）
  - **Harmonic color shift** = 邊界（modal → whole-tone → octatonic 等切換）
- **避免**：傳統 cadence 偵測（Debussy 晚期非功能和聲，cadence 失效）

### 3.4 Images / Estampes
- **時期**：1903-1908
- **樂句結構**：programmatic — 每首對應一個「場景」/「印象」
- **邊界訊號**：場景切換 (texture + tempo + dynamic 同時變)
- **代表**：Reflets dans l'eau, Pagodes, La soirée dans Grenade
- **特殊**：modal scale (pentatonic in Pagodes, gypsy scale in Grenade) 影響指法

### 3.5 Children's Corner
- **時期**：1908
- **樂句結構**：簡單 ABA / ternary，較規律
- **邊界訊號**：傳統 cadence + 8-bar period 仍有效（這集面向業餘 / 兒童）

## 4. Debussy 樂句邊界訊號優先序

按時期 / collection 加權：

| 訊號 | Suite Bergamasque / Children's Corner | Préludes / Images | Études (晚期) |
|---|---|---|---|
| 傳統 Cadence (PAC/HC) | ⭐⭐⭐ | ⭐ | ❌ |
| Tempo marking 變化 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Texture / chord density 變化 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Dynamic 突變 | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Registral shift | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Pedal change | ⭐⭐ | ⭐⭐⭐ | ⭐ |
| Pattern (figural) change | ⭐ | ⭐⭐ | ⭐⭐⭐ |
| 4-bar 週期 fallback | ⭐⭐ (Children's Corner only) | ❌ | ❌ |

## 5. Whole-tone / Pentatonic / Modal 對指法的影響

Debussy 大量使用非大小調音階：

- **Whole-tone (6 音 octave)**：相鄰音都是 2 半音；標準指法習慣（thumb pivot at fa/ti）不適用。常用 1-2-3-4-5-1-2-... 或不規則 fingering
- **Pentatonic (5 音 octave)**：5 個音剛好 5 指；常無需 thumb-pass — [[concept_running_passage_thumb_reservation]] 規則可能不適用
- **Octatonic (8 音 octave)**：交替全音半音；複雜，依音域選 finger group

→ 不同 mode 下，DP 的 thumb-pass / span 規則可能需要 mode-aware 調整。詳 [[concept_modal_scale_fingering]] (TODO)。

## 6. Pedal 重要性

Debussy 的「sound color」與 sostenuto / damper pedal **不可分**。Pedal 標記在樂譜上是樂句結構的重要 marker：

- **Pedal release** (★ 或 *)= 紋理結束 = 多半樂句邊界
- **Pedal press** (Ped.) 後接持續紋理 = 新樂句開始
- **連續 pedal 跨段** = 兩段視為一個大樂句

對 OMR：需確認 Audiveris 是否抽 pedal marking。即使無，可由 chord density 與 dynamic 推斷 pedal section。

## 7. PIG 驗證候選

| ID | 曲目 | 為何選 |
|---|---|---|
| **037** | Clair de Lune | 平衡點：早期偏古典 + 印象派 texture 特徵 |
| 035 | Arabesque No.1 | early Debussy 代表，較好處理 |
| 036 | Arabesque No.2 | scherzando 對照組 |
| 其他 6 首 | 待 PIG label 確認 | — |

**建議從 Clair de Lune 開始**（最熟悉、structurally 最容易處理）。

## 8. 與其他 wiki 頁面的關係

- 父頁 [[concept_impressionist_phrasing]]：通則
- 對比 [[composer_mozart_phrasing]]：兩者結構性差異最大（規律 vs 自由）
- 對比 [[composer_chopin_phrasing]]：兩者 lyrical 共通但 cadence 處理不同
- 工具頁 [[concept_cadence_detection]]：對 Debussy 早期作品有限 OK，晚期失效
- 待寫：
  - [[analysis_debussy_clair_de_lune]]
  - [[concept_modal_scale_fingering]] (modal 對指法的影響)
  - [[concept_pedal_as_phrase_signal]]

## 變更日誌
- 2026-05-26: 創立。Debussy 按 collection 細分，補完印象派概念的細部。
