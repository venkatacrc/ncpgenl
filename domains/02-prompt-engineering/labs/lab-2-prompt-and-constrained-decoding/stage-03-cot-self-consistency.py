"""Stage 03 — CoT + self-consistency majority vote (2.06-2.08)."""
import os, re, collections, torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = os.environ.get("MODEL", "Qwen/Qwen2.5-0.5B-Instruct")
dev = "cuda" if torch.cuda.is_available() else "cpu"
tok = AutoTokenizer.from_pretrained(MODEL)
lm = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16).eval().to(dev)

q = ("A shelf has 3 boxes of 12 items and 2 boxes of 5 items. "
     "Think step by step, then output 'Answer: <n>'.")
ids = tok(q, return_tensors="pt").to(dev)

def extract(txt):
    m = re.findall(r"Answer:\s*(\d+)", txt)
    return m[-1] if m else None

# single greedy CoT
g = lm.generate(**ids, max_new_tokens=120, do_sample=False, pad_token_id=tok.eos_token_id)
single = extract(tok.decode(g[0][ids.input_ids.shape[1]:], skip_special_tokens=True))

# self-consistency: 8 sampled traces, majority vote
votes = []
torch.manual_seed(0)
for _ in range(8):
    s = lm.generate(**ids, max_new_tokens=120, do_sample=True, temperature=0.7,
                    top_p=0.9, pad_token_id=tok.eos_token_id)
    votes.append(extract(tok.decode(s[0][ids.input_ids.shape[1]:], skip_special_tokens=True)))
votes = [v for v in votes if v]
sc = collections.Counter(votes).most_common(1)[0][0] if votes else None
print(f"single CoT = {single} | self-consistency (n=8) = {sc} | truth = 46")
