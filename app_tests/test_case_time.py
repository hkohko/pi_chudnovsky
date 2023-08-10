import app.my_chudnovsky as pi
from math import ceil
from time import perf_counter
from gmpy2 import mpz
from tqdm import tqdm

def modules():
    yield from (pi.m_q, pi.l_q, pi.x_q, pi.division)


def test_terms_module(func: mpz, code: int, digits: int):
    name_module = {0: "m_q", 1: "l_q", 2: "x_q", 3: "division"}
    n = ceil(digits / 14)
    pi.set_prec(digits)
    start = perf_counter()
    for i in tqdm(range(n)):
        func(i)
    end = perf_counter()
    result.append(end - start)

if __name__ == "__main__":
    result = []
    digits = 1000
    for code, module in enumerate(modules()):
        test_terms_module(module, code, digits)

    def calibrate_tqdm_overhead(x: float):
        overhead = 80e-9
        return x - overhead
    
    compensated_result = map(calibrate_tqdm_overhead, result)
    print(list(compensated_result))