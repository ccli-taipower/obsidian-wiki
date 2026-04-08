---
concept: 手指跨度表 (Finger Span Table)
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

## 來源

- [[src_parncutt1997_ergonomic_model]]
- [[concept_piano_fingering_principles]]
- [[src_computational_fingering]]
