"""Stage 06 — verify latency percentiles + break-it (starvation) (8.09)."""
import time, threading, numpy as np
import tritonclient.http as httpclient

URL = "localhost:8000"

def timed_request(lat):
    cli = httpclient.InferenceServerClient(url=URL)
    x = np.random.rand(1, 4).astype(np.float32)
    inp = httpclient.InferInput("IN0", x.shape, "FP32"); inp.set_data_from_numpy(x)
    t0 = time.time(); cli.infer("toy", [inp]); lat.append(time.time() - t0)

def run(concurrency, total=200):
    lat = []; done = [0]; lock = threading.Lock()
    def worker():
        while True:
            with lock:
                if done[0] >= total: return
                done[0] += 1
            timed_request(lat)
    ts = [threading.Thread(target=worker) for _ in range(concurrency)]
    [t.start() for t in ts]; [t.join() for t in ts]
    a = np.array(lat) * 1000
    print(f"concurrency={concurrency:3d} p50={np.percentile(a,50):.1f}ms "
          f"p99={np.percentile(a,99):.1f}ms")
    return np.percentile(a, 99)

print("[VERIFY] modest concurrency:"); low = run(4)
print("[BREAK-IT] high concurrency vs few instances:"); high = run(32)
print("=> p99 explodes past saturation (batching starvation). "
      "Fix: continuous batching / more instances (8.08-8.11).")
