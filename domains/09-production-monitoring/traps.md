# Traps — Production Monitoring

- **Data drift vs concept drift.** Data drift = input distribution shifts; concept drift
  = the input→output relationship shifts. Distractors swap them (9.06).
- **Shadow vs canary.** Shadow mirrors traffic with **no** user-facing responses; canary
  routes a real % of live traffic. Not the same (9.08).
- **Alerting on means.** Use percentiles (p95/p99) and burn rate; means hide tail
  problems and cause missed SLO breaches (9.02, 9.03).
- **Registry vs serving version policy.** The model registry is the source-of-truth
  lineage; `config.pbtxt` version policy controls what's *served* (9.12 vs 8.18).
- **Retraining feedback loops.** Retraining on the model's own outputs amplifies bias —
  guard against it (9.10).
- **Silent drift.** Drift throws no error; only monitoring/benchmarking catches it — the
  top "got worse over time" cause (9.06, 9.07).
- **No rollback plan.** A deploy without a proven fast rollback is unsafe (9.09).
- **Logging raw PII.** Log metadata, not sensitive content; respect privacy/compliance
  (9.04, 9.14).
