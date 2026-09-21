"""Stage 01 — build a minimal Triton model repository with a Python backend model.

A tiny 'echo-scale' model stands in for an LLM so the batching mechanics are the focus
and the lab runs anywhere. Swap the backend for tensorrtllm/vllm in production.
"""
import os, textwrap

root = "model_repo/toy/1"
os.makedirs(root, exist_ok=True)

with open("model_repo/toy/config.pbtxt", "w") as f:
    f.write(textwrap.dedent('''
    name: "toy"
    backend: "python"
    max_batch_size: 16
    input  [ { name: "IN0"  data_type: TYPE_FP32 dims: [ 4 ] } ]
    output [ { name: "OUT0" data_type: TYPE_FP32 dims: [ 4 ] } ]
    instance_group [ { count: 2 kind: KIND_GPU } ]
    dynamic_batching { max_queue_delay_microseconds: 1000 }
    ''').strip())

with open(f"{root}/model.py", "w") as f:
    f.write(textwrap.dedent('''
    import time, numpy as np, triton_python_backend_utils as pb_utils
    class TritonPythonModel:
        def execute(self, requests):
            resps = []
            for r in requests:
                x = pb_utils.get_input_tensor_by_name(r, "IN0").as_numpy()
                time.sleep(0.01)  # simulate compute
                out = pb_utils.Tensor("OUT0", (x * 2.0).astype(np.float32))
                resps.append(pb_utils.InferenceResponse([out]))
            return resps
    ''').strip())
print("built model_repo/ with dynamic_batching + instance_group count=2")
