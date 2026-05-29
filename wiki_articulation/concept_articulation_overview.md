# Concept: Articulation Overview — 11 種類型 + 對 DP cost rule 的影響

> 來源：通用 articulation pedagogy + Neuhaus / Matthay / Czerny / 19 世紀理論家
> 引用方：本 wiki 所有後續 concept 頁的基礎參考
> 狀態：種子頁 v1，2026-05-29
> 觸發 case：score-claude DP 目前對 MXL `slur` / `articulation` elements 視而不見，需要先建知識基礎再規劃 cost rule 介入

## 1. 為什麼 articulation 對指法重要

兩個音之間怎麼連接（**connection style**），不只是表情問題，**直接決定可用的手指轉換策略**：

| Articulation | 物理動作 | 對指法的約束 |
|---|---|---|
| **Legato** | 前指還按、後指彈下、前指鬆 | 允許 finger substitution；不允許 hand jump |
| **Staccato** | 每音獨立、鬆指後再彈 | 允許 thumb cross / hand jump；substitution 無意義 |
| **Tenuto** | 持滿值、明顯壓重 | 同音換指禁用；強制 hold 此指 |
| **Marcato** | 強重音 + 短斷 | 偏好強指（1/2/3）下這個音 |

→ 沒看 articulation 的 DP = 所有音當 non-legato 處理 = 對 Bach 對位 OK（baroque 默認 non-legato）但對 Chopin lyrical 段 / Beethoven *cantabile* 標記段系統性失誤。

## 2. 11 種 articulation 完整 taxonomy

依「連接性 → 音長」光譜排序，從最連到最斷：

| # | 名稱 | 符號 | 操作型 (相對音長) | 中文常見譯 |
|---|---|---|---|---|
| 1 | **Legatissimo** | (極致連) | 100% + overlap | 極連 |
| 2 | **Legato** | slur `⌒` | 100% (full duration) | 連奏 |
| 3 | **Portato / Mezzo-staccato** | 點+slur | ~75% | 半連 |
| 4 | **Non-legato** | (無符號 Baroque 默認) | ~85% | 不連 |
| 5 | **Tenuto** | `–` | 100% + 壓重 | 持音 / 保持音 |
| 6 | **Staccato** | `·` | ~50% | 斷奏 |
| 7 | **Staccatissimo** | `▼` | ~25% | 極斷 |
| 8 | **Accent** | `>` | 不變音長，重音 | 重音 |
| 9 | **Marcato** | `^` | ~75% + 強重音 | 強調 |
| 10 | **Sforzando (sfz)** | `sfz` | 不變音長，突重音 | 突強 |
| 11 | **Fermata** | `𝄐` | extend ad lib | 延長 |

