---
concept: 跨譜表聲部邊界與指法接力 (Cross-Staff Voice Boundary & Finger Relay)
date_created: 2026-06-05
tags: [piano_fingering, voice_separation, cross_staff, transition_cost, biomechanics]
---

# 跨譜表聲部邊界與指法接力 (Cross-Staff Voice Boundary)

當左手（或右手）**跨越到另一個音域**演奏旋律時——例如左手越過右手、到高音譜表彈一條獨立旋律——這條旋律是**另一個聲部**，不是低音聲部的延續。**指法接力（finger relay）不應跨越聲部邊界**。

## 為什麼這是一個聲部邊界

依 Huron 的感知原則（見 [[src_voice_separation]]）：

- **Avoid Leaps Rule**：同一聲部的相鄰音應音高接近；**大跳（large pitch gap）是聲部切換的訊號**，不是同聲部的連續。
- 因此「低音 → 八度以上跳到高音域」這個動作，感知上跨越了兩個聲部：下方的低音聲部 + 上方的跨譜表旋律聲部。

生物力學上，手跨越到高音域時會**重新定位 / 旋轉**（forearm rotation，見 [[concept_forearm_rotation]]），手型不再是原本的低音手型——所以延續低音聲部的手指（如左手小指）並無生理上的必要。

## 對指法的含意

指法接力的前提是「同一條旋律線上，前一音的手指會影響後一音」。但**跨越聲部邊界時這個前提不成立**：

- 低音聲部用什麼手指（左手低音常用 f5 彈最低音）**不應傳遞**到上方的跨譜表旋律。
- 上方旋律聲部應依**自己的舒適度**選指（鄰音音型用 [[concept_finger_span_table]] 最貼合的中指組，如全音鄰音用 2-3 而非 4-5）。

### 反例（接力錯誤把低音手指帶上去）

York Bowen *Toccatina*（SICILIANO mvt2）m17-20：左手低音是 F3+C4 雙音（小指 f5 在最低的 F3），接著**跳八度以上**到 A5-B5-A5 的跨譜表旋律。

- **錯誤**：接力把低音的 f5「同旋律指」延續到 A5 → 5-4-5。手指 4、5 彈全音鄰音不貼合跨度表，僵硬。
- **正確**：A5-B5-A5 依自己的跨度選 **3-2-3**（(2,3) 跨度=全音，完全貼合；見 [[concept_finger_span_table]]）。

## DP 實作

`program/run.py`：
- `_is_xstaff_voice_entry(prev, curr, hand)`：偵測「左手、目標音 ≥ C5（上方聲部音域）、且自前一音上跳 ≥ 八度」→ 視為跨譜表聲部進入。
- `_transition_cost` 對此 transition 回傳 **`XSTAFF_VOICE_LEAP_COST`（與手指無關的固定值）**，使接力不再偏好任一手指；上方聲部由自身的 local + 鄰音 transition cost 決定指法。

常數：`XSTAFF_VOICE_REGISTER=72 (C5)`、`XSTAFF_VOICE_LEAP=12 (八度)`、`XSTAFF_VOICE_LEAP_COST=2.0`。

## 驗證

- 由使用者 Toccatina override 反向歸納（cost-trace 確認 root cause = 低音 f5 接力到高音）。
- 加入規則後 **DP 自行產生 3-2-3**（不需 override）。
- PIG 150 曲 compare_pig GMR **byte-identical**——規則只在真正的跨譜表大跳觸發，對一般古典曲目零影響。

## 尚未涵蓋

- E4→F4 上行音型的指法方向（中音域，非大跳聲部邊界）= 另一機制，待獨立分析。
- 同音型同指法一致性（m13/14）= 既有的 HARD 問題。
