__author__ = 'Matteo'

import math

def is_prime(number):
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True

no_of_primes = 0
j = 2
list_of_primes = []
while no_of_primes < 10001:
    if is_prime(j):
        list_of_primes.append(j)
        no_of_primes += 1
    j += 1

print list_of_primes[10000]