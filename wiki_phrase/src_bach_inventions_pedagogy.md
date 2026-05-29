# Source: Bach Two-Part Inventions (BWV 772-786) — 教學註解傳統匯整

> 多源匯整，不是單一文獻
> Ingested: 2026-05-28 (⚠ training-data summary; primary editions not directly ingested — see "Verification needed" 一節)

## 一句話總結

Bach《兩聲部創意曲》(Inventions, BWV 772-786) 是西方鋼琴教學近兩百年來最密集被註解、編訂、錄音的對位曲集；從 Czerny (1838) 到現代 Urtext (Henle / Wiener / Bärenreiter)，各家在 **主題切分 (subject identification)**、**發音法 (articulation)**、**裝飾音解奏 (ornamentation)**、**指法傳統** 上有清楚的傳承與分歧 — 對指法自動化而言，這些分歧本身就是「per-piece manual override 不可避免」的最佳論據。

## 編輯 / 教學傳統概覽

### Czerny (1838 ed.) — 早期 19 世紀腳註版

- Czerny 是 Beethoven 的學生，宣稱保留了 Beethoven 對 Bach 的演奏記憶
- ⚠ training-data inferred: Czerny 版傾向 **過度規定 legato**（19 世紀鋼琴 ideal），與 Baroque non-legato 默認衝突
- 指法傾向保守的 **5-finger 位置主義**、避免拇指穿越黑鍵
- 動態 / 表情記號加得密 — 現代學者普遍認為這些是 Czerny 自己的詮釋
- 歷史價值高、文獻價值低：用來研究「19 世紀如何讀 Bach」，不是用來考據原意

### Bischoff (Steingräber / Kalmus reprint, 1880s) — Urtext-leaning critical edition

- Hans Bischoff 是現代 Urtext 編訂的先驅之一
- ⚠ training-data inferred: 採用較少的編輯記號，appendix / footnote 區分「Bach 親筆」vs「編者建議」
- 指法相對 Czerny **更為 idiomatic for piano**，承認 Bach 原曲為大鍵琴 / clavichord 而生但接受鋼琴實務
- 對裝飾音給出多種解奏選項，不強加單一答案
- 至今仍被視為「實用 Urtext」的代表版本之一

### Landowska (mid-20th c.) — Harpsichord-informed performance tradition

- Wanda Landowska (1879-1959) 是 20 世紀 harpsichord 復興運動的關鍵人物
- 影響了 Bach 演奏的「歷史知情 (historically informed)」一脈
- ⚠ training-data inferred: 強調 **發音清晰、節奏舞蹈性、avoid romantic rubato**
- 對 Inventions 的詮釋著重於 **每個聲部如 vocal line**、articulation 為主要表達手段
- 雖然不是編訂版，但她的錄音與寫作成為後代鋼琴家的參考點

### Schiff (Decca recordings + lectures, late 20th–early 21st c.)

- András Schiff 的 Bach 系列錄音 + 公開講座是當代主流教學參考
- 強調 **每首 Invention 都有獨立的 Affekt（情緒性格）**，不能一律「練習曲式」演奏
- ⚠ training-data inferred: 在分析中經常 trace **subject + answer (real or tonal) lineage** — 即使 Inventions 不是嚴格 fugue
- 對 voice independence 著墨深：每隻手必須能獨立唱出
- 不教條化 articulation，根據各曲性格選擇 detaché / legato / portato

### Donington (Performance Practice — Baroque, 1963/1973) — General Baroque performance ref

- Robert Donington《The Interpretation of Early Music》與較短的《Performance Practice — Baroque》
- 不專論 Inventions，但提供 Baroque 演奏實務的權威參考
- 涵蓋：裝飾音表（最詳盡的英文資料之一）、節奏（inégalité）、發音法、tempo conventions
- ⚠ training-data inferred: 在裝飾音上採 **upper auxiliary + on the beat** 為 Baroque 默認 (Bach 自己《Explication》支持此說)
- 對「主音 vs 上音開始 trill」的分歧，Donington 力挺 Baroque convention (upper note)

### Modern Urtext editions (Henle, Wiener Urtext, Bärenreiter)

- **G. Henle Verlag**: 編輯如 Ullrich Scheideler；提供 **suggested fingering by modern pianist** (近年版本由 Andras Schiff / Yvonne Loriod 等知名演奏家給指法)；Urtext 主文乾淨、註腳完整
- **Wiener Urtext (Schott / Universal)**: 通常附 separate performance commentary 小冊
- **Bärenreiter (NBA — Neue Bach-Ausgabe)**: 學術 Urtext 標準，最權威的 source-critical text，但不必然附鋼琴指法
- 共通特徵：
  - 區分「Bach 親筆」與「編者建議」
  - Fingering 是 **suggestion not prescription**，明確標示
  - 承認 thumb-on-black-key 在現代鋼琴上不可避免
  - voice-following finger groups（同聲部優先用相鄰指）

