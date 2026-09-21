"""Stage 04 — sampling explorer: distinct-2 diversity across methods (1.11-1.12)."""
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

dev = "cuda" if torch.cuda.is_available() else "cpu"
tok = AutoTokenizer.from_pretrained("gpt2"); tok.pad_token = tok.eos_token
lm = AutoModelForCausalLM.from_pretrained("gpt2").eval().to(dev)
ids = tok("The future of AI infrastructure is", return_tensors="pt").to(dev)

def distinct2(text):
    t = tok.tokenize(text); bg = list(zip(t, t[1:]))
    return round(len(set(bg)) / max(len(bg), 1), 3)

configs = {
    "greedy":   dict(do_sample=False),
    "beam5":    dict(do_sample=False, num_beams=5),
    "temp0.3":  dict(do_sample=True, temperature=0.3, top_k=0),
    "temp1.5":  dict(do_sample=True, temperature=1.5, top_k=0),
    "top_k50":  dict(do_sample=True, top_k=50),
    "top_p0.9": dict(do_sample=True, top_p=0.9, top_k=0),
}
torch.manual_seed(0)
for name, cfg in configs.items():
    out = lm.generate(**ids, max_new_tokens=40, pad_token_id=tok.eos_token_id, **cfg)
    txt = tok.decode(out[0][ids.input_ids.shape[1]:], skip_special_tokens=True)
    print(f"{name:9s} distinct2={distinct2(txt)}  :: {txt[:70]!r}")
# Expected: greedy/beam5 lowest distinct2; temp1.5 highest; top_p0.9 balanced.
