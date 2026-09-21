#!/usr/bin/env bash
set -euo pipefail
python - <<'PY'
import torch
cc = torch.cuda.get_device_capability(0)
print("compute capability", cc, torch.cuda.get_device_name(0))
if cc[0] >= 10:
    print("NVFP4 path AVAILABLE (Blackwell/GB200) -> use stage-03c; FP8/INT8 also work")
elif cc[0] >= 9:
    print("FP8 path AVAILABLE -> use stage-03a (H100-ONLY)")
else:
    print("FP8/NVFP4 NOT available -> use stage-03b INT8 fallback (A100-OK)")
PY
python -c "import tensorrt_llm; print('trt-llm', tensorrt_llm.__version__)" 2>/dev/null \
  || echo "tensorrt_llm not importable — run inside the TRT-LLM container (VERIFY tag)"
