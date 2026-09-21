#!/usr/bin/env bash
# Shared environment probe for all labs. Run before any lab stage-00.
set -euo pipefail

echo "== GPU inventory =="
nvidia-smi --query-gpu=index,name,memory.total,compute_cap --format=csv || {
  echo "nvidia-smi not found — are you inside the container with --gpus all?"; exit 1; }

echo "== Driver / CUDA =="
nvidia-smi | grep -E "Driver Version|CUDA Version" || true

echo "== Container runtime =="
python - <<'PY'
import torch
print("torch", torch.__version__, "| cuda", torch.version.cuda)
print("cuda available:", torch.cuda.is_available())
if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        p = torch.cuda.get_device_properties(i)
        print(f"  gpu{i}: {p.name} cc{p.major}.{p.minor} {p.total_memory/1e9:.1f}GB")
PY

echo "== Precision capability hint =="
python - <<'PY'
import torch
if torch.cuda.is_available():
    cc = torch.cuda.get_device_capability(0)
    fp8 = cc[0] >= 9         # Hopper (sm_90) and later
    fp4 = cc[0] >= 10        # Blackwell (sm_100, e.g. GB200) and later
    tier = "GB200/Blackwell [FP4/NVFP4 + 2nd-gen TE]" if fp4 else \
           ("H100/Hopper [FP8]" if fp8 else "A100/Ampere [INT8/BF16 fallback]")
    print(f"compute capability {cc} | tier: {tier}")
    print(f"  FP8 path: {'YES' if fp8 else 'NO'} | NVFP4 path: {'YES [GB200-OK]' if fp4 else 'NO -> fall back to FP8/INT8'}")
PY
