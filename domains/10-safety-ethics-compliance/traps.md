# Traps — Safety, Ethics & Compliance

- **Fairness metrics conflict.** Demographic parity, equal opportunity, and equalized
  odds cannot generally all hold at once (impossibility) — pick per context (10.03).
- **Guardrails ≠ alignment.** Rails enforce at runtime independent of the model;
  alignment/fine-tuning changes the model's tendencies. You need both (10.09, 10.10).
- **Prompting is not enforcement.** Prompt-level safety is bypassable (injection/
  jailbreak); guardrails + classifiers enforce (2.25 → 10.09).
- **Single-layer safety.** No one control suffices — defense in depth across data/model/
  prompt/rails/monitoring (10.10).
- **Bias is not only a data problem.** It enters at labeling, algorithm, eval, and
  deployment too (10.04).
- **Mitigation without re-measurement.** Always re-audit fairness after mitigation;
  watch accuracy/fairness trade-offs (10.07).
- **Colang versioning.** Colang 1.0 vs 2.0 syntax differs (10.09).
- **Feedback-loop bias.** Retraining on the model's own outputs amplifies bias (10.04,
  9.10).
