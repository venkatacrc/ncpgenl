"""Stage 05 — perplexity delta: quantized vs FP16 baseline (4.02, measure trade-off).

Portable proxy using HF (bitsandbytes int8) so it runs without a built TRT engine;
the concept (accuracy delta from quantization) matches the engine path.
"""
import os, torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset

MODEL = os.environ.get("MODEL", "TinyLlama/TinyLlama-1.1B-Chat-v1.0")
tok = AutoTokenizer.from_pretrained(MODEL)
texts = [r["text"] for r in load_dataset("wikitext", "wikitext-2-raw-v1", split="test")
         if len(r["text"].strip()) > 200][:32]

def perplexity(model):
    model.eval(); nll, ntok = 0.0, 0
    for t in texts:
        ids = tok(t, return_tensors="pt", truncation=True, max_length=512).to(model.device)
        with torch.no_grad():
            out = model(**ids, labels=ids.input_ids)
        n = ids.input_ids.numel()
        nll += out.loss.item() * n; ntok += n
    return float(torch.exp(torch.tensor(nll / ntok)))

fp16 = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.float16, device_map="cuda")
ppl_fp16 = perplexity(fp16); del fp16; torch.cuda.empty_cache()
int8 = AutoModelForCausalLM.from_pretrained(MODEL, load_in_8bit=True, device_map="cuda")
ppl_int8 = perplexity(int8)
print(f"perplexity fp16={ppl_fp16:.3f} int8={ppl_int8:.3f} delta={ppl_int8-ppl_fp16:+.3f}")
# Expected: small positive delta with good calibration.
