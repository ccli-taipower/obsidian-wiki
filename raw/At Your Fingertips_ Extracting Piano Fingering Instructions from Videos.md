---
title: "At Your Fingertips: Extracting Piano Fingering Instructions from Videos"
source: "https://ar5iv.labs.arxiv.org/html/2303.03745"
author:
published:
created: 2026-04-09
description: "Piano fingering—knowing which finger to use to play each note in a musical piece, is a hard and important skill to master when learning to play the piano. While some sheet music is available with expert-annotated finge…"
tags:
  - "clippings"
---
Amit Moryossef    Yanai Elazar    and Yoav Goldberg

###### Abstract

Piano fingering—knowing which finger to use to play each note in a musical piece, is a hard and important skill to master when learning to play the piano. While some sheet music is available with expert-annotated fingering information, most pieces lack this information, and people often resort to learning the fingering from demonstrations in online videos. We consider the AI task of automating the extraction of fingering information from videos. This is a non-trivial task as fingers are often occluded by other fingers, and it is often not clear from the video which of the keys were pressed, requiring the synchronization of hand position information and knowledge about the notes that were played. We show how to perform this task with high-accuracy using a combination of deep-learning modules, including a GAN-based approach for fine-tuning on out-of-domain data. We extract the fingering information with an f1 score of 97%. We run the resulting system on 90 videos, resulting in high-quality piano fingering information of 150K notes, the largest available dataset of piano-fingering to date.

Music Performance Analysis, Music Performance Datasets, Piano Fingering Analysis, Sound and Music Computing.

## 1 Introduction

Learning to play the piano is a difficult task which takes years to master. One of the challenging aspects when learning a new piece is the fingering choice, in which the player has to choose what finger to use for each note. While beginner booklets contain many fingering suggestions, advanced pieces seldom do.

Automatic prediction of piano-fingering can be a useful tool for piano learners, to ease the learning process of new pieces. As manually labeling fingerings for different sheet music is an exhausting and expensive task [^1], previous work [^2] [^3] [^4] [^5] [^1] used very few tagged pieces for evaluation, with minimal or no training data.

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2303.03745/assets/figs/cover/finger_detection_clean.png)

(a) A recreation of the piano, hand pose estimation and predicted fingering, which are colored in corresponding colors to the fingers.

In this paper, we propose an automatic, low-cost method for detecting piano-fingering from piano playing performances captured on video, which allows training of modern, data-hungry neural networks. We introduce a novel pipeline that adapts and combines several deep learning methods such as Object-Detection [^6] [^7] [^8] [^9], Pose-Estimation [^10] [^11] [^12], and GANs [^13] [^14], and results in an automatically labeled piano-fingering dataset. Our method serves two purposes: (1) an automatic “transcript” method that detects piano-fingering from video and MIDI files, when these are available, (Section §4.1), and (2) running the method on dozens of videos, it yields a large dataset for training models genralizing to new pieces (Section §4.2).

Given a video and a MIDI file, our system produces a probability distribution over the fingers for each played note. Running this process on large corpora of piano performances played by different artists yields a total of 90 automatically finger-tagged pieces (containing 155,107 notes in total) resulting in the first public large scale piano-fingering dataset, which we name “Automatic Piano Fingering Dataset (APFD)”. This dataset can grow over time, as more videos are uploaded to YouTube. We provide empirical evidence that APFD is valuable, by manually inspecting its labels quality and its usefulness for predictions by fine-tuning a model on a manually created dataset, which achieves state-of-the-art results on a piano-fingering task (§4.2).

The process of extracting piano-fingering from videos alone is difficult as it needs to detect keyboard presses, which are often subtle for the naked eye. We therefore turn to MIDI files which were simultaneously recorded with videos to obtain this information. The extraction process works as follows: We begin by creating a virtual keyboard, and map each key to match their location on the video (§3.2). Then, we identify the hands (§3.3), and the fingers given the hands’ bounding boxes (§3.4) for each frame of the video. Next, we align between the MIDI file and its corresponding video (§3.6) and finally, for every played note, we assign a distribution over the fingers that played it (§3.5).

Even though methods for hand detection and pose estimation were extensively studied in the computer-vision literature [^15] [^16] [^10] [^11] [^12], we find that in practice, state-of-the-art models do not generalize, and perform poorly in our scenario. We address these weaknesses by fine-tuning an object detection model (§3.3) on a new dataset that we manually annotated, and introduce a novel algorithm for adapting models on out-of-domain data.