## 重點概念清單（供其他 concept 頁引用）

### Subject identification（主題辨識）
- 每首 Invention 開頭都是 subject（多數情況下單獨呈現，沒有伴奏）
- Subject 結束位置在某些 Invention 有 **學派分歧**：
  - **Inv 1 (C major)**: 1-bar subject 派 vs 2-bar subject 派（含 m2 sequence）
  - **Inv 4 (D minor)**: m1 結束 vs m1 + m2 第一拍 — 經典爭議
  - **Inv 8 (F major)**: 類似 Inv 4 的爭議
- ⚠ training-data inferred: Schiff 通常採較短 subject + countersubject 解讀
- 對指法系統意義：subject 邊界 = phrase 邊界 99%，但邊界本身有 ±1 measure 的灰色地帶

### Voice independence rule
- 每隻手有獨立的 phrasing、articulation、dynamic shaping
- 兩聲部 **不需同步** breathe — 一手延音時另一手可能正在 phrase 起點
- 教學共識：練習時兩手分開練到能各自獨立歌唱，再合手
- 對指法系統意義：per-hand DP 是對的；不能用「兩手同時換指」當 phrase boundary 證據

### Articulation tradition
- **Baroque 默認 = detaché / non-legato**（受弦樂、聲樂、大鍵琴影響）
- legato 是 exception，多用於 **stepwise lyrical figure**
- Czerny 過度規定 legato 是 19 世紀的詮釋包袱
- 現代共識：根據 motif 性格選擇；fast 16th-note runs 多 detaché，cantabile 段 legato
- 對指法系統意義：本系統暫不模型 articulation，但若未來加入，必須以 per-piece flag 而非全域開關

### Ornamentation
- Trills, mordents, turns, appoggiaturas — Bach 留下《Explication》親自說明
- **Upper auxiliary + on the beat** 為 Baroque 默認
- 19 世紀演奏傳統（含 Czerny 沿用）改採 main note 開始 — 已被現代學界否定
- Donington 表是英文文獻中最完整的解奏參考
- 對指法系統意義：當前系統不處理裝飾音指法（trill 通常 3-2-3-2 或 4-3-4-3，自動化困難）

### Tempo and Affekt
- 「Inventions」原意為「在主題上創意發揮」(invenire = 發現 / 創造)
- 每首有獨立性格：Inv 1 教科書式、Inv 4 苦惱、Inv 8 跳躍歡愉、Inv 13 流動、Inv 14 莊嚴等
- ⚠ training-data inferred: Bach 自己在 1723 標題頁上寫到「cantabile manner of playing」(歌唱式演奏) — 即使是 fast inventions 也要 lyrical
- 對指法系統意義：tempo 與 Affekt 不直接影響指法，但影響 articulation → 間接影響指法

### Fingering tradition 分歧
| 編訂者 | 5-finger position 傾向 | Thumb on black key | Voice-following groups |
|---|---|---|---|
| Czerny (1838) | 強 | 避免 | 較弱 |
| Bischoff (1880s) | 中 | 接受 | 中 |
| Modern Urtext (Henle 等) | 弱（pragmatic） | 接受 | 強 |
| Schiff (隱含) | 弱 | 接受 | 強 |

- 對指法系統意義：**editorial fingering disagreement is expected** — 不該嘗試對齊單一傳統，而要對齊 user 自己的生物力學

### Trill execution split（裝飾音演奏分歧）
- Baroque convention: 上音開始 (`/concept_baroque_ornament`)
- 19 世紀 convention: 主音開始
- 現代共識回到 Baroque convention，但個別 trill 仍有實務考量（如已在上音則改主音開始）
- 對指法系統意義：trill 指法本身需要 per-occurrence 決定，不適合泛化

### Phrase boundary disputes
- **Inv 4 (D minor)**: subject 在 m1 結束 vs 跨入 m2 — 影響後續 entries 的對齊解讀
- **Inv 8 (F major)**: subject 長度爭議 — 1 bar vs 2 bar
- **Inv 1 (C major)**: subject 是 m1 (motif) 還是 m1-m2 (motif + sequence)
- 對指法系統意義：phrase boundary 自動偵測必然有歧義；BACH_INV_OVERRIDES 之所以 hand-curated 而非 auto-derived，正因為各家分歧無法演算法仲裁

