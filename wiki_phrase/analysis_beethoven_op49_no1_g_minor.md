---
tags:
  - analysis
  - beethoven
  - sonatina
  - phrase
  - classical
  - homophonic
---

# Analysis: Beethoven Sonata Op.49 No.1 in G minor, mov1 (Andante) — Homophonic Texture 與 Subject 軸的 N/A

> 來源：musicology 文獻 + **clean kern→MXL 實跑偵測**（`input/reference/Op49No1_Beethoven_sonata19-1_Gm.musicxml`，1093 notes / 112 measures，craigsapp/beethoven-piano-sonatas，2026-06-03）
> 對應 program：reference/eval only（無 OMR pixel → 不走標注 pipeline，per *reference_mozart_kern_mxl_source*）；尚無 `SINGLE_PDF_PHRASE_FLAGS` 條目
> 狀態：**第一個 Sonatina-level Beethoven analysis 頁**（初中階目標曲目，*project_target_repertoire_intermediate*）；建立 *homophonic Classical* 分析框架（有別於 Bach 對位）

## 1. 為什麼挑這首

Op.49 No.1 是 Beethoven 的「sonata facile」之一，**初中階目標曲目核心**。它對 wiki 框架的價值在於建立 **homophonic Classical 分析範式**，與 Bach Inventions 的對位範式形成對照：

- **Subject-imitation 軸完全不適用**：homophonic 織體（旋律 + 伴奏）無 fugal subject re-entry — grounding 確認 subject **0 命中**（§3）
- **figural RH/LH 極度不對稱**：RH 41 boundaries vs LH **僅 3** — 這是 homophonic 織體的偵測 signature（旋律手 figural-rich、伴奏手 figural-sparse），與 Bach 兩手均衡的對位織體截然不同
- **正確分析軸是 cadence + sentence/period**，不是 subject/figural — 為 Classical 曲目確立軸選擇原則

## 2. 曲目基本資訊

- **Op.49 No.1**, 約 1797（出版 1805；早期作品，"leichte Sonate"）
- **G minor**（2 flats ✓），**mov1 Andante**，**112 小節**（clean reference）
- 形式：**Sonata form**（exposition / development / recapitulation）；mov2 為 G major Rondo
- 織體：homophonic — RH 歌唱旋律 + LH 分解和弦 / 和聲伴奏
- 教學定位：sonata form 入門 + Classical 歌唱句法；ABRSM/檢定常見初中階曲目

## 3. 偵測軸 grounding — subject N/A，figural 不對稱

| 手 | subject@0.8 | subject@0.7 | figural |
|---|---|---|---|
| **RH** | **0** | **0** | **41**（m3, m4, m9, m11, m12, m14, m15, m16…）|
| **LH** | **0** | **0** | **3**（m12, m35, m74）|

**關鍵觀察 — homophonic 織體 signature**：
- **subject 0/0**：homophonic Classical 無對位 subject re-entry。`_detect_subject_entries` 從 RH 開頭抽 template，但歌唱旋律的 interval signature 不會在他處精確重現（主題再現是 *thematic return*，伴隨織體變化，非 TI-invariant 模仿）→ 0 命中為正確行為
- **figural RH 41 / LH 3**：RH 旋律的 figure 切換頻繁（樂句、裝飾、音型），LH 分解和弦伴奏幾乎無 figural 邊界（連續均勻 pattern）→ **figural 不對稱比值本身就是 homophonic 織體的偵測指標**（對比 Bach Inv 11 的 RH40/LH30 對稱對位）
- → 設計意涵：Classical homophonic 曲目應走 **cadence + sentence/period 軸**（§4），subject 軸 N/A，figural 僅對 RH 旋律手有意義

## 4. 正確分析軸 — Cadence + Sentence/Period

Op.49 No.1 的樂句結構由 **Classical 句法**（[concept_classical_period_sentence](concept_classical_period_sentence.md)）+ **終止式**（[concept_cadence_detection](concept_cadence_detection.md)）描述：

