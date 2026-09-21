#!/usr/bin/env bash
set -euo pipefail
docker --version
docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi -L || \
  echo "GPU passthrough check failed — ensure nvidia-container-toolkit installed"
python -c "import tritonclient; print('tritonclient ok')" 2>/dev/null || \
  echo "pip install tritonclient[all]"
