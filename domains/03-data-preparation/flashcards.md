# Flashcards — Data Preparation (15, keyed to verses)

1. **(3.01)** Two cleaning steps that curb memorization/leakage? → Unicode normalization + deduplication.
2. **(3.02)** Which missingness biases naive imputation? → MNAR (missing not at random).
3. **(3.03)** Where do you fit scalers? → Train only, then apply to val/test.
4. **(3.04)** Metric for imbalanced classes? → Macro-F1 / per-class recall (not accuracy).
5. **(3.05)** NVIDIA GPU pandas-like EDA tool? → RAPIDS cuDF.
6. **(3.06)** NVIDIA scale data-curation library? → NeMo Curator (Dask + RAPIDS).
7. **(3.07)** Two quality-filter layers in Curator? → Heuristic filters + classifier-based filter.
8. **(3.08)** Fuzzy dedup method? → MinHash + LSH (Jaccard estimate).
9. **(3.09)** Stage reducing private-data regurgitation? → PII redaction/content filtering.
10. **(3.10)** Top silent SFT bug? → Train/serve chat-template mismatch.
11. **(3.12)** What does sequence packing fix, and its requirement? → Padding waste; needs attention masking.
12. **(3.14)** BPE merge rule? → Greedily merge most frequent adjacent pair (byte-level = no OOV).
13. **(3.15)** WordPiece merge rule + marker? → Maximize corpus likelihood; `##` continuations.
14. **(3.16)** Is SentencePiece an algorithm? → No — a framework implementing BPE/Unigram on raw text (`▁`).
15. **(3.18)** Fertility? → Avg tokens/word; high fertility inflates cost and can truncate past max_seq_len.
