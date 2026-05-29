# Concept: Slur 與 Phrase 邊界的重合 / 不重合

> 來源：Lerdahl-Jackendoff《GTTM》(1983)、Rothstein《Phrase Rhythm in Tonal Music》(1989)、Caplin《Classical Form》(1998)
> 引用方：[[concept_articulation_overview]] §6、[[concept_legato_substitution]] §1

## 1. 為什麼必須區分 slur 與 phrase

初學者常把 slur 與 phrase 等同。**它們是不同層次的記號**：

| 屬性 | Slur | Phrase |
|---|---|---|
| **層級** | 觸鍵 / articulation 細節 | 樂句 / 音樂語法結構 |
| **長度** | 通常 1-8 拍 | 通常 4-8 小節 |
| **起源** | 作曲家標記、編輯者補加 | 樂理結構（句法 / 和聲 / 終止式）|
| **可變度** | 不同 edition 標記差異大 | 樂理共識（多數情況下穩定）|

→ 一個 phrase 內可有**多個** slur；一個 slur **不一定**等同 phrase。

## 2. 三種典型關係

### 2.1 Slur ⊂ Phrase（slur 是 phrase 子單位）— 最常見

例：Mozart K545 mvt2 (Andante)
- 一個 8-bar phrase 由 4 個 2-bar slur 組成
- 每個 slur 是 sub-phrase（motif 級別）
- Phrase 邊界在第 8 小節末（cadence）

對指法的意涵：phrase boundary 才是「**手位 free reset**」點；slur 內部仍是 legato 段，不應重新優化。

### 2.2 Slur ≡ Phrase（slur 邊界等同 phrase 邊界）— Romantic 偶見

例：Chopin Nocturne 部分長 lyrical 段
- 整個 8-bar phrase 寫在一個大 slur 內
- Slur 結束 = phrase 結束 = cadence 位置

對指法的意涵：這時可以把 slur 結束視為 phrase boundary 處理。但**判斷需謹慎**：要看 slur 是否真的覆蓋一個結構完整的 phrase。

### 2.3 Slur 跨越 Phrase 邊界（罕見但存在）— phrase elision

例：Schumann *Kinderszenen* 某些 phrase 銜接段
- 一個 slur 從 phrase A 末延續到 phrase B 起首
- 表現「**樂句 elision**」（兩 phrase 縫合）

對指法的意涵：這時 phrase boundary 不應切；slur 內保持 legato 連續處理。

## 3. 判斷規則（演奏家詮釋層）

| 觀察 | 判斷 |
|---|---|
| Slur 長度 ≤ 2 小節 | 多半是 sub-phrase / motif 級別，不等於 phrase |
| Slur 長度 4-8 小節 + 結尾落在 cadence | 可能等於 phrase；查證和聲 |
| Slur 跨越明顯 cadence | 是 phrase elision，slur 對指法重要而 cadence 對手位不重要 |
| 同段有多 slur 重疊 | Romantic 常見的「**疊瓦式**」phrasing；按 slur 處理 |

## 4. 對指法系統的意涵

score-claude DP 目前的處理：
- **Phrase boundary 由 [[../wiki_phrase/index|wiki_phrase]] 五軸偵測**（不直接看 slur）
- **Articulation rule 由 slur 觸發**（不重新計算 phrase）

兩者解耦的好處：
- Slur 標記分歧（不同 edition）不會破壞 phrase 結構分析
- Phrase 結構錯誤不會破壞 articulation 處理

但要小心：當 slur ≡ phrase（§2.2 情境）時，DP 不會主動「合一處理」 — 需依靠 phrase 偵測單獨找到 cadence boundary。

## 5. 與其他 wiki 頁面的關係

- [[concept_articulation_overview]] §6 — 本頁是其「Articulation 與樂句邊界的區別」段的深入展開
- [[concept_legato_substitution]] §1 — slur 訊號的可靠度討論
- [[../wiki_phrase/concept_phrase_elision]] — slur 跨越 phrase 邊界的樂句 elision 處理
- [[../wiki_phrase/concept_chopin_lyrical_phrase]] — Chopin 長 slur 與 phrase 重合的浪漫派常見模式
- [[../wiki_phrase/src_lerdahl_jackendoff_gttm]] — GTTM 對 grouping 與 surface markings 的區分理論

## 6. ⚠ 詮釋限制

判斷 slur 與 phrase 的關係很大程度上**仰賴音樂分析能力**：
- 何處是 cadence？需要和聲分析
- Phrase 是 4-bar 還是 8-bar？需要 hypermeter 判斷
- Slur 結束是 sub-phrase 切割還是 phrase 切割？需要綜合判斷

對指法系統來說，安全做法是**不把 slur 自動視為 phrase**，只在明確證據（cadence + 對應 slur 結束）時才併合。
