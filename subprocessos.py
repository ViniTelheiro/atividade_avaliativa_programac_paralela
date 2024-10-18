import subprocess
import argparse
from time import time

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
        p = subprocess.Popen(["python3", "worker.py"])
        process.append(p)
    
    # wait untill all workers has finished
    for p in process:
        p.wait()
    print(f"execution time: {time() - t0}")    
    

