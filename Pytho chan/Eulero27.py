# coding=utf-8
__author__ = 'Matteo'

import math


def is_prime(k):
    if k < 2:
        return False
    elif k == 2:
        return True
    elif k % 2 == 0:
        return False
    else:
        for x in xrange(3, int(math.sqrt(k) + 1), 2):
            if k % x == 0:
                return False
    return True


if __name__ == '__main__':
    n = 0
    count = 0
    longest = [0, 0, 0]
    for a in xrange(-999, 1000):
        for b in xrange(2, 1000):
            # print 'a,b:', coeff_a, coeff_b
            if is_prime(b):
                n = 0
                count = 0
                while is_prime(n**2 + n*a + b):
                    count += 1
                    n += 1
                if count > longest[0]:
                    longest = [count, a, b]
    print longest[1], longest[2], longest[1] * longest[2]




