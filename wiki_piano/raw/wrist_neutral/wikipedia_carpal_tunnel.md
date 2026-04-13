# Carpal Tunnel Syndrome — Wikipedia Extract

**Source**: https://en.wikipedia.org/wiki/Carpal_tunnel_syndrome
**Fetched**: 2026-04-11
**License**: CC BY-SA 3.0

## Wrist Position and Nerve Compression

- **Neutral tunnel pressure**: 2–10 mm Hg
- **Wrist flexion increases pressure 8×**
- **Wrist extension increases pressure 10×**
- Flexion/extension during movement can raise tunnel pressure to **111 mm Hg**
- CTS patients typically show elevated resting pressures of 12–31 mm Hg vs. controls at 2.5–13 mm Hg

## Anatomical Contents

The carpal tunnel is bounded by carpal bones (arch) and the transverse carpal ligament (anterior). It contains:
- **9 flexor tendons** (FDS × 4, FDP × 4, FPL × 1)
- **Median nerve**

## Occupational Risk Factors (odds ratios)

| Exposure | Odds Ratio |
|---|---|
| Vibration | 5.4 |
| Hand force | 4.2 |
| Wrist flexion or extension at work | 2.0 |
| Repetition | 2.0 |

## Clinical Recommendations

- Wrist splints keep the wrist in **neutral position**, particularly at night (when people naturally flex)
- Splints should be used during sleep, not daytime — daytime immobilization causes stiffness and muscle weakness

---

## Piano Relevance (Claude annotation)

**Key takeaways for the fingering DP:**

1. **Flexion at 8× and extension at 10× multipliers are enormous.** A fingering that forces even 20° of sustained wrist extension while playing is loading the median nerve roughly 10× more than a neutral-wrist version of the same passage. This is not a minor variable.

2. **Pressure scales with DISPLACEMENT, not force.** Even light-touch playing (pp passages) can stress the nerve if the wrist posture is bad. So the "rotation cost" shouldn't care about dynamics — position matters regardless.

3. **"Repetition" has odds ratio 2.0.** A fingering that introduces a non-neutral wrist position even briefly but **repeatedly** (e.g., every beat) is higher-risk than a single brief deviation. This validates the "累積損傷" principle: the DP should weight repeated offenders more heavily.

4. **Combining flexion + ulnar deviation** is the classical CTS-inducing posture (not mentioned in the extract but well-known). The DP should penalize configurations that force both simultaneously.

**DP implication**: a `wrist_deviation_cost` term should be additive across the entire phrase, not reset per-note. The total accumulated deviation-minutes matters, not just the peak.
