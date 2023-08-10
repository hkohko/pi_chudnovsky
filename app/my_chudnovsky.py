import gmpy2
from math import ceil
from enum import Enum
from gmpy2 import mpz, fac
from time import perf_counter
from tqdm import tqdm

"""
all these prime swing factorials are slower than gmpy2.fac?
"""
# from primeswing_factorial.PrimeSwingFactorialGmpy import primeswing_factorial as fac
# from primeswing_factorial.PrimeSwingFactorialPy import primeswing_factorial as fac
# from primeswing_factorial.Andreas_prime_swing import divide_swing_and_conquer as fac


def gmp_prec(n: int):
    n = n + 5  # use higher than requrested precision
    return int(ceil(n * gmpy2.log(10) / gmpy2.log(2))) + 1


def set_prec(n):
    gmpy2.get_context().precision = gmp_prec(n)


class Constants(Enum):
    A = mpz(13591409)
    B = mpz(545140134)
    C = mpz(-262537412640768000)
    D = mpz(426880) * gmpy2.sqrt(10005)


def m_q(step: int) -> mpz:
    nom = fac(6 * mpz(step))
    b = fac(3 * mpz(step))
    c = pow(fac(mpz(step)), 3)
    denom = b * c
    result = nom // denom
    return result


def l_q(step: int) -> mpz:
    a = Constants.B.value * step
    return a + Constants.A.value


def x_q(step: int) -> mpz:
    a = pow(Constants.C.value, step)
    return a


def division(steps: int) -> gmpy2.mpfr:
    for step in range(steps):
        result = (m_q(step) * l_q(step)) / x_q(step)
        yield result


def summation(step: int) -> gmpy2.mpfr:
    result = 0
    for i in tqdm(division(step)):
        result = result + i
    return result


def pi(digit: int, step: int = 4):
    a = f"{Constants.D.value / summation(step):.{digit}Df}"
    return a


if __name__ == "__main__":
    while True:
        n = int(input("Number of digits : "))
        if gmp_prec(n) < int(gmpy2.get_max_precision()):
            gmpy2.get_context().precision = gmp_prec(n)
            start = perf_counter()
            print(f"expected iteration: {ceil(n / 14)}")
            class Constants(Enum):
                A = mpz(13591409)
                B = mpz(545140134)
                C = mpz(-262537412640768000)
                D = mpz(426880) * gmpy2.sqrt(10005)

            print(pi(n, ceil(n / 14))[-10:])
            end = perf_counter()
            print(f"{end - start:.2f}s")
        else:
            print("Exceeded max precision")
