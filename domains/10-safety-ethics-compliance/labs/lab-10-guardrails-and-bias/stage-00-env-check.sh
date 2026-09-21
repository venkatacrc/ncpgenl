#!/usr/bin/env bash
set -euo pipefail
python -c "import nemoguardrails; print('nemoguardrails', nemoguardrails.__version__)" \
  || echo "pip install nemoguardrails (VERIFY Colang 1.0 vs 2.0 syntax)"
python -c "import numpy; print('numpy ok')"
