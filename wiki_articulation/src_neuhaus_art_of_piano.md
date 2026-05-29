# Source: Neuhaus《The Art of Piano Playing》

> Heinrich Neuhaus (1888-1964), *Об искусстве фортепианной игры* (1958, Moscow)；英譯 *The Art of Piano Playing* (1973, Praeger / 1993 Kahn & Averill)
> 引用方：[[concept_legato_substitution]] §2, [[concept_staccato]] §1, [[concept_tenuto]] §3, [[concept_accent_marcato]] §2

## 1. 作者背景

Heinrich Neuhaus 是 20 世紀俄羅斯鋼琴學派（Russian School）最重要的教育家之一，主要任教於 Moscow Conservatory（1922-1964）。其學生包含 Sviatoslav Richter、Emil Gilels、Radu Lupu 等 20 世紀標誌性鋼琴家。

Neuhaus 在歐洲（特別與 Leopold Godowsky 學習）+ 俄羅斯雙重訓練背景，使其 *The Art of Piano Playing* 成為**兼容俄羅斯派 重量觸鍵 與 西歐解析傳統** 的代表文獻。

## 2. 對 articulation / 觸鍵的核心主張

### 2.1 觸鍵的「重量」哲學

Neuhaus 強調觸鍵不是「手指動作」，而是「**重量傳達**」：
- Legato 觸鍵 = 重量在連續音之間平滑轉移
- Staccato 觸鍵 = 重量瞬間注入後立刻撤回
- Tenuto 觸鍵 = 重量穩定持續施加

→ 對指法的意涵：選擇手指時必須考慮該指能否做到該 articulation 所需的重量控制。例如小指 (5) 對 tenuto 重量持續較弱，應盡量避免分配 tenuto 音給 5。

### 2.2 Legato 的真實意義 — substitution 是必要技術

⚠ Training-data verification needed:
> 「legato 的真實意義不是『不分開』，而是『前一個音的釋放與後一個音的進入發生在同一瞬間』。為達此目的，finger substitution 是不可或缺的技術。」

Neuhaus 把 finger substitution 列為**legato 技術的基礎之一**，不是可選技巧。學生若無法執行 substitution，被視為 legato 技術不成熟。

詳見 [[concept_legato_substitution]] §2.1 引用。

### 2.3 Staccato 變體 — 「指尖斷」與「腕斷」與「臂斷」

Neuhaus 把 staccato 分為三層次（依使用身體部位）：
- **手指 staccato (finger staccato)**：最快、最輕，適合 leggiero / scherzando 短音
- **腕 staccato (wrist staccato)**：中等力道，最常見
- **臂 staccato (arm staccato)**：最重、最慢，適合 marcato 強斷 + 重音

→ 對指法的意涵：不同 staccato 變體對 thumb-cross 的容忍度不同。手指 staccato 容忍度最高（thumb-cross 在快速 staccato 段最自然）；臂 staccato 較不適合 thumb-cross（動作太大）。

### 2.4 Pedaling 與 articulation 的互動 ⚠

⚠ Training-data verification needed: Neuhaus 強調 articulation 標記**永遠優先於 pedaling 決定** — 即使 sustain pedal 踩著，staccato 標記仍應由手指動作體現（避免 「**踏板 legato 假裝 legato**」 的常見錯誤）。

對指法的意涵：pedaling 對 substitution 必要性的影響有限 — 即使 pedal down，legato melody 段仍應 substitution（不能依賴 pedal 隱藏 broken-finger 動作）。

## 3. 對指法系統的具體影響

| Neuhaus 教學 | 對 score-claude DP 的對應 cost rule |
|---|---|
| 重量觸鍵需強指承擔 | tenuto + accent 應偏好 1/2/3 |
| Legato substitution 必要 | [[concept_legato_substitution]] cost rule |
| Staccato 變體分層 | 短音可鬆綁 thumb-cross penalty；長 staccato 不應鬆綁 |

## 4. 文章未涵蓋

- **數字 fingering 規則**：Neuhaus 不寫具體指法表（不像 Czerny Op.500），偏重原則
- **作品分析**：少量 specific 作品段落分析（散見書中），不成系統
- **對位 fingering**：對 Bach 對位 fingering 著墨少（俄羅斯派傳統聚焦浪漫派）

## 5. 與其他 wiki 頁面的關係

- [[concept_legato_substitution]] §2.1 — Neuhaus 對 legato substitution 的最常被引用段落
- [[concept_staccato]] §1, §2 — Neuhaus 三層 staccato 分類
- [[concept_tenuto]] §3 — Neuhaus 重量觸鍵理論
- [[concept_accent_marcato]] §2 — Neuhaus 重音物理基礎
- [[../wiki_piano/concept_thumb_technique]] — Neuhaus 對 thumb-cross 的 staccato 容忍度討論
- [[../wiki_piano/analysis_common_fingering_injuries]] — Neuhaus 的「重量傳達」理論對預防 focal dystonia 也有指引意義

## 6. ⚠ Training-data verification queue

以下引述基於 training-data，需 cross-check 原書：
- §2.2 legato 真實意義引述（精確章節 / 頁碼）
- §2.4 pedaling vs articulation 優先級主張（具體章節）
- 是否明確提到「同音換指」（same-pitch substitution）vs 一般 substitution 區分
