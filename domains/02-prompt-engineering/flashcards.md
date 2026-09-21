# Flashcards — Prompt Engineering (15, keyed to verses)

1. **(2.01)** Highest-leverage cheapest steering surface? → The system message.
2. **(2.02/2.03)** Cheapest fix when zero-shot gets format wrong? → One-shot example (demonstrates format/labels).
3. **(2.04)** Two things that make few-shot worse? → Redundant/class-skewed exemplars; recency/order bias.
4. **(2.05)** Does in-context learning update weights? → No; transient forward-pass adaptation.
5. **(2.06)** Why does CoT help? → Written steps become context the autoregressive model conditions on.
6. **(2.07)** Zero-shot CoT trigger? → "Let's think step by step."
7. **(2.08)** Self-consistency = ? → Sample multiple CoT traces + majority vote.
8. **(2.10)** ReAct loop? → Thought → Action → Observation.
9. **(2.12)** Soft prompt vs hard prompt? → Soft = trainable continuous vectors (frozen weights); hard = discrete tokens.
10. **(2.15)** CLM loss? → −Σ log p(x_t | x_{<t}) cross-entropy under causal mask.
11. **(2.16)** Label construction + ignore index? → Inputs shifted by one; prompt/pad → −100.
12. **(2.18 vs 2.19)** JSON-prompt vs constrained decoding? → Prompt = soft/likely; constrained = hard guarantee via logit masking.
13. **(2.21)** Root-cause hallucination fix? → Ground on retrieved context; answer-only-from-context + "I don't know."
14. **(2.23)** Where does RAG sit in the blueprint? → Inside Prompt Engineering (prompt-context), not its own domain.
15. **(2.25)** Indirect prompt injection? → Malicious instructions hidden in retrieved documents; treat retrieved text as data.
