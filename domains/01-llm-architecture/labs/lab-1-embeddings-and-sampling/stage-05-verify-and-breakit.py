"""Stage 05 — verify asserts + break-it (temperature=0 undefined; verse 1.11)."""
import torch, torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel, AutoModelForCausalLM

dev = "cuda" if torch.cuda.is_available() else "cpu"

# --- verify 1: decoder left-pad embeddings are non-degenerate ---
tok = AutoTokenizer.from_pretrained("gpt2"); tok.padding_side = "left"; tok.pad_token = tok.eos_token
dec = AutoModel.from_pretrained("gpt2").eval().to(dev)
b = tok(["a cat sat", "quarterly revenue rose sharply"], padding=True, return_tensors="pt").to(dev)
with torch.no_grad():
    e = dec(**b).last_hidden_state[:, -1, :]
sim = F.cosine_similarity(e[0], e[1], dim=-1).item()
assert sim < 0.99, f"left-pad embeddings degenerate (sim={sim})"
print(f"[PASS] left-pad decoder embeddings non-degenerate (sim={sim:.3f})")

# --- break it: temperature=0 with sampling ---
tok2 = AutoTokenizer.from_pretrained("gpt2"); tok2.pad_token = tok2.eos_token
lm = AutoModelForCausalLM.from_pretrained("gpt2").eval().to(dev)
ids = tok2("Hello", return_tensors="pt").to(dev)
try:
    lm.generate(**ids, max_new_tokens=5, do_sample=True, temperature=0.0,
                pad_token_id=tok2.eos_token_id)
    print("[BREAK-IT] temperature=0 did not error -> framework fell back to greedy")
except Exception as ex:
    print(f"[BREAK-IT] temperature=0 raised: {type(ex).__name__} (z/0 undefined)")
