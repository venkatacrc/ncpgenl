# Lab 8 — Dynamo-Triton Serving & Batching  `[A100-OK]`

**Objective:** Build a model repository, serve via `docker run` (and a K8s manifest),
enable dynamic batching, benchmark throughput vs concurrency, and reproduce batching
starvation. Covers 8.2, 8.3.

**Tag:** `[A100-OK]` (any GPU; small model).

**Prerequisites:** Docker + `--gpus`, Dynamo-Triton container, `pip install
tritonclient[all]`. Optional TRT-LLM backend for continuous batching.

**Container (VERIFY):** `nvcr.io/nvidia/tritonserver:24.07-py3`

## Stages
| Stage | File | Verifies |
|-------|------|----------|
| 00 | `stage-00-env-check.sh` | docker + gpu |
| 01 | `stage-01-build-model-repo.py` | model_repo/ + config.pbtxt created |
| 02 | `stage-02-config-pbtxt-dynamic-batch.sh` | dynamic batching + instances set |
| 03 | `stage-03-docker-run-serve.sh` | server READY on 8000/8001/8002 |
| 04 | `stage-04-k8s-deploy.yaml` | Deployment + readiness probe (apply optional) |
| 05 | `stage-05-batching-benchmark.py` | throughput rises with concurrency |
| 06 | `stage-06-verify-and-breakit.py` | starvation when concurrency ≫ instances |

## Expected metrics
- Health `/v2/health/ready` returns 200; metrics on 8002.
- Throughput increases with concurrency until instances/batch saturate, then plateaus.
- p99 latency climbs sharply past saturation.

## Break it on purpose
Set `instance_group count=1` + small `max_batch_size`, then drive concurrency to 64 →
queue depth and p99 latency explode (batching starvation), the symptom in verse 8.09.
