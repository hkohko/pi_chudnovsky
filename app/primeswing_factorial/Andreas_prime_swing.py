# https://oeis.org/A000142/a000142.pdf

import math
from typing import List


def divide_swing_and_conquer(number: int) -> int:
    if number == 1 or number == 0:
        return 1

    prime_numbers = all_prime_numbers_up_to(number)

    prime_exponents_array = prime_exponents_of_a_swing_number(number, prime_numbers)

    sf = compute_swinging_factorial(prime_numbers, prime_exponents_array)

    return divide_swing_and_conquer(number // 2) ** 2 * sf


def prime_exponents_of_a_swing_number(
    swing_number: int, prime_numbers: List[int]
) -> List[int]:
    k = math.floor(math.log2(swing_number))

    prime_exponents_array = []

    for prime in prime_numbers:
        exponent = 0
        for i in range(1, k + 1):
            exponent += swing_number // prime**i % 2
        prime_exponents_array.append(exponent)

    return prime_exponents_array


def compute_swinging_factorial(
    prime_numbers: List[int], prime_exponents_array: List[int]
) -> int:
    swing_factorial = 1
    for prime, factor in zip(prime_numbers, prime_exponents_array):
        if factor == 0:
            continue

        swing_factorial *= prime**factor
    return swing_factorial


def is_prime(n: int) -> bool:
    """
    Checks if a number is prime or not
    :param n: any positive whole number
    :return: True if the number is prime False otherwise
    """
    if n == 1:
        return False

    if n == 2:
        return True

    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for divisor in range(3, max_divisor + 1, 2):
        if n % divisor == 0:
            return False
    return True


def all_prime_numbers_up_to(n: int) -> List[int]:
    """
    Calculates all the prime numbers up to a given number
    :param n: any positive whole number
    :return: all the prime numbers up to a given number as a list
    """
    prime_numbers_array = []
    for num in range(1, n + 1):
        if is_prime(num):
            prime_numbers_array.append(num)

    return prime_numbers_array


if __name__ == "__main__":
    try:
        n = int(input("Factorial of: "))
        if n < 0:
            raise ValueError
        else:
            print(divide_swing_and_conquer(n))
    except ValueError:
        print("Please provide a positive integer")
