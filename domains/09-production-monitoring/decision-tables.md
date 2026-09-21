# Decision Tables — Production Monitoring

## Observability pillars

| Pillar | Captures | Use | Tool |
|---|---|---|---|
| Metrics | aggregate time-series | trends, SLOs, alerts | Prometheus/Grafana, DCGM |
| Logs | discrete events | forensics (PII-safe) | log stack |
| Traces | request path across services | latency attribution | OpenTelemetry |

## SLI / SLO / error budget

| Term | Meaning | Example |
|---|---|---|
| SLI | measured indicator | p99 TTFT |
| SLO | target | p99 TTFT < 500ms, 99.9% |
| Error budget | 1 − SLO | 0.1% failures allowed |

## Drift

| Type | What changes | Detect |
|---|---|---|
| Data/covariate | input distribution | PSI/KL on inputs, embedding monitor |
| Concept | input→output mapping | quality drop vs golden set |

## Rollout strategies

| Strategy | Traffic | User risk | Purpose |
|---|---|---|---|
| Canary | small % live | low | validate before ramp |
| Shadow | mirrored copy | **none** | offline compare |
| A/B | split | medium | statistical metric diff |
| Rolling | gradual replace | low | zero-downtime deploy |
