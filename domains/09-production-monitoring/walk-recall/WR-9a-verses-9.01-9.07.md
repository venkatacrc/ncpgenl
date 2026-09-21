# Walk & Recall — WR-9a (verses 9.01–9.07)

- **Cue:** *"Stand up LLM monitoring — recite the stack and metrics."* → Prometheus
  scrapes Triton :8002 + DCGM-Exporter, Grafana visualizes/alerts (9.01); track golden
  signals + LLM metrics: TTFT, TPOT, tokens/s, queue depth, KV-cache util, at percentiles
  (9.02); turn them into SLIs/SLOs with error budgets, alert on burn rate (9.03).
- **Cue (symptom):** *"An incident happened — recite how to find the root cause."* → Three
  pillars: metrics (trends), logs (events, PII-safe), traces (request path via
  OpenTelemetry), correlated by request ID (9.04); anomaly detection on rate-of-change/
  burn rate, tuned against alert fatigue (9.05).
- **Cue (symptom):** *"The model quietly got worse over weeks with no errors — recite."*
  → Drift: data/covariate (input distribution shifts) vs concept (input→output mapping
  shifts), detected via PSI/KL/embedding monitoring — the silent-degradation cause
  (9.06); confirm with continuous benchmarking on a golden set vs prior versions to catch
  regressions (9.07).

**Three most likely to be forgotten:** 9.03 error budget = 1−SLO (alert on burn rate);
9.06 data drift vs concept drift distinction; 9.02 track percentiles not means.
