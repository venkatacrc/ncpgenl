# Walk & Recall — WR-5c (verses 5.19–5.26)

- **Cue:** *"Bi-encoder vs cross-encoder?"* → Bi-encoder encodes query/doc separately →
  cosine, fast, precomputable, RAG backbone; cross-encoder jointly encodes the pair,
  accurate but O(n)/query, used to re-rank top-k (5.19).
- **Cue (symptom):** *"Val loss rising while train loss falls — recite the overfitting
  chain."* → Early stopping on a validation metric with patience/min_delta, restore best
  checkpoint (5.20); the diverging curves are the overfitting signal; regularize with
  weight decay/dropout/fewer epochs/more data (5.21); select on validation with a single
  primary metric, never the test set (5.22).
- **Cue (symptom):** *"Model confidently fabricates after fine-tuning — recite the
  mitigation chain."* → Train on grounded data + "I don't know" examples + prefer RAG +
  DPO against fabrication (5.23); enforce at runtime with NeMo Guardrails fact-check/
  self-check rail (Cleanlab TLM) (5.24); assess before/after on held-out with a general-
  capability regression check (5.25); watch for catastrophic forgetting — mitigate with
  PEFT/replay/lower LR/KL-to-reference (5.26).

**Three most likely to be forgotten:** 5.19 cross-encoder is for *re-ranking* (not first-
stage retrieval); 5.22 never select on the test set; 5.26 PEFT resists forgetting by
freezing the base.
