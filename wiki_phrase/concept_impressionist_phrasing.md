# Concept: 印象派樂句 — Debussy / Ravel 的 texture-driven phrasing

> 來源：通用音樂理論知識 + Jankélévitch《Debussy et le mystère》、Howat《Debussy in Proportion》、Roy Howat 演奏研究、標準 20 世紀音樂理論教材
> 涵蓋 PIG：Debussy 9 + Ravel 3 = **12 曲 (8%)**
> 狀態：種子頁，第一版 2026-05-26
> 驗證樣本：PIG 037 Debussy Clair de Lune

## 1. 為什麼這頁對指法系統重要

印象派的樂句邏輯**與古典 / 浪漫派根本不同**：

- ❌ **Cadence 失效**：和聲非功能性（modal、whole-tone、parallel chords），V-I 不再是主軸 → 古典 cadence 偵測完全失靈
- ❌ **旋律不再主導**：texture / 和聲色彩 / 音色才是主角，旋律常被當成「上層 voicing」
- ❌ **節拍規律性弱**：跨節拍 rubato、自由節奏標示頻繁
- ✅ 但有新訊號：**texture change**、**pedal indications**、**dynamic / tempo markings**、**registral shift**

當前 `_detect_phrase_starts` 對印象派幾乎全失效 — 音高跳幅、cadence、4-bar 週期沒一個適用。需要的是**質地 (texture) 變化偵測**，這是全新軸線。

## 2. 印象派樂句的五大特徵

### 2.1 Texture 是樂句單位

Debussy 與 Ravel 把整段音樂視為**一個聲音紋理**（如「鐘聲」、「水波」、「月光」），紋理變化 = 樂句變化。常見紋理層：
- **Pedal halo**：sustained pedal 下的和聲渲染
- **Parallel chords**：平行和弦移動（如平行 9 度、11 度）
- **Modal scales**：以教會調式 / pentatonic / whole-tone 為素材
- **Arpeggio washes**：分解和弦快速掃過，模糊個別音

**操作型偵測**：
- 偵測 RH / LH **音域範圍**的突然變化（如從 C4-A4 跳到 C5-G6）
- 偵測 chord density 變化（從 single line 到 thick chord）
- 偵測動態突變（pp → ff 或反之）

### 2.2 Pedal 標記是樂句邊界訊號

Debussy 在 Pédal sustained 結束處（"Sans pédale" 或 release marking）通常是樂句邊界 — 一個聲音紋理結束、新紋理開始。

**對 OMR 抽取**：Audiveris 對 pedal marking 的支援需驗證。即使無法抽，仍可從 chord density 推斷 pedal 段。

### 2.3 非功能和聲 → Cadence 失效

Debussy 避免傳統 V-I，常用：
- **Plagal IV-I**（教堂式收束）
- **Whole-tone chord 解決到 modal final**
- **Tritone substitution**
- **Open 5ths / 4ths**（中世紀風）

**對指法系統的實務**：**禁用** cadence 偵測作為樂句邊界訊號（古典 / 早期浪漫的核心訊號在這裡是雜訊）。改靠**和聲色彩變化** — 從一個和聲區域（如 D♭ major 9th halo）轉到另一個（如 B♭ minor 7th halo），切換點是樂句邊界。

### 2.4 樂句長度極不規律

印象派樂句可能短至 2 bar，長至 20 bar。完全依「聲音事件」展開。**Pass 3 的 4-bar 週期是反指標。**

### 2.5 Scale Modes 影響指法

非大小調音階改變指法策略：
- **Whole-tone scale**：6 個全音 → 拇指穿越不能用標準大調規則
- **Pentatonic** (5 音)：5 個音剛好 5 指、無拇指穿越需求 ← 與 [../wiki_piano/src_chinese_style_piano](../wiki_piano/src_chinese_style_piano.md) 五聲音階指法相關
- **Modal**：依 mode 選 finger group

對樂句偵測的間接影響：scale 的 mode 切換通常 = 紋理變化 = 樂句邊界

## 3. Debussy 特有的樂句語法

