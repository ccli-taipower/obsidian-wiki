---
concept: "Legato & Staccato（連奏與斷奏的控制）"
date_created: 2026-06-18
tags:
  - articulation
  - legato
  - staccato
  - touch
  - tone_color
  - technique
---

# 連奏與斷奏的控制（Legato & Staccato）

> 前置知識：[concept_wrist_motion — 手腕運動](concept_wrist_motion.md)、[concept_hand_position_stability — 手位穩定性](concept_hand_position_stability.md)

鋼琴的「圓滑」與「斷開」不是非此即彼的二分法，而是一條**連續光譜**。從黏合到極短促，演奏者透過按鍵重疊時間（key overlap）、手指離鍵速度、以及參與動作的身體部位來精確控制每一個音符的長度與音色。

---

## 1. 連奏（Legato）的定義與物理實現

Legato（義大利文「tied together」）= 前一音鬆開的瞬間與後一音按下的瞬間**重疊**（key overlap），使制音器（damper）不在兩音之間落回琴弦，聽覺上無縫隙。

### 按鍵重疊（Key Overlap）的量化

Breithaupt（1909）最早以「按鍵重疊比例」描述 legato。現代研究量化了這個概念：

- **Legato overlap ratio** 取決於音符間距（inter-onset interval, IOI）——IOI 越短，重疊比例越高（Repp, 1997）。
- Goebl & Palmer（2008）的 MIDI 分析顯示，專業鋼琴家在 Mozart 奏鳴曲的 legato 段落中，key overlap 平均約為 IOI 的 10–30%。

### 物理實現要點

| 要素 | 技術要點 |
|---|---|
| **手指轉移** | 前指保持按下，後指按下後前指才鬆開（finger legato） |
| **手臂重量** | 重量從一指「流動」到下一指，而非每指獨立施力（Matthay, 1903） |
| **手腕柔軟** | 手腕保持 flexible，讓重量轉移自然——見 [concept_wrist_motion](concept_wrist_motion.md) |
| **聽覺監控** | 用耳朵判斷是否真正連接，不能只靠手感 |

> **引用**：Goebl, W., & Palmer, C. (2008). "Tactile feedback and timing accuracy in piano performance." *Experimental Brain Research*, 186(3), 471–479.

---

## 2. 斷奏（Staccato）的三種類型

斷奏的本質是音符被**縮短**——staccato 音符的持續時間約為寫定時值的 40–50%（Breithaupt, 1909; Repp, 1997）。根據參與動作的身體部位不同，staccato 分為三種層級：

### 2.1 手指斷奏（Finger Staccato）

- **動作源**：僅手指掌指關節（MCP joint）
- **手腕 / 手臂**：保持靜止
- **特性**：最輕、最快，適合 pp–mp 的快速單音
- **典型場景**：Mozart 奏鳴曲中的輕巧裝飾音群

### 2.2 手腕斷奏（Wrist Staccato）

- **動作源**：手腕上下運動（flexion / extension）
- **手指**：保持固定 shape，隨手腕整體彈跳
- **特性**：中等力度，適合 mp–f 的重複和弦或八度
- **典型場景**：Debussy 前奏曲中的輕彈跳和弦

> 參見 [concept_wrist_motion](concept_wrist_motion.md) §4 對 wrist staccato 的詳述。

### 2.3 手臂斷奏（Arm Staccato）

- **動作源**：上臂帶動整個手臂的投擲動作
- **手指 + 手腕**：固定 shape，作為「傳導體」
- **特性**：最重、最響，適合 f–ff 的重音和弦
- **典型場景**：Beethoven 奏鳴曲 / Prokofiev 中的激烈斷奏和弦

### 層級比較

| 類型 | 動作源 | 速度 | 力度 | 音色 |
|---|---|---|---|---|
| 手指斷奏 | MCP joint | ★★★ | ★ | 輕巧、顆粒狀 |
| 手腕斷奏 | Wrist | ★★ | ★★ | 彈跳、富彈性 |
| 手臂斷奏 | Upper arm | ★ | ★★★ | 厚重、打擊感 |

> **引用**：Furuya, S., Flanders, M., & Soechting, J. F. (2011). "Hand kinematics of piano playing." *Journal of Neurophysiology*, 106(6), 2849–2864.

---

## 3. 連跳交替（Legato-Staccato Alternation）

在實際樂曲中，legato 和 staccato 經常交替出現（例如「圓滑線 + 斷奏尾音」的兩音一組奏法）。

### 執行方式

1. **落提動作**（drop-lift）：手腕隨圓滑線**落**下按第一音，在斷奏標記處**提**起離鍵
2. **重量轉移 → 釋放**：legato 段用手臂重量連接，staccato 段瞬間釋放重量
3. **呼吸感**：連跳交替模擬人聲的「唱一句 → 換氣」，是音樂性表現的基本單位

### 常見模式

