# Bare `docker run` Path (mirrored for every lab)

Every lab has a Kubernetes path *and* this bare-metal path. No orchestration needed.

## Standard interactive dev container
```bash
docker run --gpus all -it --rm \
  --shm-size=16g --ulimit memlock=-1 --ulimit stack=67108864 \
  -v "$PWD":/work -w /work \
  nvcr.io/nvidia/pytorch:24.07-py3 bash
# inside:
pip install "transformers>=4.44" "accelerate>=0.33" datasets evaluate
```

## Multi-GPU (single node, 1–4 GPUs; no NVSwitch assumed)
```bash
# pick specific GPUs
docker run --gpus '"device=0,1"' -it --rm --shm-size=16g \
  -v "$PWD":/work -w /work nvcr.io/nvidia/pytorch:24.07-py3 bash
# launch distributed job inside
torchrun --standalone --nproc_per_node=2 stage-01-ddp-train.py
```

## Serving container (Dynamo-Triton)
```bash
docker run --gpus all --rm -p 8000:8000 -p 8001:8001 -p 8002:8002 \
  -v "$PWD/model_repo":/models \
  nvcr.io/nvidia/tritonserver:24.07-py3 \
  tritonserver --model-repository=/models
# 8000 HTTP | 8001 gRPC | 8002 Prometheus metrics
```

## Flags that matter for LLM labs
- `--shm-size=16g` — DataLoader workers / NCCL shared memory; too small → hangs.
- `--ulimit memlock=-1` — pinned memory for fast H2D copies and NCCL.
- `--gpus '"device=0,1"'` — quote form required to pin specific devices.
- `-p 8002:8002` — Triton Prometheus metrics endpoint (Lab 9).
