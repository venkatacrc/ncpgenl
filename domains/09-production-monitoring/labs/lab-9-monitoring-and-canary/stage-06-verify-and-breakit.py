"""Stage 06 — verify healthy passes; break-it by injecting drift + latency (9.06/9.09)."""
import numpy as np
rng = np.random.default_rng(1)

def psi(expected, actual, bins=10):
    edges = np.percentile(expected, np.linspace(0, 100, bins + 1))
    edges[0], edges[-1] = -np.inf, np.inf
    e = np.histogram(expected, edges)[0] / len(expected) + 1e-6
    a = np.histogram(actual, edges)[0] / len(actual) + 1e-6
    return float(np.sum((a - e) * np.log(a / e)))

baseline = rng.normal(0, 1, 5000)

# --- verify: normal traffic passes ---
normal_psi = psi(baseline, rng.normal(0, 1, 5000))
normal_slo = (rng.normal(250, 80, 1000) > 500).mean()
assert normal_psi < 0.1 and normal_slo < 0.05
print(f"[VERIFY] PSI={normal_psi:.3f} SLO-violation={normal_slo:.3f} -> healthy")

# --- break it: inject drift + latency spike ---
bad_psi = psi(baseline, rng.normal(1.5, 1.6, 5000))
bad_slo = (rng.normal(850, 150, 1000) > 500).mean()
alert = bad_psi > 0.25 or bad_slo > 0.05
print(f"[BREAK-IT] PSI={bad_psi:.3f} SLO-violation={bad_slo:.3f} -> "
      f"{'ALERT: rollback + trigger retraining' if alert else 'no alert (retune thresholds)'}")