- **兩音一組**（slur + staccato）：古典時期最常見，如 Mozart K.545 第二樂章
- **長句 + 斷尾**：浪漫時期常見，連奏長句的最後一音以 staccato 收束
- **交替句法**：整段交替 legato / staccato 句，製造問答對比效果

> NiceChord Day 10 對這種「連跳交替」有直觀的示範說明。

---

## 4. Non-legato 的定義與應用場景

Non-legato = 音符之間**有間隙但不像 staccato 那樣刻意縮短**。每個音彈到自然時值的約 70–90% 後鬆開。

### 與 Legato / Staccato 的區別

| | 按鍵重疊 | 音符時值 | 聽感 |
|---|---|---|---|
| Legato | 有重疊 | ≈100% 或略超 | 連綿不斷 |
| Non-legato | 無重疊 | ≈70–90% | 清楚分離但不跳躍 |
| Staccato | 無重疊 | ≈40–50% | 短促、斷開 |

### 應用場景

- **巴洛克鍵盤音樂**：C.P.E. Bach《論鍵盤樂器的正確演奏法》將 non-legato 定為當時的「預設觸鍵方式」
- **清晰的對位段落**：各聲部需要聽得清楚時，non-legato 比 legato 更適合
- **練習用觸鍵**：初學者先用 non-legato 建立手指控制，再進階到 legato

---

## 5. 圓滑程度的連續光譜

觸鍵的圓滑程度是一條**連續光譜**，不是幾個離散類別：

```
legatissimo → legato → non-legato → portato → staccato → staccatissimo
  (極黏合)    (連奏)    (自然分離)   (半斷奏)    (斷奏)     (極短促)
```

| 觸鍵方式 | Key overlap | 持續時值比例 | 記譜符號 |
|---|---|---|---|
| Legatissimo | 大量重疊 | >100% | 雙圓滑線或文字 |
| Legato | 些微重疊 | ≈100% | 圓滑線 (slur) |
| Non-legato | 無重疊 | ≈70–90% | 無特殊標記 |
| Portato | 無重疊 | ≈60–70% | 圓滑線下加斷奏點 |
| Staccato | 無重疊 | ≈40–50% | 斷奏點 (dot) |
| Staccatissimo | 無重疊 | ≈20–30% | 三角形斷奏記號 |

> 這條光譜上的每一點都是有效的音樂表現手段——專業演奏者在單一樂句中可能使用光譜上的多個位置。

> **引用**：Bernays, M., & Traube, C. (2014). "Investigating pianists' individuality in the performance of five timbral nuances through patterns of articulation, touch, dynamics, and pedaling." *Frontiers in Psychology*, 5, 157.

---

## 6. 不同觸鍵方式對音色的影響

### Struck Touch vs. Pressed Touch

研究顯示兩種基本觸鍵方式產生不同音色效果：

- **Struck touch**（打擊式觸鍵）：指尖從鍵面上方落下，產生較明亮、穿透力強的音色。生物力學上較高效（Furuya et al., 2020），但控制精度較低。
- **Pressed touch**（按壓式觸鍵）：指尖從鍵面出發向下按壓，產生較溫暖、柔和的音色。控制精度更高，連續音之間的時間準確度更好。

### 觸鍵方式與斷奏 / 連奏的關係

| 組合 | 音色效果 | 應用場景 |
|---|---|---|
| Pressed + Legato | 最溫暖、歌唱性 | Chopin nocturne 旋律 |
| Struck + Legato | 明亮但連貫 | 古典時期快速音階 |
| Pressed + Staccato | 柔和的斷奏 | Debussy 的輕觸斷和弦 |
| Struck + Staccato | 最銳利、打擊感 | Bartók / Prokofiev 的敲擊式段落 |

### 上肢速度差異

Furuya et al.（2020）的研究揭示：staccato 觸鍵時，掌指關節（MCP joint）前向速度比 legato 高 92%，手腕高 89%，肘部高 50%。這說明 staccato 需要更高的上肢運動速度，而 legato 則依賴更精確的重量控制。

> **引用**：Furuya, S., Tominaga, K., Miyazaki, F., & Altenmüller, E. (2020). "Effects of trunk motion, touch, and articulation on upper-limb velocities and on joint contribution to endpoint velocities during the production of loud piano tones." *Frontiers in Psychology*, 11, 1159.

---

## 7. 常見問題與解決方案

### 問題一：手腕僵硬

**症狀**：長時間 legato 或反覆 staccato 後手腕疲勞甚至疼痛。

**原因**：手腕鎖死、不隨動作自然調整。

**對策**：
- 練習前先做手腕圓周運動（circumduction）放鬆
- Legato 段落中手腕隨旋律輪廓自然起伏
- Staccato 段落確認手腕在「彈跳」而非「敲打」
- 參見 [concept_wrist_motion](concept_wrist_motion.md) §5 wrist freedom

### 問題二：斷奏太重

**症狀**：staccato 音量過大、音色粗糙，不符合樂句需要。

**原因**：使用了過高層級的 staccato 類型——用手臂斷奏彈本應手指斷奏的段落。

