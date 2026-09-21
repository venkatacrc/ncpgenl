"""Stage 05 — simulate a canary rollout with health-gated ramp/rollback (9.08, 9.09)."""
import numpy as np

rng = np.random.default_rng(0)
SLO_MS = 500

def canary_error_rate(traffic_pct, unhealthy=False):
    n = max(int(1000 * traffic_pct), 20)
    mean = 900 if unhealthy else 250          # unhealthy version is slow
    lat = rng.normal(mean, 80, n)
    return (lat > SLO_MS).mean()

def rollout(unhealthy):
    pct = 0.05
    while pct <= 1.0:
        err = canary_error_rate(pct, unhealthy)
        print(f"  canary {int(pct*100):3d}% traffic: SLO-violation rate={err:.2f}")
        if err > 0.05:
            print("  -> UNHEALTHY: ROLLBACK to previous version"); return "rollback"
        pct = min(pct * 2, 1.0) if pct < 1.0 else pct + 1
    print("  -> healthy: promoted to 100%"); return "promoted"

print("healthy new version:");   rollout(unhealthy=False)
print("faulty new version:");    rollout(unhealthy=True)
