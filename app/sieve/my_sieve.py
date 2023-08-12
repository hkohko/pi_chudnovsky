from math import sqrt


def sieve(n):
    number_range = range(2, n + 1)
    number_list = [i for i in number_range]
    p = 2

    while p <= sqrt(n):
        number_list = [0 if i % p == 0 and i != p else i for i in number_list]
        p += 1

    cleaned = [i for i in number_list if i != 0]
    return cleaned