We release this new hands dataset and the trained model in [^17], alongside the rest of the resources developed in this work, and a demonstration of the output from the entire process in [https://youtu.be/Gfs1UWQhr5Q](https://youtu.be/Gfs1UWQhr5Q).

## 2 Background

In this section, we present a literature review on the piano-fingering task, which was studied for many years. A shortcoming of most of these works is the lack of actual data for the different methods evaluation, which we aim to remedy by using our automatic method on videos.

piano-fingering was previously studied in multiple disciplines, such as music theory and computer animation [^2] [^3] [^4] [^5] [^18] [^1]. Early works have mainly focused on search-based algorithms, with limited amounts of data and many unrealistic constraints. A recent work [^1] is the first work to produce a reasonable-sized corpus of piano fingering, with rigorous labeling by multiple professional players. Although the size of this dataset is enough for training modern statistical models, it is still considered relatively small, and more data can significantly boost performance.

The fingering prediction task is formalized as follows: Given a sequence of notes, associate each note with a finger from the set $\{1,2,3,4,5\}\times\{L,R\}$. This is subject to constraints such as the positions of each hand, anatomical plausibility of transitioning between two fingers, the hands’ size, etc. Each fingering sequence has a cost of “effort” which is desired to be minimized.

One naive approach to finding the best optimal fingering sequence to play all the notes with is to exhaustively evaluate all possible transitions between one note to another which is not computationally feasible. By defining a transition matrix corresponding to the probability or “effort” of transitioning from one note to another - one can calculate a cost function, which specifies the predicted sequence likelihood. Using a search algorithm on top of the transitions allows to find a globally optimal solution. But this solution is not practical, due to the exponential complexity, therefore heuristics and pruning are employed to reduce the space complexity. The transition matrix can be manually defined by heuristics or personal estimation [^2] [^3], or instead of relying on a pre-defined set of rules, a Hidden Markov Model (HMM) can be used to learn the transitions [^19] [^20]. In practice, [^19] leave the parameter learning to future work, and instead they manually fine-tune the transition matrix.

On top of the transition matrix, practitioners suggested using dynamic programming algorithms to solve the search [^3]. Another option to solve the huge search space is to use a search algorithm such as Tabu search [^21] or variable neighborhood search [^22], to find a global plausible solution [^23] [^24]. These works are either limited by the defined transition rules, or by making different assumptions to facilitate the search space. Such assumptions come in the form of limiting the predictions to a single hand, limiting the evaluation pieces to contain no chords, rests or substantial lengths during which player can take their hand off the keyboard. Furthermore, all of these works have small evaluation sets, which in practice makes it hard to compare different approaches, and does not allow to use more advanced models such as neural networks.

Previous works also constrained their models with manually defined rules that try to imitate human behaviour as these methods require lots of training data to achieve good performance, and fingering labeling is particularly expensive and hard to obtain. One way to automatically gather rich fingering data with full hand pose estimation is by using motion capture (MOCAP) gloves when playing the piano. [^18] suggest a rule-based and data-based hybrid method, initially estimating fingering decisions using a Directed Acyclic Graph (DAG) based on rule-based comfort constraints which are smoothed using data recorded from limited playing sessions with motion capture gloves. As MOCAP requires special equipment and may affect the comfort of the player, other work, [^25] tried to automatically detect piano fingering from video and MIDI files. The pianist’s fingernails were laid with colorful markers, which were detected by a computer vision program. As some occlusions can occur, they used some rules to correct the detected fingering. In practice, they implemented the system with a camera capturing only 2 octaves (out of 8) and performed a very limited evaluation. The rules they used are simple (such as: restricting one finger per played note, two successive notes cannot be played with the same finger), but far from capturing real-world scenarios.

Previous methods for automatically collecting data [^25] [^18] were costly, as apart of the equipment needed to play a piece, the data-collectors had to pay the participating pianists. In our work, we rely solely on videos from YouTube, meaning costs remain minimal with the ability to easily scale up to new videos.

Recently, [^1] released a relatively large dataset of manually labeled piano-fingering by one to six annotators, consisting of 150 pieces, with partially annotated scores (324 notes per piece on average) with a total of 48,726 notes matched with 100,044 tags from multiple annotators, named PIG. This is the largest annotated piano-fingering corpus to date and a valuable resource for this field. The authors propose multiple methods for modeling the task of piano-fingering, including HMMs and neural networks, and report the best performance with an HMM-based model. In this work, we use PIG as a gold standard for comparison and show how a baseline model pre-trained on our dataset, can improve and achieve state-of-the-art results when fine-tuned on PIG.

## 3 Our Approach: Extracting Fingering from Online Videos

There is a genre of online videos in which people upload piano performances where both the piano and the hands are visible. On some channels, people not only include the video but also the MIDI file recorded while playing the piece. We propose an algorithm for detecting the piano-keyboard, and the fingers playing the different notes, and estimating for each note the fingers that pressed the matching piano key. This process is applied on an entire video, which makes a global inference over the notes. Running this algorithm on multiple videos, in turn, enables the creation of a large dataset of pieces and their fingering information.

The final output we produce is demonstrated in Figure 1, where we colored both the fingers and the played notes based on the pose-estimation model (§3.4) and the predicted fingers that played them (§3.5). Note that the ring fingers of both hands as well as the index finger of the left hand and the middle finger of the right hand do not press any note in this particular frame, but may play a note in others. We get the information of played notes from the MIDI events.

### 3.1 Data Source

We extract videos from [youtube.com](https://ar5iv.labs.arxiv.org/html/youtube.com), played by different piano players on a specific channel containing both video and MIDI files. In these videos, the piano is filmed in an angle horizontal to the keyboard, from which both the keyboard and hands are displayed (as can be seen in Figure 1).

MIDI files: Musical Instrument Digital Interface (MIDI) is a standard format for the interchange of musical information between electronic musical instruments. It consists of a sequence of events describing actions to carry out. In the setup of piano recording, it records what note was played in what time, for how long and its pressure strength (velocity). We only use videos that come along with MIDI files, as we use it as the source for the played notes and their timestamp.[^26] [^27] [^28]

### 3.2 Keyboard and Boundaries Detection

To allow a correct fingering assignment, we first have to find the keyboard and the bounding boxes of the keys. We detect the keyboard as the largest continuous bright area in the video and identify key boundaries using standard image processing techniques, taking into account the expected number of keys their predictable location and clear boundaries. For robustness and in order to handle the interfering hands that periodically hide parts of the piano, we combine information from multiple random frames by averaging the predictions from each frame.

### 3.3 Hands Detection

A straightforward approach for getting fingers locations in an image is to use a pose estimation model directly on the entire image. In practice, common methods for full-body pose estimation such as OpenPose [^29] containing hand pose estimation [^11], make assumptions about the wrist and elbow locations to automatically approximate the hands’ locations. In the case of piano playing, the elbow does not appear in the videos, therefore these systems don’t work. Instead, we turn to a two-steps approach where we start by detecting the hands, crop them, and pass the hand frames to a pose estimation model.

Object Detection [^6] [^7] [^8] [^9], and specifically Hand Detection [^15] [^30] [^11] are well studied subjects. However, we found results to be hard to replicate, due to missing code, compilation problems, private datasets and, most importantly, different lenient assumptions (e.g. no separation between left and right hands).

Therefore, we created a small dataset with random frames from different videos, corresponding to 476 hands in total, evenly split between left and right [^31]. We then fine-tuned a pre-trained object detection model (Inception v2 [^32], based on Faster R-CNN [^33], trained on COCO challenge [^34]) on our new dataset. The fine-tuned model works well and some hand detection bounding boxes are presented in Figure 1.

Having an accurate hand-detection model, we perform hand detection on every frame in the video. If more than two hands are detected, we choose the two bounding boxes with the highest probability. When two hands are detected with the same label (“left-left” or “right-right”), we discard the model’s label, and instead choose the leftmost bounding box to have the label “left” and the other to have the label “right” - which is the most common position of hands on the piano.

### 3.4 Finger Pose Estimation

Having the bounding box of each hand is not sufficient, as in order to assign fingers to notes we need the hand’s pose. How can we detect fingers that pressed the different keys? We turn to pose estimation, a well-studied subject in computer vision [^10] [^11] [^12] in order to tackle this part.

Domain mismatch: The videos we use contain different visual effects, are usually very dark, high-contrast, and blurry due to motion blur. These are real-world conditions, which standard datasets and models rarely encounter [^35] [^36] [^11]. Therefore off-the-shelf pose estimation models often fail in our scenario. Some failure examples are presented in Figure 2(c) where the first pose is estimated correctly, but the rest either have wrong finger positions, shorter, or broken fingers.

GAN-based adaptation: Given the observation that pose-estimation works well on well-lit images, how can we adapt it to work as well for other lighting situations?

Algorithm 1 Pose Estimation Domain Adaptation

Input: unlabeled source data $\mathbb{X_{S}}$, unlabeled target data $\mathbb{X_{T}}$,

Pose Estimation model ($PE$) for source data

Output: Model for target data

Algorithm:

 $L\leftarrow\{\}$

Train CycleGAN from $\mathbb{X_{S}}$ to $\mathbb{X_{T}}$

for $x_{i}\in\mathbb{X_{S}}$ do

 $\hat{y_{i}}=PE(x_{i})$ $\hat{x_{i}}=\textbf{CycleGAN}(x_{i})$ $L\leftarrow(\hat{x_{i}},\hat{y_{i}})$

end for

Fine-Tune $PE$ on $L$

Return $PE$

We propose a new algorithm for adapting a pose-estimation model to out-of-domain inputs, described in Algorithm 1. We seek a mapping $G:S\rightarrow T$ that transforms the source domain (the well-lit videos) into the target domain (the challenging-lit scenarios). We obtain this transformation function using a CycleGAN [^14]. Then, we use a trained pose estimation model $PE$ on the source inputs to get a silver tag $\hat{y_{i}}$, use the transformation $G$ to get a target-input $\hat{x_{i}}$, and align the prediction to the adapted input, resulting in a tuple $(\hat{x_{i}},\hat{y_{i}})$. We use this procedure iteratively and collect silver data, which is then used to fine-tune the original pose-estimation model on. This algorithm results in a new model, which was fine-tuned on data from the target domain (in our case, extremely colorful images) and therefore is robust to this data. We note that this model’s execution time is equivalent to the pre-trained pose-estimation model, as we use the transformation function offline, rather then using it for every prediction. We also benefit of better generalization as we keep good performance on the source domain, and gain major performance on the target domain.

This scenario resembles to sim2real works [^37] [^38] [^39] where one wants to transfer a model from simulations to the real-world. These works learn a mapping function $G^{\prime}:T\rightarrow S$ that transfers instances from the target domain $T$ (the real-world) into the source domain $S$ (the simulation), where the mapping is usually achieved by employing a CycleGan [^14]. Then, models which are trained on the source domain are used on the transformation of the target domain $G_{1}(x_{i})$ and manage to generalize on the target domain. We stress that we differ from these works conceptually as our method uses the transformation from the source to target domain, instead of the other way around. Furthermore, our method benefits from a performance boost, as at test-time, we only have to use the classification function, and not the transformation function.

We employ Algorithm 1 on 21,746 images we automatically collected from videos, and use the convolutional-pose-machines pose estimation [^10] <sup>4</sup>. Some examples can be seen in Figure 2(b), and 2(d) demonstrating the performance on different lighting scenarios.

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2303.03745/assets/figs/cycle/pre-trained.jpg)

(a) Pre-trained model on CycleGAN checkpoints.

### 3.5 Pressed Finger Estimation

Given that we know which notes were pressed in any given frame (see §3.6 below), there is uncertainty as to which finger pressed them. This uncertainty either comes from imperfect pose estimation, or multiple fingers located on top of a single note. We wish to estimate the finger press by calculating the probability of a specific finger that was used, given the hand pose and the pressed note: $argmax_{i}~{}P(x_{i}|n_{k},pose)$

where $i\in[1,10]$ for 10 fingers from both hands, $n_{k}\in[1,88]$ corresponding to the played key and $pose$ correspond to the hand pose.

We model the probability of each finger being pressed as a gaussian distribution where the mean $\mu$ is the center of the key and the variance $\sigma$ is its width. Each finger gets a score for how much it “fits” to play the given key, calculated by the probability density function $x_{i}$, with a given finger $i$, on the key $k$ as: $g_{k}(x_{i})=\mathcal{N}(x_{i}|\mu_{k},\sigma^{2}_{k})$. Then, to derive a distribution over fingers we normalize the scores across all fingers $P(x_{i}|n_{k},pose)=\frac{g_{k}(x_{i})}{\sum_{j}g_{k}(x_{j,k})}$.

As most keyboard presses last more than one frame, we make use of multiple frames to overcome some of the errors from previous steps and to provide a more accurate prediction. To achieve this, we collect the frames that were used during a key press. We treat the first frame as the main signal point, and assign each successive frame an exponentially declining weight. Finally, we normalize the weighted sum of probabilities to achieve a probability distribution for all frames.

In our dataset, we release all probabilities for each played note, along with the maximum likelihood finger estimation. We define the “confidence” score of the extraction from a single piece, as the product of the highest probability for a finger for each note.

### 3.6 Video and MIDI Alignment

We consider the MIDI and video files to be complementary, as they were recorded simultaneously. The MIDI file is the source for key pressing info: what key was pressed, when, and for how long. The video is the source for the piano, hands, and fingers locations. These two sources are not synchronized, but as they depict the same piano performance, a perfect alignment exist (up to the video frequency resolution).

We begin by extracting the audio track from the video, and treat the first audio peak as the beginning of the piece, clipping the prior part of the video and aligning it with the first event from the MIDI file. In practice, we find the starting point as the first signal point that surpasses a threshold.

This heuristic achieves a reasonable alignment, but we observe some alignment mismatch of 80-200ms which affect the entire procedure performance. We tackle the misalignment by using the signal from the final system confidence (Section 3.5), where every piece gets a confidence score from our system. We look for an alignment that maximizes the system confidence over the entire piece:

$$
align(MIDI,Vid)=argmax_{i}score(MIDI_{t_{0}},Vid_{t_{i}})
$$

where $MIDI_{t_{0}}$ is the starting time of the MIDI file, and $Vid_{t_{j}}$ is the alignment time of the video. $Vid_{t_{0}}$ is obtained by the heuristic alignment described in the previous paragraph. We use the confidence score as a proxy of the alignment precision and search the alignment that maximizes the confidence score of the system. More specifically, given the initial offset from the audio-MIDI alignment, we take a window of 1 second in frames (usually 25) from each side and compute the score of the final system on the entire piece. We choose the offset that results in the best confidence score as the alignment offset.

### 3.7 The Resulting Dataset: APFD

We follow the procedure described in this section, and use it to label 90 piano pieces from 42 different composers with 155,107 notes in total. On average, each piece contains 1,723 notes.

## 4 Evaluation

In this section, we provide two evaluations that show that (1) our system for detecting fingering from videos is accurate and (2) the dataset we achieved by repeating this process over dozens of videos is of good quality.

### 4.1 Finger Press Estimation Evaluation

We manually annotated five random pieces from our dataset by marking the pressing finger for each played note in the video. Then, by using our system (§3.5), we estimate what finger was used for each key. We use the confidence score produced by the model as a threshold to use or discard the key prediction of the model, and report precision, recall and F1 scores of multiple thresholds. As discussed in Section 3.4, current pose-estimation models perform poorly, and we propose a new method for domain adaptation. In Table 1 we report the entire system performance on the original pose-estimation [^10] model (Pretrained) using multiple frames, as well as the results using fine-tuned, both by using just the first frame (FT Single Frame) and multiple frames (FT Multiple Frames), which performs best.

When considering a high confidence score (>90%) both the pre-trained and fine-tuned models correctly mark all of the considered notes (which consist of between 34-36% of the data). However, when considering decreasing confidences <sup>5</sup>, our method achieves higher precision and higher recall. With no confidence threshold (i.e using all fingering predictions), the pre-trained model achieves 93% F1, while the fine-tuned one achieves 97% F1, a 57% error reduction.

<table><thead><tr><th>Confidence</th><th colspan="3">c > 0.9</th><th colspan="3">c > 0.5</th><th colspan="3">c > 0</th></tr><tr><th>Metrics</th><th>p</th><th>r</th><th>f1</th><th>p</th><th>r</th><th>f1</th><th>p</th><th>r</th><th>f1</th></tr></thead><tbody><tr><th>Pretrained</th><td>1.0</td><td>0.34</td><td>0.51</td><td>0.95</td><td>0.78</td><td>0.86</td><td>0.88</td><td>1.0</td><td>0.93</td></tr><tr><th>FT Single Frame</th><td>0.99</td><td>0.36</td><td>0.53</td><td>0.97</td><td>0.8</td><td>0.88</td><td>0.9</td><td>1.0</td><td>0.95</td></tr><tr><th>FT Multiple Frames</th><td>1.0</td><td>0.35</td><td>0.52</td><td>0.98</td><td>0.8</td><td>0.88</td><td>0.94</td><td>1.0</td><td>0.97</td></tr></tbody></table>

Table 1: Precision, Recall, F1 scores for 6,894 notes we manually tagged across 5 different pieces, at different confidence points. The first row depict the performance of the system with the vanilla pose estimation. The second and the third rows present the results on the fine-tuned (FT) pose estimation model (§3.4) on a single and multiple frames accordingly.

### 4.2 Automatic Piano Fingering Prediction

In Section 4.1 we showed that our method for extracting piano-fingering from videos is accurate. By running this process on dozens of videos we created the largest dataset for piano-fingering to date. Is this dataset useful?

We begin by training a standard sequence tagging model on APFD and perform evaluations on the subset we manually annotated and on PIG [^1]. Then, by fine-tuning the pre-trained model on PIG, we achieve improvements in performance over the previous state-of-the-art which was trained solely on PIG, suggesting that our dataset is indeed accurate and useful.

We model the piano-fingering as a sequence labeling task, where given a sequence of notes $n_{1},n_{2},...,n_{n}$ we need to predict a sequence of fingering: $y_{1},y_{2},...,y_{n}$, where $y_{i}\in\{1,2,3,4,5\}$ corresponding to 5 fingers of one hand. We employ a standard sequence tagging technique, by embedding each note and using a BiLSTM on top of it. On every contextualized note we then use a Multi-Layer-Perceptron (MLP) to predict the label. The model is trained to minimize cross-entropy loss. This is the same model used in [^1], referred to as DNN (LSTM).

For evaluation, we use the match rate between the prediction and the ground truth. For cases where there is a single ground truth, this is equivalent to accuracy measurement. When more than one labeling is available, we simply average the accuracies with each labeling.[^1] The results are summarized in Table 2.

<table><tbody><tr><th>Training</th><td colspan="2">Evaluation Data</td></tr><tr><th></th><td>APFD</td><td>PIG</td></tr><tr><th>Human Agreement</th><td>—</td><td>71.4</td></tr><tr><th>Previous Neural</th><td>—</td><td>61.3</td></tr><tr><th>Previous SOTA</th><td>—</td><td>64.5</td></tr><tr><th>PIG</th><td>49.9</td><td>64.1</td></tr><tr><th>+ FT APFD</th><td>73.6</td><td>54.4</td></tr><tr><th>APFD</th><td>73.2</td><td>55.2</td></tr><tr><th>+ FT PIG</th><td>62.9</td><td>66.8</td></tr></tbody></table>

Table 2: Results of training and fine tuning on APFD and PIG.

We begin by experimenting on our dataset. APFD is composed of 90 pieces, which we split into 75/10 for training and development sets respectively, and use the 5 manually annotated pieces as a test set. We note that the development set is silver data (automatically annotated) and is likely to contain mistakes. We run the model and achieve 73.2% accuracy.

Next, to test how useful our data is to a real-world gold dataset we wish to inspect its usefulness with a transfer-learning approach. By first pre-training a simple model on our data and then fine-tune the model on PIG. If our data is indeed of quality we’d expect to see performance improvements on PIG, especially as this data is relatively small.

We begin by training the LSTM model solely on PIG,[^1] which results in 64.1% accuracy. This result is higher than the neural model of the same architecture that was reported by [^1] (61.3%) but 0.4% lower than their best performing model (an HMM based). We continue by using the model trained on APFD and then fine-tune it on PIG, which leads to 66.8% accuracy, an improvement of 2.7 points over the previous SOTA. We attribute this gain in performance to our dataset, which both increases the number of training examples and allows to train bigger neural models which excel with more training examples. We also experiment in the opposite direction and fine-tune the model trained on PIG with our data, which result in 73.6% accuracy, which is better than training on our data alone, achieving 73.2% accuracy.

## 5 Discussion and Future Work

In this work, we present an automatic method for detecting piano-fingering from MIDI and video files of a piano performance. We employ this method on a large set of videos, and create the first large scale piano-fingering dataset, containing 90 unique pieces, with 155,107 notes in total. We show that this dataset—although noisy–is valuable, by pre-training a model on it and fine-tuning it on a gold dataset, where we achieve state-of-the-art results. In future work, we intend to improve the data collection by ameliorating the pose-estimation model to better handle the high speed movements and the proximity of the hands, which often cause errors in estimating their pose. Furthermore, we intend to design improved neural models that can take previous fingering predictions into account, in order to have a better global fingering transition.

## References

## 6 Dataset Samples

For every video our system extracts piano-fingering from it also outputs the video overlayed by the estimation of the piano keys, an indication of which notes are played, and what fingers are being used to play them (the key’s color), up to two bounding boxes, for both hands (where light blue means left hand, and light green means right hand), and the pose estimation for each hand.

We include the output videos for all of the pieces we manually annotated to visually demonstrate our system and its accuracy on different playing cases. The videos were uploaded to a new, anonymous YouTube channel, and each contain a link to the original video in the description.

- Yiruma - River Flows in You:  
	[https://youtu.be/Gfs1UWQhr5Q](https://youtu.be/Gfs1UWQhr5Q)
- Alan Walker - Faded:  
	[https://youtu.be/LU2ibOW6z7U](https://youtu.be/LU2ibOW6z7U)
- Beethoven - Moonlight Sonata 1st Movement:  
	[https://youtu.be/wp8j239fs9o](https://youtu.be/wp8j239fs9o)
- Mozart - Rondo Alla Turca:  
	[https://youtu.be/KqTaPfoIuuE](https://youtu.be/KqTaPfoIuuE)
- Chopin - Nocturne in E Flat Major (Op. 9 No. 2):  
	[https://youtu.be/xXHUUzTa5vU](https://youtu.be/xXHUUzTa5vU)

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2303.03745/assets/figs/fingering-estimation/smooth_confidence.png)

Figure 3: Precision and recall based on confidence for all 6,894 manually tagged notes

[^1]: E. Nakamura, Y. Saito, and K. Yoshii, “Statistical learning and estimation of piano fingering,” *arXiv preprint arXiv:1904.10237*, 2019.

[^2]: R. Parncutt, J. A. Sloboda, E. F. Clarke, M. Raekallio, and P. Desain, “An ergonomic model of keyboard fingering for melodic fragments,” *Music Perception: An Interdisciplinary Journal*, vol. 14, no. 4, pp. 341–382, 1997.

[^3]: M. Hart, R. Bosch, and E. Tsai, “Finding optimal piano fingerings,” *The UMAP Journal*, vol. 21, no. 2, pp. 167–177, 2000.

[^4]: J. P. Jacobs, “Refinements to the ergonomic model for keyboard fingering of parncutt, sloboda, clarke, raekallio, and desain,” *Music Perception: An Interdisciplinary Journal*, vol. 18, no. 4, pp. 505–511, 2001.

[^5]: A. A. Kasimi, E. Nichols, and C. Raphael, “A simple algorithm for automatic generation of polyphonic piano fingerings,” in *ISMIR*, 2007.

[^6]: P. Viola and M. Jones, “Rapid object detection using a boosted cascade of simple features,” *CVPR (1)*, vol. 1, no. 511-518, p. 3, 2001.

[^7]: J. Redmon, S. Divvala, R. Girshick, and A. Farhadi, “You only look once: Unified, real-time object detection,” in *Proceedings of the IEEE conference on computer vision and pattern recognition*, 2016, pp. 779–788.

[^8]: T.-Y. Lin, P. Dollár, R. Girshick, K. He, B. Hariharan, and S. Belongie, “Feature pyramid networks for object detection,” in *Proceedings of the IEEE conference on computer vision and pattern recognition*, 2017, pp. 2117–2125.

[^9]: T.-Y. Lin, P. Goyal, R. Girshick, K. He, and P. Dollár, “Focal loss for dense object detection,” in *Proceedings of the IEEE international conference on computer vision*, 2017, pp. 2980–2988.

[^10]: S.-E. Wei, V. Ramakrishna, T. Kanade, and Y. Sheikh, “Convolutional pose machines,” in *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, 2016, pp. 4724–4732.

[^11]: T. Simon, H. Joo, I. Matthews, and Y. Sheikh, “Hand keypoint detection in single images using multiview bootstrapping,” in *Proceedings of the IEEE conference on Computer Vision and Pattern Recognition*, 2017, pp. 1145–1153.

[^12]: B. Doosti, “Hand pose estimation: A survey,” *CoRR*, vol. abs/1903.01013, 2019. \[Online\]. Available: [http://arxiv.org/abs/1903.01013](http://arxiv.org/abs/1903.01013)

[^13]: I. Goodfellow, Y. Bengio, A. Courville, and Y. Bengio, *Deep learning*. MIT Press, 2016, vol. 1.

[^14]: J.-Y. Zhu, T. Park, P. Isola, and A. A. Efros, “Unpaired image-to-image translation using cycle-consistent adversarial networks,” in *Computer Vision (ICCV), 2017 IEEE International Conference on*, 2017.

[^15]: M. Kölsch and M. Turk, “Robust hand detection.” in *FGR*, 2004, pp. 614–619.

[^16]: A. Tang, K. Lu, Y. Wang, J. Huang, and H. Li, “A real-time hand posture recognition system using deep neural networks,” *ACM Transactions on Intelligent Systems and Technology (TIST)*, vol. 6, no. 2, p. 21, 2015.

[^17]: A. Moryossef, Y. Elazar, and Y. Goldberg, “Piano hands dataset,” [https://github.com/AmitMY/piano-hands](https://github.com/AmitMY/piano-hands), 2021.

[^18]: Y. Zhu, A. S. Ramakrishnan, B. Hamann, and M. Neff, “A system for automatic animation of piano performances,” *Computer Animation and Virtual Worlds*, vol. 24, no. 5, pp. 445–457, 2013.

[^19]: Y. Yonebayashi, H. Kameoka, and S. Sagayama, “Automatic decision of piano fingering based on a hidden markov models.” in *IJCAI*, 2007, pp. 2915–2921.

[^20]: E. Nakamura, N. Ono, and S. Sagayama, “Merged-output hmm for piano fingering of both hands.” in *ISMIR*, 2014, pp. 531–536.

[^21]: F. Glover and M. Laguna, “Tabu search,” in *Handbook of combinatorial optimization*. Springer, 1998, pp. 2093–2229.

[^22]: N. Mladenović and P. Hansen, “Variable neighborhood search,” *Computers & operations research*, vol. 24, no. 11, pp. 1097–1100, 1997.

[^23]: M. Balliauw, D. Herremans, D. P. Cuervo, and K. Sörensen, “Generating fingerings for polyphonic piano music with a tabu search algorithm,” in *International Conference on Mathematics and Computation in Music*. Springer, 2015, pp. 149–160.

[^24]: M. Balliauw, D. Herremans, D. Palhazi Cuervo, and K. Sörensen, “A variable neighborhood search algorithm to generate piano fingerings for polyphonic sheet music,” *International Transactions in Operational Research*, vol. 24, no. 3, pp. 509–535, 2017.

[^25]: Y. Takegawa, T. Terada, and S. Nishio, “Design and implementation of a real-time fingering detection system for piano performance.” in *ICMC*, 2006.

[^26]: C. Hawthorne, A. Stasyuk, A. Roberts, I. Simon, C. A. Huang, S. Dieleman, E. Elsen, J. H. Engel, and D. Eck, “Enabling factorized piano music modeling and generation with the MAESTRO dataset,” *CoRR*, vol. abs/1810.12247, 2018. \[Online\]. Available: [http://arxiv.org/abs/1810.12247](http://arxiv.org/abs/1810.12247)

[^27]: Y. Hung, Y. Chen, and Y. Yang, “Learning disentangled representations for timber and pitch in music audio,” *CoRR*, vol. abs/1811.03271, 2018. \[Online\]. Available: [http://arxiv.org/abs/1811.03271](http://arxiv.org/abs/1811.03271)

[^28]: F. C. Cwitkowitz Jr, “End-to-end music transcription using fine-tuned variable-q filterbanks,” 2019.

[^29]: Z. Cao, T. Simon, S.-E. Wei, and Y. Sheikh, “Realtime multi-person 2d pose estimation using part affinity fields,” in *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, 2017, pp. 7291–7299.

[^30]: S. Sridhar, F. Mueller, A. Oulasvirta, and C. Theobalt, “Fast and robust hand tracking using detection-guided optimization,” in *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, 2015, pp. 3213–3221.

[^31]: “labelimg,” [https://github.com/tzutalin/labelImg](https://github.com/tzutalin/labelImg).

[^32]: S. Ioffe and C. Szegedy, “Batch normalization: Accelerating deep network training by reducing internal covariate shift,” *arXiv preprint arXiv:1502.03167*, 2015.

[^33]: S. Ren, K. He, R. Girshick, and J. Sun, “Faster r-cnn: Towards real-time object detection with region proposal networks,” in *Advances in neural information processing systems*, 2015, pp. 91–99.

[^34]: T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan, P. Dollár, and C. L. Zitnick, “Microsoft coco: Common objects in context,” in *European conference on computer vision*. Springer, 2014, pp. 740–755.

[^35]: J. Tompson, M. Stein, Y. Lecun, and K. Perlin, “Real-time continuous pose recovery of human hands using convolutional networks,” *ACM Transactions on Graphics*, vol. 33, August 2014.

[^36]: S. Yuan, Q. Ye, B. Stenger, S. Jain, and T.-K. Kim, “Bighand2. 2m benchmark: Hand pose dataset and state of the art analysis,” in *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, 2017, pp. 4866–4874.

[^37]: F. Sadeghi, A. Toshev, E. Jang, and S. Levine, “Sim2real viewpoint invariant visual servoing by recurrent control,” in *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, 2018, pp. 4691–4699.

[^38]: A. Gupta and J. Booher, “Cyclegan for sim2real domain adaptation.”

[^39]: S. Gamrian and Y. Goldberg, “Transfer learning for related reinforcement learning tasks via image-to-image translation,” *arXiv preprint arXiv:1806.07377*, 2018.