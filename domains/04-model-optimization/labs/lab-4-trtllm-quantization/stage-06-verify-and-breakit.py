"""Stage 06 — break-it: bad calibration -> accuracy collapse (4.09/4.10).

Demonstrates conceptually why calibration data must match deployment distribution.
Uses a synthetic per-tensor INT8 fake-quant with a range fit on the WRONG data.
"""
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import os

MODEL = os.environ.get("MODEL", "TinyLlama/TinyLlama-1.1B-Chat-v1.0")
tok = AutoTokenizer.from_pretrained(MODEL)
m = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.float16, device_map="cuda").eval()

def fake_quant_(t, s):
    t.copy_((t / s).round().clamp(-127, 127) * s)

def perplexity():
    ids = tok("The transformer architecture uses self-attention.",
              return_tensors="pt").to(m.device)
    with torch.no_grad():
        return float(torch.exp(m(**ids, labels=ids.input_ids).loss))

base = perplexity()

# GOOD calibration: scale from the layer's own weight range
lin = [mod for mod in m.modules() if isinstance(mod, torch.nn.Linear)][0]
w = lin.weight.data.clone()
good_s = w.abs().max() / 127
fake_quant_(lin.weight.data, good_s); good = perplexity(); lin.weight.data.copy_(w)

# BAD calibration: absurd scale from unrepresentative "data"
bad_s = good_s * 50
fake_quant_(lin.weight.data, bad_s); bad = perplexity(); lin.weight.data.copy_(w)

print(f"[VERIFY] ppl base={base:.2f} good-calib={good:.2f} bad-calib={bad:.2f}")
print("[BREAK-IT] bad calibration scale collapses accuracy"
      if bad > good * 1.5 else "[BREAK-IT] increase scale factor to exaggerate")
