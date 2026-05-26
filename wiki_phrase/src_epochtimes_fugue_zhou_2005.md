# Source: 周怡秀《【藝術小百科】音樂中的復格形式（Fugue）》

> 大紀元，2005-10-29 發表（2025-03-20 更新），中文
> URL: https://www.epochtimes.com/b5/5/10/29/n1101361.htm
> Ingested: 2026-05-26

## 一句話總結

中文鋼琴 / 音樂百科風格文章，定義 fugue (復格 / 賦格) 為「以模仿 + 對位為特徵的多聲部音樂」，介紹其歷史源起 (文藝復興 → Bach 高峰)、典型結構 (主題 / 答題 / 插曲 / 開展部 / 結束部)、四種模仿形式、以及 Bach《復格藝術》作為經典案例。

## 重點概念清單（供其他 concept 頁引用）

### 對位 Counterpoint (contrepoint)
- 多聲部音樂中兩條以上旋律同時進行
- 每條旋律保有獨立性，但避免聲音過於嘈雜
- 內涵兼具「抗衡」與「互補」（相生相剋）
- 不和諧音的緊張 + 和諧音的舒緩互為因果

### 模仿 Imitation
- 一段旋律先在一個聲部出現 (antécédent 先行)
- 隨後另一聲部重現 (conséquent 後行)
- 四種形式：正向、逆向、正向顛倒（倒影）、逆向顛倒
- 文章指出後兩種一般聽眾不易辨認

### Fugue 結構
- **主題 (subject)**：開頭單一旋律
- **答題 (answer)**：主題在較高 / 較低音域 (通常 5 度或 4 度) 的模仿
- **插曲 (divertissement / episode)**：各聲部輪流呈現主題後進入自由對位
- **開展部 (development)**：在關係調上各聲部重新主題模仿
- **結束部 (recapitulation)**：常經由強化主題手法回到主調
- **Stretto**：以更密集的方法在各聲部重現主題

### 歷史與作曲家
- 源起：文藝復興時期
- 高峰：Bach（《復格藝術》Die Kunst der Fuge 是經典）
- 後續運用：Mozart (Sym. 41 K.551 末樂章)、Beethoven (晚期奏鳴曲、Op.133 Große Fuge)、Bartók (Music for strings, percussion & celesta)

### 文章未涵蓋（要 P1 補的）
- ❌ 具體的演奏 / 指法建議
- ❌ Bach Inventions（2 聲部，非嚴格 fugue 但同源）
- ❌ 每段樂句 / phrase 的長度與邊界判斷
- ❌ 各聲部間樂句邊界是否同步（counterpoint 的關鍵指法問題）

## 對指法系統的啟示（synthesized — 不是文章原文）

1. **對位音樂中，每條聲部 / 每隻手有獨立的樂句結構**：兩手樂句邊界 NOT 必然同步。`_detect_phrase_starts` per-hand 跑是對的，但要承認結果可能不對齊（mvt4 LH 抓到 m50 boundary、RH 沒抓到，就是這種非對齊在現實裡發生）。
2. **主題 (subject) 入聲 = 樂句邊界**：fugue / Invention 裡，新聲部接過主題或同聲部再次提出主題的瞬間，幾乎一定是樂句起點。這比泛用的「音高跳幅 > N」更精準。
3. **插曲與主題段落的樂句長度不同**：episode 常用 motivic fragment + sequence，樂句較短；exposition / recapitulation 樂句以完整主題長度為單位。
4. **Stretto 段落樂句重疊**：邊界可以非常密集，甚至跨聲部同拍開始 — 不能假設樂句至少 N 拍長。

詳見 [[concept_fugue]] 與 [[concept_counterpoint]]。
