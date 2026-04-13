# Taubman / Golandsky Approach — Forearm Rotation

**Sources**:
- https://www.ednagolandsky.com/the-taubman-approach-basic-principles/ (public)
- https://www.pointofsound.com/single_v_double/Single_and_double_07.html (public)
- https://www.pointofsound.com/Taubman_essence/seven_pillars.html (public)
- https://www.pianistmagazine.com/blogs/what-is-the-taubman-approach-and-how-can-it-help-you-as-a-pianist/ (public)

**Fetched**: 2026-04-11
**Access note**: Edna Golandsky's *"Why Rotation Matters"* article is paywalled ("Inside Edna's Studio" membership). Below is content from her public Basic Principles page plus the public Point of Sound exposition of single/double rotation.

---

## The Taubman Approach: Basic Principles (Golandsky, public)

Dorothy Taubman's core principles:

- **Alignment and Coordination**: "Correct alignment is fundamental to a well-coordinated and high functioning technique." Fingers, hand, and forearm move together as a **unified mechanism**.
- **Seat Height**: Proper seating is essential for alignment.
- **Rotational and Lateral Forearm Motions**: Enable hand + forearm to operate as a single unit, **preventing isolated finger movements that cause fatigue, tension, and pain**.
- **In and Out Motions**: Movements between black and white key areas prevent **curling and twisting**.
- **Shaping Motions**: "Curvilinear motions by the hand and forearm over groups of notes" accommodate varying finger lengths and directional changes.
- **Tone Production**: Combining **weight and speed** delivered into the keys.
- **Leaps**: Specific strategies for reliable execution.
- **Fingering**: "Comfortable fingering aligns with coordination principles and is absorbed quickly by the hand." ← directly relevant to our DP.
- **Grouping**: Dividing complex passages into clusters.
- **Hand Interdependence**, **Legato** (via shaping + pedaling, not finger-holding), **Octaves and Chords**: opening hand to maximum without stretching.

---

## Single vs Double Rotation (Point of Sound)

The Taubman approach **avoids using finger muscles to lift fingers repeatedly**. Instead, it organizes rotational movements of the forearm to lift the fingers, which:

1. Frees finger muscles for subtler, anatomically appropriate work
2. Protects them from overexertion

### Directional Terms

- **Supination**: "the thumb side of my forearm lifts upward"
- **Pronation**: "the pinky side of my forearm lifts upward"

### Directional Organization

- Thumb sides are **closer to the core** of the body
- Pinky sides **extend farther from the core**
- Symmetry: "coordinations that work as you move up in pitch with the right hand work for moving down in the left"

**Implication for DP**: RH ascending = same biomechanical pattern as LH descending. Our separate RH/LH code paths mirror this anatomical reality, but the cost functions currently treat them as independent. They should be mirrors.

### Single Rotation

(Inferred from the page context — full detail is on the follow-up page not fetched.)
Single rotation = one direction: e.g., a run of notes moving in one pitch direction is lifted by **one continuous rotational impulse** in the appropriate direction (supination for RH ascending, pronation for RH descending).

### Double Rotation

(Inferred — common Taubman teaching.)
Double rotation = **a preparatory counter-rotation before the playing rotation**. Used for repeated notes, trills, alternating patterns — the hand first rotates *away from* the note, then *toward* it, giving a pendulum-like lift mechanism.

---

## Seven Pillars of Taubman Technique

1. **Passive Energy Sources**: Harness gravity and momentum rather than muscular effort. "Free" physical resources enable speed, timing precision, and pain-free playing.
2. **Unified Forearm-Hand Unit**: When wrist is correct, forearm + hand operate as one unit (~1-2 lbs combined weight) delivering force via gravity/momentum.
3. **Optimal Body Architecture**: Proper alignment prevents "broken fulcrums" (joints where weight transmission fails). Bones transmit force with minimal muscle.
4. **Sensory Continuum**: Proportional awareness between momentum/gravity input and resulting tone.
5. **Rebound Mechanics**: Force returned from the keybed propels the hand unit toward the next note. Walking hand/arm, rotation, and shifting maximize rebound.
6. **Muscular Elasticity and Recoil**: Forearm rotation and finger lifting occur largely through **passive muscular recoil**, not active exertion. Fingers provide feedback + minimal color.
7. **Potentiation**: All six pillars amplify each other.

