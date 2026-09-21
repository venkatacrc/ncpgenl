# Walk & Recall — WR-3b (verses 3.10–3.18)

- **Cue (symptom):** *"Fine-tuned model behaves oddly at inference though training loss
  was fine — recite."* → Train/serve **chat-template mismatch** is a top silent bug;
  format as JSONL messages rendered with the model's template (3.10); split without
  leakage by group/time, decontaminate, fit preprocessing on train only (3.11); pack
  sequences to max_seq_len with masking to kill padding waste (3.12).
- **Cue:** *"Why subword tokenization, and which algorithm?"* → Subword balances vocab
  size vs sequence length, no true OOV (3.13). BPE = greedy frequency merges, byte-level
  = no OOV (3.14); WordPiece = likelihood-maximizing merges with ## continuations
  (3.15); Unigram prunes a big vocab by likelihood; SentencePiece is the *library*, not
  an algorithm (3.16).
- **Cue (symptom):** *"Inference cost per request is higher than expected on our code/
  non-English data — recite the tokenizer chain."* → Vocab size trades sequence length
  vs embedding-matrix size (3.17); high **fertility** (tokens/word) on unseen domains
  inflates length/cost and can silently truncate past max_seq_len (3.18) — the cause.

**Three most likely to be forgotten:** 3.16 SentencePiece is a *framework* (implements
BPE/Unigram), not its own algorithm; 3.15 WordPiece merges by *likelihood* not
frequency; 3.18 fertility = tokens/word drives cost and truncation.
