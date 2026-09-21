"""Stage 01 — load a small instruct model and render its chat template (2.01)."""
import os, torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = os.environ.get("MODEL", "Qwen/Qwen2.5-0.5B-Instruct")
tok = AutoTokenizer.from_pretrained(MODEL)
lm = AutoModelForCausalLM.from_pretrained(
    MODEL, torch_dtype=torch.bfloat16).eval().to("cuda" if torch.cuda.is_available() else "cpu")

msgs = [{"role": "system", "content": "You are terse."},
        {"role": "user", "content": "Say hi in one word."}]
prompt = tok.apply_chat_template(msgs, add_generation_prompt=True, tokenize=False)
print("---- rendered chat template ----")
print(prompt)
