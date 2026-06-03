---
tags:
  - analysis
  - beethoven
  - sonatina
  - phrase
  - classical
  - homophonic
---

# Analysis: Beethoven Sonata Op.49 No.2 in G major, mov1 (Allegro ma non troppo) — Thematic Return ≠ Fugal Subject

> 來源：musicology 文獻 + **clean kern→MXL 實跑偵測**（`input/reference/Op49No2_Beethoven_sonata20-1_G.musicxml`，1523 notes / 122 measures，craigsapp/beethoven-piano-sonatas，2026-06-03）
> 對應 program：reference/eval only（無 OMR pixel → 不走標注 pipeline）；尚無 `SINGLE_PDF_PHRASE_FLAGS` 條目
> 狀態：第二個 Sonatina-level Beethoven analysis 頁
> 觸發 case：homophonic Classical 但 subject detector **有命中** — 揭示「thematic return ≠ fugal subject」的偵測語意混淆

## 1. 為什麼挑這首

Op.49 No.2 是 Beethoven 最知名的 sonatina-level 曲（mov1 主題後來用於七重奏 Op.20 Menuetto）。它對 wiki 框架的關鍵價值是一個**偵測語意陷阱**：

- 與 Op.49 No.1（subject 0/0）不同，**subject detector 在此曲有命中**（RH m5/m67/m71，LH m68，見 §3）
- 但這些命中是 **sonata form 的主題再現（thematic return / recapitulation）**，不是 fugal subject imitation
- → 揭示 `_detect_subject_entries` 在 homophonic Classical 上會把「主題在 recap 重現」誤報為「subject re-entry」— 兩者機制不同，**需要區分**

## 2. 曲目基本資訊

- **Op.49 No.2**, 約 1795–96（出版 1805；早於 No.1 作曲但同 opus）
- **G major**（1 sharp ✓），**mov1 Allegro ma non troppo**，**122 小節**（clean reference）
- 形式：**Sonata form**；mov2 為 G major Tempo di Menuetto（= Septet Op.20 主題）
- 織體：homophonic — RH 旋律 + LH Alberti / 和聲伴奏
- 教學定位：最普及的 sonatina 入門曲之一；ABRSM/檢定常見

## 3. 偵測軸 grounding — subject 有命中（但是 thematic return）

| 手 | subject@0.8 | subject@0.7 | figural |
|---|---|---|---|
| **RH** | **m5, m67, m71**（3）| m5, m67, m71, m94（4）| **48**（m2, m5, m6, m9, m13, m21, m22, m23…）|
| **LH** | **m68**（1）| m68（1）| **39**（m3, m13, m28, m37×3, m40, m49…）|

**關鍵觀察 — thematic return ≠ fugal subject**：
- RH subject 命中 **m5（presentation 內動機重複）、m67/m71/m94（development 末 + recapitulation 區）** — m67-71 正是 sonata form **recap 主題回歸**的位置
- LH m68 命中與 RH m67/71 同步 → 是 recap 的**整體主題回歸**，兩手一起回來（homophonic），不是對位中一手獨立 subject entry
- 對比 Bach 對位：fugal subject 是**一手獨立進入、移調、與另一手交織**；Classical recap 是**整體織體回到主題**。`_detect_subject_entries` 用 TI signature 比對，會把後者也抓到（主題再現的 interval signature 自然與開頭一致）
- → 設計意涵：subject detector 的命中在 homophonic 曲目應**重新詮釋為 thematic-return boundary**（仍是合法 phrase boundary！只是語意是「主題回歸」非「對位模仿」）。若未來要區分，需加 texture/voice-independence 判斷
- **figural RH48 / LH39**：比 No.1（RH41/LH3）對稱得多 — 因 No.2 LH 是 Alberti bass（有規律 figure 切換）而非 No.1 的長分解和弦；Alberti 的 figural 邊界較密

## 4. 正確分析軸 — Cadence + Thematic Boundary

| 軸 | 在 Op.49 No.2 的角色 |
|---|---|
| **Cadence (PAC/HC)** | sonata form 結構主軸（[concept_cadence_detection](concept_cadence_detection.md)）|
| **Sentence/Period** | 主題句法（[concept_classical_period_sentence](concept_classical_period_sentence.md)）|
| **Thematic return** | subject detector 的命中（m67-71 recap）可作 recapitulation boundary 訊號 — 但須標記為「主題回歸」語意 |
| **Texture (Alberti)** | LH Alberti bass 是 homophonic 標記；[concept_texture_change_detection](concept_texture_change_detection.md) 可偵測伴奏型轉換 |

### 4.1 Cadence detection 實跑輸出（2026-06-03）

`_detect_cadence_boundaries`（整曲 key=G major）命中：**PAC m103, m107, m113, m122** — 全部 cluster 在曲末（recap 後段 + coda，回主調 G major）。

⚠ **modulation 限制（本曲是最明顯案例）**：exposition 第二主題在 **D major（V）** 的 cadence **全部抓不到**（整曲 key=G major 框架下 D 的 V→I 不成立）。故 cadence 只在**回到主調的 recap/coda** 才出現 → tonic-PAC cluster m103-122 反而**佐證 recapitulation 在主調收束**。與 §3 subject hits（recap m67/71）+ 此 PAC cluster 交叉印證 recap 範圍 m67→末。

## 5. Sonata form 段落（subject + cadence grounded）

| 段落 | 小節 | 調性 | 角色 | grounding 佐證 |
|---|---|---|---|---|
| **Exposition** | m1–m~36 | G major → D major (V) | 第一主題（G）→ 過渡 → 第二主題（D）| D-major cadence missed（modulation 限制）|
| **Development** | m~37–m~66 | 多調離轉 | 動機發展（figural 密集區 m37×3）|（離調，無 home-key cadence）|
| **Recapitulation** | m~67–m122 | G major（第二主題回主調）| **主題回歸 + coda** | subject hits m67/71 + tonic PAC cluster m103/107/113/122 ✓✓ |

→ recap 範圍由**兩個獨立軸交叉佐證**：subject detector（thematic return m67/71，§3）+ cadence detector（tonic PAC cluster m103-122）。這是 homophonic 曲目用 *thematic-return + cadence* 雙軸定位 form 的範例。

## 6. 與其他 wiki 頁面的關係

- 與 [analysis_beethoven_op49_no1_g_minor](analysis_beethoven_op49_no1_g_minor.md) 構成 Op.49 雙頁：No.1 = subject 0（純 homophonic），No.2 = subject 命中但為 thematic return
- 對 [concept_subject_imitation_detection](concept_subject_imitation_detection.md) 提供 **「homophonic thematic return 被誤報為 subject」** 的關鍵語意 case（命中合法但語意需重詮釋）
- 對 [concept_texture_change_detection](concept_texture_change_detection.md) 提供 Alberti bass homophonic 標記
- 對 [composer_beethoven_phrasing](composer_beethoven_phrasing.md) 提供最普及 sonatina 範例（+ Septet Op.20 主題淵源）
- 正確軸依 [concept_cadence_detection](concept_cadence_detection.md) + [concept_classical_period_sentence](concept_classical_period_sentence.md)
- clean reference 來源依 *reference_mozart_kern_mxl_source*；目標曲目定位依 *project_target_repertoire_intermediate*；分析獨立性依 *feedback_phrase_analysis_is_its_own_discipline*
