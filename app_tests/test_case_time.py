import app.my_chudnovsky as pi
from time import perf_counter
from gmpy2 import mpz
from tqdm import tqdm

def modules():
    yield from (pi.m_q, pi.l_q, pi.x_q, pi.division, pi.summation, pi.pi)


def test_modules(func: mpz, code: int):
    name_module = {0: "m_q", 1: "l_q", 2: "x_q", 3: "division", 4: "summation", 5: "pi"}
    n = 10000
    pi.set_prec(n)
    start = perf_counter()
    for i in tqdm(range(n)):
        func(i)
    end = perf_counter()
    result.append(f"{name_module.get(code)}: {end - start:.2f}s")

if __name__ == "__main__":
    result = []
    for code, module in enumerate(modules()):
        test_modules(module, code)
    print(result)