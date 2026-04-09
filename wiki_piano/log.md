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

## [2026-04-08] ingest | Computational Fingering Models + Motor Control Papers (10 papers)

Sources: Nakamura 2019 (HMM fingering), Moryosef 2023 (video extraction), Parlitz 1999 (finger forces), Goebl & Palmer 2019 (touch & tempo), Aoki/Furuya/Kinoshita 2005 (finger-tapping), Goebl 2017 (movement & touch handbook), Goebl & Palmer 2008 (tactile feedback), Hsiao 2015 (tactile teacher), Dinov 2023 (role of fingering), Furuya 2013 (transfer of practice).
Pages: `src_computational_fingering`, `src_piano_motor_control`
Key: Nakamura HMM is current state-of-the-art for fingering estimation; PIG Dataset (150 pieces, 100K notes) available for V6 validation. Moryosef extracts fingering from video (F1=97%). Ring/pinky fingers confirmed slower by tapping study. Tactile feedback critical for timing accuracy. Practice transfer works within-hand but not across-hand. Fingering is part of musical gesture creation (Dinov). Five themes: (1) standard fingerings as foundation, (2) thumb on black keys — generally avoided but sometimes deliberate for tone, (3) pedal-fingering relationship debated, (4) tempo affects finger choice, (5) interpretation is THE primary determinant. Finger "personalities": thumb=horn, 4=violin, 5=oboe. Procedural knowledge dominates — pianists can't fully articulate rules. V6 implications: model is purely biomechanical but experts prioritize interpretation; speed-dependent fingering not modeled; repeat-passage consistency is debated among experts.

## [2026-04-09] ingest | 音樂家的無聊人生 Musecow — 音樂分析系列（4 部影片）

Sources: 4 YouTube transcripts from Musecow channel (許崴/海牛): (1) 蕭邦為什麼這麼好聽 (2021-05), (2) 蕭邦第一首夜曲 Op.9-1 和聲分析 (2021-06), (3) 幻想波蘭舞曲 Op.61 (2025-12), (4) 德布西《月光》演奏詮釋 (2025-12).
Pages: `src_musecow_music_analysis`, `concept_chromatic_harmony`, `concept_pedal_technique`
Key: 蕭邦三大好聽原因（義大利裝飾旋律、巴赫式多聲部對位、半音化和聲）。內聲部是蕭邦的秘密武器——Op.25-1 分解和弦中暗藏半音階連接線。Op.9-1 用反覆建立心理期待再以簡單和弦轉換製造情緒轉折。幻想波蘭舞曲融合四種曲式，核心動機貫穿全曲如萬花筒。德布西《月光》踏板技法：半踏板利用粗弦/細弦差異保留低音同時換高音和聲；延遲換踏板讓兩和聲短暫重疊漸變（曖昧音色最美）。V6 DP 啟示：內聲部連貫性、踏板對指法的放寬效果、裝飾音指法均為未建模維度。

## [2026-04-09] lint | Wiki health check

Result: 0 broken links, 0 orphan pages. 2 low-connectivity pages (`concept_hand_distribution`, `src_piano_motor_control`) — added inbound links from `concept_musical_fingering`. Previous orphans (`concept_scale_fingering`, `src_computational_fingering`) fixed earlier this session. Escaped pipe in table (concept_piano_fingering_principles line 24) is valid Markdown table escaping — no fix needed. Total pages: 25.

## [2026-04-09] query | 指法如何表現或強化力度？

Filed as `analysis_fingering_and_dynamics`. Synthesized from 7 wiki pages. Six dimensions: (1) finger strength hierarchy (thumb strongest, ring weakest — Aoki 2005), (2) deliberate strong/weak finger selection (Roskell finger personalities, Chopin five-finger-five-colors), (3) touch mechanism constrained by finger choice (Goebl pressing vs striking), (4) hand position strategy — experts move more to keep strong fingers (Sloboda 1998), (5) speed-dynamics interaction — fast+forte forces strong-finger fingering (Dalla Bella 2011), (6) V6 DP limitations — no dynamics markup awareness, possible improvement via MusicXML `<dynamics>` tags. Total pages: 26.

## [2026-04-09] query | 拍子強弱能否加入指法考量？

