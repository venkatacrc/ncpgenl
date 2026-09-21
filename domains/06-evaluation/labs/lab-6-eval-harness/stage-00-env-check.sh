#!/usr/bin/env bash
set -euo pipefail
python -c "import sacrebleu, rouge_score, nltk; print('metric libs ok')"
python -m nltk.downloader -q wordnet omw-1.4 punkt || true
python -c "import torch;print('cuda',torch.cuda.is_available())"
