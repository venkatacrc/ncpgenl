# Question Bank — Data Preparation (12 scenario MCQ)

**Q1.** Benchmark scores are implausibly high. Investigation finds test items duplicated
in training. Root cause + fix?
A. Overfitting; add dropout  B. Eval-set contamination; decontaminate/dedup across splits  C. Bad tokenizer; retrain  D. Learning rate; lower it

**Q2.** Which statement about WordPiece vs BPE is correct?
A. Both merge by raw frequency  B. WordPiece merges to maximize corpus likelihood; BPE merges most frequent pair  C. BPE uses `##` markers  D. WordPiece cannot represent OOV, BPE always can regardless of variant

**Q3.** A team calls SentencePiece "a tokenization algorithm distinct from BPE and
Unigram." Correct response?
A. True  B. SentencePiece is a framework implementing BPE or Unigram on raw text  C. It's the same as WordPiece  D. It only does character-level

**Q4.** Inference cost per request is unexpectedly high on source-code inputs with a
32k English-trained tokenizer. Most likely cause?
A. Vocab too large  B. High fertility (tokens/word) inflating sequence length  C. Temperature too high  D. Missing system prompt

**Q5.** You scale numeric features using statistics computed over train+val+test
combined. Problem?
A. None  B. Data leakage; fit on train only  C. Slower training  D. Requires GPU

**Q6.** A classifier ignores a rare but critical class. Best combination of metric +
mitigation?
A. Accuracy; oversample majority  B. Macro-F1/per-class recall; class-weighted or focal loss  C. Perplexity; dropout  D. BLEU; undersample minority

**Q7.** Which best removes near-duplicate (not identical) documents at scale?
A. md5 exact hashing only  B. MinHash + LSH (Jaccard estimate)  C. Random sampling  D. Sorting alphabetically

**Q8.** Larger tokenizer vocabulary primarily trades what?
A. Longer sequences for smaller embedding matrix  B. Shorter sequences for a larger embedding + softmax matrix  C. Nothing  D. Accuracy for latency only

**Q9.** In NeMo Curator, which stage most directly reduces the model's risk of
regurgitating private data?
A. Quality filtering  B. PII redaction/content filtering  C. Language ID  D. Sequence packing

**Q10.** Why is sequence packing used when preparing pretraining shards?
A. To increase vocab size  B. To eliminate padding waste and raise throughput (with masking)  C. To add PII  D. To shuffle labels

**Q11.** A fine-tuned model behaves oddly at inference despite good training loss. Data
team used a different chat template than serving. Diagnosis?
A. Overfitting  B. Train/serve template mismatch  C. Tokenizer OOV  D. Class imbalance

**Q12.** Which tool does NVIDIA recommend for GPU-accelerated pandas-like EDA on large
corpora?
A. RAPIDS cuDF  B. Matplotlib  C. NumPy  D. scikit-learn

---

## Answers & rationale

**Q1 — B.** Duplicated test items in train = contamination; decontaminate/dedup across
splits. A: dropout doesn't fix leakage. C/D: unrelated.

**Q2 — B.** WordPiece = likelihood merges; BPE = frequency merges. A: false. C: `##` is
WordPiece. D: byte-level BPE has no OOV, but not "always... regardless of variant."

**Q3 — B.** SentencePiece is a framework implementing BPE/Unigram on raw text. A/C/D:
false.

**Q4 — B.** English tokenizer fragments code → high fertility → long sequences → cost.
A: vocab isn't too large here. C/D: unrelated.

**Q5 — B.** Using val/test statistics leaks information; fit scalers on train only.
A/C/D: wrong.

**Q6 — B.** Macro-F1/per-class recall exposes rare-class failure; class-weighted/focal
loss mitigates. A: accuracy hides it, oversampling majority worsens. C/D: wrong metrics.

**Q7 — B.** MinHash+LSH estimates Jaccard for near-dups without O(n²). A: exact only.
C/D: don't detect duplicates.

**Q8 — B.** Larger vocab → shorter sequences but larger embedding/softmax matrix. A:
reversed. C/D: incomplete.

**Q9 — B.** PII redaction directly reduces private-data regurgitation. A: quality, not
privacy. C: language detection. D: batching.

**Q10 — B.** Packing removes padding waste (needs masking). A/C/D: wrong.

**Q11 — B.** Template mismatch between train and serve. A/C/D: not indicated.

**Q12 — A.** RAPIDS cuDF is NVIDIA's GPU pandas-like tool. B/C/D: CPU/not EDA-scale.
