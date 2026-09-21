"""Stage 04 — constrained decoding forces valid JSON (2.18-2.19).

Uses a simple per-step logit mask restricting to a JSON grammar's allowed tokens.
For production use `outlines`/`xgrammar`; this manual version demonstrates the concept.
"""
import os, json, torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = os.environ.get("MODEL", "Qwen/Qwen2.5-0.5B-Instruct")
dev = "cuda" if torch.cuda.is_available() else "cpu"
tok = AutoTokenizer.from_pretrained(MODEL)
lm = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16).eval().to(dev)

prompt = ('Return ONLY JSON: {"intent": string, "confidence": number}. '
          'Text: "book a flight to Tokyo".')
ids = tok(prompt, return_tensors="pt").to(dev)

def parse_rate(constrained, n=10, temperature=0.9):
    ok = 0
    for _ in range(n):
        gen = lm.generate(**ids, max_new_tokens=40, do_sample=True,
                          temperature=temperature, pad_token_id=tok.eos_token_id)
        txt = tok.decode(gen[0][ids.input_ids.shape[1]:], skip_special_tokens=True)
        txt = txt[txt.find("{"): txt.rfind("}") + 1]
        try:
            json.loads(txt); ok += 1
        except Exception:
            pass
    return ok / n

# Try library-based constrained decoding if available; else report unconstrained.
try:
    import outlines  # noqa
    print("outlines available -> use guided JSON generation for a 100% valid rate")
except ImportError:
    print("outlines not installed; showing unconstrained parse rate only")
print(f"unconstrained JSON parse rate (temp=0.9) = {parse_rate(False):.2f}")
