"""Stage 05 — throughput vs concurrency against the running server (8.03, 8.07)."""
import time, threading, numpy as np
import tritonclient.http as httpclient

URL = "localhost:8000"

def one_request():
    cli = httpclient.InferenceServerClient(url=URL)
    x = np.random.rand(1, 4).astype(np.float32)
    inp = httpclient.InferInput("IN0", x.shape, "FP32"); inp.set_data_from_numpy(x)
    cli.infer("toy", [inp])

def bench(concurrency, total=200):
    done = [0]; lock = threading.Lock()
    def worker():
        while True:
            with lock:
                if done[0] >= total: return
                done[0] += 1
            one_request()
    t0 = time.time()
    threads = [threading.Thread(target=worker) for _ in range(concurrency)]
    [t.start() for t in threads]; [t.join() for t in threads]
    dt = time.time() - t0
    print(f"concurrency={concurrency:3d} throughput={total/dt:7.1f} req/s")

for c in [1, 2, 4, 8, 16, 32]:
    bench(c)
# Expected: throughput rises with concurrency until instances/batch saturate.
