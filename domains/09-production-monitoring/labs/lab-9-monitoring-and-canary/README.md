# Lab 9 — Monitoring, Drift & Canary  `[A100-OK]`

**Objective:** Scrape Triton/DCGM metrics with Prometheus + Grafana, compute an SLO and
error budget, detect input drift with PSI, and simulate a canary rollout + rollback.
Covers 9.1, 9.2, 9.3.

**Tag:** `[A100-OK]` (metrics/analysis are CPU-light; reuses Lab 8's server).

**Prerequisites:** Lab 8 server running (:8002 metrics), Docker for Prometheus/Grafana,
`pip install requests numpy prometheus-client`.

**Container (VERIFY):** `prom/prometheus`, `grafana/grafana` (Docker Hub); server from
Lab 8.

## Stages
| Stage | File | Verifies |
|-------|------|----------|
| 00 | `stage-00-env-check.sh` | metrics endpoint reachable |
| 01 | `stage-01-prometheus-config.yml` | scrape config targets :8002 |
| 02 | `stage-02-docker-compose-monitoring.yml` | Prometheus+Grafana up |
| 03 | `stage-03-slo-error-budget.py` | SLO compliance + budget computed |
| 04 | `stage-04-drift-psi.py` | PSI flags shifted distribution |
| 05 | `stage-05-canary-rollout-sim.py` | canary ramps or rolls back |
| 06 | `stage-06-verify-and-breakit.py` | inject drift/latency → alert fires |

## Expected metrics
- SLO: % of requests under the latency target; error budget = 1 − SLO_target.
- PSI < 0.1 no drift, 0.1–0.25 moderate, > 0.25 significant drift.
- Canary: healthy → ramp to 100%; unhealthy → auto rollback.

## Break it on purpose
`stage-06` injects a latency spike / shifted inputs so the SLO burn-rate and PSI cross
thresholds and the canary rolls back — reproducing drift-triggered rollback (9.06/9.09).
