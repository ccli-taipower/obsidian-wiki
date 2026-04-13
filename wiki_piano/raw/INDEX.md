# Raw Reference Material — Index

**Purpose**: primary/near-primary sources on piano biomechanics, ergonomics, and injury prevention. Populated to address the project's reframing (2026-04-11) from "override agreement" toward "long-term biomechanical correctness".

**Status**: initial 9-item fetch complete (2026-04-11). Review this list to decide which files are worth deep reading. None of this material has yet been converted into operational `concept_*.md` wiki pages — that's the next step.

---

## 1. `weight_transfer/` — Classic weight-school texts

### `ortmann_1929_physiological_mechanics.pdf` + `ortmann_1929_text.txt`
- **Source**: archive.org `in.ernet.dli.2015.89583` (Digital Library of India, public domain)
- **Full title**: *The Physiological Mechanics of Piano Technique* by Otto Ortmann, 1929
- **Why it matters**: Ortmann is the first rigorous experimental biomechanics of piano playing — he built measurement apparatus and actually quantified forces, not just theorised. This is the empirical foundation of everything that followed (Taubman, Sándor, modern research).
- **Size**: 38 MB PDF, 918 KB plaintext. Long — treat as reference, not cover-to-cover.
- **Worth reading**: chapters on finger force vs weight, wrist positions, and the "reach" mechanism if we want to validate our span costs against measured data.

### `matthay_1903_act_of_touch.pdf` + `matthay_1903_text.txt`
- **Source**: archive.org `actoftouchinalli009163mbp` (public domain)
- **Full title**: *The Act of Touch in All Its Diversity* by Tobias Matthay, 1903
- **Why it matters**: Matthay is the philosophical grandfather of the "weight school" (arm weight > finger force). Anticipates Taubman by ~70 years. Language is 1903-Victorian but the observational content is solid.
- **Size**: 29 MB PDF, 824 KB plaintext.
- **Worth reading**: primarily if we want historical context for why modern pedagogies disagree. For practical DP work, Ortmann is more useful.

---

## 2. `forearm_rotation/` — Taubman-school sources

### `taubman_golandsky_rotation.md`
- **Source**: aggregated from 4 public URLs (Edna Golandsky, Point of Sound, Pianist Magazine) — see file header.
- **License note**: Golandsky's most substantive article ("Why Rotation Matters") is **paywalled**. This file contains only the public material + my synthesis.
- **Why it matters**: Articulates the single most important non-obvious principle we are currently missing in the DP — **forearm rotation does the finger lifting, not the finger extensors**. If true, our entire span-cost model is measuring the wrong physical quantity for fast passages.
- **Contains**:
  - Taubman Basic Principles (alignment, rotation, in-out, shaping, grouping, etc.)
  - Single vs double rotation terminology (supination = thumb side lifts, pronation = pinky side lifts)
  - Seven Pillars summary
  - Three fulcrums (knuckles, wrist, elbow) with injury-prevention mechanics
  - **Detailed Claude-annotated "DP implications"** section at the end
- **Worth reading**: **YES** — read the Claude annotation at the bottom first. The "rotation-consistent cost" idea is the most significant design question raised by this entire exercise.
- **Gap**: single vs double rotation distinction is stated but not fully explained in public sources. If we decide to implement rotation costs, we need the Taubman DVDs or Golandsky's tonebase workbook (paid) to get the actual rules.

---

## 3. `wrist_neutral/` — Carpal tunnel and wrist-neutral mechanics

### `wikipedia_carpal_tunnel.md`
- **Source**: https://en.wikipedia.org/wiki/Carpal_tunnel_syndrome (CC BY-SA 3.0)
- **Why it matters**: Quantifies wrist-position cost. Neutral = 2-10 mm Hg; flexion × 8; extension × 10; dynamic motion up to 111 mm Hg. This tells us that wrist angle is not a soft penalty — it's a nonlinear multiplier on nerve pressure.
- **Contains**:
  - Tunnel pressure multipliers
  - Anatomical contents (9 flexor tendons + median nerve)
  - Occupational odds ratios (vibration 5.4, hand force 4.2, wrist flex/ext 2.0, repetition 2.0)
  - Clinical neutral-splint guidance
  - **Detailed Claude DP-implications section** covering the "累積損傷" (cumulative damage) principle
- **Worth reading**: **YES** — short (~50 lines) and directly actionable.

---

## 4. `anatomy/` — Hand and forearm muscle anatomy

### `wikipedia_hand_muscles.md`
- **Source**: Wikipedia lumbricals of the hand + extensor digitorum muscle (CC BY-SA 3.0)
- **Why it matters**: Explains the **anatomical root** of the f3↔f4 coupling (juncturae tendinum) and why f2/f3 feel different from f4/f5 (lumbricals have dual nerve supply — median for f2/f3, ulnar for f4/f5).
- **Key facts**:
  - Juncturae tendinum mechanically link the extensor tendons — this is why f4 cannot extend independently
  - Lumbricals produce the "hook" position (MCP flex + IP extend) used in scales — **small muscles that fatigue quickly**
  - Dual nerve supply creates a natural f2-f3 vs f4-f5 asymmetry in motor control