---

## Pianist Magazine (public) — Biomechanical Details

- Playing apparatus (fingers, hand, forearm) "must move together at all times, in the same direction and at the same speed"
- Fingers maintain "a gently curved position"
- "The forearm is always directly behind the playing finger, to support it" ← **critical**

### Three Fulcrums

1. **Knuckles**: Top knuckles should be "slightly higher than the middle knuckles" for free finger motion without extreme ranges.
2. **Wrist**: "at the level where the hand and forearm are connected" — unified support, **prevents wrist pain and carpal tunnel**. Matches the CTS extract in `wrist_neutral/wikipedia_carpal_tunnel.md`.
3. **Elbow**: Forearm fulcrum; "when the playing apparatus moves to the right or left, the elbow follows proportionally."

### Positioning

- Seat height: forearm + elbow at white-key level
- Straight torso follows playing apparatus up/down the keyboard

---

## Piano Relevance (Claude annotation, 2026-04-11)

### The core Taubman thesis vs. our DP

Taubman/Golandsky say: **fingers should not lift themselves**. The rotation of the forearm does the lifting. Our V6 DP currently ignores rotation entirely — every finger is treated as an independent actuator paying a "span cost" for stretching.

This is not a minor oversight. If the Taubman thesis is correct (and it has decades of clinical evidence behind it in the RSI literature), then our `FINGER_COMFORT_SPAN` table is measuring the **wrong thing** — it measures static stretch cost, not rotational feasibility cost.

A fingering that demands a 7-semitone stretch between f1 and f5 is:
- **Expensive** under our current span-cost model
- **Cheap** under a Taubman model if the motion is *played as a single supinating rotation* (the hand rotates so the two notes land naturally under the finger tips, no stretch needed)

### Concrete DP implications

1. **Single-hand runs should have rotation-consistent cost**: A scale run ascending in RH should reward fingerings whose implied thumb-position arc is smooth in the supination direction. Abrupt direction changes in the hand's rotational state should be penalized. Our current `_transition_cost` only looks at finger-to-finger pitch deltas, not at whether consecutive notes ask for consistent forearm rotation.

2. **Double rotation for repeated notes is expensive**: Taubman uses it specifically *because* single rotation cannot get back to the same starting position. Our same-note substitution (`sub_from`) annotation currently treats finger changes on repeated pitches as free — it isn't. Every substitution costs a counter-rotation.

3. **f4 independence issue reframed**: The extensor digitorum note (`anatomy/wikipedia_hand_muscles.md`) said f4 can't lift independently due to juncturae tendinum. Taubman's answer is: *don't lift f4 with its own extensor — use forearm rotation instead*. So the `ADJACENT_COUPLING_PENALTY = 0.6` is technically correct under the "isolated lifting" model but becomes **negotiable** if rotation is properly accounted for.

4. **"Weight and speed"**: Tone is `weight × speed`, not `force`. Our DP has no concept of dynamics or speed. This is fine for fingering selection per se, but it means we cannot distinguish "fast passage fingering" from "slow expressive fingering" — they have different optimal solutions in the Taubman framework.

5. **Fulcrum failure as a constraint**: The "broken fulcrum" concept says certain positions make the wrist/elbow lose its ability to transmit force. This is a **hard constraint**, not a soft penalty. Positions that break the wrist fulcrum should be rejected outright, not just cost more.

### What we're still missing from Taubman

The paywalled article and the follow-up single/double rotation page would give us:
- Exact rules for when to use single vs double rotation
- How rotation interacts with specific finger sequences (e.g., 1-3-1-3 vs 1-2-1-2)
- The "walking hand/arm" mechanism for shifts

Without these, a rotation-aware DP cost term would be guesswork. **Recommendation**: prioritize getting the Taubman Techniques DVD transcripts or Golandsky's tonebase workbook (referenced in search results) before implementing rotation-cost logic.

### Risk assessment

Taubman is **one school** of piano biomechanics. It is NOT universally accepted — some traditions (e.g., Russian "weight school" via Neuhaus) emphasize arm weight differently, and some modern biomechanics researchers dispute specific Taubman claims. Before we rewrite the DP around rotation, we should read at least one counter-source (Neuhaus or Sándor's *On Piano Playing*) to avoid single-school bias.
