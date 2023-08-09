import gmpy2
from math import pow
from enum import Enum
from gmpy2 import mpz, fac

gmpy2.get_context().precision = 200

pi_check = "3.1415926535897932384626433832795028841971693993751"


class Constants(Enum):
    A = mpz(13591409)
    B = mpz(545140134)
    C = mpz(-262537412640768000)
    D = mpz(426880) * gmpy2.sqrt(10005)


def m_q(step: int):
    nom = fac(6 * mpz(step))
    b = fac(3 * mpz(step))
    c = pow(fac(mpz(step)), 3)
    denom = b * c
    result = nom / denom
    print(f"m_q: {result}")
    return result


def l_q(step: int):
    a = Constants.B.value * step
    print(f"l_q: {a}")
    return a + Constants.A.value


def x_q(step: int):
    a = pow(Constants.C.value, step)
    print(f"x_q: {a}")
    return a


def division(steps: int):
    for step in range(steps):
        print(f"step: {step}")
        result = (m_q(step) * l_q(step)) / x_q(step)
        yield result


def summation(step: int):
    result = 0
    for i in division(step):
        result = result + i
    return result


def pi(step: int = 4):
    return f"{Constants.D.value / summation(step):.49Df}"


print(pi())
print(pi_check)
