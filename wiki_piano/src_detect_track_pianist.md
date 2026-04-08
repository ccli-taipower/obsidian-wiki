---
title: "Detection and Tracking of Pianist Hands and Fingers"
date_ingested: 2026-04-08
source_type: academic_paper
authors: "Dmitry O. Gorodnichy, Arjun Yogeswaran"
institution: "NRC-CNRC Canada, University of Ottawa"
tags: [computer_vision, hand_tracking, finger_detection, MIDI, video_recognition, piano_teaching]
---

# Detection and Tracking of Pianist Hands and Fingers

電腦視覺應用：從影片中偵測和追蹤鋼琴家的手與手指。

## 系統架構

1. 攝影機架設在鍵盤上方
2. 同步 MIDI 數據與影片
3. 偵測手部 → 追蹤手指 → 標注「哪根手指彈哪個鍵」
4. 產生標注影片供遠端教學使用

## 應用場景

- **遠端鋼琴教學**：學生不僅能聽到老師彈什麼，還能看到用哪根手指
- **自動指法標注**：從演奏影片中提取指法資訊
- **樂譜製作**：自動產生含指法標注的樂譜
- **合成手指動畫**：生成虛擬鋼琴演奏動畫

## 與本專案的潛在關聯

未來若要從影片中學習鋼琴家的指法偏好（learn 流程的擴展），這類影片辨識技術可作為指法數據來源。

## 相關頁面

- [[concept_piano_fingering_principles]]
