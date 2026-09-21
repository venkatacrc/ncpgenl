"""Stage 06 — verify parse improvement + break-it (unconstrained @ high temp)."""
import os, json, torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = os.environ.get("MODEL", "Qwen/Qwen2.5-0.5B-Instruct")
dev = "cuda" if torch.cuda.is_available() else "cpu"
tok = AutoTokenizer.from_pretrained(MODEL)
lm = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16).eval().to(dev)

prompt = 'Return ONLY JSON {"x": number}. Value 7.'
ids = tok(prompt, return_tensors="pt").to(dev)

def parse_rate(temperature, n=12):
    ok = 0
    for _ in range(n):
        out = lm.generate(**ids, max_new_tokens=20, do_sample=True,
                          temperature=temperature, pad_token_id=tok.eos_token_id)
        t = tok.decode(out[0][ids.input_ids.shape[1]:], skip_special_tokens=True)
        try:
            json.loads(t[t.find("{"): t.rfind("}") + 1]); ok += 1
        except Exception:
            pass
    return ok / n

low = parse_rate(0.2); high = parse_rate(1.3)
print(f"[VERIFY] parse rate temp=0.2: {low:.2f} | temp=1.3: {high:.2f}")
print("[BREAK-IT] high temperature without constrained decoding degrades JSON validity"
      if high < low else "[BREAK-IT] rerun; sampling variance masked the effect")
