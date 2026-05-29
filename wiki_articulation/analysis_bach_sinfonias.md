# Analysis: Bach Three-Part Sinfonias (BWV 787-801) — Articulation 詮釋

> 來源：Donington《Baroque Music》§Bach polyphony, Schiff Bach lectures, Bischoff / Henle / Bärenreiter editions
> 對應 PIG：未列入
> 引用方：*project_target_repertoire_intermediate* §推薦曲目, [concept_articulation_in_polyphony](concept_articulation_in_polyphony.md) §對位

## 1. 為什麼挑 Sinfonias 作為 polyphonic articulation 案例

Bach Three-Part Sinfonias (BWV 787-801) = 15 首三聲部對位作品，與 Two-Part Inventions 同期創作（1723 *Aufrichtige Anleitung*）。理由：
- **比 Inventions 高一階**：3 聲部需處理 within-hand polyphony (一手承載兩聲部)
- 是 *project_target_repertoire_intermediate* 推薦曲目 — 學完 Inventions 的自然進階
- 對位 articulation **複雜度高** — RH 同時負載 melody + counter-melody，每聲部 articulation 可能不同
- Bach 三聲部寫作的精緻代表，articulation 詮釋仍是當代爭議

## 2. 與 Two-Part Inventions 的對比

| 屬性 | Two-Part Inventions | Three-Part Sinfonias |
|---|---|---|
| 聲部數 | 2 | 3 |
| 手分配 | RH 一聲部, LH 一聲部 | RH 2 聲部 + LH 1, OR RH 1 + LH 2 |
| Articulation 複雜度 | 中 | 高 — within-hand polyphony |
| 演奏難度 | 入門對位 | 進階入門對位 |
| 教學階段 | 初中階起點 | 初中階深化 |
| 主題密度 | 每首 subject 重複 5-10 次 | 同樣 |

→ Sinfonias 從 articulation 角度比 Inventions 更具挑戰。

## 3. Within-hand polyphony 的 articulation 處理

⚠ Training-data verification needed:

當 RH 同時演奏 melody (上聲部) + counter-melody (中聲部) 時：
- **melody (上)** 通常 legato 或略 cantabile
- **counter-melody (中)** 通常 non-legato 或 detache
- 同一手指可能要先處理「melody legato」再「counter-melody detache」（或反之）

對指法的意涵：
- 同一手指**不應**強制承擔兩個聲部的不同 articulation 需求
- 通常**分指**處理：melody 用 4-5（外側），counter-melody 用 1-2-3（內側）
- 例外：當 melody 跨越 counter-melody 音高範圍時，需要 voice crossing 處理

## 4. Sinfonias 中 articulation 詮釋的典型挑戰

### 4.1 三聲部同時呈現 subject

⚠ Training-data verification needed:
- Sinfonia 9 (F minor) 與 Sinfonia 11 (G minor) 中段有三聲部同時 subject statement
- 每聲部 articulation 應該**對等** — 都 detache 或都略 legato，不應該某一聲部「突出」
- 演奏家共識：Bach 三聲部 stretto 段強調**結構平衡**，不強調 voice ranking

### 4.2 Inner voice 處理

中聲部（middle voice）通常是「**結構性內聲部**」：
- 不是主旋律
- 不是純伴奏
- 是對位填充 + 和聲指示

對 articulation：通常 non-legato，但若與 melody 形成 sigh motif 等表情，可短暫 legato。

### 4.3 Subject 在不同聲部出現的 articulation 一致性

Bach 對位作品的詮釋傳統：subject 每次出現的 articulation 應該**一致**（即使在不同聲部）。
- RH subject 用某 articulation → LH 後來 subject statement 應用同 articulation
- 確保聽眾能識別 subject 的「**主題身份**」

## 5. Audiveris MXL 對 Sinfonias 的 articulation 抓取

⚠ Bach Sinfonias 多數 edition（Bischoff / Henle 等）原譜 articulation 標記與 Inventions 相同 — 接近 0 slur, 接近 0 articulation marker。Audiveris OMR 對這些印刷品 articulation 抓取率預期同 Inventions（接近 0）。

→ 對 score-claude DP 的意涵：Sinfonias 啟用 [concept_legato_substitution](concept_legato_substitution.md) = no-op（無訊號）。圖法系統對 Sinfonias 主要依賴 [concept_non_legato_baroque](concept_non_legato_baroque.md) default 處理。

## 6. 對 score-claude DP 的 within-hand polyphony 限制

score-claude DP 目前**不處理 within-hand polyphony**：
- 把單手序列當單一聲部排序處理
- 不識別 voice crossing 或 voice-distinct articulation

對 Sinfonias 的影響：
- 兩聲部都在同一手時，DP 把它們混為一序列
- Articulation rule 對「混合序列」啟用，可能不符任何單一聲部的最佳指法

→ 是 known 限制，Sinfonias 屬「**邊緣難度**」for score-claude 當前架構。未來改進方向：voice-aware DP（將是 architectural 變更，非小修正）。

## 7. 演奏家對 Sinfonias 詮釋的經典版本

⚠ Training-data verification needed:

| 演奏家 | Sinfonias 詮釋風格 |
|---|---|
| **Glenn Gould** | 極度 detache，每聲部清晰，articulation 對比鮮明 |
| **András Schiff** | 較 cantabile，articulation 隨表情變化 |
| **Wanda Landowska** | Harpsichord 演奏，本來就 non-legato，articulation 由 voicing 而非觸鍵體現 |
| **Angela Hewitt** | 平衡 — 對位清晰 + 表情兼顧 |
| **Anton Rubinstein 學派** | 19 世紀浪漫派化處理，較多 editorial slur |

## 8. 每首 Sinfonia 的 articulation 詮釋簡述

⚠ Training-data verification needed:

| Sinfonia | Key | Articulation 特性 |
|---|---|---|
| 1 | C major | 簡單對位，default non-legato |
| 4 | D minor | 沉重，慢動作，部分 cantabile 段 |
| 5 | Eb major | 抒情，較 legato 詮釋空間 |
| 9 | F minor | **半音變化激烈**，articulation 詮釋難度高 |
| 11 | G minor | 對位密集，三聲部 stretto 多 |
| 15 | B minor | 結尾首，戲劇 cadential extensions |

## 9. 與其他 wiki 頁面的關係

- *project_target_repertoire_intermediate* §推薦曲目 — Sinfonias 在 in-scope list（進階入門）
- [concept_articulation_in_polyphony](concept_articulation_in_polyphony.md) — 三聲部 within-hand polyphony 是本頁主要挑戰
- [concept_non_legato_baroque](concept_non_legato_baroque.md) — Baroque default 對 Sinfonias 同樣適用
- [analysis_bach_inv_articulation](analysis_bach_inv_articulation.md) — Inventions 是 Sinfonias 的入門先導
- [../wiki_phrase/concept_fugue](../wiki_phrase/concept_fugue.md) — Fugue 是 Sinfonias 結構的延伸
- [src_donington_baroque_music](src_donington_baroque_music.md) — Donington 對 Bach 對位 articulation 的處理

## 10. ⚠ Training-data verification queue

- §3 within-hand polyphony 在 Sinfonias 各首的具體段落
- §6 score-claude voice-aware DP 是否值得實作
- §8 每首 Sinfonia articulation 詮釋特徵（演奏家共識）
