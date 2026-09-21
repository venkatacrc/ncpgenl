# Flashcards — Production Monitoring (15, keyed to verses)

1. **(9.01)** Monitoring stack + GPU telemetry exporter? → Prometheus + Grafana; DCGM-Exporter.
2. **(9.02)** Four golden signals? → Latency, traffic, errors, saturation.
3. **(9.02)** Key LLM latency metrics? → TTFT and TPOT (inter-token latency), at percentiles.
4. **(9.03)** SLI vs SLO vs error budget? → Measured indicator; target; 1 − SLO.
5. **(9.04)** Three observability pillars? → Metrics, logs, traces.
6. **(9.05)** Alert on what to avoid fatigue? → Rate of change / burn rate, deduped.
7. **(9.06)** Data drift vs concept drift? → Input distribution shifts vs input→output mapping shifts.
8. **(9.06)** Drift detection metrics? → PSI, KL, embedding-space monitoring.
9. **(9.07)** Continuous benchmarking catches? → Quality/latency regressions vs prior versions.
10. **(9.08)** Shadow vs canary? → Shadow mirrors traffic (no responses returned); canary sends live %.
11. **(9.09)** Rollback prerequisite? → Versioned/immutable artifacts + readiness-gated updates.
12. **(9.10)** Retraining feedback-loop risk? → Training on the model's own outputs amplifies bias.
13. **(9.12)** Registry vs version policy? → Registry = lineage source of truth; version policy = served versions.
14. **(9.13)** Graceful degradation? → Fallback to smaller/cached model, shed load, circuit breakers.
15. **(9.14)** Trust artifacts? → Audit trails, model cards, provenance, citations.
