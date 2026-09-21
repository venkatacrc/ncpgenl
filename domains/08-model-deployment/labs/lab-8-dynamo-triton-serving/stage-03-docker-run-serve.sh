#!/usr/bin/env bash
# Stage 03 — serve the model repo with Dynamo-Triton via bare docker run (8.16).
set -euo pipefail
docker run --gpus all --rm -d --name triton8 \
  -p 8000:8000 -p 8001:8001 -p 8002:8002 \
  -v "$PWD/model_repo":/models \
  nvcr.io/nvidia/tritonserver:24.07-py3 \
  tritonserver --model-repository=/models

echo "waiting for READY..."
for i in $(seq 1 30); do
  if curl -s localhost:8000/v2/health/ready >/dev/null; then echo "READY"; break; fi
  sleep 2
done
curl -s localhost:8000/v2/health/ready -o /dev/null -w "health: %{http_code}\n"
echo "metrics sample:"; curl -s localhost:8002/metrics | head -n 5
# stop with: docker stop triton8