(註：1-7 是 connection 光譜；8-10 是 dynamic accent overlay；11 是 duration 修飾。可疊加，例如 `sfp` + tenuto 同一個音）

## 3. 時代 default 差異 (period-dependent baseline)

當 MXL **沒** articulation 標記時，假設什麼 default：

| 時代 | Default articulation | 對 DP 假設的影響 |
|---|---|---|
| **Baroque (1600-1750)** | non-legato (~85%) | 不假設 legato bias；DP 目前的行為相對正確 |
| **Classical (1750-1820)** | Mozart/Haydn balance — 短音 detache，長音 legato | 需以音長分類，短音允許 hand jump |
| **Romantic (1820-1900)** | legato 為主（除非標記 staccato）| 強烈假設 substitution-friendly；DP 目前對 Chopin Op.9-2 失誤的主因之一 |
| **Modernism (1900+)** | 必須有明確標記，無 default | 不適用 default 假設 |

→ 對於初中階目標曲目（[[../score-claude/memory/project_target_repertoire_intermediate]]）：
- Bach 2-voice (Baroque) → 目前 DP 預設行為合理
- Beethoven Op.49 (Classical) → 需引入音長 → articulation 推論
- Mozart K545 (Classical) → 同上
- → **Classical period default 推論是初中階 articulation 最關鍵的 missing piece**

## 4. 對 score-claude DP cost rule 的對應表

| Articulation | DP 受影響項 | 修改方向 | 對應 wiki 深入頁 |
|---|---|---|---|
| Legato 段 | `NOTE_RETENTION_PENALTY` (現 0.0) | 允許 substitution，substitution_bonus = +負值 (誘導) | [[concept_legato_substitution]] |
| Legato 段 | `INTRA_PHRASE_TRANSITION_SCALE` (現 1.0) | 不變或微增 (continuity 加重) | [[concept_legato_substitution]] |
| Staccato 段 | `INTRA_PHRASE_TRANSITION_SCALE` | 大幅放鬆 (× 0.5)，允許 hand jump | concept_staccato_hand_jump.md (待寫) |
| Staccato 段 | `THUMB_PASS_PHRASE_BUDGET` | 加寬 (×2) | concept_staccato_hand_jump.md |
| Non-legato (Baroque default) | (無修改) | 維持目前 DP 行為 | concept_baroque_non_legato.md (待寫) |
| Portato | (混合 legato/staccato 中間值) | 介於兩者；保守選 legato | concept_portato_mezzo_staccato.md (待寫) |
| Tenuto | `NOTE_RETENTION_BONUS` | 強制持指（substitution_penalty = +∞） | concept_tenuto_hold.md (待寫) |
| Accent (`>`) | 偏好強指 | 該音 finger ∈ {1, 2, 3} 加 cost bonus | concept_accent_voicing.md (待寫) |
| Marcato (`^`) | 同 accent + 短斷 | accent + staccato 雙修飾 | concept_accent_voicing.md |
| Sforzando | 同 accent，但更強 | accent_weight × 2 | concept_accent_voicing.md |
| Fermata | duration override | extend duration 至 ≥ 2× original | (邊緣 case，暫不單獨開頁) |

## 5. Articulation 訊號從哪來

| 訊號源 | 可靠度 | 取得方式 |
|---|---|---|
| **MXL `<slur>` element** | 高（編輯者明確標記） | music21 `note.slurs` 或 `note.spannerSites` |
| **MXL `<articulation>` element** | 高（同上）| music21 `note.articulations` |
| **MXL `<notations>/<accent>`** | 高 | music21 `note.articulations` (Accent 類) |
| **編輯者推斷 / urtext editorial** | 中（會有 edition 差異）| 同上但需 edition 標記 |
| **音長 + 時代推論**（無明確標記時）| 中（fallback）| 自訂規則：短音 + Classical = staccato 嫌疑、長音 + Romantic = legato 嫌疑 |
| **演奏家詮釋傳統** | 低（不入 DP）| 不應 hard-code |

→ DP hook 點：在 head dict 建構時讀 `note.articulations` 與 `note.slurs`，存入 `head["articulation"]` 與 `head["slur_id"]`。後續 cost rule 條件式讀此欄位。

## 6. 與 wiki_phrase 的邊界

Articulation 影響的「分段」不是 phrase boundary：

| 分段類型 | 來自 | DP 行為 |
|---|---|---|
| **Phrase boundary** | wiki_phrase 五軸 (rest gap / pitch jump / cadence / subject / texture / figural) | DP 樂句間獨立優化，free hand reposition |
| **Slur boundary** | articulation slur start/end | DP 不切樂句；只調整 cost rule conditional |
| **Articulation marking start** | 個別音符標記 (staccato / tenuto / accent) | DP 不切樂句；只調整該音 cost |

→ Slur 結束**通常**不是 phrase 結束（Chopin lyrical 段一個 phrase 可有多個 slur 子分句；Bach 一個 figure 可橫跨 slur 邊界）。**Articulation 是 within-phrase 屬性，不是 phrase 切分訊號。**

例外：超長 slur（如 Wagner / Liszt 整段持續 slur）等同 phrase boundary 標記 — 但屬罕見浪漫派情境，初中階目標曲目不太遇到。

## 7. 對既有 cost rule 的 retrofit 影響評估

當 articulation cost rule 引入後，現有 cost rule 需重新檢視：

| 既有 rule | 是否需要 articulation 條件化 | 理由 |
|---|---|---|
| `NOTE_RETENTION_PENALTY` (現 0.0) | 是 | legato 段應 bonus，staccato 段保持 0 |
| `THUMB_PASS_PHRASE_BUDGET` | 是 | staccato 段加寬 |
| `WRIST_EXT_PHRASE_BUDGET` | 否 | wrist extension 與 articulation 解耦 |
| `STEP_AGILITY_WEIGHT` | 否 | velocity-driven，與 articulation 不直接相關 |
| `PINKY_BLACK_MELODY_PENALTY` | 可選 | accent 段該音若為 pinky 應加重 penalty |
| `RH_F3F4_EXTRA_COST` | 否 | 解剖學常數，不變 |
| `THUMB_PASS_UPWARD_EXTRA` | 否 | 解剖學常數 |

→ 多數既有 cost rule 是純解剖學，不受 articulation 影響。只有 substitution-friendly / hand-jump-friendly 兩類 rule 是 articulation-sensitive。

## 8. 未解 questions / 待 ingest 來源

- 不同教學派系（Russian / German / French）對「legato」程度的詮釋差異 — 待 ingest Neuhaus + Czerny + (Russian-school 待找)
- 編輯者標記與 urtext 不一致時的處理 — 待 ingest Henle / Bärenreiter editorial principles
- 演奏家 articulation vs 樂譜標記 — 待 ingest Brendel + Schiff essays (Beethoven articulation 詮釋差異)
- Articulation 與 ornament（trill / mordent）互動 — 待 ingest Donington《Baroque Music: Style and Performance》

## 9. 與其他 wiki 頁面的關係

- [[index]] — 本 wiki 入口
- [[concept_legato_substitution]] — legato 條目深入版（最大 DP 衝擊）
- [[../wiki_phrase/concept_figural_boundary_detection]] — figure 邊界與 slur 邊界的區分（兩者不一定重合）
- [[../wiki_piano/concept_thumb_technique]] — staccato 段 thumb-cross 放鬆與 thumb 解剖學的對位
- [[../score-claude/memory/project_target_repertoire_intermediate]] — 為何 Classical period default 推論最關鍵
