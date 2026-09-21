"""Stage 02 — encoder embeddings: CLS vs masked mean pooling (verse 1.09)."""
import torch, torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel

dev = "cuda" if torch.cuda.is_available() else "cpu"
tok = AutoTokenizer.from_pretrained("bert-base-uncased")
enc = AutoModel.from_pretrained("bert-base-uncased").eval().to(dev)

sents = ["a cat sat on the mat", "a kitten rested on the rug", "quarterly revenue rose"]
b = tok(sents, padding=True, return_tensors="pt").to(dev)
with torch.no_grad():
    h = enc(**b).last_hidden_state
m = b.attention_mask.unsqueeze(-1)
mean_emb = (h * m).sum(1) / m.sum(1)          # masked mean pooling
cls_emb = h[:, 0, :]                          # [CLS]

def cos(a, b): return F.cosine_similarity(a, b, dim=-1).item()
print("mean-pool cos(cat,kitten) =", round(cos(mean_emb[0], mean_emb[1]), 3))
print("mean-pool cos(cat,revenue)=", round(cos(mean_emb[0], mean_emb[2]), 3))
print("CLS      cos(cat,kitten)  =", round(cos(cls_emb[0], cls_emb[1]), 3))
# Expected: mean-pool related > unrelated by ~0.1-0.4; CLS noisier (untuned).
