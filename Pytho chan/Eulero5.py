__author__ = 'Matteo'

'''massimo intero divisibile da tutti i numeri da 1 a 20'''
from collections import Counter
import time

primes_below_20 = (2, 3, 5, 7, 11, 13, 17, 19)
primes_needed = Counter()
total = 1


def prime_factors(num):
    # Assume n <= 20
    if num == 1:
        return []
    for primo in primes_below_20:
        if num % primo == 0:
            return [primo] + prime_factors(num / primo)

if __name__ == '__main__':
    start = time.time()
    for n in xrange(2, 21):
        primes = Counter(prime_factors(n))
        primes_needed = primes_needed | primes  # | gives the max of existing values

    for prim, amount in primes_needed.items():
        total *= prim ** amount
    print total
    end = time.time()
    print end - start
