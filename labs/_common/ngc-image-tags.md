# Pinned NGC / Container Image Tags Used by Labs

> **VERIFY** every tag against the current NGC catalog before a lab run — NVIDIA
> rotates these monthly and deprecates old ones. The "Verify" column flags the
> highest-churn items.

| Purpose | Image (example pin) | Used by | Verify |
|---------|---------------------|---------|--------|
| General PyTorch + CUDA | `nvcr.io/nvidia/pytorch:24.07-py3` | Labs 1,2,3,5,6,7 | tag month |
| TensorRT-LLM | `nvcr.io/nvidia/tritonserver:24.07-trtllm-python-py3` | Lab 4, 8 | **name+tag churn** |
| Triton / Dynamo-Triton | `nvcr.io/nvidia/tritonserver:24.07-py3` | Lab 8, 9 | **"Dynamo-Triton" rename** |
| NeMo framework | `nvcr.io/nvidia/nemo:24.07` | Labs 3, 5 (optional) | **NeMo 2.0 API churn** |
| NeMo Curator | `nvcr.io/nvidia/nemo:24.07` (curator module) | Lab 3 | module path may move |
| NeMo Guardrails | `pip install nemoguardrails` in pytorch img | Lab 10 | Colang 1.0 vs 2.0 |
| Prometheus/Grafana | `prom/prometheus`, `grafana/grafana` (Docker Hub) | Lab 9 | stable |

## Notes on churn (stale-knowledge flags)
- **Dynamo-Triton**: the study guide renames *Triton Inference Server* → *Dynamo-Triton*.
  The container is still published as `tritonserver` and the binary is still
  `tritonserver`. Expect the exam to use the new product name.
- **TensorRT-LLM**: the checkpoint-convert → `trtllm-build` → engine flow and flag
  names change frequently. Treat any exact flag here as "verify."
- **NeMo**: 24.07 references in the guide predate NeMo 2.0. Configs/recipe APIs
  (`nemo run`, Megatron-Core integration) have changed. Verify before memorizing.
- **NVFP4 / Blackwell FP4 (GB200)**: runnable on Blackwell (`sm_100`) via Lab 4
  `stage-03c` — requires a **recent CUDA ≥ 12.6 / Blackwell-enabled** container image and
  a TensorRT-LLM/ModelOpt build with NVFP4 support (the pinned 24.07 tags above predate
  it — pull a newer `tritonserver:*-trtllm` / `pytorch` tag). Naming (NVFP4 vs MXFP4) and
  quant flags are new and unstable — VERIFY.
