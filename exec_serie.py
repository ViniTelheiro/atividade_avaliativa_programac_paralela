from time import time
from utils import is_prime

if __name__ == "__main__":
    t0 = time() # tempo de inicio da execução
    cont = 0
    n = 1
    result = []
    while cont != 100:
        if is_prime(n=n):
            cont+=1
            result.append(n)
        n += 1
    
    exec_time = time() - t0
    print(f"execution_time(s): {exec_time}")
    assert len(result)==100
    print(result)
