	# Piano Fingering Wiki

> Last updated: 2026-05-29 | Sources: 21 | Concepts: 23 | Analyses: 7 | Total: 53 active pages | Raw: 9 files
> 並列 wiki：[[../wiki_phrase/index]] (樂句分段) + [[../wiki_articulation/index]] (連結 / 斷奏 / 觸鍵詮釋)

## Sources — Computational Models

- [Parncutt et al. (1997) — Ergonomic Model](src_parncutt1997_ergonomic_model.md) — ⭐ 指法計算奠基論文：12 條規則、跨度表、與 V6 DP 對應
- [Computational Fingering Models (3 篇)](src_computational_fingering.md) — ⭐ Nakamura HMM + PIG Dataset；Moryosef 影片指法提取（F1=97%）；⭐ Ramoneda 2022 ArGNN + ThumbSet（新 SOTA，超越 HMM +8%）
- [鋼琴指法演算法第二批（4 篇）](src_fingering_algorithms_batch2.md) — Telles 指法作為分析工具、兩篇 KTH 學位論文、⭐ Liao 2025 Transformer 多模態（96%準確率）
- [強化學習與元啟發式指法演算法（3 篇）](src_fingering_rl_metaheuristic.md) — Ramoneda DQN、⭐ Gao MBRL（Invalid Action Masking）、⭐ Balliauw VNS（多聲部、個人化距離矩陣）

## Sources — Anatomy & Injury (New)

- [⭐ 生物力學與解剖新批：手部肌腱、前臂旋轉、臨床傷害研究（5 份）](src_biomechanics_anatomy.md) — 指伸肌腱聯合（f3-f4 耦合解剖根源）、蚓狀肌雙神經支配、Taubman 旋轉教學法、PMC 臨床 f3-f4 RH 傷害預測、Altenmüller 焦點失張力症

## Sources — Biomechanics & Motor Control

- [Biomechanics & Kinematics (5 篇)](src_piano_biomechanics_papers.md) — Sloboda 視譜驗證、Furuya 手指協同、Dalla Bella 速度效應、Ferrario 3D 分析、Neuhaus 技巧哲學
- [Motor Control & Tactile (8 篇)](src_piano_motor_control.md) — 手指力量、觸覺回饋、敲擊能力、運動遷移、音樂手勢
- [Talking Fingers — 鋼琴家指法訪談](src_talking_fingers_interview.md) — ⭐ Clarke/Parncutt 1997，7 位專家的指法哲學
- [人體工學、小手策略與傷害預防（6 篇）](src_piano_ergonomics_small_hands.md) — 手部解剖、小手障礙、ESPK 鍵盤、53 篇生物力學系統回顧、運動介入、Suchitphanit 個體差異
- [鋼琴家手部跨度測量與人體工學鍵盤（3 篇）](src_hand_span_keyboards.md) — ⭐ Boyle 2015（473 人跨度數據）、Ortmann 生物力學、Yoshimura DS6.0 臨床疼痛降低
- [技巧、表現力與傷害預防（4 篇）](src_technique_expressiveness_injury.md) — 技巧歷史演變、延伸技巧教學、Wristen 7 個生物力學清單、Hanon 技法應用

## Sources — Voice Separation

- [聲部分離演算法（2 篇）](src_voice_separation.md) — McLeod HMM（Huron 感知原則）、⭐ Karystinaios GNN Link Prediction（SOTA，F1=0.97）

## Sources — Technology & Datasets

- [手部偵測與追蹤技術（2 篇）](src_detect_track_pianist.md) — 鋼琴家手指追蹤、⭐ MediaPipe Hands（21 關鍵點、即時、開源）
- [ASAP 數據集](src_asap_dataset.md) — ⭐ 222 樂譜 × 1068 演奏、MusicXML+MIDI+音訊、拍級對齊

## Sources — Teaching Articles & Videos

- [Fingering (music) — Wikipedia](src_piano_fingering_wikipedia.md) — 指法百科概述、歷史演變
- [鋼琴指法教學文章合集（8 篇）](src_piano_fingering_articles.md) — 基礎原則、和弦指法、極簡主義指法、7 條規則
- [Graham Fitch & Tim Stein 影片系列（6 部）](src_graham_fitch_video_series.md) — 音階琶音指群法、Rubinstein 方案、手部重分配
- [鋼琴指法教學第二批（7 篇）](src_piano_fingering_articles_batch2.md) — 手指個性、音域適應指法、換指進階
- [鍵盤指法歷史與詮釋（4 篇）](src_historical_fingering_interpretation.md) — ⭐ 16 世紀至今的指法哲學演變、Beethoven/Chopin/Schenker 的詮釋性指法、Mozart 指法選擇
- [中國風鋼琴音樂（2 篇）](src_chinese_style_piano.md) — 五聲音階指法、模仿傳統樂器、散板節奏

## Sources — Music Analysis & Interpretation

- [音樂家的無聊人生 Musecow（4 部影片）](src_musecow_music_analysis.md) — 蕭邦三大好聽原因、Op.9-1 和聲心理學、幻想波蘭舞曲 Op.61、德布西《月光》踏板技法

## Concepts (New)

