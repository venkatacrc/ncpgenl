# Walk & Recall — WR-8a (verses 8.01–8.09)

- **Cue:** *"Cost profile by model type?"* → Encoder = one pass, cheapest; decoder =
  prefill + serial decode + KV cache; enc-dec = both stacks + cross-attention, most
  expensive (8.01).
- **Cue (symptom):** *"First token is slow but per-token is fine (or vice versa) — recite
  the phase chain."* → Prefill (parallel, compute-bound) sets TTFT; decode (serial,
  memory-bound) sets TPOT; latency ≈ TTFT + (out−1)·TPOT (8.02). Bigger batch raises
  throughput but per-request latency; decode is memory-bound so batching is near-free on
  compute (8.03).
- **Cue (symptom):** *"Throughput is low because short requests wait behind long ones —
  recite the batching chain."* → Containerize preprocess→model→postprocess (8.04) from
  NGC images + model repo (8.05) on Dynamo-Triton (renamed from Triton) with config.pbtxt
  (8.06). Dynamic batching waits for the whole batch to finish (good for encoders) (8.07);
  continuous/in-flight batching frees a slot per finished sequence at the token level
  (8.08) — that fixes the symptom; LLM generation → continuous, fixed-shape → dynamic
  (8.09).

**Three most likely to be forgotten:** 8.02 TTFT=prefill vs TPOT=decode; 8.08 continuous
batching works at the *token/iteration* level; 8.06 Triton→Dynamo-Triton rename.
