"""Stage 04 — Population Stability Index (PSI) for input drift detection (9.06)."""
import numpy as np

def psi(expected, actual, bins=10):
    edges = np.percentile(expected, np.linspace(0, 100, bins + 1))
    edges[0], edges[-1] = -np.inf, np.inf
    e = np.histogram(expected, edges)[0] / len(expected) + 1e-6
    a = np.histogram(actual, edges)[0] / len(actual) + 1e-6
    return float(np.sum((a - e) * np.log(a / e)))

rng = np.random.default_rng(0)
baseline = rng.normal(0, 1, 5000)              # e.g. prompt-length distribution at train
no_drift = rng.normal(0, 1, 5000)
drifted = rng.normal(1.2, 1.5, 5000)           # distribution shifted

for name, cur in [("no-drift", no_drift), ("drifted", drifted)]:
    p = psi(baseline, cur)
    tag = "OK" if p < 0.1 else ("MODERATE" if p < 0.25 else "SIGNIFICANT DRIFT")
    print(f"{name:9s} PSI={p:.3f} -> {tag}")
