#!/usr/bin/env bash
set -euo pipefail
python -c "import torch;print('gpus',torch.cuda.device_count())"
command -v nsys >/dev/null && echo "nsys present" || echo "nsys MISSING (use profiling container)"
command -v ncu  >/dev/null && echo "ncu present"  || echo "ncu MISSING"
python - <<'PY'
import torch
cc = torch.cuda.get_device_capability(0)
if cc[0] >= 10:
    print("GB200/Blackwell: FP4 (NVFP4) + 2nd-gen TE available (stage-04b runs FP8/FP4)")
elif cc[0] >= 9:
    print("H100/Hopper: FP8 branch (stage-04b) available")
else:
    print("A100/Ampere: no FP8/FP4 -> use BF16 fallback")
PY
