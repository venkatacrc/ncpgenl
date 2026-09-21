# Walk & Recall — WR-3a (verses 3.01–3.09)

- **Cue (symptom):** *"Model memorizes and test scores look suspiciously high — recite
  the data-hygiene chain."* → Clean and Unicode-normalize (3.01); duplicates cause
  memorization and leakage, so dedup: exact hashing plus fuzzy MinHash+LSH for
  near-duplicates (3.08); decontaminate against eval sets (ties 3.11) — that is the
  cause of inflated scores.
- **Cue:** *"Records with missing fields / skewed labels?"* → Impute by mechanism
  (MCAR tolerates simple, MNAR biases), or drop; filter degenerate short docs (3.02);
  scale numeric features fit-on-train-only (3.03); detect imbalance and mitigate with
  resampling/class-weighted/focal loss, judging by macro-F1 not accuracy (3.04).
- **Cue:** *"Curate billions of docs at scale — which NVIDIA tool and what stages?"* →
  Profile with RAPIDS cuDF on GPU (3.05); NeMo Curator pipeline: extract → language ID
  → quality filter (heuristic + classifier, 3.07) → dedup → PII/content filter (3.09)
  → decontaminate → format.

**Three most likely to be forgotten:** 3.08 fuzzy dedup = MinHash+LSH (Jaccard, avoids
O(n²)); 3.04 imbalance → macro-F1/per-class recall, not accuracy; 3.03 fit scalers on
train only.
