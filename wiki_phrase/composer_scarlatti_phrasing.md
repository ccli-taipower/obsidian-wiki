# Composer: Scarlatti 樂句分段

> 來源：Kirkpatrick《Domenico Scarlatti》(1953), Sutcliffe《The Keyboard Sonatas of Domenico Scarlatti and Eighteenth-Century Musical Style》(2003)
> 引用方：[[../wiki_articulation/concept_non_legato_baroque]], [[composer_bach_phrasing]]（Baroque 對比）

## 1. Scarlatti 樂句的特殊性

Domenico Scarlatti (1685-1757)（與 J.S. Bach 同年生）樂句結構**極度獨特**：
- 555 首單樂章 **keyboard sonatas** — 數量驚人 + 風格多樣
- **Binary form** (AABB) 結構為主，與 sonata form 不同
- **不規則樂句長度** — 9-bar, 11-bar, 13-bar phrase 並存
- **Iberian 影響**：吉他模仿、Andalusian cadence、flamenco-like 節奏

→ Scarlatti 不能套用 Bach (對位) 或 Mozart (sonata form) 的樂句邏輯。

## 2. Scarlatti 樂句邏輯的核心特色

⚠ Training-data verification needed:

### 2.1 Binary form 是樂句結構基礎

每首 Scarlatti sonata 標準 AABB 結構：
- **A 段**: 主調 → 屬調 (或關係調)，內部多個樂句
- **A 重複**
- **B 段**: 從屬調回主調，含 development-like 段
- **B 重複**

→ 樂句層級：phrase < section A < whole binary form。

### 2.2 不規則 phrase length

⚠ Training-data verification needed: 與 Bach（規則 sequence）或 Mozart（規則 4-bar）不同，Scarlatti phrase 經常**不規則**：
- 5-bar / 7-bar / 9-bar / 11-bar 並存
- 同一 sonata 內 phrase length 可變化
- 似乎反映**舞蹈節奏 + 吉他模仿** 的靈活性

對 [[concept_hypermeter]] 的適用：Scarlatti 段**不適合** 4-bar fallback — 需要 cadence-based phrase detection。

### 2.3 Iberian + 吉他模仿

⚠ Training-data verification needed: Scarlatti 大量曲目模仿西班牙 / 葡萄牙 musical idioms：
- 吉他 rasgueado（連續和弦 strumming）
- Andalusian cadence (vi - V - iv - III)
- Flamenco-like rhythmic motifs
- Cross-rhythm (3:2 / 2:3 polyrhythm)

對指法的意涵：Iberian 段 **articulation 偏 detache**（模仿吉他撥弦），與 Italian opera-style 抒情段對比。

### 2.4 Hand-crossing 技巧

Scarlatti 著名**hand-crossing** (兩手交叉) 技巧：
- 一手跨越另一手到對側音域
- 樂句結構與 hand-crossing 同步
- 需要 hand-distribution 特殊處理

對指法系統：是 [[../wiki_piano/concept_hand_distribution]] 的早期典範。

## 3. Scarlatti sonatas 重要曲目 ⚠

⚠ Training-data verification needed:

| K (Kirkpatrick) | 別名 | 樂句特性 |
|---|---|---|
| K.1 (d minor) | "Allegro" | 早期 — 較簡單 binary form |
| K.9 (d minor) | "Pastoral" | Lyrical, intermediate |
| K.27 (b minor) | — | Hand-crossing 技巧 |
| K.119 (D major) | — | Iberian rhythm |
| K.141 (d minor) | "Toccata" | Repeated notes virtuoso (Liszt *La Campanella* 靈感來源)|
| K.380 (E major) | "Cortège" | Lyrical + slow, intermediate-advanced |
| K.466 (f minor) | — | 浪漫 lyrical |
| K.466 / K.481 | — | 雙手對話 |

→ Scarlatti sonatas 多為 intermediate 範圍 — 是 [[../score-claude/memory/project_target_repertoire_intermediate]] 潛在候選。

## 4. Scarlatti articulation 標記

⚠ Training-data verification needed:

Scarlatti 原譜 articulation 標記**極少**（典型 Baroque 默契：依時代 default）：
- 幾乎無 slur
- 偶見 staccato dot（特別 detache 段）
- 無 tenuto / accent

→ 演奏家完全依 [[../wiki_articulation/concept_non_legato_baroque]] default 處理 + 依**段落性格**（Iberian vs Italian）做 articulation 詮釋。

## 5. Scarlatti 與 Bach 的 Baroque 對比

⚠ Training-data verification needed:

| 屬性 | Bach (德國 Baroque) | Scarlatti (Iberian Baroque) |
|---|---|---|
| 樂句結構 | 對位主導，subject + counterpoint | Binary form, 不規則 phrase |
| Texture | 對位 (2-3 voice) | Homophonic + Iberian texture |
| 樂句 length | 規則 + 對稱 (序列為主) | 不規則 + 自由 |
| Articulation default | non-legato (典型 Baroque) | non-legato + Iberian 啟發 detache |
| 演奏 fingering 慣例 | thumb-pass + 5-finger | hand-crossing 特殊技巧 |
| 教學優先 | 對位教學 | 風格多樣 + 技巧訓練 |

兩者同為 Baroque，但風格完全不同。

## 6. 演奏家 Scarlatti 詮釋

⚠ Training-data verification needed:

| 演奏家 | Scarlatti 風格 |
|---|---|
| **Horowitz** | Virtuoso + 個性化 — 著名 Scarlatti 演奏家 |
| **Mikhail Pletnev** | 細膩 + 結構性 |
| **Christian Zacharias** | Iberian 風格突出 |
| **Scott Ross** | HIP 派 (harpsichord 演奏全 555 sonatas) |
| **Yuja Wang** | 速度 + 戲劇性 |

## 7. 對 score-claude DP 的意涵

Scarlatti 對 score-claude DP 的對應：
- 多數 intermediate 範圍 — 是潛在啟用對象
- 樂句結構不規則 → 需依 cadence-based 偵測
- Iberian articulation → 未來 v3 candidate：Iberian-style detection
- Hand-crossing → [[../wiki_piano/concept_hand_distribution]] 觸發 hand reassignment

未實作 Scarlatti specific rules。未來方向：取得 Scarlatti sonatas MXL → 驗證 cadence-based phrase detection。

## 8. 與其他 wiki 頁面的關係

- [[composer_bach_phrasing]] — 同為 Baroque 但風格對比
- [[concept_hypermeter]] — Scarlatti 不規則性 vs Mozart 規則性
- [[concept_cadence_detection]] — Scarlatti 段 phrase 偵測主要靠 cadence
- [[../wiki_articulation/concept_non_legato_baroque]] — Scarlatti Baroque default
- [[../wiki_piano/concept_hand_distribution]] — Scarlatti hand-crossing 技巧典範

## 9. ⚠ Training-data verification queue

- §2.2 Scarlatti phrase length 不規則性的學術文獻
- §2.3 Iberian 影響的具體 sonata 案例（K 數對應）
- §3 各 K 數 sonata 樂句結構的精確分析
- §6 演奏家詮釋差異的具體 recording 比較
