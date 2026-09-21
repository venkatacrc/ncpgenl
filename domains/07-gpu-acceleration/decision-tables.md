# Decision Tables — GPU Acceleration

## Parallelism selection

| Situation | Strategy | Comm | Placement |
|---|---|---|---|
| Fits 1 GPU, want speed | DDP | all-reduce grads | any |
| Optimizer/grad too big | FSDP/ZeRO | all-gather | any |
| Single layer too big | Tensor Parallel | all-reduce/layer (high) | **intra-node NVLink** |
| Model too big for node | Pipeline Parallel | stage boundaries (low) | cross-node |
| Long sequences | Sequence Parallel (+TP) | moderate | intra-node |
| MoE | Expert Parallel | all-to-all | topology-aware |

## Precision (training)

| Format | Loss scaling? | Use | Hardware |
|---|---|---|---|
| BF16 | no | default LLM training | Ampere+ |
| FP16 | **yes** | legacy/where required | all |
| FP8 (TE) | recipe scaling | fastest, H100 | **Hopper+** |
| TF32 | n/a | matmul accel | Ampere+ |

## Profiler division of labor

| Tool | Scope | Answers | Command |
|---|---|---|---|
| Nsight Systems | system timeline | **where** time goes | `nsys profile` |
| Nsight Compute | single kernel | **why** kernel slow | `ncu --set full` |

## Bottleneck → fix

| Symptom | Class | Fix |
|---|---|---|
| GPU idle, CPU busy | data loading | more workers, prefetch, packing |
| GPU idle, waiting NCCL | comm-bound | overlap, TP on NVLink, larger buffers |
| Low FLOP/s, low intensity | memory-bound (decode) | weight-only quant, fusion |
| Low FLOP/s, high intensity | compute-bound (prefill) | FP8/INT8, Tensor Cores |
| Many tiny kernels | launch-bound | CUDA graphs / torch.compile |
| OOM | memory | accum, checkpoint, FSDP, lower precision |
