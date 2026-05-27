# Concept: Long-Scale Thumb-Under Protection

> Source: K545 m5 PIG 6/6 unanimous fingering vs DP regression after Cadence Phase 2
> Status: implemented 2026-05-27 (default OFF, per-piece opt-in for K283 + K545)
> See: docs/superpowers/specs/2026-05-27-long-scale-thumb-under-design.md
>       docs/superpowers/plans/2026-05-27-long-scale-thumb-under.md

## 1. Why this rule exists

Standard piano pedagogy for diatonic scales longer than 5 notes uses **thumb-under**
(RH ascending) / **thumb-over** (RH descending) — alternating finger groups via a thumb
pivot. K545 RH m5 (A4-B4-C5-D5-E5-F5-G5-A5 ascending) has PIG 6/6 unanimous
`1-2-3-1-2-3-4-5` with thumb-under at D5.

But `_transition_cost` at `program/run.py:1166-1178` classifies thumb-under transitions
(RH ascending: pf=3, cf=1, cm>pm) as **WRONG_DIRECTION** because the finger NUMBER
decreases while the pitch INCREASES. Plus Altenmüller (PMC3865372) anti-focal-dystonia
penalty `THUMB_PASS_UPWARD_EXTRA` adds extra cost. Total surcharge ≈ 11.0 per qualifying
transition. Without contextual cancellation, DP picks the stretchy alternative
`1-2-3-4-5` which is biomechanically dead-end (f5 strands).

## 2. Sensor predicate

A "scale segment" requires:
- All consecutive transitions stepwise: `|interval| in {1, 2}` (whole or half steps)
- Same direction throughout (all ascending or all descending)
- Length ≥ `SCALE_MIN_LEN` (default 4)
- Not chromatic: max consecutive `|interval|==1` < `SCALE_MAX_CHROMATIC_RUN + 1` (default 2+1=3)
- All groups single-note (chord groups close any open segment)

Chromatic scales (`|interval|=1` throughout) intentionally use 1-3-1-3 alternation, NOT
thumb-under — hence the exclusion.

## 3. Cost cancellation + v1 guards

When a transition (prev_idx → curr_idx) lies inside a detected segment AND matches one
of the 4 thumb-pass patterns, the rule subtracts the WRONG_DIRECTION +
THUMB_PASS_UPWARD_EXTRA amount from `tc`.

**Asymmetric impact** (verified against `_transition_cost`):

| Case | WRONG_DIRECTION fires? | THUMB_PASS_UPWARD_EXTRA fires? | Subtract |
|---|---|---|---|
| RH ascending  thumb-under (pf≥3, cf=1, cm>pm) | YES | YES | ~11.0 |
| RH descending thumb-over (pf=1, cf≥3, cm<pm) | YES | no  | ~10.5 |
| LH ascending  thumb-over (pf=1, cf≥3, cm>pm) | no  | YES | ~0.5  |
| LH descending thumb-under (pf≥3, cf=1, cm<pm) | no  | no  | 0     |

LH cases mostly no-op because `_transition_cost` already accepts LH thumb-pass.

## 4. v1 implementation deviations from spec (known limitations)

The deployed v1 has two guards added during implementation that are NOT in the original spec:

### 4.1 Direction guard

Only `(hand="right" and direction=+1)` OR `(hand="left" and direction=-1)` triggers cancellation.
The 2 thumb-OVER cases are NOT cancelled in v1:
- RH descending thumb-over (would benefit Bach WTC descending RH scales)
- LH ascending thumb-over (LH no-op anyway, see asymmetry table)

K545 (target) only uses RH ascending — guard is safe for our validation but limits applicability
to non-target pieces with descending RH scales.

### 4.2 Position guard `offset % 5 == 2`

`offset = (prev_idx - seg["start"])`. Cancellation fires only at `offset % 5 == 2`.

This pins the rule to the conventional C-major-style pivot position (thumb-under after 3
white-key notes from segment start). Without this guard, DP cycles `1-2-3-1-2-3-1-2-3`
indefinitely because every thumb-under transition costs 0 (over-cancellation).

**Known limitation**: hardcoded for the 5-note "thumb period" of C major / A natural minor.
Other key signatures (F# major, modal scales) have different pivot positions; rule may not
generalize without further work.

### 4.3 Future v2 candidates
- Replace `offset % 5 == 2` with diatonic-pattern-aware pivot detection (count white-key
  positions, not transitions)
- Remove direction guard once a proper "thumb-over pivot" position scheme is added
- Add per-key-signature pivot offset table

## 5. Validation results

| Run | Config | K545 RH | K283 RH |
|---|---|---|---|
| BASE | all OFF | 69.44% | 53.27% |
| LS only | long_scale ON | 73.47% | 54.28% |
| LS+Cadence | long_scale + cadence ON | 73.47% | 54.28% |

Δ K545 = **+4.06pp** (PIG val 28 weighted aggregate, see `tmp/pig28_phrase_ab.py` Run D)
Δ K283 = +1.01pp (cadence preserved)

26 other PIG val pieces byte-identical across Runs A/B/C/D (per-piece flag isolation OK).

## 6. Cross-refs

- Cost-function side: [[concept_thumb_technique]] §Long-scale exception
- Phrase track: [[wiki_phrase/_implementation_status]] §long_scale per-piece flag
- K545 case study: [[wiki_phrase/analysis_mozart_k545_first_mov]] §4 (FIXED 2026-05-27)
- Source: Altenmüller PMC3865372 (the rule we're contextually cancelling)
- Spec: `docs/superpowers/specs/2026-05-27-long-scale-thumb-under-design.md`
- Memory: [[../score-claude/memory/project_long_scale_thumb_under]]
