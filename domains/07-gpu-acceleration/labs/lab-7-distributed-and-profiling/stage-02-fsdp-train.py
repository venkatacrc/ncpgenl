"""Stage 02 — FSDP training (7.03); shards params/grads/optimizer. Launch w/ torchrun."""
import os, functools, torch, torch.distributed as dist
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
from torch.distributed.fsdp.wrap import transformer_auto_wrap_policy
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.models.gpt2.modeling_gpt2 import GPT2Block

def main():
    dist.init_process_group("nccl")
    rank = dist.get_rank(); local = int(os.environ["LOCAL_RANK"])
    torch.cuda.set_device(local)
    tok = AutoTokenizer.from_pretrained("gpt2"); tok.pad_token = tok.eos_token
    model = AutoModelForCausalLM.from_pretrained("gpt2").to(local)
    policy = functools.partial(transformer_auto_wrap_policy, transformer_layer_cls={GPT2Block})
    model = FSDP(model, auto_wrap_policy=policy, device_id=local)
    opt = torch.optim.AdamW(model.parameters(), lr=5e-5)
    batch = tok(["fully sharded data parallel"] * 4, return_tensors="pt", padding=True).to(local)
    for step in range(5):
        loss = model(**batch, labels=batch.input_ids).loss
        loss.backward(); opt.step(); opt.zero_grad()
        if rank == 0:
            mem = torch.cuda.max_memory_allocated(local) / 1e9
            print(f"step {step} loss {loss.item():.4f} peak_mem {mem:.2f}GB")
    dist.destroy_process_group()

if __name__ == "__main__":
    main()
