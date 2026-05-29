# Analysis: Bach Two-Part Inventions — Articulation 詮釋

> 來源：Donington《Baroque Music》、Türk《Klavierschule》、Bischoff / Mikuli / Henle / Bärenreiter editions 比較、Schiff 演奏實踐
> 對應 PIG：未列入 / 教學用 Inv 1, 4 在 wiki_phrase 有專頁
> 引用方：[[../wiki_phrase/analysis_bach_inv_1_c_major]] §articulation, [[concept_non_legato_baroque]] §例外 Bach legato 段, [[concept_period_defaults]] §Baroque

## 1. 為什麼挑 Bach Inventions 作為 Baroque articulation 案例

理由：
- Bach 2-voice Inventions 是初中階學生最早接觸的對位作品（[[../score-claude/memory/project_target_repertoire_intermediate]]）
- Bach 自己沒在 Inventions 上寫多少 articulation 標記 — 演奏者必須依**時代 default**詮釋
- 不同 edition 對「該加什麼 slur」分歧巨大 — 是研究 editorial slur 汙染的最佳案例

## 2. Bach 原譜 articulation 標記分布 ⚠

⚠ Training-data verification needed: Bach 1723 *Aufrichtige Anleitung* 手稿（Inventions 原始版）articulation 標記極少：

| Inv | 原譜 slur 數量（估）| 原譜 articulation 標記 |
|---|---|---|
| Inv 1 (C major) | 幾乎無 | 無 staccato / tenuto / accent |
| Inv 4 (D minor) | 偶爾 sigh motif 短 slur | 同上 |
| Inv 8 (F major) | 同 Inv 1 | 同上 |
| 全部 15 mvts 平均 | 每首 < 5 個 slur | 接近 0 articulation 標記 |

→ 結論：演奏 Bach Inventions 時，**沒有 slur 標記是常態**，演奏者必須依 [[concept_non_legato_baroque]] default 處理。

## 3. 不同 edition 的 articulation 編輯傾向

| Edition | Slur 補加量 | 風格 |
|---|---|---|
| **Bärenreiter NBA** | 最少 — 接近原稿 | Urtext，最 conservative |
| **Henle Urtext** | 少 — 區分原譜 vs editorial | Urtext，標 editorial slur 用括號 |
| **Wiener Urtext** | 中等 | 中性學術版 |
| **Bischoff (Steingräber 1880)** | 大量 — 19 世紀浪漫派化 | 19 世紀演奏傳統的痕跡 |
| **Mikuli (Schirmer 1894)** | 大量 — 加 slur + fingering 編輯 | 19 世紀浪漫派化 |
| **Czerny 編 (1840s)** | 中等 — Czerny 學派詮釋 | 19 世紀但較克制 |
| **Landowska 版** | 中等 — harpsichord-aware | HIP-influenced |

→ **使用建議**：score-claude DP 對 Bach Inventions MXL 應**優先使用 Bärenreiter / Henle Urtext** 來源；避免基於 Bischoff / Mikuli MXL 的過度 legato substitution。

## 4. Bach Inventions 中的「**例外 legato 段**」⚠

⚠ Training-data verification needed: 雖然 non-legato 是默認，部分 mvts / 段落應 legato 處理：

| Mvt | Legato-適用段落 | 理由 |
|---|---|---|
| **Inv 4 (D minor) Adagio 段** | mvt4 是 3/8 但帶有 slow 性格 | 慢速暗示 legato（Donington §慢板原則）|
| **Inv 5 (Eb major)** | 部分 cantabile 旋律段 | Bach 寫得抒情，現代演奏家普遍 legato 詮釋 |
| **Inv 11 (G minor)** | Chromatic descending 段 | 半音下行常 legato (sigh 表情) |
| **Sigh motif (Inv 4, Inv 7, Inv 13)** | 2-音 下行（appoggiatura-resolution）| Baroque 表情慣例就是 legato 2-音 sigh |

