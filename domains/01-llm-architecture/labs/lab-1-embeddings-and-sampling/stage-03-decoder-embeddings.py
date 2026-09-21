"""Stage 03 — decoder embeddings; left vs right padding (verse 1.10)."""
import torch, torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel

dev = "cuda" if torch.cuda.is_available() else "cpu"
sents = ["a cat sat", "a dog ran across the yard today"]

def last_token_emb(padding_side):
    tok = AutoTokenizer.from_pretrained("gpt2"); tok.padding_side = padding_side
    tok.pad_token = tok.eos_token
    dec = AutoModel.from_pretrained("gpt2").eval().to(dev)
    b = tok(sents, padding=True, return_tensors="pt").to(dev)
    with torch.no_grad():
        h = dec(**b).last_hidden_state
    return h[:, -1, :]

for side in ["left", "right"]:
    e = last_token_emb(side)
    sim = F.cosine_similarity(e[0], e[1], dim=-1).item()
    print(f"padding_side={side:5s} cos(sent0,sent1) = {sim:.4f}")
# Expected: left ~meaningful (<0.99); right ~degenerate (>0.99, reading pad vectors).
