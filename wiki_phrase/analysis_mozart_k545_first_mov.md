# Analysis: Mozart Piano Sonata K545 in C major, 1st movement (B1-12 excerpt)

> Source: PIG val piece 017 (`017_Mozart_PSon_K545_C_i_B1-12`)
> Cadence Phase 2 validation result: secondary (texture limit) — see [[concept_cadence_detection]] §7.4
> Status: tested 2026-05-27, IAC detected at m7→m8 but DP fingering improvement NOT realized

## 1. Excerpt structure

12 bars of K545 mvt1 — the famous opening of "Sonata facile". B1-12 covers:
- m1-4: first theme antecedent (4 bars, ends on HC at m4 — but m4's dominant landing is too short for our HC detection)
- m5-8: consequent — running ascending scale m5-m7 + descending resolution m8 (IAC: V7 in 3rd inversion at m7 → I root at m8, soprano on E not C)
- m9-12: transition / second theme group in dominant key (G major)

## 2. Cadence detection result

- **m7→m8**: detected as **IAC** by `_classify_cadence_pair`. music21 returns:
  - m7 final = [F4, B4, G5] → `V inv=3` (V7 in 3rd inversion, bass=F)
  - m8 final = [C2, E2, E4] → `I inv=0` (root position), soprano=E4 (pc=4) ≠ C tonic → IAC
- **Result**: boundary added at first group of m9 (correct, matches musical phrase structure)
- **Pass 3 fallback m5 boundary**: NOT suppressed in window mode (distance from cadence m9 = 4 bars > suppress_bars=1)
- **Pass 3 fallback m9 boundary**: SUPPRESSED (window mode removes Pass 3 m9 because cadence is at m9)
- **Final phrase_starts under cadence config**: identical to BASE (m1, m5, m9, m11 — m9 just sourced from cadence instead of Pass 3)

## 3. PIG fingering disagreement

K545 RH B1-12 had pre-existing -8.4pp regression with figural+thumb flags ON (Phase 2.3 PIG sweep). Root cause traced to m5 ascending scale:
- PIG 6/6 annotators: 1-2-3-1-2 (thumb-under at D5)
- BASE DP: 1-2-3-4-5 (no thumb-under — already wrong vs PIG, but stable)
- With thumb-reservation ON (TRT): 2-3-4-5-2 (worse — boundary at m5 triggers anti-thumb cost)

## 4. Why Cadence Phase 2 doesn't fix this

The hope was: detect cadence elsewhere → disable Pass 3 fallback → remove m5 false boundary → DP gets longer planning horizon → maybe chooses thumb-under naturally.

What actually happened:
1. Cadence detected at m8 IAC ✓
2. Window mode default kept Pass 3 m5 boundary alive (only Pass 3 m9 boundary suppressed since it overlapped with cadence)
3. Even with full-disable mode (CADENCE_DISABLES_FALLBACK=True), K545 m5 boundary removed → DP fingering still 1-2-3-4-5 (no change)

The conclusion: K545 m5 fingering is determined by DP cost terms, not phrase boundary structure. Boundaries are necessary but not sufficient. Future fix candidates:
- "Long-scale protection" cost rule (don't shift fingers mid-scale)
- Manual per-piece fingering override for the m5 region
- Reweight existing scale-aware cost terms

## 5. HC over-fire concern (why HC was not included in Phase 2)

K545 m1, m2, m4 all have measures ending on a single bass note D (dominant), which music21 classifies as `v` (incomplete minor dominant) or `V`. Including HC detection would add false boundaries at m2, m3, m5 — one per bar in the opening. This is the main reason HC is excluded from Phase 2 scope.

## 6. Cross-refs

- [[concept_cadence_detection]] §7 — Phase 2 algorithm + K283/K545 validation summary
- [[composer_mozart_phrasing]] §7 — K545 status
- [[analysis_mozart_k283_first_mov]] — sister piece, primary success case
- score-claude memory: `project_cadence_phase_2.md`
