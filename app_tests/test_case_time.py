from app.my_chudnovsky import Pi
from math import ceil
from time import perf_counter


def modules_term():
    yield from (pi.m_q, pi.l_q, pi.x_q)


def calc():
    yield from (pi.division, pi.summation, pi.generate)


def test(digits: int):
    for module in modules_term():
        start = perf_counter()
        module(digits)
        end = perf_counter()
        result.append(end - start)

    for module in calc():
        start = perf_counter()
        module(True, digits)
        end = perf_counter()
        result.append(end - start)


if __name__ == "__main__":
    result = []
    digits = int(input("digits: "))
    pi = Pi(digits)

    test(digits)

    def calibrate_tqdm_overhead(x: float):
        overhead = 80e-9 * ceil(digits / 14)
        return x - overhead

    name_module = {
        0: "m_q",
        1: "l_q",
        2: "x_q",
        3: "division",
        4: "summation",
        5: "generate",
    }
    print(f"\nexpected iteration: {ceil(digits / 14)}")
    for code, i in enumerate(result):
        print(f"{name_module.get(code)}: {i:.2f}s")