對指法的意涵：這些段落應 honor [[concept_legato_substitution]] rule，即使 MXL 沒明確 slur 標記。但 score-claude DP 目前無法**自動判斷**這些段落 —— 需要 manual per-mvt opt-in 或 editorial slur 訊號。

## 5. Audiveris MXL 對 Bach Inventions 的 articulation 抓取

從 score-claude 實測（2026-05-29）：
- Audiveris MXL 從 Bach Inventions Contrapunctus Press PDF 抓出的 slur 數 = **0**
- Articulation marker（staccato / tenuto / accent）數 = **0**

可能原因：
1. 原 Contrapunctus Press PDF 是 19 世紀 edition，本來就少標記
2. Audiveris OMR 對 Baroque 細小標記辨識率低
3. Bach 原稿確實無這些標記

→ 對 score-claude DP 的意涵：對 Bach Inv 啟用 [[concept_legato_substitution]] **基本 no-op**（無 slur 訊號）。其他 articulation 規則對 Bach Inv 也預期 no-op。Bach Inventions 是「**non-legato default 應該主導**」的案例。

## 6. 每首 Inv 的 articulation 詮釋建議

⚠ 簡化建議，演奏家詮釋差異仍大：

| Inv | 推薦 articulation 風格 | 典型演奏家對比 |
|---|---|---|
| 1 C major | non-legato + slight detache | Gould (very detache) vs Schiff (slight legato) |
| 2 C minor | 對位 detache，subject 略 legato | 同上對比 |
| 3 D major | non-legato + 16th-note 段 detache | — |
| 4 D minor | sigh motifs legato, 其餘 non-legato | — |
| 5 Eb major | 較 legato（cantabile 性格）| Hewitt (legato), Gould (non-legato) |
| 6 E major | strict canon — 每聲部清晰 non-legato | — |
| 7 E minor | chromatic legato 段 + 餘 non-legato | — |
| 8 F major | non-legato，subject motif 略 detache | — |
| 9-15 | 普遍 non-legato 默認 | — |

## 7. 對 score-claude DP 的影響

| 觀察 | 對 DP 的意涵 |
|---|---|
| Bach Inv MXL 無 slur | [[concept_legato_substitution]] 在 Bach Inv 啟用 = no-op |
| 部分 mvt 內有 legato 段（Inv 4, 5, 7, 11）| 未來 v3：per-mvt 段落級 articulation override |
| Editorial slur 不可靠 | 若取得 Bischoff / Mikuli 的 MXL，**不應**啟用 legato substitution |

## 8. 與其他 wiki 頁面的關係

- [[concept_non_legato_baroque]] §6 — Bach 是 Baroque non-legato 主要曲目代表
- [[concept_period_defaults]] §5 — Bach editions 的編輯者 articulation 是 editorial slur 汙染最典型案例
- [[concept_legato_substitution]] §5 — Bach Inv 在「適用情境」表中標「部分適用（看 edition slur 標記）」
- [[../wiki_phrase/analysis_bach_inv_1_c_major]] 等 7 個 Bach Inv analysis 頁 — 樂句結構分析，本頁是 articulation 補充
- [[../wiki_phrase/src_bach_inventions_pedagogy]] — 多 edition pedagogy 比較
- [[src_donington_baroque_music]] — Donington 對 editorial slur 汙染的批評
- [[src_turk_klavierschule]] — Türk 18 世紀末文獻支持 Baroque non-legato default

## 9. ⚠ Training-data verification queue

以下基於 training-data + 一般 Bach edition 知識：
- §2 Bach 原譜各 Inv 的 slur 數量精確統計
- §3 各 edition 補加 slur 量的精確比較
- §4 哪些 mvt / 段落應 legato 的演奏傳統共識
- §6 演奏家對比表（Gould vs Schiff vs Hewitt 等）的具體段落 timestamps
