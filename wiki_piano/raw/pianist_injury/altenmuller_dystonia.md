# Pianist's Focal Dystonia — Altenmüller group

**Source**: https://pmc.ncbi.nlm.nih.gov/articles/PMC3865372/
**License**: CC BY (PMC open access)
**Fetched**: 2026-04-11
**Citation**: Altered sensory feedbacks in pianist's dystonia: the altered auditory feedback paradigm and the glove effect
**Authors include**: Eckart Altenmüller (Hannover University of Music, Drama and Media — the leading researcher on musician's dystonia)

---

## Abstract (verbatim)

> "Background: This study investigates the effect of altered auditory feedback (AAF) in musician's dystonia (MD) and discusses whether AAF can be considered as a sensory trick in MD. Furthermore, the effect of AAF is compared with altered tactile feedback, which can serve as a sensory trick in several other forms of focal dystonia.
>
> Methods: The method is based on scale analysis (Jabusch et al., 2004). Experiment 1 employs synchronization paradigm: 12 MD patients and 25 healthy pianists had to repeatedly play C-major scales in synchrony with a metronome on a MIDI-piano with three auditory feedback conditions: (1) normal feedback; (2) no feedback; (3) constant delayed feedback. Experiment 2 employs synchronization-continuation paradigm: 12 MD patients and 12 healthy pianists had to repeatedly play C-major scales in two phases: first in synchrony with a metronome, secondly continue the established tempo without the metronome. There are four experimental conditions, among them three are the same AAF as in Experiment 1 and 1 is related to altered tactile sensory input. The coefficient of variation of inter-onset intervals of the key depressions was calculated to evaluate fine motor control.
>
> Results: In both experiments, the healthy controls and the patients behaved very similarly. There is no difference in the regularity of playing between the two groups under any condition, and neither did AAF nor did altered tactile feedback have a beneficial effect on patients' fine motor control.
>
> Conclusions: The results of the two experiments suggest that in the context of our experimental designs, AAF and altered tactile feedback play a minor role in motor coordination in patients with musicians' dystonia. We propose that altered auditory and tactile feedback do not serve as effective sensory tricks and may not temporarily reduce the symptoms of patients suffering from MD in this experimental context."

---

## What dystonia is (biomechanical/neurological)

> "The degradation of voluntary control of highly skilled movement patterns involved in piano playing"

Symptomatically:
> "Co-contraction of wrist flexors and extensors and in involuntary curling, or extending of digits, thus rendering fast movements involved for example in scale playing irregular"

Sensory abnormalities (cited from broader literature):
- Reduced two-point discrimination thresholds
- Reduced graphaesthesia
- Impaired thermal detection thresholds
- Altered temporal perception of somatosensory + auditory stimuli

**Neurological model**: impaired internal motor models — the brain's forward prediction of the motor outcome is broken. "The internal model has been shown to be impaired in MD."

---

## Triggering movements (most DP-relevant)

The paper characterises dystonia as **task-specific** — particular patterns trigger symptoms rather than the hand being globally affected. Key observation:

> "Upward scales proved especially problematic due to requiring complex anticipatory coordination maneuver of thumb, remaining four fingers and the wrist"

**This is the most important sentence in the paper for us**: ascending scales require *anticipatory* coordination of the thumb pass-under with the remaining fingers and wrist. It's the thumb-pass mechanism itself that is cognitively and neurally demanding.

---

## Piano Relevance (Claude annotation, 2026-04-11)

### Epidemiological context

From the sister search results: focal dystonia affects **1-2% of highly skilled musicians**. This sounds low until you realise it is the **career-ending injury** in classical music. A cost function that reduces dystonia risk by even 10% is enormously valuable — far more so than shaving 5% off override agreement.

### DP implications

1. **Ascending scales are neurally expensive.** Our DP currently treats ascending and descending runs symmetrically (same span costs, same transition costs). This paper says ascending is harder because of anticipatory thumb coordination. We could introduce a modest **directional asymmetry**: ascending runs with thumb-pass should cost slightly more than descending runs with finger-crossover.

2. **Thumb-pass overuse is a dystonia risk factor.** The current V6 DP has no "thumb-pass count" penalty — if thumb-passes are cheap individually, the DP is happy to use them repeatedly. But the dystonia literature suggests repeated thumb-passes in tight sequences may be cumulatively harmful. This connects to `累積損傷` (cumulative damage) principle already noted in the CTS extract.

3. **"Co-contraction of wrist flexors and extensors"** as a dystonia hallmark means our wrist model (if we add one) should penalise fingerings that force simultaneous flex and extend demands — not just one or the other.

4. **"Involuntary curling or extending of digits"** — dystonia presents as loss of independence between fingers. This validates the juncturae tendinum story (see `anatomy/wikipedia_hand_muscles.md`) and the f3↔f4 coupling penalty, but from a neurological rather than mechanical perspective. The brain cannot reliably differentiate the neighbouring fingers when motor control degrades.

### What this paper does NOT tell us

- No specific fingering patterns are identified as dystonia-causing
- No prevention guidelines
- No dose-response for practice hours
- The experimental result was actually **null** (AAF didn't help MD patients) — the paper is more useful for its *description* of the condition than for intervention

### Follow-up worth reading

Search results mentioned:
- Altenmüller & Détári (2025): *"Preventing Musician's Focal Dystonia: A guide for music educators"* — this is the actionable paper. Not fetched yet; worth chasing.
- Altenmüller (2010) *European Journal of Neurology* review — may have fingering-specific guidance.

Both are behind paywalls on the original search results. Check if DOI-based sci-hub or institutional access is available.
