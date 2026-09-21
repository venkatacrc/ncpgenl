"""Stage 03 — compute SLO compliance and error budget from latency samples (9.03)."""
import numpy as np

# Simulated (or measured) per-request latencies in ms.
rng = np.random.default_rng(0)
latencies = np.concatenate([rng.normal(200, 40, 950), rng.normal(700, 120, 50)])

SLO_TARGET = 0.99          # 99% of requests must meet the threshold
THRESHOLD_MS = 500         # p-latency objective

compliant = (latencies < THRESHOLD_MS).mean()
error_budget = 1 - SLO_TARGET
consumed = max(0.0, (1 - compliant))
print(f"compliance={compliant:.3f} (target {SLO_TARGET})")
print(f"error budget={error_budget:.3f} consumed={consumed:.3f} "
      f"-> {'WITHIN budget' if consumed <= error_budget else 'BUDGET EXCEEDED (freeze risky changes)'}")
print(f"p50={np.percentile(latencies,50):.0f}ms p99={np.percentile(latencies,99):.0f}ms")