### Subject + answer (real or tonal)
- Inventions 不是嚴格 fugue，但 2-3 首具明確的 subject + answer 結構
- "Real answer": 嚴格移調（通常 5 度 / 4 度）
- "Tonal answer": 為避免轉調過快做局部調整（fugue exposition 常見）
- Schiff 強調這條 lineage 對 voice-leading 的影響
- 對指法系統意義：subject 在另一聲部 entry 時 → phrase boundary；同手不同聲部可能 finger reset

### Beat hierarchy
- Bach 的節奏感建立在 **metric placement** 而非 beat counting
- Strong beat (1, 3 in 4/4) vs weak beat 的層級結構決定 phrasing 與 articulation
- 樂句通常起於 weak beat / pickup，結束於 strong beat（典型 Baroque cadential pattern）
- 對指法系統意義：phrase boundary detection 可以利用 strong-beat alignment 做 tie-breaker（但不該硬性要求）

## ⚠ Training-data verification needed

下列具體 claim 為訓練資料記憶，**不保證準確**，等 raw editions ingested 後逐條核對：

- [ ] Czerny 1838 edition 的具體出版資訊與指法慣例
- [ ] Bischoff edition 是否真為 1880s 出版 / Steingräber vs Kalmus reprint 細節
- [ ] Landowska 對 Inventions 的具體論述出處（書名 / 章節）
- [ ] Schiff 「每首 Invention 有獨立 Affekt」的具體出處（Wigmore Hall lectures? Decca booklet?）
- [ ] Donington 對 Bach trill 的具體 quote 與頁碼
- [ ] Henle Inventions 編輯者實際姓名（Scheideler? other?）
- [ ] Bach 1723 標題頁「cantabile manner of playing」原文與精確翻譯
- [ ] Inv 1 / Inv 4 / Inv 8 subject 長度爭議的具體文獻引用
- [ ] NBA (Neue Bach-Ausgabe) Inventions 卷的編輯者與年份
- [ ] Czerny 與 Beethoven 對 Bach 演奏的傳承鏈是否真實 vs 後人神話化

## 對指法系統的啟示（synthesized — 不是文獻原文）

1. **Bach Inventions 是本專案的 primary test corpus**：15 mvt、每首 16-30 小節、教學文獻最密集 — daily-driver 測試材料。`BACH_INV_OVERRIDES` 是專案核心 ground truth。

2. **Per-hand DP 在對位音樂裡是必要的**：兩聲部 phrasing 不同步是 Baroque 對位的本質，不是 bug；不能要求兩手 phrase boundary 對齊。詳見 [concept_counterpoint](concept_counterpoint.md)。

3. **Editorial fingering disagreement is expected**：Czerny、Bischoff、Henle、Schiff 各家指法不同 — 不該嘗試對齊某單一傳統，而要對齊 user 自己的 biomechanical optimum（*feedback_personal_biomechanics*）。

4. **Subject detection 是最強的 phrase boundary cue**：每次 subject entry（同手或跨手）幾乎必然是 phrase 起點；比泛用「音高跳幅 > N」更精準。詳見 [concept_subject_imitation_detection](concept_subject_imitation_detection.md)。

5. **Phrase boundary 在 Inv 4 / Inv 8 等曲有真實的學派分歧**：自動偵測不可能對所有 case 命中正確答案；**BACH_INV_OVERRIDES 之所以 hand-curated，正是為了承認這種歧義**。

6. **Articulation 系統暫不模型化**：Baroque non-legato 默認 vs Czerny legato 過度規定的歷史包袱，加上 per-piece variation，自動化收益不高；保留為未來方向。

7. **裝飾音 (trills/mordents) 是已知未解問題**：當前系統不處理；下一步優先做 (a) detect ornament markers in MXL (b) 為 trill segment 預留 specialized fingering（通常 3-2-3-2 或 4-3-4-3）。可參考 Donington table 與 Bach《Explication》。

8. **Voice independence → per-hand phrase 不對齊是正常**：mvt4 LH 抓到 m50 boundary、RH 沒抓到，與 fugue / counterpoint 傳統一致；不是演算法錯誤，是設計正確的反映。

詳見 [concept_fugue](concept_fugue.md)、[concept_counterpoint](concept_counterpoint.md)、[concept_subject_imitation_detection](concept_subject_imitation_detection.md)、[analysis_bach_inv_4_d_minor](analysis_bach_inv_4_d_minor.md)。

## Cross-references

[concept_counterpoint](concept_counterpoint.md)、[concept_fugue](concept_fugue.md)、[concept_subject_imitation_detection](concept_subject_imitation_detection.md)、[analysis_bach_inv_4_d_minor](analysis_bach_inv_4_d_minor.md)、[src_fux_gradus_ad_parnassum](src_fux_gradus_ad_parnassum.md)、[src_epochtimes_fugue_zhou_2005](src_epochtimes_fugue_zhou_2005.md)、*project_bach_inv_measure_mapping*。
