__author__ = 'Matteo'

import math
import time

tot = 0


def is_prime(number):
    for i in xrange(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    start = time.time()
    for num in xrange(2, 2000000):
        if is_prime(num):
            tot += num
    print tot
    end = time.time()
    print end-start