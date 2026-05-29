# Analysis: Mozart Piano Sonata K283 in G major, 1st movement (B0-22 excerpt)

> Source: PIG val piece 011 (`011_Mozart_PSon_K283_G_i_B0-22`)
> Cadence Phase 2 validation result: **primary success — Δ+1.01pp RH**
> Status: tested 2026-05-27, IAC detected at m9→m10
> 前身：Phase 1 prediction page (2026-05-26); Phase 2 實測結果覆蓋

## 1. Excerpt structure

22 bars of K283 mvt1 (G major) with pickup measure (m0). Sonata-allegro exposition opening:
- m1-8: opening theme group (period structure, several sub-phrases via Pass 3 fallback)
- m9-10: IAC arrival in G major — V root → i root + soprano F# (not tonic → IAC)
- m11-22: continuation / transition

## 2. Cadence detection result

- **m9 final** = [D4, C5, F#5] → music21 `V inv=0` (root position dominant)
- **m10 final** = [G2, F#5] → music21 `i inv=0` (root position tonic, music21 marks lowercase because chord is incomplete)
- soprano midi=78 (F#, pc=6) ≠ G tonic (pc=7) → IAC
- Boundary added at first group of m11

## 3. Other cadences explicitly NOT detected (correct behavior)

- m7 V inv=1 → m8 vi inv=0: V→vi = **deceptive cadence (DC)**. `_classify_cadence_pair` correctly returns `None`. Not a phrase boundary.
- m4 final = `i inv=0` (lowercase, partial chord): no V before it → not classified as cadence
- m6 final = `v inv=0` (lone D): not followed by I → no cadence pair

## 4. Result

- BASE phrase_starts include Pass 3 fallback at m5, m9, m13, m17, m21 (every 4 bars)
- Cadence boundary at m11 added (no Pass 3 boundary at m11 — gap filled by cadence)
- Window mode: Pass 3 boundaries at m9, m13 within ±1 of cadence m11? m9 distance = 2 > 1 (kept), m13 distance = 2 > 1 (kept)
- Final difference: cadence m11 ADDED to existing Pass 3 boundaries
- **Δ RH GMR = +1.01pp** (PIG val all-annotator weighted)

## 5. Why Phase 2 works here (and not on K545)

K283 has fuller texture — LH actually plays bass under RH melody, so chordify produces clean V/I chord identifications. K545 m5-m7 has LH absent / sparse, so music21 sees only the RH scale; harmonic bass is implicit (Mozart wrote alberti elsewhere but not in scale runs).

## 6. Full-piece prediction (pre-Phase 2 context, retained for reference)

K283 1st mov (G major, Allegro, ~120 bars) is a textbook sonata-allegro:
- Exposition (bb. 1-53): first theme PAC at b8 → transition → second theme in D → closing PAC at b53
- Development (bb. 54-71): fragmentation + re-transition
- Recapitulation (bb. 72-end): themes in tonic

PIG val piece covers only B0-22 (exposition opening). The IAC at m10 is within the first theme group (consequent ending), consistent with antecedent (m1-8) + consequent (m9-10) period structure.

PIG K283 has 6 annotators (ES, HI, HK, YI / YS, EF) — more than most pieces, indicating it is a PIG benchmark. Cost framework uses `min(cost_pig_min, cost_pp)` as the strongest opponent.

## 7. Cross-refs

- [concept_cadence_detection](concept_cadence_detection.md) §7 — Phase 2 algorithm + validation
- [composer_mozart_phrasing](composer_mozart_phrasing.md) §7 — K283 status
- [analysis_mozart_k545_first_mov](analysis_mozart_k545_first_mov.md) — sister piece, shows texture-limit case
- [concept_classical_period_sentence](concept_classical_period_sentence.md) — period 4+4 structure context
- [analysis_bach_inv_4_d_minor](analysis_bach_inv_4_d_minor.md) — counterpoint vs homophony contrast
- score-claude memory: `project_cadence_phase_2.md`

