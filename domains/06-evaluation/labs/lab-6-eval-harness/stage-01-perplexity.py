"""Stage 01 — perplexity on held-out text (6.01)."""
import os, torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset

MODEL = os.environ.get("MODEL", "gpt2")
dev = "cuda" if torch.cuda.is_available() else "cpu"
tok = AutoTokenizer.from_pretrained(MODEL)
m = AutoModelForCausalLM.from_pretrained(MODEL).eval().to(dev)

texts = [r["text"] for r in load_dataset("wikitext", "wikitext-2-raw-v1", split="test")
         if len(r["text"].strip()) > 200][:16]
nll, ntok = 0.0, 0
for t in texts:
    ids = tok(t, return_tensors="pt", truncation=True, max_length=512).to(dev)
    with torch.no_grad():
        loss = m(**ids, labels=ids.input_ids).loss
    n = ids.input_ids.numel(); nll += loss.item() * n; ntok += n
print(f"perplexity = {torch.exp(torch.tensor(nll/ntok)):.2f}")
