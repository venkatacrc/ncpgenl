"""Stage 04 — compare fertility (tokens/word) across vocab sizes (3.17, 3.18)."""
from tokenizers import ByteLevelBPETokenizer

text = ("Distributed training of transformer language models on NVIDIA GPUs "
        "requires careful tokenization and vocabulary sizing decisions.")
n_words = len(text.split())

for out in ["tok8k", "tok32k"]:
    tk = ByteLevelBPETokenizer(f"{out}/vocab.json", f"{out}/merges.txt")
    n_tok = len(tk.encode(text).ids)
    print(f"{out}: tokens={n_tok} fertility={n_tok / n_words:.3f}")
# Expected: tok8k fertility > tok32k fertility (smaller vocab => more tokens/word).
