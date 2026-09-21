"""Stage 06 — force OOM, then fix with accumulation + checkpointing (7.20)."""
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

dev = "cuda"
tok = AutoTokenizer.from_pretrained("gpt2"); tok.pad_token = tok.eos_token

def try_big_batch(batch_size, seq_len, checkpoint=False):
    torch.cuda.empty_cache(); torch.cuda.reset_peak_memory_stats()
    m = AutoModelForCausalLM.from_pretrained("gpt2").to(dev)
    if checkpoint:
        m.gradient_checkpointing_enable(); m.config.use_cache = False
    opt = torch.optim.AdamW(m.parameters(), lr=5e-5)
    ids = torch.randint(0, 50257, (batch_size, seq_len), device=dev)
    try:
        loss = m(input_ids=ids, labels=ids).loss
        loss.backward(); opt.step()
        return f"OK peak {torch.cuda.max_memory_allocated(dev)/1e9:.2f}GB"
    except torch.cuda.OutOfMemoryError:
        return "CUDA OOM"

print("[BREAK-IT] big batch, no checkpointing:", try_big_batch(64, 1024, checkpoint=False))
print("[FIX] smaller micro-batch + checkpointing:", try_big_batch(4, 1024, checkpoint=True))
print("(Use gradient accumulation to recover the effective batch — see stage-03.)")
