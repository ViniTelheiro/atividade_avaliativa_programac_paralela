from typing import List
from utils import is_prime

def worker()->List[int]:
    cont = 0
    n = 1
    while cont != 100:
        if is_prime(n=n):
            cont+=1
        n+=1

if __name__ == "__main__":
    worker()
