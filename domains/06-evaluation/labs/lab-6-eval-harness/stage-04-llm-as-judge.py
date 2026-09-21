"""Stage 04 — LLM-as-judge pairwise with order swap (6.06).

Uses a small local model as a toy judge; in production use a strong judge / NIM.
"""
import os, torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = os.environ.get("MODEL", "Qwen/Qwen2.5-0.5B-Instruct")
dev = "cuda" if torch.cuda.is_available() else "cpu"
tok = AutoTokenizer.from_pretrained(MODEL)
lm = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16).eval().to(dev)

q = "Explain why the sky is blue."
A = "Rayleigh scattering: shorter blue wavelengths scatter more in the atmosphere."
B = "Because it is."

def judge(first, second):
    prompt = (f"Question: {q}\nAnswer 1: {first}\nAnswer 2: {second}\n"
              "Which answer is better? Reply '1' or '2' only.\nBetter:")
    ids = tok(prompt, return_tensors="pt").to(dev)
    out = lm.generate(**ids, max_new_tokens=2, do_sample=False, pad_token_id=tok.eos_token_id)
    return tok.decode(out[0][ids.input_ids.shape[1]:], skip_special_tokens=True).strip()

print("order (A,B) ->", judge(A, B))
print("order (B,A) ->", judge(B, A))
print("If verdicts don't agree after swap, that's position bias (verse 6.06).")
