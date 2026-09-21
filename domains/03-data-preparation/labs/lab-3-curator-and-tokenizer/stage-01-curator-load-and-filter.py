"""Stage 01 — heuristic quality filtering (3.07). Portable fallback for NeMo Curator."""
docs = [
    "NVIDIA GPUs accelerate large language model training and inference.",
    "!!!! $$$$ %%%% ^^^^ &&&&",                       # symbol junk
    "ok",                                             # too short
    "The transformer architecture uses self-attention over token sequences.",
    "buy now buy now buy now buy now buy now buy now",# repetition
]

def symbol_ratio(t):
    non_alnum = sum(not c.isalnum() and not c.isspace() for c in t)
    return non_alnum / max(len(t), 1)

def repeat_ratio(t):
    w = t.split()
    return 1 - len(set(w)) / max(len(w), 1)

def keep(t):
    return len(t.split()) >= 4 and symbol_ratio(t) < 0.3 and repeat_ratio(t) < 0.5

kept = [d for d in docs if keep(d)]
print(f"input={len(docs)} kept={len(kept)}")
for d in kept:
    print("  KEEP:", d)
# Expected: keeps the two informative sentences; drops junk/short/repeat.
