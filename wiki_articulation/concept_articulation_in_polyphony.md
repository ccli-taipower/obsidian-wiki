# Concept: Articulation in Polyphony — 對位 texture 中各聲部的不同 articulation

> 來源：Donington《Baroque Music》§polyphony, Schiff Bach lectures（演奏實踐）, Bach 演奏傳統共識
> 引用方：[[analysis_bach_inv_articulation]] §對位, [[concept_non_legato_baroque]] §對位處理

## 1. 為什麼對位 texture 需要 articulation 分聲部處理

對位作品（Bach Inventions / Sinfonias / Fugues、Brahms inner-voice melody）的 texture 是**多條獨立旋律線同時進行**。每條線都有自己的：
- Phrase 結構
- 表情張力
- 觸鍵需求

**問題**：兩條同時進行的聲部，articulation 可能完全不同 — RH 同時要演奏 legato melody + LH 同時要演奏 detache 對位線，怎麼辦？

## 2. Bach 2-voice 對位 articulation 處理範式

⚠ Training-data verification needed:

### 2.1 Subject 與 Counterpoint 的 articulation 對比

Bach Inventions 中，**Subject (主題)** 與 **Counterpoint (對位線)** 通常用對比 articulation 區分：

| 聲部 | 典型 articulation | 為何 |
|---|---|---|
| Subject (出現處)| 略 legato 或 stronger detache | 突出主題輪廓 |
| Counterpoint | 更 non-legato 或 less articulated | 不喧賓奪主 |
| Episode 段 | 兩聲部對等 detache | 結構上 transition |

例：Inv 1 (C major) 開頭 RH subject 第一次出現時，演奏家常用**略 legato 的 detache**（每音清楚但有些連續感），LH 等到 m3 補入 subject 時也用同 articulation；其餘 counterpoint 段更平淡。

### 2.2 兩手 articulation 同步 vs 異步

| 模式 | 範例 |
|---|---|
| **同步** | 兩聲部同時 legato 或同時 detache（Inv 1 開頭）|
| **異步** | 一手 legato + 一手 detache（Inv 4 sigh motif 段，RH sigh legato 而 LH 16th-note detache）|
| **複雜對位** | 三聲部 Sinfonia 可能三聲部各自不同 articulation |

→ 對指法的意涵：當兩手 articulation 不同步，每手獨立 fingering 評估 — 不應強制兩手用同 articulation rule。

## 3. 對 score-claude DP 的意涵

DP 已經 per-hand 獨立優化 — 這對對位處理是天然優勢：
- RH 的 articulation rule 啟用情況不影響 LH
- LH 可以保持 non-legato default 即使 RH 啟用 legato substitution

對位 texture 的 DP 注意點：
- **不應啟用 cross-hand phrase coupling**（兩手 phrase boundary 不必一致）
- Articulation rule per-hand 條件化（slur_active 在 head 上 per-hand 設定）

## 4. 多聲部 within-hand 處理（罕見但存在）

某些情況下，**一隻手同時負載兩條獨立聲部**：
- Bach 三聲部 Sinfonia 中聲部由 RH 或 LH 負擔
- Beethoven 後期 inner voice melody（如 Op.110 mvt3）
- Brahms Intermezzi 大量內聲部

這時**單手內** articulation 處理變複雜：
- 旋律音可能 legato，伴奏音可能 detache
- 同一手指可能要連續處理「legato 旋律音 → detache 伴奏音」

對指法的意涵：score-claude DP 目前無法處理 within-hand 多聲部 articulation 區分 — 把單手序列當單一聲部處理。對 Bach 2-voice OK，對 Sinfonia + Beethoven inner voice 是 known 限制。

## 5. Per-voice articulation 詮釋傳統

⚠ Training-data verification needed:

### 5.1 Baroque 對位（Bach）

- 默認：non-legato for everything
- 例外：明確 slur 標記的段落
- 不同聲部 articulation 應**對等處理**（不是「主旋律 legato + 伴奏 staccato」這種浪漫派假設）

### 5.2 Classical 對位段（Mozart fugal、Haydn quartet-like 段）

- 較自由，主聲部可略 legato，副聲部維持 detache
- 但比 Romantic 對比更克制

### 5.3 Romantic 對位段（Brahms、Schumann）

- 主聲部 legato 為主
- 內聲部 / 副聲部仍可獨立 articulation
- 大量 cantabile 標記

## 6. 與其他 wiki 頁面的關係

- [[concept_non_legato_baroque]] §對位 — Baroque 對位 articulation 預設處理
- [[concept_legato_substitution]] §適用情境 — Romantic 對位段 legato 處理
- [[analysis_bach_inv_articulation]] — Bach 2-voice 具體案例
- [[../wiki_phrase/concept_counterpoint]] — 對位 texture 樂句結構分析
- [[../wiki_phrase/concept_fugue]] — Fugue subject 與 episode 結構區分
- [[../wiki_piano/concept_hand_distribution]] — 兩手 fingering 獨立性
