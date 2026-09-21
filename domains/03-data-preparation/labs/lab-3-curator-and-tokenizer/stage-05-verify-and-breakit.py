"""Stage 05 — verify fertility ordering + break-it with a tiny vocab (3.18)."""
from tokenizers import ByteLevelBPETokenizer

text = ("Distributed training of transformer language models on NVIDIA GPUs "
        "requires careful tokenization and vocabulary sizing decisions.")
n_words = len(text.split())

def fert(out):
    tk = ByteLevelBPETokenizer(f"{out}/vocab.json", f"{out}/merges.txt")
    return len(tk.encode(text).ids) / n_words

f8, f32 = fert("tok8k"), fert("tok32k")
assert f8 > f32, f"expected smaller-vocab higher fertility ({f8} vs {f32})"
print(f"[PASS] fertility tok8k={f8:.3f} > tok32k={f32:.3f}")

# --- break it: train a tiny vocab and watch fertility explode ---
import os
os.makedirs("tok300", exist_ok=True)
tk = ByteLevelBPETokenizer()
tk.train(files=["corpus.txt"], vocab_size=300, min_frequency=2)
tk.save_model("tok300")
tiny = ByteLevelBPETokenizer("tok300/vocab.json", "tok300/merges.txt")
MAX_SEQ = 64
n = len(tiny.encode(text).ids)
print(f"[BREAK-IT] vocab=300 fertility={n/n_words:.3f} tokens={n} "
      f"-> would truncate at max_seq_len={MAX_SEQ}? {n > MAX_SEQ}")
