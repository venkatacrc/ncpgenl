#!/usr/bin/env bash
set -euo pipefail
python -c "import tokenizers;print('tokenizers',tokenizers.__version__)"
python - <<'PY'
try:
    import cudf; print("cudf available (GPU EDA path)")
except Exception:
    print("cudf not present -> using pandas/pure-python fallback")
PY
