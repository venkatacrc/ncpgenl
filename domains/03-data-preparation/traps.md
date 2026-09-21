# Traps — Data Preparation

- **SentencePiece is not an algorithm.** It is a library implementing BPE or Unigram on
  raw text. Distractors present it as a fourth algorithm (3.16).
- **WordPiece merges by likelihood, not frequency.** BPE is the frequency one (3.14 vs
  3.15).
- **Fitting scalers/tokenizers on the full dataset.** Leakage — fit on train only
  (3.03, 3.11).
- **Accuracy on imbalanced data.** Misleading; use macro-F1 / per-class recall (3.04).
- **Ignoring eval-set decontamination.** A test item duplicated in train inflates
  benchmark scores — a classic "why are my scores too good" trap (3.11).
- **Train/serve chat-template mismatch.** Silent behavioral degradation despite clean
  training loss (3.10).
- **Ignoring fertility.** High tokens/word on code/other languages inflates cost and
  silently truncates beyond max_seq_len (3.18).
- **Padding waste.** Not packing short sequences wastes throughput; packing needs
  attention masking to prevent cross-example attention (3.12).
