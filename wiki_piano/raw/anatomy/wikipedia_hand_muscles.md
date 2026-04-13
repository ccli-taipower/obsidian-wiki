# Hand Muscles — Wikipedia Extracts

**Fetched**: 2026-04-11
**License**: CC BY-SA 3.0

---

# Lumbricals of the Hand

**Source**: https://en.wikipedia.org/wiki/Lumbricals_of_the_hand

- **Origin**: tendons of the flexor digitorum profundus. Lumbricals 1 & 2 attach to the radial side of single tendons (unipennate); lumbricals 3 & 4 are bipennate (attach to tendons of adjacent fingers)
- **Insertion**: extensor expansions near the MCP joints of digits 2-5
- **Innervation**:
  - **Lumbricals 1 & 2** (index, middle): **median nerve**
  - **Lumbricals 3 & 4** (ring, little): **deep branch of ulnar nerve**
  - Variation: ~60% have this pattern; alternatives are 1:3 or 3:1 ratios
- **Action**: simultaneously flex MCP joints and extend IP joints
- **Etymology**: Latin "lumbricus" = worm

## Piano relevance (Claude annotation)

The **dual nerve supply** (median for f2/f3, ulnar for f4/f5) means that f2/f3 and f4/f5 are driven by **different neural pathways**. This is part of why f3-f4 coupling feels stronger than f2-f3 — they share the ulnar nerve pathway for their intrinsic muscles.

Lumbricals are what produce the "held finger + moving finger" pattern used in scales (MCP flex + IP extend = the "hooked" position). This is a **small-muscle action** and fatigues quickly, which is the whole reason the "weight school" exists (to use arm gravity instead of lumbrical force for key depression).

---

# Extensor Digitorum Muscle

**Source**: https://en.wikipedia.org/wiki/Extensor_digitorum_muscle

- **Origin**: lateral epicondyle of humerus via common extensor tendon
- **Insertion**: middle and distal phalanges of digits 2-5 (four tendons)
- **Innervation**: posterior interosseous nerve (branch of radial nerve)
- **Action**: extends MCP joints; extends wrist; extends elbow (in order of leverage)
- **Key structural feature**: the four tendons are interconnected by **juncturae tendinum** (transverse bands) over the metacarpal heads

## Juncturae Tendinum — why f4 lacks independence

> "The extensor tendons are connected by juncturae tendinum (transverse bands), which serve to maintain the central alignment of the extensor tendons over the metacarpal head. This interconnection mechanism explains why independent finger extension is limited — the tendons are mechanically linked, restricting isolated movement, particularly affecting the ring finger's independence from adjacent digits."

## Piano relevance

This is the **anatomical root** of the V6 DP's `ADJACENT_COUPLING_PENALTY` for f3↔f4 transitions. The ring finger (f4) cannot extend independently from f3 or f5 because they share tendon bands. Any fingering that demands f4 to move while f3/f5 stay still is **fighting the anatomy**.

The IP joint extension is "mediated predominantly by the dorsal and palmar interossei and lumbricals" — so the extensor digitorum itself is mostly an MCP extender. Fine IP control (needed for legato note shaping) comes from the intrinsics, which are small-muscle territory.

**DP implication**: the current `ADJACENT_COUPLING_PENALTY = 0.6` is lower-bound correct — f3↔f4 genuinely costs more. But it should probably also fire on **simultaneous** requirements (f3 held while f4 plays), not just sequential transitions. Current V6 only sees the transition case.
