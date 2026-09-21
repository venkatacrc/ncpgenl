"""Stage 04b [H100-ONLY] — one FP8 training step via Transformer Engine (7.13).

A100 fallback: this script detects non-Hopper and runs the same layer in BF16 instead,
demonstrating the identical mixed-precision concept without FP8 units.
"""
import torch

cc = torch.cuda.get_device_capability(0)
x = torch.randn(8, 512, 1024, device="cuda")

if cc[0] >= 9:
    import transformer_engine.pytorch as te
    from transformer_engine.common.recipe import DelayedScaling, Format
    layer = te.Linear(1024, 1024).cuda()
    recipe = DelayedScaling(fp8_format=Format.HYBRID)   # E4M3 fwd / E5M2 bwd
    with te.fp8_autocast(enabled=True, fp8_recipe=recipe):
        y = layer(x)
    print("[H100] FP8 forward ok, out", tuple(y.shape))
else:
    layer = torch.nn.Linear(1024, 1024).cuda()
    with torch.autocast("cuda", dtype=torch.bfloat16):
        y = layer(x)
    print("[A100 fallback] BF16 forward ok (same mixed-precision concept), out", tuple(y.shape))
