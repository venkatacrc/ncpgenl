# Module 9 — Production Monitoring & Reliability (Exam Weight 7%)

Verses 9.01–9.14.

## Contents
- [Objectives covered](objectives.md)
- Verses: [`verses/`](verses/) — 9.01→9.14
- Walk & Recall: [WR-9a](walk-recall/WR-9a-verses-9.01-9.07.md), [WR-9b](walk-recall/WR-9b-verses-9.08-9.14.md)
- [Decision tables](decision-tables.md) · [Traps](traps.md) · [Question bank](question-bank.md) · [Flashcards](flashcards.md)
- Lab: [lab-9-monitoring-and-canary](labs/lab-9-monitoring-and-canary/)

## Verse chain
9.01–9.03 stack/metrics/SLO → 9.04–9.06 logs-traces/anomaly/drift → 9.07–9.09
benchmarking/canary-shadow-AB/rollback → 9.10–9.12 retraining/pipelines/registry →
9.13–9.14 uptime-HA/transparency-trust → (Domain 10).

## NVIDIA-specific layer
- **Triton metrics** (:8002) + **DCGM-Exporter** → **Prometheus** → **Grafana** is the
  reference observability stack.
- Continuous benchmarking reuses **NeMo Evaluator** (Domain 6); automated tuning uses
  **NeMo** recipes + **Base Command**/cluster schedulers.
- Model repo **version policy** (8.18) enables canary/A-B; a **model registry** tracks
  lineage.
- Reliability engineering (SLOs, error budgets, graceful degradation) is standard SRE
  applied to GPU inference.

> **Stale-knowledge flag:** dashboard/exporter names and MLOps tooling evolve; verify
> current DCGM/Triton metric names.
