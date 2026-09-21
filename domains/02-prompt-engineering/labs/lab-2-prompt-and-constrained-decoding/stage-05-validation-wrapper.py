"""Stage 05 — LLM-wrapping module: build -> generate -> validate -> retry (2.20)."""
import os, json, torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = os.environ.get("MODEL", "Qwen/Qwen2.5-0.5B-Instruct")
dev = "cuda" if torch.cuda.is_available() else "cpu"
tok = AutoTokenizer.from_pretrained(MODEL)
lm = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16).eval().to(dev)

def validate(text, keys=("intent", "confidence")):
    try:
        obj = json.loads(text[text.find("{"): text.rfind("}") + 1])
        return all(k in obj for k in keys), obj
    except Exception:
        return False, None

def call(user_text, retries=3):
    prompt = ('Return ONLY JSON {"intent": string, "confidence": number}. '
              f'Text: "{user_text}".')
    ids = tok(prompt, return_tensors="pt").to(dev)
    for attempt in range(retries + 1):
        temp = 0.2 + 0.3 * attempt
        out = lm.generate(**ids, max_new_tokens=40, do_sample=temp > 0,
                          temperature=max(temp, 1e-3), pad_token_id=tok.eos_token_id)
        txt = tok.decode(out[0][ids.input_ids.shape[1]:], skip_special_tokens=True)
        ok, obj = validate(txt)
        if ok:
            print(f"[ok attempt {attempt}] {obj}"); return obj
    raise ValueError("validation failed after retries")

call("cancel my subscription")
