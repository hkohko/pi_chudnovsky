import app.my_chudnovsky as pi
from time import perf_counter
from gmpy2 import mpz
from tqdm import tqdm


def modules():
    yield from (pi.m_q, pi.l_q, pi.x_q)


def test_modules(func: mpz, code: int):
    name_module = {0: "m_q", 1: "l_q", 2: "x_q"}
    n = 1000
    pi.set_prec(n)
    start = perf_counter()
    for i in tqdm(range(n)):
        func(i)
    end = perf_counter()
    print(f"{name_module.get(code)}: {end - start:.2f}s")


for code, module in enumerate(modules()):
    test_modules(module, code)
