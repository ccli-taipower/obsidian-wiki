# Concept: Pedaling 與 Articulation 的互動 — 最常見的混淆

> 來源：Neuhaus《The Art of Piano Playing》§pedaling, Banowetz《The Pianist's Guide to Pedaling》(1985), Brendel essays §pedal
> 引用方：[[concept_legato_substitution]] §6（不依賴 pedal 隱藏 broken-finger）

## 1. 核心混淆 — 「踏板 legato」≠ 真正 legato

最常見學生錯誤：「**這段反正踩 sustain pedal，所以可以隨便換指**」。這是錯的。

理由：
- Sustain pedal 確實會延長音 — 已經彈下的音不會在指尖鬆開時停止
- **但**：sustain pedal 不能掩飾**音與音的 attack 銜接**問題
- 如果用 finger A 彈下、鬆開、再用 finger A 彈下同音 — 中間的「鬆開」期間沒被 pedal 蓋過（pedal 只延長已奏出的音，新音的 attack 仍清楚可聞）
- 結果：**Pedal 下的「broken-finger 同音換指」聽起來仍是 broken**

→ Neuhaus / Brendel / Banowetz 共識：**Articulation 應由手指動作體現，不依賴 pedal 掩護**。

## 2. Pedal 與 articulation 的「無關性」原則

⚠ Training-data verification needed: Neuhaus 在 *The Art of Piano Playing* §pedal 章節主張：

> 「Pedal 是音響效果的修飾，**不**是 articulation 的替代。Articulation 標記永遠優先於 pedal 決定。Staccato 標記 + pedal 踩著仍應該以手指做出 staccato — pedal 提供共鳴 / 殘響，但 attack 的清晰度由手指決定。」

對指法的意涵：
- Legato 標記段：finger substitution 仍必要（不能用 pedal「假裝 legato」）
- Staccato 標記段：手指離鍵動作仍必要（即使 pedal down）
- Pedal 與 finger articulation **解耦**處理

## 3. 兩種典型錯誤

### 3.1 「Pedal-disguised broken legato」

- 段落要求 legato，學生用同指彈重複音 + 踩 pedal 補救
- 結果：pedal 共鳴 OK，但每次 attack 仍清晰可聞「**前音斷掉、後音重新開始**」
- 對訓練有素的耳朵：仍是 broken legato

### 3.2 「Pedal-blurred staccato」

- 段落要求 staccato，學生踩 pedal「為了聲音飽滿」
- 結果：staccato attack 仍在，但短斷的「停頓感」被 pedal 共鳴蓋過
- 結果是「**強奏 detache 加 reverb**」而非「staccato」

## 4. Sustain pedal 與 una corda 的區別

| 踏板 | 對 articulation 的影響 |
|---|---|
| **Sustain (right pedal)** | 延長音長 + 增加共鳴；不改變 attack |
| **Sostenuto (middle pedal)** | 選擇性延長已按下的音；同上 |
| **Una corda (left pedal)** | 改變 attack 音色（柔化 hammer）；間接影響 articulation 質感 |

對指法的意涵：una corda 段可能使 staccato attack 較不銳利 — 但這是音色問題，不改變指法決策。

## 5. Pedal 與 finger substitution 的特殊關係

⚠ Training-data verification needed:

某些案例下，pedal 提供 finger substitution 的「**輔助掩護**」：
- 浪漫派 lyrical 段，melody 同音重複時 substitution + pedal
- Pedal 在 substitution 切換瞬間提供共鳴「填補」極微小的 attack 不完美

但這是「**輔助**」而非「**替代**」— substitution 仍應該以手指做到，pedal 只是讓 substitution 不完美時聽不出來。Neuhaus 認為應該追求**不靠 pedal 也能 substitution legato**的技術。

## 6. Baroque 演奏 vs Pedal

⚠ Baroque 時代沒有現代 sustain pedal（鋼琴前的 harpsichord 無 pedal；clavichord 也無 modern sustain mechanism）。當代演奏 Baroque 時：
- HIP 派（[[src_donington_baroque_music]]）：**幾乎不踩 pedal**，articulation 完全靠手指
- 浪漫派傳統：用 pedal 但不應掩蓋 Baroque non-legato default

對指法的意涵：演奏 Bach 時不應依賴 pedal，所有 articulation 都應 finger-level 完成。score-claude DP 對 Bach Inv 啟用 legato substitution 時，假設**不靠 pedal 也要 legato** — 這是正確設計。

## 7. 對 score-claude DP 的意涵

- DP 不看 pedal marking（MXL 雖然有 pedal marking，DP 不基於此調整指法）
- DP 假設「**指法應該獨立於 pedal 體現 articulation**」
- 因此 substitution / hand jump / thumb cross 等決策**不應**因 pedal 出現而改變

例外：[[../score-claude/memory/project_texture_phase_2_2026-05-28]] — texture phase 2 中 pedal 訊號用於**樂句邊界偵測**（pedal release 段是 phrase boundary signal），不是 articulation。這兩用途分清楚。

## 8. 與其他 wiki 頁面的關係

- [[concept_legato_substitution]] §6 — substitution 不應依賴 pedal 隱藏的觀察
- [[src_neuhaus_art_of_piano]] §2.4 — Neuhaus 對 pedaling vs articulation 優先級的主張
- [[src_donington_baroque_music]] — Baroque 演奏中 pedal 使用的爭議
- [[../wiki_piano/concept_thumb_technique]] — thumb cross 與 pedal 互動
- [[../score-claude/memory/project_texture_phase_2_2026-05-28]] — score-claude texture phase 2 用 pedal release 偵測 phrase boundary
