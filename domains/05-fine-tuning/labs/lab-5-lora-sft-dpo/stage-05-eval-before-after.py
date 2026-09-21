"""Stage 05 — evaluate base vs SFT adapter on held-out prompts (5.25)."""
import os, torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

MODEL = os.environ.get("MODEL", "Qwen/Qwen2.5-0.5B-Instruct")
tok = AutoTokenizer.from_pretrained(MODEL); tok.pad_token = tok.pad_token or tok.eos_token
held = [("Capital of France?", "paris"), ("2+2?", "4"), ("Opposite of hot?", "cold")]

def score(model):
    ok = 0
    for q, a in held:
        ids = tok(q, return_tensors="pt").to(model.device)
        out = model.generate(**ids, max_new_tokens=8, do_sample=False,
                             pad_token_id=tok.eos_token_id)
        txt = tok.decode(out[0][ids.input_ids.shape[1]:], skip_special_tokens=True).lower()
        ok += a in txt
    return ok / len(held)

base = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16).to("cuda")
print("base   score", score(base))
ft = PeftModel.from_pretrained(base, "adapter_sft").to("cuda")
print("sft-ft score", score(ft))
