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

## 4. v2 direction-aware modular pattern (2026-05-27)

v1 deployed with two hardcoded guards (`offset % 5 == 2` modular + RH-asc/LH-desc direction restriction) that worked for K545's specific 8-note segment but didn't generalise. v2 (commit `2a9d136`) replaced both with a principled rule derived from standard piano pedagogy.

### 4.1 Pedagogical basis

| Case | 1-octave (8-note) pattern | Multi-octave extension |
|---|---|---|
| RH asc / LH desc (thumb-under) | `1-2-3-1-2-3-4-5` | `(1-2-3)(1-2-3)...(1-2-3-4-5)` |
| RH desc / LH asc (thumb-over) | `5-4-3-2-1-3-2-1` | `(5-4-3-2-1)(3-2-1)(3-2-1)...` |

Pivot transition offsets:
- **Thumb-under**: `offset % 3 == 2` (offsets 2, 5, 8, 11...)
- **Thumb-over**: `offset >= 4 AND (offset - 4) % 3 == 0` (offsets 4, 7, 10...)

### 4.2 End-guard

Uniform across directions: pivot fires only if `seg["end"] - curr_idx >= 2` — leaving at least 2 notes after the pivot landing for the closing finger group (3-4-5 ascending or 3-2-1 descending).

### 4.3 What this fixes vs v1

| Limitation | v1 | v2 |
|---|---|---|
| Modular pattern | hardcoded `% 5 == 2` | direction-aware `% 3 == 2` / `>= 4 AND (-4) % 3 == 0` |
| 5-note scale spurious thumb-under | could fire | end-guard rejects ✓ |
| Long scale missing 2nd thumb-under | only offset 2 fired | both 2 + 5 fire ✓ (K545 m9 +3.51pp gain) |
| RH descending thumb-over | disabled by direction guard | enabled ✓ |
| LH ascending thumb-over | disabled by direction guard | enabled ✓ |

### 4.4 K545 + K283 regression test (v1 → v2)

| Piece | v1 RH | v2 RH | Δ v2 - v1 |
|---|---|---|---|
| K545 (PIG 017) Run D | 74.08% | **77.59%** | **+3.51pp** |
| K283 (PIG 011) Run D | 54.28% | 54.28% | 0pp (preserved) |

26 non-target PIG val pieces byte-identical across Runs A/B/C/D (isolation preserved).

v2 unexpectedly IMPROVES on v1: K545 m9 has a longer ascending segment than m5, and v2 fires multiple thumb-unders (offsets 2 + 5) where v1's `% 5 == 2` only fired once. m9 now matches PIG `1-2-3-1-2-3-4-5` pattern with partial PIG agreement at the top (midi 79: PIG `1/1/4/1/1/4`, v2 picks `1` matching 4/6 annotators).

### 4.5 Cross-piece probe (Layer 4)

075 Chopin Op64-2: 1 RH segment detected (length 4, descending). Δ RH = 0.00pp (no DP change).
140 Scarlatti K208: 4 RH segments detected (lengths 5, 5, 9, 9). Δ RH = 0.00pp (no DP change).

Both neutral — v2 doesn't help nor hurt non-target pieces. Confirms v2 is safe to enable on other pieces (no false-positive cascade).

### 4.6 v3 candidates (future)

- Per-key-signature pivot offset table (v2 assumes segment first transition starts the "1-2-3" or "5-4-3-2-1" pattern; F# major or chromatic-leaning keys may differ)
- Bach Inv mvts enablement (1-3-1-3 alternation preference in Bach scales)
- Pivot-position-aware DP rather than cost-cancellation

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

- Cost-function side: [concept_thumb_technique](concept_thumb_technique.md) §Long-scale exception
- Phrase track: [wiki_phrase/_implementation_status](wiki_phrase/_implementation_status.md) §long_scale per-piece flag
- K545 case study: [wiki_phrase/analysis_mozart_k545_first_mov](wiki_phrase/analysis_mozart_k545_first_mov.md) §4 (FIXED 2026-05-27)
- Source: Altenmüller PMC3865372 (the rule we're contextually cancelling)
- Spec: `docs/superpowers/specs/2026-05-27-long-scale-thumb-under-design.md`
- Memory: *project_long_scale_thumb_under*