- **Worth reading**: **YES** — validates and refines `ADJACENT_COUPLING_PENALTY`. Claude annotation notes current penalty should fire on *simultaneous* f3+f4 demands, not just transitions.

### `wikipedia_pronation_supination.md`
- **Source**: Wikipedia anatomical_terms_of_motion + supinator muscle + pronator teres (CC BY-SA 3.0)
- **Why it matters**: The anatomy underlying the Taubman rotation concept. Also introduces **pronator teres syndrome** — a real RSI from repetitive forearm rotation.
- **Key facts**:
  - Rotation axis is the ulna (f5 side) — so rotation around f5 is mechanically cheaper than rotation around f1
  - Disabling supinator = −64% supination strength (it's a dedicated muscle, not a side-effect)
  - Biceps takes over under heavy load — so ff passages recruit different muscles than pp passages
  - **Ulnar deviation + palmar flexion** = classical CTS-inducing posture
- **Worth reading**: **YES** — short and clarifies what "rotation" actually is physically.

---

## 5. `pianist_injury/` — Clinical and empirical studies

### `pmc_kinematics_and_review.md`
- **Sources**: two PMC open-access papers (CC BY)
  1. *PMC6300245*: piano-student joint kinematics + MSD correlations
  2. *PMC7007903*: systematic review of musculoskeletal disorders in professional musicians (109 papers)
- **Why it matters**: The strongest evidence-based material in this collection. Numbers you can actually trust.
- **Most important findings**:
  - Wrist extension > 20° significantly increases striking force + correlates with MSD
  - Small hand span vs MSD: r = −0.69 (huge effect size)
  - **"Finger joint mobility, particularly right 3–4 span, is a risk factor for piano-related pain"** — this is the single most DP-actionable sentence found in the entire literature search
  - Octaves + chords = 74% of techniques practiced at injury onset
  - >20 h/week practice threshold for MSD
  - Pianist MSD prevalence: 45-93% across studies
- **Worth reading**: **YES — highest priority after the Claude annotation on Taubman.**

### `altenmuller_dystonia.md`
- **Source**: PMC3865372 (CC BY open access)
- **Why it matters**: Eckart Altenmüller is the leading researcher on musician's focal dystonia (the career-ending injury). Even though the experimental result was null, the paper's *description* of dystonia includes a critical observation:
  > "Upward scales proved especially problematic due to requiring complex anticipatory coordination maneuver of thumb, remaining four fingers and the wrist"
- **Worth reading**: skim for the description of dystonia mechanics. The experimental methodology is not directly useful.
- **Gap**: Altenmüller & Détári (2025) "Preventing Musician's Focal Dystonia" is the actionable paper but is behind a paywall — worth chasing via institutional access.

---

## Items not fetched

- **PAMA position papers** (item #5 in original fetch list): the Performing Arts Medicine Association publishes *Medical Problems of Performing Artists* journal, but open-access position papers specifically on pianist hand injury are not directly downloadable from artsmed.org. The two PMC papers above cover the same territory authoritatively.
- **Golandsky "Why Rotation Matters"** (item #3 partial): paywalled. Public substitutes were used instead.
- **Altenmüller & Détári 2025**: paywalled. Citation noted for future follow-up.
- **Sándor's "On Piano Playing"**: would be the ideal counterweight to Taubman (Russian weight school vs rotation school) but is under copyright and not freely available.
- **Neuhaus "The Art of Piano Playing"**: same — copyright-restricted.

---

## How I recommend reading this

If you have 30 minutes:
1. `taubman_golandsky_rotation.md` — Claude annotation section (bottom)
2. `pmc_kinematics_and_review.md` — full file, focusing on the f3-f4 span finding
3. `wikipedia_carpal_tunnel.md` — full (it's short)

If you have an hour:
- Add `anatomy/wikipedia_hand_muscles.md` (juncturae tendinum) and `anatomy/wikipedia_pronation_supination.md`.

Deep dive:
- `ortmann_1929_text.txt` — use ctrl-F to find specific topics (force measurements, wrist positions, octave stretches). Don't read linearly.

---

## Proposed next step

Once you've reviewed which of these you find convincing, we should decide whether to:

- **(A)** Add a wrist-angle cost term to the DP — low risk, directly supported by the PMC + CTS data, no Taubman dependency.
- **(B)** Add a rotation-continuity cost term — high value but requires more Taubman material before we can implement it non-hand-wavingly.
- **(C)** Re-weight the existing f3-f4 span cost to be asymmetric (RH > LH) based on the Sakai/Shimawaki finding.
- **(D)** Keep this as background-only and continue optimizing override agreement.

My recommendation: **(C)** and **(A)** are safe immediate wins. **(B)** deserves a separate design discussion before implementation.
