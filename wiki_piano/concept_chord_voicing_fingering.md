# Concept: Chord Voicing Fingering — 和弦聲部突顯指法

> 來源：Neuhaus *The Art of Piano Playing* §voicing, Cortot *Rational Principles* §chord balance, Brendel essays §chord textures
> 引用方：[concept_chord_fingering](concept_chord_fingering.md), [concept_finger_substitution](concept_finger_substitution.md), [../wiki_articulation/concept_articulation_in_polyphony](../wiki_articulation/concept_articulation_in_polyphony.md)

## 1. Chord Voicing 是什麼

Chord voicing（和弦聲部突顯）= 在多音和弦中**讓某一聲部突出**，其他音作為和聲背景。是鋼琴演奏的核心藝術之一。

典型情境：
- **Top voice 突出** (melody): 4-音 chord 中最高音為 melody，其餘為 harmonic filler
- **Bass voice 突出** (LH melody): bass 線是主旋律，其餘為和聲
- **Inner voice 突出**: 中聲部 melody (Brahms / Schumann 特色)

## 2. 指法選擇對 voicing 的影響

不同手指有不同**強度** + **可控性**：

| 手指 | 強度 | 可控性 | 適合 voicing |
|---|---|---|---|
| **1 (拇指)** | 最強 | 中（粗糙）| Bass voice, 但需精細控制 |
| **2 (食指)** | 強 | 高 | 突出聲部首選 |
| **3 (中指)** | 強 | 最高 | 突出聲部首選 |
| **4 (無名指)** | 弱 | 低 | 突出聲部最差選 |
| **5 (小指)** | 弱 | 中 | Top voice 必須 — 解剖位置 |

→ 突出聲部應**優先 1/2/3**。但 top voice 通常是 5（旋律最高音），是不得已 — 需 5 強化訓練彌補。

## 3. Voicing 的物理動作

⚠ Training-data verification needed:

Neuhaus / Cortot 描述 voicing 物理：
- **突出指**: 比其他指**更深 + 更快**地下鍵
- **背景指**: 較淺 + 較慢地下鍵
- **時序**: 突出指略早 attack（音響上有微小先後感）
- **重量**: 整手重量**偏向**突出指側

→ 這是「**一手內 dynamic 區分**」技術，鋼琴最難掌握的技巧之一。

## 4. RH Top-Voice 突出（最常見）

4-音 chord 中 top voice (typically melody) 突出：

| 案例 | 指法 + voicing 策略 |
|---|---|
| Chopin Nocturne RH melody | top: 5 (深下) / inner: 1-2-3 (淺) |
| Brahms Intermezzo lyrical | 同上 |
| Schubert lieder accompaniment | 同上 |

關鍵：5 雖弱，但解剖學位置「**outer**」更易由 wrist + arm weight 加重。

## 5. LH Bass-Voice 突出

LH 4-音 chord 中 bass (typically melody for accompaniment-melody pieces):

| 案例 | 指法 + voicing 策略 |
|---|---|
| Chopin Op.28 No.6 LH melody (cello-line) | bass: 5 (深下) / inner: 1-2-3 (淺) |
| Brahms Op.118 No.2 LH | 同上 |

LH bass 突出 = thumb (1) 對 inner voice，pinky (5) 對 melody/bass。與 RH top-voice 突出相對稱。

## 6. Inner Voice 突出（Brahms / Schumann 特色）

當中聲部是 melody：
- 用 inner 手指（2 / 3）強化
- 外側手指（1, 5）作為 harmonic frame
- 是「**rare voicing**」— 需特殊訓練

例：Brahms Intermezzo Op.118 No.6 多處 inner-voice melody，Schumann *Kreisleriana* 部分段。

對 inner voice 突出，最佳指法是 **2** 或 **3**（解剖位置在中間 + 強度 + 可控性 high）。

## 7. Voicing 與 finger substitution 的互動

⚠ Training-data verification needed:

Voicing 需要的手指**位置穩定** — substitution 可能干擾 voicing：
- 突出指若需 substitution（換指）→ voicing 突出度暫時降低
- 解決：**voicing 段不啟用 substitution**（保持突出指持續）
- 例外：legato voicing 不可避免時做 careful substitution

對 [../wiki_articulation/concept_legato_substitution](../wiki_articulation/concept_legato_substitution.md) 的意涵：substitution 在 voicing 段需謹慎，可能與 voicing 衝突。

## 8. 對 score-claude DP 的影響

DP 對 chord voicing 目前**不直接 model**：
- DP 計算 chord 指法是 [concept_chord_fingering](concept_chord_fingering.md) 的標準分配
- 不識別「哪音是 melody / 哪音是 filler」
- 不對 voicing 偏好優化 fingering

是 known 限制。Voicing 是 advanced 藝術 — 對 intermediate 目標曲目影響有限（intermediate 級 chord voicing 要求低）。未來 v3 candidate：melody-voicing-aware chord fingering（識別 top voice 為 melody 後加 5 強化）。

## 9. 適用作曲家 / 曲目

| 作曲家 | Voicing 重要性 |
|---|---|
| **Bach** | 高 — 對位每聲部 voicing 對等突出 |
| **Mozart** | 中 — Classical 透明度，voicing 自然 |
| **Beethoven** | 高 — 後期作品大量內聲部 voicing |
| **Schubert lieder** | 高 — accompaniment 中 melody 突出 |
| **Schumann** | 極高 — *Kinderszenen* / *Kreisleriana* inner-voice 主導 |
| **Brahms** | 極高 — *Intermezzi* / *Klavierstücke* 內聲部複雜 |
| **Chopin** | 中 — Nocturne lyrical RH top-voice + Op.28 No.6 LH bass |

## 10. 與其他 wiki 頁面的關係

- [concept_chord_fingering](concept_chord_fingering.md) — Chord 指法基礎，voicing 是其應用層
- [concept_finger_substitution](concept_finger_substitution.md) — Voicing 段 substitution 互動限制
- [concept_hand_anatomy](concept_hand_anatomy.md) — 各指強度差異是 voicing 物理基礎
- [../wiki_articulation/concept_articulation_in_polyphony](../wiki_articulation/concept_articulation_in_polyphony.md) — Voicing 是 polyphony articulation 的一個層面
- [../wiki_articulation/concept_tenuto](../wiki_articulation/concept_tenuto.md) — Voicing + tenuto 強指偏好邏輯類似
