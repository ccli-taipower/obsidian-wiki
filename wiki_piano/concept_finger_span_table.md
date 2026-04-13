---
concept: 手指跨度表 (Finger Span Table)
date_created: 2026-04-08
tags: [biomechanics, ergonomics, span, fingering_model, Parncutt]
---

# 手指跨度表 (Finger Span Table)

定義每對手指之間可達的最大/最小/舒適/放鬆跨度（以半音為單位），是所有指法演算法的基礎數據。

## 跨度層級

```
MinPrac ← MinComf ← MinRel ← MaxRel → MaxComf → MaxPrac
  最小實用    最小舒適    最小放鬆    最大放鬆    最大舒適    最大實用
```

- **Practical**：音樂演奏中實際會用的極限
- **Comfortable**：Practical ± 2 半音
- **Relaxed**：手自然放鬆時的間距

## Parncutt (1997) 右手跨度表

| 指對 | MinPrac | MinRel | MaxRel | MaxComf | MaxPrac |
|------|---------|--------|--------|---------|---------|
| 1-2 | -5 | 1 | 5 | 8 | 10 |
| 1-3 | -4 | 1 | 7 | 10 | 12 |
| 1-4 | -3 | 1 | 9 | 12 | 14 |
| 1-5 | -1 | 1 | 10 | 13 | 15 |
| 2-3 | 1 | 1 | 2 | - | 2 |
| 2-4 | 1 | 1 | 3 | - | 5 |
| 2-5 | 2 | 1 | 6 | 6 | 8 |
| 3-4 | 1 | 1 | 2 | - | 2 |
| 3-5 | 1 | 1 | 4 | 3 | 5 |
| 4-5 | 1 | 1 | 3 | - | 4 |

負值 = 拇指穿越（拇指移到另一指下方）

## 與 V6 DP 的對應

V6 的 `FINGER_COMFORT_SPAN` 字典：

```python
{(1,2):5, (1,3):4, (1,4):8, (1,5):7,
 (2,3):2, (2,4):5, (2,5):5,
 (3,4):2, (3,5):4, (4,5):2}
```

與 Parncutt 的 MaxRel 基本一致但有微調（如 1-3 從 7 改為 4，經 DP 調參最佳化）。

## 個體差異調整

- 小手：所有值 × 0.9
- 寬指：需靠近鍵盤邊緣
- 拇指靈活性因人而異（MinPrac 負值的實際範圍差異大）
- 手部大小與傷害強相關：PMC6300245 測得 hand span ↔ 手部 MSD 相關係數 r = −0.69（p ≤ 0.004）。小手鋼琴家更易受傷，這不只是「舒適度」而是臨床風險。

## 傷害風險的不對稱性（2026-04-11 新增）

Jurinič et al. 2026 的 53 篇系統回顧及 Sakai & Shimawaki 的 case-control 研究明確指出：

> **"Finger joint mobility, particularly right 3–4 span, is a risk factor for piano-related pain"**

這句話對 DP 有三個直接意涵：

1. **RH f3–f4 span 應比 LH f3–f4 span 付更多代價**。V6 目前對稱處理兩手，但 Sakai 資料顯示不對稱。可考慮對 RH 的 f3-f4 跨度代價 ×1.2–1.5。
2. **f3-f4 不只是 transition 問題**。V6 的 `ADJACENT_COUPLING_PENALTY = 0.5` 懲罰 f3↔f4 過渡，但臨床風險是**靜態跨度本身**。即使不換指、兩指同時按住延續和弦，f3-f4 被強制撐開仍是風險。
3. **octaves 與 chords 佔受傷前練習技巧的 74%**（Sakai n=200 臨床資料）。和弦 span cost 比單音旋律的 span cost 更值得加權。

### 腕關節延伸限制

PMC6300245 同時測得：腕關節 **extension > 20°** 顯著增加擊鍵力、且與手部/全身 MSD 顯著相關（preceding week 與 preceding year 皆成立）。腕關節狀態目前 V6 完全未建模；若將來加入，這是第一條 hard threshold 候選。

### 右手-左手合成風險

> "Pianists with small hands prone to overuse injuries in upper extremities"（PMC6300245）

加上本節前述的 RH f3-f4 效應，**小手 + 右手 + 和弦密集** = 三風險因子疊加。這是 V6 DP 未來若引入 injury_cost 項時的主要目標情境。

## 來源

- [src_parncutt1997_ergonomic_model](src_parncutt1997_ergonomic_model.md)
- [concept_piano_fingering_principles](concept_piano_fingering_principles.md)
- [concept_small_hands](concept_small_hands.md)
- [src_computational_fingering](src_computational_fingering.md)
- [src_piano_ergonomics_small_hands](src_piano_ergonomics_small_hands.md)
- Raw：`raw/pianist_injury/pmc_kinematics_and_review.md`（PMC6300245 + PMC7007903）
