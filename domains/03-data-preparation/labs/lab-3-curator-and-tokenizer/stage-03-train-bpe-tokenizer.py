"""Stage 03 — train byte-level BPE tokenizers at two vocab sizes (3.14, 3.17)."""
import os
from datasets import load_dataset
from tokenizers import ByteLevelBPETokenizer

os.makedirs("tok8k", exist_ok=True); os.makedirs("tok32k", exist_ok=True)
# small openly available text corpus
ds = load_dataset("wikitext", "wikitext-2-raw-v1", split="train")
with open("corpus.txt", "w") as f:
    for row in ds:
        t = row["text"].strip()
        if t:
            f.write(t + "\n")

for vocab, out in [(8000, "tok8k"), (32000, "tok32k")]:
    tk = ByteLevelBPETokenizer()
    tk.train(files=["corpus.txt"], vocab_size=vocab, min_frequency=2,
             special_tokens=["<pad>", "<bos>", "<eos>", "<unk>"])
    tk.save_model(out)
    print(f"trained vocab={vocab} -> {out}")
