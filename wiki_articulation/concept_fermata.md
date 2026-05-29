# Concept: Fermata — 延長標記

> 來源：Czerny《Op.500》§表情標記, Türk《Klavierschule》§延長, Brendel essays §Beethoven 延長
> 引用方：[[concept_articulation_overview]] §2 (taxonomy 第 11 項)

## 1. Fermata 是什麼

Fermata（中文「**延長記號**」）= 標記 `𝄐`（半圓 + 點，置於音符上方或下方）

意涵：
- **延長該音的時值**到演奏者裁量的長度
- 通常 1.5× 至 2× 書寫值（極端情況 3× 或更多）
- 出現在**樂句結尾、戲劇性段落、cadence 強拍**

不是 articulation connection 的修飾，是 **duration override**。

## 2. 對指法的影響 — 通常不大

Fermata 的指法影響有限：
- 該音的指法選擇按一般規則（fermata 只改 duration，不改 finger 偏好）
- 但需確保該指能**穩定持指 longer**（避免弱指 4/5 在長持音時抖動）

→ 對指法的意涵：**強指偏好**（與 [[concept_tenuto]] 類似邏輯）— 1/2/3 優先，4/5 盡量避免承擔 fermata 強指責任。

## 3. Fermata 與 phrase boundary 的關係

Fermata 通常出現在 phrase 結尾：
- 樂章末強 fermata = phrase 收結 + structural break
- 中段 fermata = 內部戲劇暫停

對指法系統的意涵：fermata 後的下一音 = phrase boundary 級別的「**重置點**」。手位可以 free reposition。

## 4. 與其他 articulation 的疊加

| 疊加 | 處理 |
|---|---|
| **Fermata + tenuto** | duration 大幅延長 + 壓重；強指偏好（[[concept_tenuto]]）|
| **Fermata + slur 結尾** | slur 涵蓋至 fermata 音為止；下一 phrase 從 fermata 後重新開始 |
| **Fermata + accent** | 戲劇性延長 + 重音；典型用於 cadenza 開始或樂章高點 |
| **Fermata 後 一拍空白 (caesura)** | 雙重 reset — phrase 邊界 + 拍子重設 |

## 5. 演奏實踐：fermata 長度差異

⚠ Training-data verification needed: 不同學派對 fermata 長度的傳統：

| 學派 | Fermata 長度 |
|---|---|
| **Baroque (per C.P.E. Bach)** | 1.5× ~ 2× 書寫值 |
| **Classical (Mozart, Haydn)** | 1.5× ~ 2× |
| **Beethoven** | 自由度高，1.5× 至 3× 都可（依戲劇性）|
| **Romantic (Chopin, Liszt)** | 高自由度，常 2× 至 4× |
| **20 世紀 Urtext 派** | 適中 1.5× ~ 2.5× |

## 6. 對 score-claude DP 的意涵

DP 目前完全不看 fermata 標記：
- Fermata 音的 duration 仍取 MXL 原值（未延長）
- 不會把 fermata 視為 phrase boundary

未來改進方向：
1. **Fermata-aware duration**: 把 fermata 音的有效 duration 設為 1.5× 或 2× 書寫值（影響 cost 計算）
2. **Fermata 後 phrase reset**: 自動把 fermata 視為 phrase boundary signal

是 future direction，未實作。對初中階目標曲目來說，fermata 出現不頻繁（Bach Inv 幾乎無 fermata；Mozart sonata 偶爾用；Beethoven 較多用），優先級不高。

## 7. 與其他 wiki 頁面的關係

- [[concept_articulation_overview]] §2 — taxonomy 第 11 項
- [[concept_tenuto]] — fermata 持音的強指偏好邏輯類似
- [[../wiki_phrase/concept_cadence_detection]] — fermata 常出現在 cadence 位置
- [[../wiki_piano/concept_finger_span_table]] — 持音時手指穩定度

## 8. ⚠ Training-data verification queue

- §5 各學派 fermata 長度傳統的具體文獻
- §6 fermata-aware DP 規則的實際 cost 影響預測
