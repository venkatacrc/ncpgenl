#!/usr/bin/env bash
set -euo pipefail
python -c "import torch;print('cuda',torch.cuda.is_available())"
python -c "import transformers;print('transformers',transformers.__version__)"
echo "Set MODEL env var, e.g.: export MODEL=Qwen/Qwen2.5-0.5B-Instruct"
