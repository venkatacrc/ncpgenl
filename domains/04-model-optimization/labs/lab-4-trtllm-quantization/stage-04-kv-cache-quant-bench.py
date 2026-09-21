"""Stage 04 — compute KV-cache memory and show quantization halving it (4.16, 4.26)."""

def kv_bytes_per_token(n_layers, n_kv_heads, head_dim, bytes_per_elt):
    return 2 * n_layers * n_kv_heads * head_dim * bytes_per_elt   # 2 = K + V

# TinyLlama-ish config; adjust to your model.
cfg = dict(n_layers=22, n_kv_heads=4, head_dim=64)
seq, batch = 4096, 8

for dtype, b in [("fp16", 2), ("int8/fp8", 1)]:
    per_tok = kv_bytes_per_token(**cfg, bytes_per_elt=b)
    total_gb = per_tok * seq * batch / 1e9
    print(f"KV dtype={dtype:9s} per-token={per_tok} B  total(seq={seq},batch={batch})={total_gb:.2f} GB")
# Expected: int8/fp8 total is ~half of fp16 total.
