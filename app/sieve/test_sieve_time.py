from my_sieve import sieve as my_sieve
from gfg_sieve import SieveOfEratosthenes as gfg_sieve
from sieve_np import np_sieve
from time import perf_counter


def modules():
    yield from (my_sieve, gfg_sieve, np_sieve)


def test_time(n):
    for func in modules():
        start = perf_counter()
        func(n)
        end = perf_counter()
        print(end - start)


test_time(100000)
