---
concept: 鋼琴指法原則 (Piano Fingering Principles)
date_created: 2026-04-08
tags: [piano_fingering, technique, pedagogy, motor_learning]
---

# 鋼琴指法原則 (Piano Fingering Principles)

綜合 9 篇來源的鋼琴指法核心原則。

## 基礎編號

拇指=1、食指=2、中指=3、無名指=4、小指=5（左右手相同，大陸式）

## 五大共識原則

1. **沒有唯一正確的指法** — 指法因手型、曲目、速度而異，編輯指法僅為建議
2. **一致性優先** — 選定後固定練習，讓動作記憶自動化（Practice makes permanent）
3. **拇指通常避免黑鍵** — 會使手部前移，影響白鍵控制
4. **善用所有手指** — 避免只用前 2-3 指，保持流暢
5. **音階/琶音指法是基礎** — 熟記標準指法加速視譜能力

## 傳統 vs 極簡主義

| 面向 | 傳統指法 | [極簡主義指法](concept_minimalist_fingering\.md) |
|------|----------|------|
| 預設模型 | C 大調 (123-12345) | F 大調 (1234-1234) |
| 小指使用 | 盡量使用所有 5 指 | 盡量省略小指 |
| 拇指穿越 | 減少穿越次數 | 增加穿越次數 |
| 哲學 | 訓練弱指平衡 | 最大化強指（1-2-3）優勢 |

## 選擇指法的考量因素

- 最終演奏速度（非練習速度）
- 力度、觸鍵方式、分句
- 雙手合練的可行性
- 手部大小（小手需特殊方案）
- 重複動機的一致性

## 嵌入指法的步驟

1. 選定指法 → 2. 慢速固定練習 → 3. 短期允許微調 → 4. 確定後永不更改 → 5. 自動化

## 腕關節中立原則（2026-04-11 新增）

鋼琴指法的「舒適度」不只是美學問題，而是**神經壓迫的物理量**。Wikipedia CTS 條目與 PMC 臨床研究給出明確數據：

| 腕關節狀態 | 相對 tunnel 壓力 |
|------------|------------------|
| 中立位 | 2–10 mm Hg（基準） |
| 屈曲 (palmar flexion) | ×8 |
| 伸展 (dorsiflexion) | ×10 |
| 動態屈伸 | 可達 111 mm Hg |

**關鍵門檻**：PMC6300245 測得腕關節 extension > 20° 時，擊鍵力顯著上升，且與手部/全身肌骨不適（MSD）在週與年層級皆顯著相關。

**壓力由位移決定，不是力**。即使輕觸 pp 段，若腕關節姿勢不良，神經壓迫一樣高。指法評估不應只看音量層面的「吃力度」，而應優先看位置。

**累積損傷原則**：職業傷害的 odds ratio 表中「重複動作 = 2.0」與「腕關節屈伸工作 = 2.0」並列——反覆的小偏差比單次大偏差更危險。對應到 DP：某個指法若「每拍都把腕關節推離中立位 5°」比「偶爾一次推到 20°」更值得懲罰。這是**累積式 cost**，不是 peak cost。

**經典 CTS 姿勢** = 尺側偏離 + 屈曲同時出現。若將來 DP 引入腕關節模型，這兩個維度同時觸發應視為硬約束，不只是加總懲罰。

### 對 V6 DP 的意涵

V6 目前無任何腕關節模型，這是已知缺口。短期內不打算建 full kinematic model，但：

- `_assignment_cost` 若要加 wrist-angle 項，第一優先應為 **RH 外側 f1/f5 的 reach cost**（這是 extension 的主要來源）
- 任何此類新項必須是**累積型**（phrase-level sum），不是 per-note peak
- 累積項需要跨整個樂句計算，因此建議走 post-processing 層而非 DP inner-loop

**2026-05-13 update — DP v1 落地**：`_wrist_extension_phrase_cost` 已實作為 RH-only post-hoc phrase surcharge（`program/run.py`）。常數：`WRIST_EXT_THRESHOLD=FINGER_COMFORT_MAX_SPAN[(1,5)]`、`WRIST_EXT_PHRASE_BUDGET=4`、`WRIST_EXT_SURCHARGE=0.4`。A/B 在 Bach-heavy 156-piece eval 中 dormant；wide-chord 單元測試確認觸發正確。詳見 score-claude memory `project_wrist_extension_rule.md`。

## 同指異音重定位（same-finger reposition，2026-07-16 新增）

**現象**：同一根手指連續彈兩個**不同**音、音程超過級進範圍（>2 半音，即手指必須
離鍵重定位，不是走鄰鍵）。與同音重複
（[concept_repeated_note_fingering](concept_repeated_note_fingering.md)，標準解=換指）
和同指級進（一指無法連兩鍵，量小、已接受樂章大量存在=容忍類）是三個相鄰但不同的問題。
**邊界實證**：Bach 已接受樂章（Inv1-8）step band（≤2 半音）13-14 對/樂章屬常態，
mid/leap band（>2）0-3 對——人類容忍線恰在級進/重定位交界。

