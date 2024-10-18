import threading
from time import time
import argparse

from worker import worker

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_workers", "-n", type=int, default=2, help="set the number of workers.")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    process = []
    n_workers = args.n_workers
    t0 = time()
    for _ in range(n_workers):
        t = threading.Thread(target=worker)
        process.append(t)
        t.start()
    
    # wait untill all workers has finished
    for t in process:
        t.join()
    print(f"execution time: {time() - t0}")
