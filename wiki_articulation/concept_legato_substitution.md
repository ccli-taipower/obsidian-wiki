# Concept: Legato Substitution — 連奏段的同音換指偏好

> 來源：Neuhaus *The Art of Piano Playing* §觸鍵章、Matthay *The Visible and Invisible* §legato chapter、Czerny Op.500 Vol.III §legato touch、Heinrich Schmidt-Belden 教學論
> 引用方：[[concept_articulation_overview]] §4、analysis_beethoven_op49_articulation (待寫)
> 狀態：spec v1，2026-05-29；DP 實作 PENDING
> 觸發 case：score-claude DP 目前 `NOTE_RETENTION_PENALTY = 0.0`（同音換指中性），對 legato 段不主動 favor substitution → 浪漫派 + Classical *cantabile* 段系統性失誤

## 1. 為什麼 legato 段要 favor finger substitution

物理上 legato = 「前指還按 → 後指彈下 → 前指鬆」**重疊期 ≥ 1 ms**。當旋律線需要在同一音上維持 legato，**沒有 finger substitution 就無法達成**：

- 旋律從 C5(f5) → C5（同音）→ B4(f4)
- 不換指：f5 彈 C5 → 鬆 → f5 再彈 C5 → 無 overlap，audibly broken
- 換指：f5 彈 C5 → f4 接住 C5 → f5 鬆 → f4 鬆 + f3 彈 B4 → 全 legato ✓

→ 在 legato 段，**同音換指不只是允許，是必要**。

對於非同音的 legato 段，substitution 也常用於「reset 手位」維持連續性（例如八度跨越時用 4-3 substitution 為 thumb-pass 準備手位）。

## 2. Pedagogical 文獻共識

### Neuhaus《The Art of Piano Playing》§連奏觸鍵
> 「legato 的真實意義不是『不分開』，而是『前一個音的釋放與後一個音的進入發生在同一瞬間』。為達此目的，finger substitution 是不可或缺的技術。」

→ Neuhaus 明確把 substitution 列為 legato 的「**技術基礎之一**」，不是可選技巧。

### Matthay《The Visible and Invisible》§legato touch
> 「在持續 melody line 中，同一根手指不能既彈下又釋放給後續音，因為釋放動作本身會中斷聲音持續。Substitution 是樂手的解決方案。」

→ Matthay 從觸鍵物理（不可同時兼任「彈下」與「釋放」）論證 substitution 必要性。

### Czerny Op.500 Vol.III §legato touch (German title: "Vollständige theoretisch-practische Pianoforte-Schule")
> 「Legato 段中，凡是同音重複，應使用 finger change（同音換指）；凡是接續長線條，應預備性地用 substitution 為下個 hand-position 鋪路。」

→ Czerny 把 substitution 分為兩類：
1. **同音換指 (same-pitch substitution)** — 對重複音；本 wiki 主題
2. **預備性換指 (preparatory substitution)** — 為下個 hand position 鋪路；下方 §6 處理

### 19 世紀理論共識
- Kullak《Die Ästhetik des Klavierspiels》§連奏 — 同上觀點
- Türk *Klavierschule* (1789) — 已提到 substitution 是「成熟演奏者必備」

→ 自 18 世紀末以來 substitution 在 legato 段是**標準教學**，不是個人風格選擇。

## 3. 對 score-claude DP 的實作影響

### 3.1 目前狀態

```python
# program/run.py
NOTE_RETENTION_BONUS  = 0.0   # 同音保留 bonus，已停用
NOTE_RETENTION_PENALTY = 0.0   # 同音換指 penalty，已停用
```

註解：「同音可換指」— 這個設計是中性，**DP 不 favor 也不 disfavor** substitution。對 Baroque non-legato（default）合理，但對 legato 段不主動誘導 substitution。

實際結果：DP 對 legato melody 同音重複時，會選 **arbitrary** finger（兩個音可能 f5/f5 重複也可能 f5/f4 substitution，看誰 cost 低）。在 Bach Inv 等 non-legato repertoire 看不出問題，在 Chopin lyrical 段會出現 audibly broken 換指序列。

### 3.2 提案修改

加入 articulation-conditional rule：

```python
# 新增 constant
USE_LEGATO_SUBSTITUTION = False  # opt-in flag, default OFF
LEGATO_SAME_PITCH_SUB_BONUS = -1.5   # 同音換指 cost bonus (負值 = 鼓勵)
LEGATO_PREP_SUB_BONUS       = -0.5   # 預備性換指 cost bonus
```

在 `_run_phrase_dp` cost 計算時：

