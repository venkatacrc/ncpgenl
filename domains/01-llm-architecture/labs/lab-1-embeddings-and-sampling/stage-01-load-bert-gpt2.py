"""Stage 01 — load BERT (encoder) and GPT-2 (decoder); print param counts."""
from transformers import AutoModel

for name in ["bert-base-uncased", "gpt2"]:
    m = AutoModel.from_pretrained(name)
    n = sum(p.numel() for p in m.parameters())
    print(f"{name:20s} params = {n/1e6:6.1f}M")
# Expected: bert-base-uncased ~110.0M | gpt2 ~124.4M
