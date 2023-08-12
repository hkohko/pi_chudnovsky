import gmpy2
from math import ceil
from gmpy2 import mpz, fac
from time import perf_counter
from tqdm import tqdm

"""
all these prime swing factorials are slower than gmpy2.fac?
"""
# from primeswing_factorial.PrimeSwingFactorialGmpy import primeswing_factorial as fac
# from primeswing_factorial.PrimeSwingFactorialPy import primeswing_factorial as fac
# from primeswing_factorial.Andreas_prime_swing import divide_swing_and_conquer as fac


class Pi:
    def __init__(self, n: int):
        self.set_prec(n)
        self.digit = n
        self.step = ceil(n / 14)
        self.A = mpz(13591409)
        self.B = mpz(545140134)
        self.C = mpz(-262537412640768000)
        self.D = mpz(426880) * gmpy2.sqrt(10005)

    def gmp_prec(self, n: int):
        n = n + 5  # use higher than requrested precision
        return int(ceil(n * gmpy2.log(10) / gmpy2.log(2))) + 1

    def set_prec(self, n):
        gmpy2.get_context().precision = self.gmp_prec(n)

    def m_q(self, step: int) -> mpz:
        nom = fac(6 * mpz(step))
        b = fac(3 * mpz(step))
        c = pow(fac(mpz(step)), 3)
        denom = b * c
        result = nom // denom
        return result

    def l_q(self, step: int) -> mpz:
        a = self.B * step
        return a + self.A

    def x_q(self, step: int) -> mpz:
        a = pow(self.C, step)
        return a

    def division(self) -> gmpy2.mpfr:
        for step in range(self.step):
            result = (self.m_q(step) * self.l_q(step)) / self.x_q(step)
            yield result

    def summation(self) -> gmpy2.mpfr:
        result = 0
        for i in tqdm(self.division()):
            result = result + i
        return result

    def generate(self):
        return self.D / self.summation()

    def __repr__(self):
        a = f"{self.generate():.{self.digit}Df}"
        return a[-10:]


if __name__ == "__main__":
    n = int(input("Number of digits: "))
    print(f"expected iteraton: {ceil(n / 14)}")
    start = perf_counter()
    print(f"The last 10 digit of {n} digits:\n{Pi(n)}")
    end = perf_counter()
    print(f"Elapsed: {end - start:.2f}s")
