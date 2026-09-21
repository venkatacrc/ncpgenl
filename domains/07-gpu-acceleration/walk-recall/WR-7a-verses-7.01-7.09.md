# Walk & Recall — WR-7a (verses 7.01–7.09)

- **Cue:** *"Recite the parallelism axes."* → Data (replicate, split batch), tensor
  (split a layer's matrices), pipeline (split layers into stages), sequence (split
  tokens), expert (split MoE experts) (7.01). DDP all-reduces gradients via NCCL ring,
  needs whole model per GPU (7.02); FSDP/ZeRO shards optimizer→grads→params, all-gather
  just-in-time (7.03).
- **Cue (symptom):** *"A single layer doesn't fit on one GPU — recite the split chain
  and its constraint."* → Tensor parallel splits matrices intra-layer with per-layer
  all-reduce; high comm → keep within a node/NVLink (7.04). Pipeline splits across
  layers, micro-batches shrink the bubble ≈(p−1)/(m+p−1), low comm, cross-node (7.05);
  sequence parallel shards tokens for long context (7.06); expert parallel does
  all-to-all with load-balancing loss (7.07).
- **Cue:** *"Choose a parallelism strategy?"* → Fits+speed→DDP; memory→FSDP; layer too
  big→TP (NVLink); model too big→PP (cross-node); long seq→SP; MoE→EP (7.08); large runs
  compose TP×PP×DP mapped to topology (7.09).

**Three most likely to be forgotten:** 7.03 ZeRO stages (opt→grad→param); 7.04 keep TP
intra-node (NVLink); 7.05 pipeline bubble formula (micro-batches shrink it).
