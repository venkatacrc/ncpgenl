#!/usr/bin/env bash
set -euo pipefail
curl -s localhost:8002/metrics | head -n 3 || echo "start Lab 8 server first (metrics :8002)"
python -c "import numpy, requests; print('deps ok')"
