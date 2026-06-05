---
concept: 標準音階與琶音指法 (Standard Scale & Arpeggio Fingering)
date_created: 2026-06-05
tags: [piano_fingering, pedagogy, scales, arpeggios, thumb_under, convention]
---

# 標準音階與琶音指法 (Standard Scale & Arpeggio Fingering)

教學傳統的**基石**（見 `[[concept_pedagogical_fingering_tradition]]`）：音階與琶音的指法是每個學生反覆操練、最早內化的 pattern。本專案的 long-scale thumb-under 規則就是在近似這套慣例。

## 大調音階（白鍵調，C/G/D/A/E）

以 thumb-under 把 7 音分成 **3+4** 兩組：

| 手 | 上行（一個八度）| 下行 |
|---|---|---|
| **RH** | 1 2 3　1 2 3 4　(5 在頂) | 5 4 3 2　1 3 2 1 |
| **LH** | 5 4 3 2　1 3 2 1 | 1 2 3　1 2 3 4　(5 在底) |

- **RH 上行**：拇指在第 4 音（F）穿到第 3 指之下 → 1234 再接。下行則第 3 指跨過拇指。
- **LH 與 RH 鏡像**：LH 上行用 5 起、拇指在第 5 音附近接力。
- 記憶法：RH「拇指過 E、B」（即每組 3、4 音後 thumb-under）；LH 鏡像。

## 核心規則

1. **拇指不落黑鍵**（主要原則）— 決定 thumb-under 的位置。黑鍵多的調（B / F♯ / D♭…）依此調整分組。
2. **以 3 或 4 分組** — 白鍵調是 3+4；黑鍵調依「拇指落白鍵」重新分組（如 B♭ 大調 RH 從 f4 起）。對應 DP 的 black-key-aware pivot（`[[concept_long_scale_thumb_under]]` v3）。
3. **F 大調 RH 例外**：1 2 3 4　1 2 3（B♭ 在第 4 音用 f4，拇指落 C）。
4. **B 大調 / 黑鍵調**：起始指與分組隨黑鍵位置變，不是 3+4。

## 小調

- **和聲 / 旋律小調**：指法通常與其平行/同名大調相近（升高的 7 音 / 6 音不改 thumb-under 結構，除非變成黑鍵影響拇指落點）。

## 琶音（三和弦）

| 調型 | RH 上行 | LH 上行 |
|---|---|---|
| 多數大三和弦（白鍵根音）| 1 2 3　(5 在頂) / 1 2 3 5 | 5 3 2 1 / 5 4 2 1 |
| 含黑鍵者 | 依「拇指落白鍵」調整（如 F 大調琶音 RH 1 2 4）| 鏡像 |

- 原則同音階：**拇指盡量落白鍵**，跨指（3 或 4 過拇指）發生在能讓拇指落白鍵的位置。

## 與 DP 的對應

- `USE_LONG_SCALE_THUMB_UNDER`（`[[concept_long_scale_thumb_under]]`）即在偵測到音階段落時，取消 thumb-pass 的 wrong-direction 懲罰，並以 black-key-aware greedy 3-or-4 pivot 近似上表。
- **偏離標準指法需要理由**：若 DP 在音階段落給出非標準指法，應能追溯到具體生物力學或樂句邊界因素，否則視為 bug（標準指法是 performance floor 之一）。
- ⚠️ 標準指法是**慣例**，仍受**手大小**（`HAND_SIZE` / `[[concept_finger_span_table]]`）與**樂句邊界**調節——不是硬約束。

## 待驗證 / 開放問題

- 各黑鍵調的精確 thumb-under 分組是否要進 DP 的 explicit 表，或維持 greedy 近似（目前後者，150 曲掃描 4 改善 0 退步）。
- 雙手反向 / 同向音階的接縫指法（cross-staff 不適用，見 `[[concept_cross_staff_voice_boundary]]`）。
