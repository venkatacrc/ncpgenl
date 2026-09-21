# Traps — Prompt Engineering

- **Confusing in-context learning with training.** ICL (2.05) updates *no* weights;
  it is transient (KV/activations). Soft prompts / P-tuning (2.12, 5.15) *do* train
  vectors. Exam distractors swap these.
- **Assuming more few-shot examples always help.** Redundant/class-skewed exemplars and
  recency bias can *lower* accuracy; balance and diversify (2.04).
- **Treating JSON-schema prompting as a guarantee.** It only improves parse rates;
  hard validity needs constrained decoding (2.18 vs 2.19).
- **Self-consistency ≠ one longer CoT.** It is *multiple sampled traces + majority
  vote*; a single greedy trace is not self-consistency (2.08).
- **Treating retrieved content as trusted instructions.** Indirect prompt injection
  hides directives in RAG documents; treat retrieved text as data (2.25).
- **Believing prompting can add durable knowledge.** Context is capped and transient;
  new durable knowledge requires fine-tuning/RAG (2.14, 2.23).
- **`temperature=0` for "creative" UX.** Backwards — low temp = deterministic/factual
  (2.26; see 1.11).
- **Placing RAG as its own domain.** The blueprint has no RAG domain; RAG verses live
  in Prompt Engineering (context), Evaluation (Ragas), Deployment, and Safety.
