#!/usr/bin/env bash
set -euo pipefail
python -c "import peft, trl, transformers; print('peft',peft.__version__,'trl',trl.__version__)"
python -c "import torch;print('cuda',torch.cuda.is_available())"
echo "export MODEL=Qwen/Qwen2.5-0.5B-Instruct (default)"
