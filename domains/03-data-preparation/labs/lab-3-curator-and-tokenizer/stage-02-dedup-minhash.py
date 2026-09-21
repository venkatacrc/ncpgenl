"""Stage 02 — fuzzy dedup via MinHash Jaccard estimate (3.08), no external deps."""
import random

def shingles(t, k=3):
    w = t.lower().split()
    return {" ".join(w[i:i+k]) for i in range(max(len(w)-k+1, 1))}

def minhash(sig_set, n=64, seed=1):
    rnd = random.Random(seed)
    salts = [rnd.randrange(1 << 32) for _ in range(n)]
    return [min((hash(s) ^ salt) & 0xFFFFFFFF for s in sig_set) for salt in salts]

def est_jaccard(a, b):
    return sum(x == y for x, y in zip(a, b)) / len(a)

docs = [
    "the quick brown fox jumps over the lazy dog",
    "the quick brown fox jumped over the lazy dog",   # near-duplicate
    "distributed training scales across many gpus",
]
sigs = [minhash(shingles(d)) for d in docs]
kept, seen = [], []
for i, d in enumerate(docs):
    if any(est_jaccard(sigs[i], sigs[j]) > 0.5 for j in seen):
        print(f"  DROP near-dup: {d!r}")
    else:
        seen.append(i); kept.append(d)
print(f"kept {len(kept)} of {len(docs)}")