- [⭐ Forearm Rotation 前臂旋轉](concept_forearm_rotation.md) — Taubman 七大支柱、單/雙旋轉、旋後肌解剖、旋前圓肌症候群、DP 對應（旋轉成本尚未實作）
- [⭐ Hand Anatomy 手部解剖](concept_hand_anatomy.md) — 蚓狀肌雙神經支配、指伸肌腱聯合（juncturae tendinum）、f3-f4 RH 不對稱臨床實證、f3-f4 靜態同時耦合建議

## Concepts

- [Finger Span Table](concept_finger_span_table.md) — ⭐ Parncutt 跨度表與 V6 FINGER_COMFORT_SPAN 對應
- [Piano Fingering Principles](concept_piano_fingering_principles.md) — 五大共識原則、傳統 vs 極簡、歷史演變
- [Scale Fingering](concept_scale_fingering.md) — 指群法、指法家族、半音階、雙音音階
- [Chord Fingering](concept_chord_fingering.md) — 三和弦各轉位標準指法、音域適應、左手例外規則
- [Thumb Technique](concept_thumb_technique.md) — 拇指穿越 (thumb under)、Bach 的拇指革新
- [Finger Substitution](concept_finger_substitution.md) — 換指技巧：連奏延長、管風琴式替換
- [Chopin Method](concept_chopin_method.md) — Chopin 教學法：自然手位、黑鍵優先、五指五色
- [Minimalist Fingering](concept_minimalist_fingering.md) — Cory Hall 2024，用最少手指+最多拇指穿越
- [Hand Distribution](concept_hand_distribution.md) — 手部重分配：何時該用、何時不該用
- [Musical Fingering](concept_musical_fingering.md) — 指法選擇如何影響音色與分句
- [Chromatic Harmony](concept_chromatic_harmony.md) — 半音化和聲：多聲部半音移動、蕭邦內聲部、三度關係
- [Pedal Technique](concept_pedal_technique.md) — 踏板技法：半踏板、延遲換踏板、粗弦/細弦差異
- [Small Hands](concept_small_hands.md) — 小手鋼琴家：定義、障礙、ESPK 鍵盤、傷害統計、應對策略
- [Arpeggio Fingering](concept_arpeggio_fingering.md) — 分解和弦標準指法（三和弦 1-2-3-5、七和弦 1-2-3-4）+ thumb-pass 訓練
- [Octave Fingering](concept_octave_fingering.md) — 八度指法（1-5 標準 + 1-4 legato 替代 + 黑鍵特殊處理）+ wrist motion 主導
- [Double Thirds / Sixths](concept_double_thirds_sixths.md) — 雙音指法（Chopin Op.25 No.6 經典）+ 連續 double notes legato 物理限制
- [Trill Fingering](concept_trill_fingering.md) — 顫音標準指法（2-3 通用、3-4 進階、4-5 高難）+ finger independence 要求
- [Repeated Note Fingering](concept_repeated_note_fingering.md) — 同音重複（Liszt *La Campanella* 4-3-2-1 經典）+ 換指 vs substitution 物理區分
- [Chord Voicing Fingering](concept_chord_voicing_fingering.md) — 和弦聲部突顯（top-voice / bass-voice / inner-voice）+ 強指偏好
- [Wrist Motion](concept_wrist_motion.md) — 手腕運動四自由度 + 八度技術核心 + 與 forearm rotation 區分
- [Finger Independence](concept_finger_independence.md) — 手指獨立性（4 最弱、5 中弱）+ 解剖限制 + 訓練 vs 解剖區分
- [Weak Finger Development](concept_weak_finger_development.md) — 弱指 4-5 訓練（Hanon/Czerny 派傳統）+ Schumann 失敗教訓 + 現代最佳實踐
- [Hand Position Stability](concept_hand_position_stability.md) — 手位穩定性 + 與 thumb-pass / substitution / phrase boundary 互動

## Analyses

- [指法如何表現或強化力度？](analysis_fingering_and_dynamics.md) — 六個層面：手指力量差異、強/弱指選擇、觸鍵方式、手位策略、速度交互、V6 限制
- [拍子強弱能否加入指法考量？](analysis_metric_accent_and_fingering.md) — 結論：不建議，例外太多（切分、rubato、對位）；力度標記優先於節拍位置
- [不同樂派/作曲家/時期的指法差異](analysis_period_style_fingering.md) — 歷史演變（Bach→Chopin→Liszt→現代）、作曲家指法即詮釋、樂派風格隱性影響、踏板差異
- [小手學習者的技巧與曲目建議](analysis_small_hands_advice.md) — 7 種應對策略、Meinke 4 法則、各時期曲目推薦、音域適應指法
- [常見錯誤指法與生理傷害](analysis_common_fingering_injuries.md) — 7 類錯誤依傷害嚴重度排列：腕隧道→肌腱炎→尺偏→孤立指力→拇指過伸→小指塌陷→聳肩
- [Chopin Etudes Op.10/Op.25 技術 fingering 俯瞰](analysis_chopin_etudes_overview.md) — 24 首 etude 各自技術焦點 + 對後續文獻影響 + edition 差異
- [Hanon & Czerny 練習傳統評估](analysis_hanon_czerny_exercises.md) — 19 世紀練習教材 + 20 世紀後批評 + 現代教學替代方案