**對策**：
- 確認段落需要的力度等級 → 選擇對應的 staccato 類型
- 練習「只用指尖輕觸琴鍵表面」的超輕 staccato
- 從 pp 開始練，逐步增加力度

### 問題三：連奏模糊

**症狀**：legato 段落音符互相混在一起，聽不清楚每個音。

**原因**：key overlap 過長，或過度依賴踏板掩蓋不乾淨的手指連接。

**對策**：
- **不踩踏板**練習 legato，確認純手指 legato 是乾淨的
- 用耳朵確認每個音的起始點清楚可辨
- 控制 key overlap 在 IOI 的 10–30% 以內
- 參見 [concept_pedal_technique](concept_pedal_technique.md) 對踏板與手指 legato 的區分

---

## 8. 小測驗

試著回答以下問題（答案在下方）：

1. Legato 的物理實現關鍵是什麼？用一個術語描述。
2. 三種 staccato 類型中，哪一種速度最快但力度最輕？
3. Staccato 音符的持續時值大約是寫定時值的百分之幾？
4. Non-legato 和 staccato 的主要區別是什麼？
5. 「兩音一組」連跳交替的手腕動作可以用哪兩個字概括？
6. 按照圓滑程度光譜排列：staccato、legato、portato、legatissimo、non-legato。
7. Pressed touch 和 struck touch 哪個控制精度更高？
8. 如果 staccato 段落音量過大，最可能的原因是什麼？
9. C.P.E. Bach 認為鍵盤音樂的「預設觸鍵方式」是什麼？
10. 練習 legato 時為什麼建議先不踩踏板？

<details>
<summary>答案</summary>

1. **按鍵重疊（key overlap）**——前一音鬆開與後一音按下之間有時間重疊，使制音器不在兩音間落回琴弦。

2. **手指斷奏（finger staccato）**——僅用手指 MCP 關節動作，速度最快但力度最輕，適合 pp–mp 的快速單音。

3. **約 40–50%**。例如一個四分音符的 staccato 版本，實際發聲時間約為原時值的一半。

4. **持續時值比例不同**：non-legato 的音符約佔寫定時值的 70–90%，而 staccato 僅約 40–50%。Non-legato 只是「不黏合」，staccato 則是「刻意縮短」。

5. **「落提」**（drop-lift）——手腕落下按 legato 音，提起離 staccato 音。

6. **legatissimo → legato → non-legato → portato → staccato**。從最黏合到最斷開。

7. **Pressed touch** 控制精度更高，因為指尖從鍵面出發，觸覺反饋更直接，連續音之間的時間準確度更好。

8. **使用了過高層級的 staccato 類型**——例如用手臂斷奏彈本應手指斷奏的段落。解決方法是降低動作層級，從手指 staccato 開始練習。

9. **Non-legato**。巴洛克時期的鍵盤樂器（大鍵琴、早期鋼琴）以 non-legato 為基本觸鍵方式，legato 反而是特殊效果。

10. **為了確認純手指 legato 是乾淨的**。踏板會掩蓋不精確的手指連接，如果先不踩踏板練習，能用耳朵確認每個音的起始點清楚可辨，key overlap 控制得當。之後加踏板才是在乾淨的手指基礎上增添色彩，而非用踏板掩蓋問題。

</details>

---

## 下一步

掌握連奏與斷奏的控制之後，下一步是將觸鍵控制應用於音樂性的指法選擇：

- [concept_musical_fingering — 音樂性指法](concept_musical_fingering.md)：如何根據音樂表現需求選擇指法，而非僅追求技術便利

---

## 延伸參考

- [concept_wrist_motion — 手腕運動](concept_wrist_motion.md)：staccato 三層級中手腕的關鍵角色
- [concept_hand_position_stability — 手位穩定性](concept_hand_position_stability.md)：穩定的手位是精確觸鍵控制的前提
- [concept_pedal_technique — 踏板技法](concept_pedal_technique.md)：踏板與手指 legato 的配合運用

### 學術文獻

- Goebl, W., & Palmer, C. (2008). Tactile feedback and timing accuracy in piano performance. *Experimental Brain Research*, 186(3), 471–479.
- Furuya, S., Tominaga, K., Miyazaki, F., & Altenmüller, E. (2020). Effects of trunk motion, touch, and articulation on upper-limb velocities. *Frontiers in Psychology*, 11, 1159.
- Bernays, M., & Traube, C. (2014). Investigating pianists' individuality in the performance of five timbral nuances. *Frontiers in Psychology*, 5, 157.
- Repp, B. H. (1997). The aesthetic quality of a quantitatively average music performance. *Music Perception*, 14(4), 419–444.
- Breithaupt, R. M. (1909). *Die natürliche Klaviertechnik*. Leipzig: C. F. Kahnt.
- Furuya, S., Flanders, M., & Soechting, J. F. (2011). Hand kinematics of piano playing. *Journal of Neurophysiology*, 106(6), 2849–2864.
