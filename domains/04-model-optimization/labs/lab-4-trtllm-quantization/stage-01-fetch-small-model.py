"""Stage 01 — fetch a small open model for quantization."""
import os
from huggingface_hub import snapshot_download

MODEL = os.environ.get("MODEL", "TinyLlama/TinyLlama-1.1B-Chat-v1.0")
path = snapshot_download(MODEL, local_dir="hf_model")
print("downloaded to", path)