| 訊號 | 描述 | 信心度 |
|---|---|---|
| **Tempo marking 變化** | `Modéré` → `Animé`, `Calmato` 等 | ⭐⭐⭐ |
| **Texture layer 切換** | LH 從 single line → arpeggio wash → block chord | ⭐⭐⭐ |
| **Registral shift** | RH 突然 +/- 1.5 octave | ⭐⭐ |
| **Dynamic level shift** | pp → mf 或 mf → pp 跨多 chord | ⭐⭐ |
| **Pedal change** | sostenuto / damper pedal 切換 | ⭐⭐ (需驗證 OMR) |
| **Time signature change** | Debussy 常在中段換拍 | ⭐⭐ |
| **明確 phrase mark** | 譜面上的長 slur 或 phrasing 線 | ⭐⭐⭐ (若 Audiveris 抽得到) |

## 4. Ravel 與 Debussy 差異

| 特徵 | Debussy | Ravel |
|---|---|---|
| 樂句邊界訊號 | texture 為主 | **織度更精緻**，但仍有古典感 |
| Cadence 殘留 | 弱 | 中等（Ravel 偶用 V-I） |
| 節拍規律 | 自由 | **較規律** (8/16 bar 結構常見) |
| 對位 | 少 | 中等 (Ravel 偶用 fugato) |

**操作型**：Ravel 比 Debussy 更可套用「弱化古典規則」。完全 Debussy-style 規則對 Ravel 過於激進。

## 5. 印象派樂句邊界偵測啟發式（草案）

```
impressionist_phrase_detector(groups):

1. 禁用：
   - 4-bar Pass 3 fallback
   - 古典 cadence 偵測
   - 標準音高跳幅 PHRASE_BREAK_THRESHOLD (Debussy 內 octave 跳常見、不是樂句訊號)

2. 啟用 (依優先序)：
   a. tempo marking 變化 (要求 Audiveris 抽 <words> 元素)
   b. chord density 變化 (連續 4 chord 平均 note 數突變 ≥ 2)
   c. registral shift (連續 4 chord 平均 MIDI 範圍中心移動 ≥ 7 半音)
   d. dynamic shift (連續 dynamic marking 變化 ≥ 2 階)
   e. time signature 變化

3. Fallback：
   - 若上述訊號都無 → 完全不切，整段為一個樂句
   - 對 Debussy 而言這常是正確答案（如 Clair de Lune 中段一氣呵成）
```

**實作風險**：很多訊號依賴 Audiveris 對 tempo / dynamic / pedal marking 的抽取能力 — 未驗證。Phase 1 先做純結構訊號（chord density + registral shift），marking 偵測作為 Phase 2 升級。

## 6. PIG 驗證樣本

### 037 Debussy Clair de Lune (D♭ major)
- 三段 ABA' (含 introduction)
- A 段：8-bar period-like，但內部 modal harmony 已淡化 cadence
- B 段 (中段)：arpeggio wash，連續 16-note 流動，**樂句長度 ~16 bar**
- A' 段：類似 A 但簡化
- **預期收穫**：B 段絕對不能用 4-bar 切；應檢測 A→B 的 texture 切換（single melodic line → arpeggio wash）

### 035 / 036 Debussy Arabesque 1 / 2
- E major / G major
- 流暢 texture，sequential 樂句
- **預期收穫**：sequence 重複是同樂句內事件、不是新樂句

### 035-043 (Debussy 其他 7 首)
- 待 PIG 全 label 細看

### Ravel 三首
- 138 Sonatine, 139 Jeux d'Eau, 140 Pavane (推測, 待 PIG 確認)
- 較規律，可半套用古典規則

## 7. 與其他 wiki 頁面的關係

- **不**依賴 [concept_classical_period_sentence](concept_classical_period_sentence.md)（cadence 失效）
- **不**依賴 [concept_fugue](concept_fugue.md)（無 subject 結構）
- 部分概念延伸 [concept_chopin_lyrical_phrase](concept_chopin_lyrical_phrase.md) 的「不規律長度」與「texture change」訊號
- 與 [../wiki_piano/src_chinese_style_piano](../wiki_piano/src_chinese_style_piano.md) 五聲音階指法直接相關（pentatonic 是兩者交集）
- 待寫：
  - [concept_texture_change_detection](concept_texture_change_detection.md) (chord density + registral shift 偵測演算法)
  - [concept_modal_scale_fingering](concept_modal_scale_fingering.md) (mode-aware fingering)
  - [composer_debussy_phrasing](composer_debussy_phrasing.md) (Debussy 細分)

