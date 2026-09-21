# Walk & Recall — WR-4d (verses 4.28–4.34)

- **Cue:** *"How are encoders pretrained?"* → MLM: mask ~15% (80% [MASK]/10% random/10%
  unchanged), predict from bidirectional context (4.28); NSP was BERT's second objective,
  but RoBERTa dropped it as unhelpful (4.29).
- **Cue:** *"Sampling knobs in optimization/ablation studies?"* → Beam search keeps top-b
  by length-normalized log-prob, helps constrained not open-ended, cost linear in b
  (4.30); temperature scaling is both a decoding knob and a post-hoc calibration method;
  ablations change one variable per run with fixed seeds/decoding (4.31).
- **Cue (symptom):** *"Training diverges in the first hundred steps at large batch —
  recite the schedule chain."* → Warmup ramps LR from ~0 to avoid early divergence, then
  cosine decay (4.32) — missing warmup is the cause; linear scaling rule ties LR to batch
  size up to a critical batch (4.33); search hyperparameters with grid/random/Bayesian/
  PBT distributed across GPUs with early stopping (4.34).

**Three most likely to be forgotten:** 4.28 the 80/10/10 mask split; 4.29 RoBERTa
*dropped* NSP; 4.33 linear scaling rule + critical batch size.
