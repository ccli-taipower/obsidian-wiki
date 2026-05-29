# Composer: Mozart 樂句 — 古典 period / sentence 純正範本

> 來源：[concept_classical_period_sentence](concept_classical_period_sentence.md) 基底 + Caplin《Classical Form》、Rosen《The Classical Style》Mozart 章節
> 涵蓋 PIG：Mozart 20 曲（第二大 composer bloc）
> 狀態：第一版 2026-05-26
> 引用方：[concept_classical_period_sentence](concept_classical_period_sentence.md) (反向引用 — 純正範本)

## 1. Mozart 為何單獨開頁

Mozart 是古典時期樂句結構最「規範」的作曲家 — Caplin《Classical Form》大量使用 Mozart 範例來定義 period / sentence。Mozart 樂句的優點對指法系統而言：

- **高度可預測**：period (4+4) / sentence (2+2+4) 適用率比 Beethoven、Schubert 都高
- **Cadence 訊號清晰**：V-I 根位 + soprano 在 tonic 為標準
- **Sonata-allegro 結構規範**：主題 / 過渡 / 副題 / development / recap 段落邊界明確

→ Mozart 是驗證 [concept_cadence_detection](concept_cadence_detection.md) 與 [concept_classical_period_sentence](concept_classical_period_sentence.md) 演算法的**理想 baseline**。

## 2. PIG 20 首 Mozart 大致分類（待逐曲確認）

從 label 推測：

| 形式 | 預期數 | 代表 PIG ID |
|---|---|---|
| Sonata 1st mov (sonata-allegro) | 8-10 | 011 K283 i, 012 K310 i, 013 K330 i, 017 K545 i |
| Sonata 2nd mov (slow, lyrical) | 3-5 | 待查 |
| Sonata 3rd mov (rondo / minuet) | 3-5 | 待查 |
| Variations / Fantasia | 1-2 | 待查 |

## 3. Sonata-allegro 段落結構（樂句邊界 anchor）

```
Exposition (呈示部)
  ├─ 第一主題群 (Theme 1):
  │     8-bar period 或 sentence
  │     → PAC in tonic 結尾
  ├─ Transition / Bridge:
  │     模進、modulation 到 dominant
  │     → HC on dominant of new key
  ├─ 第二主題群 (Theme 2):
  │     新主題、新 key (dominant 或 relative major)
  │     → 多個 phrase 組成
  └─ Closing theme (codetta):
        cadential extension
        → PAC in new key

Development (發展部)
  ├─ 主題碎片變奏
  ├─ Far-key modulation
  └─ Re-transition back to tonic

Recapitulation (再現部)
  ├─ Theme 1 (in tonic)
  ├─ Transition (modified)
  ├─ Theme 2 (now in tonic — 與 exposition 不同 key)
  └─ Coda
```

每個段落邊界 = **strong phrase reset**。

## 4. 樂句邊界訊號優先序（Mozart 特化）

| 訊號 | 操作型 | 信心度 |
|---|---|---|
| **PAC 結尾段落** | V-I 根位 + soprano 落 tonic | ⭐⭐⭐ |
| **HC 在 4+4 period 中點** | bar 4 末 V chord | ⭐⭐⭐ |
| **Sentence presentation/continuation 切換** | bar 1-2 motif 在 bar 3-4 重複 → bar 5 邊界 | ⭐⭐⭐ |
| **Sonata 段落切換** | tempo / texture / key 變化 | ⭐⭐⭐ |
| **4-bar 週期 fallback** | **Mozart 適用**（Pass 3 OK） | ⭐⭐ |
| Albert bass change | LH alberti pattern 切換到其他 texture | ⭐⭐ |

## 5. Mozart vs Beethoven (與 [composer_beethoven_phrasing](composer_beethoven_phrasing.md) 對比)

| 特徵 | Mozart | Beethoven (Op.30 後) |
|---|---|---|
| Period 4+4 規律性 | ⭐⭐⭐ 高 | ⭐⭐ 常 expansion |
| Sentence 2+2+4 規律性 | ⭐⭐⭐ 高 | ⭐⭐ |
| Cadence 訊號 | ⭐⭐⭐ 清晰 V-I 根位 | ⭐⭐ 常被 DC 延後 |
| 4-bar 週期適用 | ✅ | ❌ (中晚期) |
| 戲劇性 tempo/dynamic 切換 | 少 | 多 |

**操作意涵**：對 Mozart，可以**信任 [concept_classical_period_sentence](concept_classical_period_sentence.md) 的演算法**直接套用。對 Beethoven 需個別判斷時期。

## 6. Mozart 樂句特有細節

### 6.1 主題群內的次階結構
Mozart 第一主題群常分**前 antecedent 4 bar + 後 consequent 4 bar**，後者結尾 PAC。次主題群可能更長，含 sentence 結構。

### 6.2 Codetta (結尾段)
第一主題群結束 PAC 後，常加 2-4 bar codetta（反覆 cadential progression）— 視為**同主題群的 cadential extension**，**不**獨立樂句。

### 6.3 Transition / Bridge
過渡段常用 sequential treatment + 持續加速感。多個短 phrase 接連，但**整段是一個 transitional unit**。可以視為一個大 phrase 或一系列 micro-phrases，看 detection scale。

### 6.4 Slow movement (2nd mov)
2nd mov 多為 song-form (ABA)、theme + variations、或 sonata。Tempo 慢，phrase 較長（8-16 bar），但仍 period / sentence 為主。

### 6.5 Rondo (3rd mov)
ABACA / ABACABA 結構。A 段為 refrain，B/C 段為 episode。**段落切換明確**（return to A 時通常 tempo + texture 都對齊原始）。

## 7. PIG 驗證狀態

| ID | 曲目 | 形式 | 狀態 |
|---|---|---|---|
| **011** | K283 G i | sonata-allegro | **verified** — Cadence Phase 2 at m9→m10 IAC, **+1.01pp RH** improvement (2026-05-27); see [analysis_mozart_k283_first_mov](analysis_mozart_k283_first_mov.md) |
| **017** | K545 C i | sonata-allegro (簡化) | **tested** — m7→m8 IAC detected, boundary structure changed; Δ+0.00pp RH (texture-driven limit: m5 ascending scale fingering not fixable by phrase boundary alone); see [analysis_mozart_k545_first_mov](analysis_mozart_k545_first_mov.md) |
| 012 | K310 a i | sonata-allegro (戲劇性) | candidate — a minor，驗證 Mozart 是否偶爾打破規律 |
| 013 | K330 C i | sonata-allegro | candidate — 另一個標準範例 |

## 8. 與其他 wiki 頁面的關係

- 父頁 [concept_classical_period_sentence](concept_classical_period_sentence.md)：通則 — Mozart 是純正範本
- 對比 [composer_beethoven_phrasing](composer_beethoven_phrasing.md)：Beethoven 同源但更自由
- 工具頁 [concept_cadence_detection](concept_cadence_detection.md)：對 Mozart 信心度最高
- [analysis_mozart_k283_first_mov](analysis_mozart_k283_first_mov.md) — K283 Phase 2 primary success case
- [analysis_mozart_k545_first_mov](analysis_mozart_k545_first_mov.md) — K545 Phase 2 texture-limit case

