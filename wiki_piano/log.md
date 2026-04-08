# Piano Fingering Wiki Log

## [2026-04-08] init | Wiki split from unified wiki

Separated piano fingering pages into independent wiki. 2 sources, 4 concepts.

## [2026-04-08] ingest | Piano Fingering Articles (9 sources)

Sources: Wikipedia + 8 web clippings (practisingthepiano.com, pianoguidelessons.com, pianomarvel.com, pianoscales.org, bachscholar.com, key-notes.com, informance.biz, yamaha.com).
Pages: `src_piano_fingering_wikipedia`, `src_piano_fingering_articles`, `concept_piano_fingering_principles`, `concept_thumb_technique`, `concept_chord_fingering`, `concept_minimalist_fingering`
Key: Five consensus principles. Cory Hall's minimalist fingering challenges 200-year tradition.

## [2026-04-08] ingest | Graham Fitch & Tim Stein Video Series (6 videos)

Sources: 6 YouTube video transcripts from Pianist Magazine (Graham Fitch 4 parts + Tim Stein 2 parts, 2013-2018).
Pages: `src_graham_fitch_video_series`, `concept_hand_distribution`, `concept_musical_fingering`
Key: Rubinstein's closed-hand solution for Chopin Op.10/1. Hand distribution ethics (when to redistribute vs preserve gesture). Feuchtwanger's musical fingering (finger choice = tone color). Tim Stein's finger group method for scales. Advanced chromatic fingering (1-2-3-4 groups). Busoni tripod fingering.

## [2026-04-08] ingest | Piano Fingering Articles Batch 2 (7 sources)

Sources: Peterson Piano Academy, Penelope Roskell (informance.biz), practisingthepiano.com, liveabout.com, livingpianos.com, Tonara, Digital Piano School (Instagram).
Pages: `src_piano_fingering_articles_batch2`
Updated: `concept_chord_fingering` (added register adaptation, left hand exceptions)
Key: Finger personalities (Roskell). Register adaptation (same chord needs different fingering in bass vs treble). Finger substitution for legato. "Beethoven is handmade" — don't cover bad fingering with pedal. Rapid repeated notes must change fingers.

## [2026-04-08] ingest | Parncutt et al. (1997) — Ergonomic Fingering Model

Source: Academic paper (42p), Music Perception Vol.14 No.4.
Pages: `src_parncutt1997_ergonomic_model`, `concept_finger_span_table`
Key: ⭐ FOUNDATIONAL PAPER for piano fingering algorithms. 12 scoring rules (Stretch, Small/Large-Span, Position-Change, Weak-Finger, Thumb-on-Black, Thumb-Passing, etc.). Table 1 defines MinPrac/MaxPrac/MinRel/MaxRel/MaxComf/MinComf for all 10 finger pairs. Directly maps to V6 DP's FINGER_COMFORT_SPAN, span_cost(), _assignment_cost, and _transition_cost. Model validated against Czerny Op.821 with pianist fingerings. Limitations: right hand only, single notes only, no musical interpretation.

## [2026-04-08] ingest | Piano Biomechanics & Kinematics Papers (5 papers)

Sources: Sloboda et al. 1998 (J Exp Psych), Furuya et al. 2011 (J Neurophysiol), Dalla Bella & Palmer 2011 (PLoS ONE), Ferrario et al. (Med Prob Performing Artists), Neuhaus 2008 (The Art of Piano Playing Ch.IV).
Pages: `src_piano_biomechanics_papers`
Key: Sloboda validates Parncutt model experimentally — experts tolerate position changes over weak fingers. Furuya confirms ring-middle finger coupling (supports RING_FINGER_CHORD_PENALTY). Dalla Bella shows finger height increases at fast tempo (speed-accuracy tradeoff). Ferrario shows expert efficiency = minimal extraneous movement. Neuhaus/Chopin: practice black-key scales first (B major before C major).

## [2026-04-08] ingest | Detection and Tracking of Pianist Hands and Fingers

Source: Gorodnichy & Yogeswaran (NRC-CNRC Canada).
Pages: `src_detect_track_pianist`
Key: Computer vision system to detect which finger plays which key from video + MIDI sync. Potential future data source for learn pipeline.

## [2026-04-08] update | concept_chord_fingering — 新增分解和弦章節

Updated: `concept_chord_fingering` (added broken chord / arpeggio section)
Key: 分解和弦（連續 ≥3 音、音程 ≥3 半音、單方向）應用 C(5,k) 和弦指法而非 relay 公式。BWV 775 m3 RH F4-A4-D5 = 1-3-5。

## [2026-04-08] ingest | Talking Fingers — Pianists' Views on Fingering

Source: Clarke, Parncutt, Raekallio & Sloboda (1997). Musicae Scientiae, Vol.I No.1, 87-107.
Pages: `src_talking_fingers_interview`
Key: ⭐ Qualitative companion to Parncutt 1997 model.

## [2026-04-08] lint | Wiki health check

Result: 0 broken links, 0 orphan pages. Suggested 3 new concept pages for frequently mentioned but uncovered topics.

## [2026-04-08] lint-fix | Added 3 concept pages

Pages: `concept_chopin_method`, `concept_scale_fingering`, `concept_finger_substitution`
Key: Chopin's teaching method (natural hand position, black-key-first, five-finger-five-colors). Scale fingering (finger groups, families, chromatic, double notes). Finger substitution (silent key change for legato extension).
Total pages: 17 → 20.

---
End of log. Next entry: Key: Five themes: (1) standard fingerings as foundation, (2) thumb on black keys — generally avoided but sometimes deliberate for tone, (3) pedal-fingering relationship debated, (4) tempo affects finger choice, (5) interpretation is THE primary determinant. Finger "personalities": thumb=horn, 4=violin, 5=oboe. Procedural knowledge dominates — pianists can't fully articulate rules. V6 implications: model is purely biomechanical but experts prioritize interpretation; speed-dependent fingering not modeled; repeat-passage consistency is debated among experts.
