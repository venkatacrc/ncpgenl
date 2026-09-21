#!/usr/bin/env bash
set -euo pipefail
nvidia-smi --query-gpu=name,memory.total --format=csv
python -c "import torch;print('cuda',torch.cuda.is_available(), torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'cpu')"
python -c "import transformers;print('transformers',transformers.__version__)"