| Classical 句法元素 | 在 Op.49 No.1 的角色 |
|---|---|
| **Period（樂段）** | 主題呈示常為 antecedent（半終止 HC）+ consequent（完全終止 PAC）對稱 8 小節 |
| **Sentence（樂句）** | presentation（2+2 基本動機）+ continuation（fragmentation → cadence） |
| **PAC** | exposition 第一主題 / 第二主題終點、recap 終點 → phrase boundary 高信心訊號 |
| **HC** | antecedent 結尾、development 前的屬準備 |

→ 這正是 [concept_cadence_detection](concept_cadence_detection.md) Phase 2（music21 roman on measure-final chord）的適用場景；與 Mozart K283/K545（[analysis_mozart_k283_first_mov](analysis_mozart_k283_first_mov.md)）同屬 Classical sonata cadence 範式。

### 4.1 Cadence detection 實跑輸出（2026-06-03）

`_detect_cadence_boundaries`（整曲 key=g minor）在 reference MXL 上的命中：

| measure | 類型 | 角色 |
|---|---|---|
| m3, m11 | IAC | presentation 層內小終止 |
| **m9** | **PAC** | **第一主題 / period consequent 收束**（高信心 phrase boundary）|
| m66, m72, m74 | IAC | recapitulation 區終止 cluster |
| m103 | IAC | coda 接近 |

⚠ **modulation 限制**：偵測用**整曲單一 key（g minor）**，故 exposition 第二主題在 **B♭ major（relative major）的 cadence 抓不到 PAC**（在 B♭ 是 V→I，但在 g minor 框架下不成立）。這正是 [concept_cadence_detection](concept_cadence_detection.md) deferred 的 *windowed key analysis for mid-piece modulation* 的代表案例（Cadence Phase 3 候選）。

## 5. Sonata form 段落（cadence-grounded）

| 段落 | 小節 | 調性 | 角色 | cadence 佐證 |
|---|---|---|---|---|
| **Exposition** | m1–m~34 | g minor → B♭ major (III) | 第一主題（g，PAC m9）→ 過渡 → 第二主題（B♭）| PAC m9 ✓；B♭ cadence missed（modulation 限制）|
| **Development** | m~35–m~63 | 多調離轉 | 主題動機 fragmentation（LH figural m35/m74）|（離調區，無 home-key cadence）|
| **Recapitulation** | m~64–m112 | g minor（回主調）| 主題再現 + coda | IAC cluster m66/72/74 + coda m103 ✓ |

→ cadence cluster（m66-74）與 recap 起點吻合，PAC m9 標出 exposition 第一樂段收束；form 表已由 cadence grounding 佐證（非純文獻推定）。

## 6. 與其他 wiki 頁面的關係

- **第一個 Sonatina-level 頁**，與 [analysis_beethoven_op49_no2_g_major](analysis_beethoven_op49_no2_g_major.md) 構成 Op.49 雙頁
- 對 [composer_beethoven_phrasing](composer_beethoven_phrasing.md) 提供早期 leichte Sonate 的 homophonic 範例
- 與 Bach Inv 對照：homophonic（subject N/A、figural 不對稱）vs 對位（subject 適用、figural 對稱）— 支持 *feedback_phrase_analysis_is_its_own_discipline*「不同曲目主導軸不同」
- 正確軸依 [concept_classical_period_sentence](concept_classical_period_sentence.md) + [concept_cadence_detection](concept_cadence_detection.md)；Classical form 理論引 *src_caplin_classical_form*
- 與 [analysis_mozart_k283_first_mov](analysis_mozart_k283_first_mov.md) 同屬 Classical sonata cadence 範式
- clean reference 來源依 *reference_mozart_kern_mxl_source*；目標曲目定位依 *project_target_repertoire_intermediate*