Filed as `analysis_metric_accent_and_fingering`. Conclusion: not recommended. Evidence supports the concept (Peterson Tip #4 phrasing, Talking Fingers finger personalities, Sloboda strong-finger preference), but too many exceptions in real music (syncopation, rubato, counterpoint). V6 already handles phrase-start stability via W_PHRASE_ANCHOR. If implemented, must be very small penalty (0.2-0.3) on weak fingers at strong beats, single-note only. Priority suggestion: MusicXML `<dynamics>` tags (explicit composer intent) are more valuable than metric position (default pattern). Total pages: 27.

## [2026-04-09] query | 不同樂派/作曲家/時期的指法差異

Filed as `analysis_period_style_fingering`. Three dimensions: (1) historical evolution — pre-Bach no thumb → Bach thumb revolution → Chopin natural hand position → Liszt technical neutrality → 2024 minimalism; (2) composer fingering as interpretation — Beethoven structural, Chopin tonal, Busoni timbral, contemporary creative; (3) style influences — Baroque strictest legato (no pedal), Classical phrase-aware, Romantic pedal-relaxed + chromatic black keys, Impressionist half-pedal precision. Pedal availability is a key driver of fingering differences across periods. V6 DP is style-neutral; suggested improvements: style profiles from MusicXML metadata, composer fingering as soft constraint, pedal-aware legato relaxation. Total pages: 28.

## [2026-04-09] ingest | Piano fingering algorithms batch 2 + ergonomics/small hands (8 papers)

Sources: Telles 2020 (fingering as analytical tool, contemporary music), Nellåker & Lu KTH (13-rule tree search), Andersson & Håkansson KTH (DP + trellis), Tworko 2020 (hand anatomy/physiology), Chi et al. 2020 (ergonomics systematic review, hand size), Jurinič et al. 2026 (53-study biomechanics review), Chong 2021 (small hands DM dissertation), Farzana & Mathew 2021 (exercise intervention). Note: Parncutt 1997 duplicate detected and deleted from raw/ (kept as "An ergonomic model of keyboard fingering for melodic fragments.pdf").
Pages: `src_fingering_algorithms_batch2`, `src_piano_ergonomics_small_hands`, `concept_small_hands`
Key: Telles argues fingering is analytical tool for contemporary music — unconventional fingering (thumb on black, one-finger martellato, fist) can reveal musical structure. "Three-fingered" (Czerny) vs "five-fingered" (Liszt/Busoni) historical split. KTH theses validate Parncutt-based algorithms with pause handling and DP/trellis approaches. Small hands: self-defined condition, standard keyboard discriminates (6.5" octave since 1860s), ESPK keyboards exist but unknown, 10/13 studies show smaller hand → higher injury risk, 40-60% PRMD prevalence. Jurinič 2026 is most comprehensive biomechanics review (53 studies): experts use proximal-to-distal coordination, touch type affects muscle activation, thumb-under involves anticipatory modifications. V6 implications: fixed FINGER_COMFORT_SPAN could benefit from hand-size parameter; contemporary music may need non-ergonomic fingering model. Total pages: 31.

## [2026-04-09] ingest | Historical fingering & interpretation (4 papers)

Sources: Fytika 2004 (500-year historical overview, FSU DM), Swinkin 2007 (historical vs modern fingering philosophy, Performance Practice Review), Chai 2016 (Mozart fingering selection, U Kansas DMA), Pozzo 2021 (pedal-finger coordination, conference abstract).
Pages: `src_historical_fingering_interpretation`
Key: ⭐ Fytika provides the most comprehensive fingering history (1520-present) in 4 periods: Renaissance/Baroque (articulation-based, no thumb), Classical (C.P.E. Bach thumb revolution, legato default), Romantic (finger gymnastics → tone production), 20th century (scientific/anatomical basis, unconventional fingering). Swinkin argues historical fingerings serve interpretation (grouping, articulation, dynamics, voicing) while modern fingerings prioritize comfort — fundamental philosophical split. Beethoven's fingerings create hemiola, forced accents, Bebung illusion, inner voice emphasis. Chopin's 6 preferred techniques include thumb on black keys, silent substitution, sliding, 3-4-5 crossing. Chai demonstrates 18th-century performance practice (speech-like articulation, fortepiano characteristics) informs Mozart fingering. Pozzo shows pedal-finger coordination differs between experts (anticipatory) and students. Total pages: 32.

## [2026-04-09] ingest | Technique, expressiveness & injury prevention (3 papers)

Sources: Jia 2023 (technique & expressiveness overview), Proulx 2009 (extended piano techniques DMA, Temple U), Wristen 2000 (biomechanical analysis procedure for injury prevention, Medical Problems of Performing Artists).
Pages: `src_technique_expressiveness_injury`
Key: Jia traces technique evolution from Baroque to contemporary (7 aspects of expressiveness). Proulx covers extended techniques (string pizzicato, glissando, bowed piano, clusters, prepared piano) — pioneers Cowell and Crumb. Wristen provides ⭐ 7 detailed biomechanical checklists (scales, arpeggios, trills, double-thirds, octave scales, broken chords, broken octaves) describing correct motion from spine to fingertips; Meinke's 4 ergonomic laws (momentum, smooth curves, best-suited muscles, neutral wrist); injury prevention recommendations (never practice through pain, ≤30min segments, warm-up/cool-down). V6 implications: span_cost aligns with Meinke law 4; thumb-under transition rules align with Wristen's scale checklist; small hands need more lateral wrist adjustment (supports HAND_SIZE_SCALE concept). Total pages: 33.

## [2026-04-09] ingest | Hanon technique for Chopin Ballade (1 paper, added to existing page)

Source: Su & Hirunrak 2024 (Journal of Modern Learning Development). Added to `src_technique_expressiveness_injury` (now 4 papers).
Key: Hanon's 60 exercises in 3 parts (preparatory/transcendent/virtuoso); adopted by Paris, Brussels, Moscow conservatories; Rachmaninoff confirms Moscow used Hanon for first 5 years; China inherited via Soviet system. Pros: systematic, low barrier, dual-hand training. Cons: mechanical habit, no musicality/sight-reading/harmony training. Application to Chopin Ballade No.1 Op.23: finger independence for rapid passages, but cannot substitute musical understanding. Total pages: 33.

## [2026-04-09] lint | Wiki health check

Result: 0 broken links, 0 orphan pages (fixed 3: src_historical_fingering_interpretation, src_technique_expressiveness_injury, analysis_metric_accent_and_fingering — added inbound links from concept_piano_fingering_principles, concept_chopin_method, analysis_fingering_and_dynamics, src_piano_ergonomics_small_hands). Total pages: 33.

## [2026-04-09] query | 小手學習者的技巧與曲目建議

Filed as `analysis_small_hands_advice`. Synthesized from 6 wiki pages. Seven coping strategies: alternative fingering (Roskell register adaptation), hand redistribution, rolling chords, note omission, pedal assistance, audiation (Fink), warm-up exercises (Farzana 4-week protocol). Core principle: maintain neutral wrist position (Meinke's 4 laws, Wristen's checklists). Repertoire: Baroque (Bach) and Impressionist (Debussy) most suitable; Romantic late period (Liszt, Rachmaninoff) most challenging. Specific pieces listed. ESPK keyboards as permanent solution. V6 DP: HAND_SIZE_SCALE parameter (×0.9) suggested. Total pages: 34.

## [2026-04-09] ingest | 4 new papers (multimodal fingering, small hands, Chinese style)

Sources: Liao & Fan 2025 (IEEE Access, Transformer multimodal fingering 96% accuracy), Suchitphanit 2017 (small hands DMA, U Kansas), 2 Chinese-style piano music papers.
Pages updated: `src_fingering_algorithms_batch2` (3→4), `src_piano_ergonomics_small_hands` (5→6). New: `src_chinese_style_piano`.
Key: ⭐ Liao & Fan achieve 96% finger accuracy with Transformer + PAE + DCA on MAESTRO + RoboPianist data — current SOTA for multimodal fingering analysis. Suchitphanit adds disability studies perspective to small hands (growth vs fixed mindset), Ortmann's 6 natural hand positions (50K people), quantitative small-hand definition (≤8" span, need 7.5" for octave), famous small-handed pianists (Pires, de Larrocha, Hoffmann). Chinese-style papers cover pentatonic scale fingering and traditional instrument imitation techniques. Total pages: 35.
