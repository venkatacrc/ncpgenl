"""Stage 05 — demographic parity & equal opportunity on a toy classifier (10.03)."""
import numpy as np
rng = np.random.default_rng(0)

# Simulated predictions y_pred, ground truth y_true, and protected group g.
n = 2000
g = rng.integers(0, 2, n)                       # 0/1 protected groups
y_true = rng.integers(0, 2, n)
# Inject bias: group 1 gets fewer positive predictions.
base = 0.5 - 0.2 * g
y_pred = (rng.random(n) < np.clip(base + 0.3 * y_true, 0, 1)).astype(int)

def rate(mask): return y_pred[mask].mean()
def tpr(mask):  return y_pred[mask & (y_true == 1)].mean()

dp = abs(rate(g == 0) - rate(g == 1))           # demographic parity gap
eo = abs(tpr(g == 0) - tpr(g == 1))             # equal opportunity gap
print(f"positive rate g0={rate(g==0):.3f} g1={rate(g==1):.3f} -> demographic parity gap={dp:.3f}")
print(f"TPR        g0={tpr(g==0):.3f} g1={tpr(g==1):.3f} -> equal opportunity gap={eo:.3f}")
print("Larger gaps => more unfair. Mitigate (10.07) then RE-MEASURE.")