**為何大跳同指比級進同指更差**：
1. **飛行中無準備指（in-flight preparation 喪失）**：換指跳躍時，手在空中移動的同時
   下一指已可預先伸出瞄準目標鍵（手在飛行中「塑形」）；同指跳躍 = 同一指尖先釋放、
   裸移、再落鍵——落點精準度沒有任何冗餘，速度受限、miss 率上升。
2. **單指重複負荷**：同一 flexor/extensor 單元連續做「按—抬—按」，與同音重複需要
   換指的肌理相同（見 repeated_note_fingering §3），大跳再疊加移位加速度。
3. **手位經濟歸零**：跳躍換指（如 5→1 或 1→5）本身就是 relay 的自然解、近乎免費——
   人類指法在大跳幾乎永遠換指；選同指等於放棄免費的手位重整機會。

**例外**：staccato / detached（手有充分時間重定位）→ 豁免；同音大跳重複（octave
tremolo 類）屬 repeated-note 主題另議。

**實證（Bach Inv12 pre-screen, 2026-07-02）**：DP 在音型轉折點的大跳給出 1-1 / 5-5
（RH 19 / LH 13 處，全書 outlier，其餘樂章 ≤8）。根因是 cost model 漏洞：大跳分支
（`abs(interval) > LARGE_LEAP_THRESHOLD`）早退進 relay 公式，`cf==pf` 從未被計價——
同指（actual=0）在 relay 眼中反而「方向中性」最便宜。級進同指有 `SAME_FINGER_REPEAT_COST
= 5.0` 兜底，大跳同指卻只付 2.0–5.25 的 relay 價，**大跳同指比級進同指便宜**，排序
違反上述生物力學。

**DP 對應（2026-07-16 實作定稿）**：`SAME_FINGER_REPOSITION_PENALTY = 4.0`——
(1) 級進分支：`cf==pf` 且 >2 半音 → REPEAT(5.0) + REPOSITION(4.0)；(2) 大跳分支
（>5）入口攔截 `cf==pf`，取代無意義的 relay 計價（同公式）；(3) **weak surcharge
（`SAME_FINGER_WEAK_WEIGHT×(1−agility)`）延伸到重定位 band**——單指重複負荷與距離
無關，2026-06-25 的 step-only gate 是「當時重定位 band 未計價」的 artifact；
(4) 排序不變式 = 重定位 > 級進同指（含弱指）；(5) `relax_continuity`（staccato）→ 0。

**實作結果**：single→single 重定位類 Inv12/13 全歸零；收割 Bach Inv3-R m3/m45
（1→1 大跳 → 1-2-3-4-5，cost −29.2）、Inv3-L m38（5→5 → 5→4）、Inv4-L m51
（5→5 大跳 → 2→5 relay，正是 2026-06-02 m47 同型病灶的通用化）。

**殘餘（獨立問題）**：Inv12 音型轉折的主力病灶（RH 16 / LH 12 對）在 **arpeggio-merge
群組接縫**——上/下交替的分解和弦被 Step-1b 合併成 chord 群組後，(a) 接縫邊緣同指
（如上組頂 A5(5) → 下組頂 F#5(5)）走 chord→chord transition 未被本規則計價，枚舉內
存在替代解（如 1-2-4）可用 edge-adjacency 計價引導；(b) **bottom-to-bottom 接縫的
1→1 被「拇指固定最低音」硬約束強制**（desc 組尾=底音=1、asc 組頭=底音=1），計價無用，
需放寬 merged 群組（本質是序列非同時）的枚舉——設計決策待定。

## 歷史演變

- Bach 以前：極少使用拇指
- J.S. Bach：引入拇指廣泛使用，指法革新
- Chopin：自然手位（2-3-4 在黑鍵），每指有獨特音色
- 現代：拇指穿越 (thumb under) 為核心技巧
- 2024 Cory Hall：極簡主義挑戰傳統 C 大調模型

## 來源

- [src_piano_fingering_wikipedia](src_piano_fingering_wikipedia.md)
- [src_piano_fingering_articles](src_piano_fingering_articles.md)
- [concept_scale_fingering](concept_scale_fingering.md)
- [concept_finger_span_table](concept_finger_span_table.md)
- [src_computational_fingering](src_computational_fingering.md)
- [src_historical_fingering_interpretation](src_historical_fingering_interpretation.md)
- [src_technique_expressiveness_injury](src_technique_expressiveness_injury.md)
- Raw：`raw/wrist_neutral/wikipedia_carpal_tunnel.md`（CTS tunnel pressure）
- Raw：`raw/pianist_injury/pmc_kinematics_and_review.md`（PMC6300245 腕關節 20° 門檻）