```python
if USE_LEGATO_SUBSTITUTION and is_in_legato_segment(prev_head, curr_head):
    # 同音 + 不同指 = substitution
    if prev_head["midi"] == curr_head["midi"] and prev_finger != curr_finger:
        cost += LEGATO_SAME_PITCH_SUB_BONUS   # 鼓勵
    # 同音 + 同指 = audibly broken in legato → penalty
    elif prev_head["midi"] == curr_head["midi"] and prev_finger == curr_finger:
        cost += abs(LEGATO_SAME_PITCH_SUB_BONUS) * 2   # 強懲罰
```

判斷 `is_in_legato_segment` 需 articulation 訊號（slur ID 或 articulation marker）— 由 [[concept_articulation_overview]] §5 描述的 hook 提供 `head["slur_id"]` 或 `head["articulation"]`。

### 3.3 Per-piece opt-in

效仿 BACH_INV_PHRASE_FLAGS 機制，新增 articulation 軸：

```python
BACH_INV_PHRASE_FLAGS[N] = {..., "legato_substitution": True}
SINGLE_PDF_PHRASE_FLAGS[stem] = {..., "legato_substitution": True}
```

並進 `_VALID_PHRASE_FLAG_KEYS` + `_PHRASE_FLAG_MAPPING`（score-claude `302926f` refactor 已經為此鋪好 single-source-of-truth 機制）。

預期啟用對象：
- 易 Beethoven 奏鳴曲（Op.49 等）— Classical period 有明確 cantabile 段標記
- Chopin Op.9-2 → 已 fioritura filter 在；legato substitution 可進一步改善 melody 段
- Bach 2-voice → 大部分 mvts 是 non-legato，**不啟用**

## 4. 預期 cost 改變

對 Beethoven Op.49 No.2 mvt2 (G major、F major lyrical 段)：
- 預期 RH 多處同音換指（特別 4→5 與 3→4 在 melody pivot 處）
- LH alberti bass 段不受影響（已 alternation 模式）
- 預期 cost 變化：以 substitution-bonus 計，整曲 cost 應略降；過度禁用同指重複會略升
- Red-line 預期：對既有 Bach Inv (非啟用) bit-identical

## 5. 預備性換指 (preparatory substitution) — 次要分支

Czerny 提到的第二類 substitution：為下個 hand position 鋪路。

例：上行 octave scale C → D → E → F → G → A → B → C：
- 標準指法 1-2-3-1-2-3-4-5 (with thumb cross at F)
- 在 F 那個 thumb cross 之前，若上一句末是 C5(f3)，可以**預備性** substitution 把 f3 換成 f4 給下一段更好 hand position
- 這需要 multi-step lookahead，DP 內部自然會處理

→ 此類別不需要新 cost rule（DP 透過 transition cost 已隱式處理），但需要 wiki 文獻支持 substitution 不只是同音換指，也包括這類預備手段。

## 6. 失效情境 / 不適用 case

- **Baroque non-legato 段**: 不啟用此 rule，否則會誘導 unnecessary substitution
- **快速 passage**（≥ Allegro tempo 的 16th-note runs）：substitution 來不及執行，反而要 hand-position-stable
- **Trill / mordent / ornament**：ornament 內部 fingering 由獨立規則處理，不適用 substitution rule
- **Chordal texture**: 和弦 voicing 由 `_assignment_cost` 處理，substitution 不適用於 simultaneous attack 的和弦

→ 這也是為何 `USE_LEGATO_SUBSTITUTION` 應 default OFF + per-piece opt-in：避免 over-application。

## 7. A/B 驗證計畫（未跑）

當 DP 實作後，驗證流程：

1. **Cost red-line** — 對 Bach Inv 全 8 首跑 baseline (flag OFF) vs test (flag ON 對個別 piece) 比 cost
2. **Override match** — 對 K283 / K545 (already in scope) 看 substitution 啟用後 override match rate
3. **Visual inspection** — Beethoven Op.49 No.2 mvt2 lyrical 段渲染 PDF 看 fingering 是否更自然

## 8. 與其他 wiki 頁面的關係

- [[concept_articulation_overview]] — 本頁的 parent 概覽
- concept_baroque_non_legato.md (待寫) — 為何 Baroque 不應該預設啟用
- concept_staccato_hand_jump.md (待寫) — 互補頁，staccato 段做的事相反
- [[../wiki_piano/concept_thumb_technique]] — substitution 與 thumb cross 的互動
- [[../wiki_piano/concept_finger_span_table]] — substitution 改變了「下一步」的 hand position
- [[../score-claude/memory/project_target_repertoire_intermediate]] — 為何此 rule 對 intermediate 階段最有用（lyrical Beethoven Op.49）
