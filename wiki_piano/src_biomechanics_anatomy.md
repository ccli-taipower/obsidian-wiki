---
title: "Biomechanics & Anatomy — New Source Batch (wiki_piano/raw/)"
date_ingested: 2026-04-11
source_type: mixed
tags: [biomechanics, anatomy, injury, taubman, rotation, forearm, carpal-tunnel, dystonia]
---

# Biomechanics & Anatomy — New Source Batch

Five files from `wiki_piano/raw/`. All fetched 2026-04-11.

---

## 1. Hand Muscles — Wikipedia (anatomy/wikipedia_hand_muscles.md)

**Sources**: en.wikipedia.org — Lumbricals of the hand + Extensor digitorum muscle (CC BY-SA 3.0)

**Key takeaways**:
- Lumbricals 1-2 (index, middle) = **median nerve**; lumbricals 3-4 (ring, little) = **ulnar nerve**. Dual neural pathway is the anatomical root of f2/f3 vs f4/f5 asymmetry in motor control.
- **Juncturae tendinum** (transverse bands between extensor tendons) mechanically link f3 and f4 — this is why f4 cannot extend independently of f3/f5.
- Lumbricals produce the "hook" position used in scales (MCP flex + IP extend); they are **small muscles that fatigue quickly** → weight school's rationale.
- `ADJACENT_COUPLING_PENALTY = 0.6` for f3↔f4 is directionally correct but should also fire on **simultaneous** demands (f3 held while f4 plays), not just sequential transitions.

→ See [[concept_hand_anatomy]]

---

## 2. Pronation / Supination — Wikipedia (anatomy/wikipedia_pronation_supination.md)

**Sources**: en.wikipedia.org — anatomical terms of motion, supinator muscle, pronator teres (CC BY-SA 3.0)

**Key takeaways**:
- **Ulna is the rotation axis** (f5 side stays fixed; radius orbits around it). DP consequence: f5 as pivot is anatomically cheap; rotation around f5 costs less than rotation around f1.
- Supinator accounts for **64% of supination strength** — dedicated, powerful muscle.
- **Pronator teres syndrome** = RSI from repetitive forearm rotation/supination. Long-term overuse damages the median nerve at the pronator teres.
- Biceps takes over supination under heavy load (ff passages). Different muscle recruitment at forte vs piano.
- **Ulnar deviation + palmarflexion** = classical CTS posture. Penalise fingerings forcing both simultaneously.

→ See [[concept_forearm_rotation]]

---

## 3. Taubman / Golandsky — Forearm Rotation (forearm_rotation/taubman_golandsky_rotation.md)

**Sources**: golandsky.com, pointofsound.com, pianistmagazine.com (all public)
**Access gap**: Golandsky's core article "Why Rotation Matters" is paywalled. Below uses public materials only.

**Key takeaways**:
- **Core thesis**: forearm rotation does the finger lifting; fingers should not lift themselves. Isolated finger lifting causes fatigue, tension, and RSI.
- **Single rotation**: one continuous rotational impulse for runs in one pitch direction. RH ascending = supination. RH descending = pronation.
- **Double rotation**: preparatory counter-rotation before playing rotation. Used for repeated notes, trills, alternating patterns (pendulum mechanism).
- **Seven Pillars**: passive energy sources, unified forearm-hand unit, optimal alignment, sensory continuum, rebound mechanics, muscular recoil, potentiation.
- DP implication: current `FINGER_COMFORT_SPAN` measures static stretch, not rotational feasibility. A Taubman model would reframe span costs as rotation-arc costs.
- **Still missing**: exact rules for single vs double rotation. Do not implement rotation-cost DP terms until more Taubman material is available (Golandsky tonebase or DVDs).

→ See [[concept_forearm_rotation]]

---

## 4. PMC — Pianist Kinematics & MSD Systematic Review (pianist_injury/pmc_kinematics_and_review.md)

**Sources**:
- PMC6300245 — joint kinematics & MSD in piano students (CC BY)
- PMC7007903 — systematic review of musculoskeletal disorders in professional musicians, 109 papers (CC BY)

**Key takeaways**:
- Wrist extension > 20° significantly increases striking force and correlates with MSD. Mean healthy wrist: −5.2° (slight flexion). **Hard threshold, not a soft penalty.**
- Hand span vs MSD: **r = −0.69** (p ≤ 0.004) — very strong inverse correlation. Small hands = clinically validated injury group.
- **"Finger joint mobility, particularly right 3–4 span, is a risk factor for piano-related pain"** (Sakai & Shimawaki). Most DP-actionable sentence in the entire literature. → RH f3-f4 span should cost more than LH.
- Octave + chord techniques = **74% of techniques practiced at injury onset**.
- >20 h/week practice significantly raises MSD incidence.
- MSD prevalence across studies: 45-93%.
- Joint synchronisation: experts show negative elbow-wrist correlation (elbow extends when wrist flexes) — an efficiency pattern.

→ See [[concept_finger_span_table]], [[concept_small_hands]]

---

## 5. Altenmüller — Focal Dystonia (pianist_injury/altenmuller_dystonia.md)

**Source**: PMC3865372, Altenmüller et al. (CC BY)
**Note**: Experimental result was null (altered auditory feedback did not help MD). Use for descriptive content, not intervention guidance.

**Key takeaways**:
- Dystonia = "degradation of voluntary control of highly skilled movement patterns" + co-contraction of wrist flexors and extensors.
- **"Upward scales proved especially problematic due to requiring complex anticipatory coordination maneuver of thumb, remaining four fingers and the wrist."** Thumb-pass mechanism is the neurally demanding part.
- Affects 1-2% of professional musicians — low prevalence but **career-ending**.
- Involuntary curling/extending of digits = loss of finger independence → validates f3↔f4 coupling penalty from a neurological angle.
- DP implication: ascending scales with thumb-pass should cost slightly more than descending. Cumulative thumb-pass count matters; do not let cheap individual cost lead to overuse.

→ See [[concept_forearm_rotation]], [[concept_thumb_technique]]

---

## Weight Transfer Texts (weight_transfer/)

`ortmann_1929_physiological_mechanics.pdf` and `matthay_1903_act_of_touch.pdf` are in raw but not deeply read for this ingest. Both are public-domain historical texts:
- **Ortmann (1929)**: first rigorous experimental biomechanics of piano playing. Quantified finger force vs arm weight, wrist positions.
- **Matthay (1903)**: philosophical grandfather of the "weight school" (arm weight > finger force). Anticipates Taubman.

**Status**: retained as deep-reference. No concept pages created yet; revisit if we add arm-weight cost to DP.
