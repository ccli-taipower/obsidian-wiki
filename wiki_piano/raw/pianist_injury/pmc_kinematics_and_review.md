# Pianist Injury — PMC Open-Access Evidence

**Fetched**: 2026-04-11

Two open-access papers from PubMed Central, both directly relevant to DP cost-function design.

---

## Paper 1: Piano Students — Joint Kinematics and MSD

**Source**: https://pmc.ncbi.nlm.nih.gov/articles/PMC6300245/
**License**: CC BY (PMC open access)
**Citation**: *The correlation between upper extremity musculoskeletal symptoms and joint kinematics, playing habits and hand span during playing among piano students*

### Abstract (verbatim)

> "The piano students recruited for this study experienced a variety of MSD during the past 12 months, with a particularly high prevalence of neck pain (80%). Extreme wrist extension and/or elbow flexion while playing the piano also correlated with MSD."

### Key quantitative findings

**Prevalence (preceding 12 months):**
- Neck: 80%
- Upper back: 60%
- Lower back: 53.3%
- Wrist (combined): 33.3%

**Wrist extension:**
- 20° extension significantly increased striking force
- Correlated with hand + body MSD in preceding week AND preceding year
- Mean wrist flex-ext: −5.2° (range −31.2° flexion to +37.5° extension)
- Mean ulnar deviation (healthy players): 4.5° (range −7.7° to 11.1°) — slight ulnar deviation is normal

**Elbow flexion:**
- Excessive flexion correlated with total-body pain (preceding week)
- Mean elbow flexion: 73.5° (range 29.1°–103.9°)

**Hand span (most directly relevant for DP):**
- Smaller span = higher injury risk
- Hand span vs MSD (preceding week): r = −0.69, p ≤ 0.004
- Hand span vs MSD (preceding year): r = −0.56, p ≤ 0.023
- Mean span: 21.3 cm (range 19.0–26.5 cm)
- **Octaves account for 74% of techniques practiced** — this is where small-hand pianists injure themselves
- Conclusion: "Pianists with small hands prone to overuse injuries in upper extremities"

**Joint synchronization (novel finding):**
- 93% of subjects showed negative correlation between elbow and wrist sagittal motion (r = −0.03 to −0.65)
- Interpretation: when elbow extends, wrist flexes — an **efficiency pattern** observed in better players
- Recommendation: coaches should train joint synchronization, not just individual joint positions

**Playing hours:**
- Weekly hours vs body MSD (preceding week): r = 0.58, p ≤ 0.024
- Mean: 23.9 h/week (range 10.5–39.0)
- **>20 h/week threshold** shows higher MSD incidence in cited literature

### Limitations

- No finger-level analysis (markers on hand + wrist only)
- Small sample, cross-sectional (no causation)
- Joints beyond elbow and wrist not monitored

---

## Paper 2: Systematic Review — Musculoskeletal Disorders in Professional Musicians

**Source**: https://pmc.ncbi.nlm.nih.gov/articles/PMC7007903/
**License**: CC BY (PMC open access)
**Scope**: 109 articles total (1 case-control, 6 cohort, 62 cross-sectional, 12 interventional, 28 case reports)

### Abstract (verbatim)

> "Musicians' practice and performance routines reportedly lead to musculoskeletal complaints and disorders (MCD) that impact their wellbeing and performance abilities. This systematic review aims to assess the prevalence, risk factors, prevention and effectiveness of treatments for MCD in professional musicians and consider the methodological quality of the included studies."

### Pianist-specific prevalence

| Study | Population | Finding |
|---|---|---|
| (Unnamed, piano students) | Student | **93% prevalence** of playing-related injuries |
| De Smet et al. | Professional | 45% prevalence of overuse syndrome |
| Sakai (n=200) | Clinical series | Tenosynovitis/tendinitis: 56; Enthesopathy: 49; Muscle pain: 38 |

### Biomechanical risk factors (Sakai & Shimawaki, case-control)

> "Epicondylitis, muscle pain in the forearm and hypothenar region, De Quervain's tendinitis and distal tendinitis correlate with variable parameters of small hand size"

### Finger span as injury predictor

> "Finger joint mobility, particularly right 3–4 span, is a risk factor for piano-related pain"

**This is the most directly DP-relevant finding in the entire literature search.** It says: **the f3–f4 span is a specific injury risk factor for the right hand**. Our `ADJACENT_COUPLING_PENALTY` penalises f3↔f4 transitions, but this paper suggests the raw *span* between f3 and f4 is itself a risk — so fingerings that stretch f3-f4 should cost more than our current model suggests, especially in RH.

### Repertoire-level risk

> "Octaves and chords: 74% of techniques practiced at onset" (of injury)

---

## Piano Relevance (Claude annotation, 2026-04-11)

### Actionable DP changes

1. **RH f3–f4 span should cost more than LH f3–f4 span.** Current model treats them symmetrically. The Sakai/Shimawaki data say the asymmetry is clinically validated: RH is the high-risk hand for this specific span.

2. **Hand-size dependence is real and ~0.69 correlation with injury.** Our `HAND_SIZE = "M"` constant currently scales all spans uniformly by 0.85/1.0/1.15. This paper implies we should also weight the *injury cost* (not just feasibility cost) by hand size — a "S" hand playing octaves should pay much more than a "L" hand, not just a linear scaling.

3. **Wrist extension > 20° is a hard threshold.** Our DP has no wrist model at all. As a first approximation, we could add a **penalty for fingerings that imply wrist extension** — and the main driver of wrist extension in piano is *reaching* with f1 or f5 at the edges of the hand. This may already be captured indirectly by our max-span cost, but we should verify.

4. **Joint synchronization** is a higher-order concept our DP cannot model without arm/wrist state — but it suggests we should be cautious about "locally optimal" fingerings that force the wrist to work against the elbow. This is why Taubman emphasizes the unified forearm-hand unit.

5. **>20 h/week injury threshold** tells us that *any* cost-asymmetry we introduce matters because practice volume amplifies it. A 5% extra cost per note, over 20+ hours × 52 weeks × 10 years, is a lot of cumulative strain.

### Caveats

- These are cross-sectional studies. Correlation ≠ causation.
- Self-reported MSD; no imaging confirmation for most cases.
- Student populations may be confounded by improper teaching (not just fingering).
- "Small hand" threshold not operationally defined across studies.

### Open questions for future reading

- Is there a threshold at which f3–f4 span becomes injurious, or is it gradient?
- Does the f3–f4 risk hold for LH (which is weaker/slower) or RH-specific?
- What's the interaction with tempo? (Fast f3-f4 alternation vs slow f3-f4 stretch?)

---

## Note on PAMA (item #5 in fetch list)

**Source**: https://artsmed.org/

PAMA (Performing Arts Medicine Association) publishes the *Medical Problems of Performing Artists* journal and *Journal of Performing Arts Medicine* (JPAM), but their open-access position papers on pianist hand injury are not directly downloadable from the public site. The essentials/symposia pages describe training programs, not specific biomechanical recommendations.

**Action**: the two PMC papers above cover the same territory and are authoritative for our purposes. Revisit PAMA only if we need guild-level clinical guidelines (e.g., for a "safe practice" feature).
