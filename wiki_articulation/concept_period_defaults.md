# Concept: Period Defaults — 無 articulation 標記時各時代假設

> 來源：Türk *Klavierschule* (1789)、C.P.E. Bach *Versuch* (1753)、Brendel essays §Beethoven articulation 詮釋、Donington *Baroque Music: Style and Performance*、Czerny *Op.500*
> 引用方：[[concept_articulation_overview]] §3、[[concept_non_legato_baroque]] §5

## 1. 為什麼需要時代 default

樂譜常常不會明確標記每個音的 articulation — 只有部分音帶 slur / staccato / tenuto / accent 標記，其餘音「沒有指示」。

「沒有指示」不等於「沒有 articulation」。演奏家會依**時代慣例**填補空白。同一段「沒標記」的旋律，Bach 時代演奏成 non-legato，Chopin 時代演奏成 legato，是不同的 default 假設。

指法系統如果要做時代-sensitive 的決策，必須先有「無標記 = ?」的對應表。

## 2. 四時代 default 對應

| 時代 | 年份範圍 | 無標記時假設 | 操作型音長 | 對指法的意涵 |
|---|---|---|---|---|
| **Baroque** | 1600–1750 | non-legato（[[concept_non_legato_baroque]]）| ~85% | 不誘導 substitution；不誘導 hand jump |
| **Classical** | 1750–1820 | 音長相關平衡 — 短音 detache，長音 legato | 短音 ~70%、長音 ~95% | 對短音允許 hand jump、對長音偏好 substitution |
| **Romantic** | 1820–1900 | legato 為主 | ~100% | 強烈誘導 substitution；限制 hand jump（除非標記 staccato）|
| **Modernism** | 1900+ | 無 default — 必須明確標記 | 信樂譜原文 | 不做時代推論 |

## 3. 各時代代表作曲家

依時代 default 對應的曲目選擇：

| 時代 | 代表作曲家 | 典型曲目 |
|---|---|---|
| **Baroque** | J.S. Bach, Handel, Scarlatti, Couperin | Bach Inventions, Sinfonias, French Suites |
| **Classical** | Haydn, Mozart, Beethoven (early)** | Mozart sonatas, Beethoven Op.49, Haydn sonatas |
| **Romantic** | Chopin, Schumann, Brahms, Liszt | Chopin Nocturnes, Schumann *Kinderszenen* |
| **Modernism** | Debussy, Ravel, Bartók, Prokofiev | Debussy *Arabesques*, Ravel *Pavane* |

**Beethoven 的 articulation 跨期 — 早期 (Op.49) 接近 Classical default，後期 (Op.110-111) 帶有 Romantic 自由度，標記也更密集。

## 4. Classical 「音長相關平衡」的細節

Classical 時代是過渡期，default 不是單一規則，而是依音長分類：

| 音長 (QN) | 假設處理 | 為何 |
|---|---|---|
| **< 0.5 (16th note 以下)** | Detache（~70%）| 短音適合 articulation independence；浪漫派 cantabile 不適用 |
| **0.5 (eighth note)** | 短 detache 或 portato | 中間值，看上下文 |
| **1.0+ (quarter 以上)** | Legato（~95%）| 長音值需要 phrasing 連續性；substitution 適用 |

→ Classical 段落（Mozart sonatas, Beethoven Op.49 等）：指法系統可以**依音長**自動判斷 substitution 是否適用，不需明確 slur 標記。

## 5. 編輯者 articulation 與時代 default 的衝突

許多現代 edition 會「補上」原譜沒有的 articulation 標記：

| Edition 風格 | Articulation 風險 |
|---|---|
| **Henle / Bärenreiter Urtext** | 保留作曲家原譜；少 editorial slur | 低 |
| **Schirmer / Peters 19 世紀版** | 大量 editorial slur 對 Baroque 強加 legato | 高（破壞時代 default）|
| **Wiener Urtext** | 折衷 — 區分原譜與 editorial | 中 |
| **National Editions（Ekier, Chopin）** | 依 manuscript 原始；少 editorial | 低 |

→ 指法系統的最佳實踐：
- Baroque 曲目優先用 Urtext / Bärenreiter / Henle
- 不要因為 Schirmer Mikuli 加大量 slur 就對 Bach 觸發 legato substitution

## 6. 對指法系統的實作意涵

時代 default 推論若要落地，需要：

1. **時代判定**：作曲家出生 / 創作年份 → 時代分類
2. **per-時代 baseline 行為**：
   - Baroque 段落 → 不啟用 legato substitution rule
   - Classical 段落 → 啟用 substitution，但依音長條件化
   - Romantic 段落 → 強啟用 substitution
   - Modernism 段落 → 不推論，信樂譜
3. **與明確標記的互動**：明確 slur / staccato 標記永遠覆寫時代 default

實作風險：作曲家 metadata 在 MXL 不一定可靠（OMR 可能漏；editor 可能填錯）。指法系統需要 fallback 策略。

## 7. 對使用者的演奏意涵

了解時代 default 對使用者選曲與練習方式有實際影響：

- **學 Bach 之前**：理解 Baroque non-legato，不要強求「彈得很連」
- **學 Mozart 之前**：理解 Classical 平衡，短音和長音應該不一樣處理
- **學 Chopin 之前**：理解 Romantic legato，但具體的 substitution 細節仍需老師指導
- **學 Debussy 之前**：信樂譜每個標記，不要套用浪漫派 default

## 8. 與其他 wiki 頁面的關係

- [[concept_articulation_overview]] — 本頁的 parent 概覽
- [[concept_non_legato_baroque]] — Baroque default 的詳細展開
- [[concept_legato_substitution]] — Romantic default 觸發的主要規則
- [[concept_staccato]] — Classical 短音 default 對應的策略
- [[../wiki_phrase/composer_chopin_phrasing]] / [[../wiki_phrase/concept_chopin_lyrical_phrase]] — Chopin 浪漫派 articulation 的具體展開
- [[../score-claude/memory/project_target_repertoire_intermediate]] — 為何 Classical period default 對初中階目標曲目最重要
