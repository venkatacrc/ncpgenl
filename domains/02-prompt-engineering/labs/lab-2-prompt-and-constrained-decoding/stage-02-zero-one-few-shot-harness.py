"""Stage 02 — zero/one/few-shot sentiment accuracy (2.02-2.04)."""
import os, torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = os.environ.get("MODEL", "Qwen/Qwen2.5-0.5B-Instruct")
dev = "cuda" if torch.cuda.is_available() else "cpu"
tok = AutoTokenizer.from_pretrained(MODEL)
lm = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16).eval().to(dev)

data = [("Loved it.", "positive"), ("Broke in a week.", "negative"),
        ("It's fine.", "neutral"), ("Best purchase ever!", "positive"),
        ("Waste of money.", "negative")]
shots = {
    "zero": "",
    "one":  "Text: 'Great!' -> positive\n",
    "few":  "Text: 'Great!' -> positive\nText: 'Awful.' -> negative\nText: 'Okay.' -> neutral\n",
}
def classify(prefix, text):
    p = f"{prefix}Reply with one word (positive/negative/neutral).\nText: '{text}' ->"
    ids = tok(p, return_tensors="pt").to(dev)
    out = lm.generate(**ids, max_new_tokens=3, do_sample=False, pad_token_id=tok.eos_token_id)
    return tok.decode(out[0][ids.input_ids.shape[1]:], skip_special_tokens=True).strip().lower()

for name, prefix in shots.items():
    acc = sum(classify(prefix, t).startswith(y) for t, y in data) / len(data)
    print(f"{name:4s}-shot accuracy = {acc:.2f}")
# Expected: few >= one >= zero.
