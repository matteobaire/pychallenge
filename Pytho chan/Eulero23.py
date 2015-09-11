__author__ = 'Matteo'
import time


def divisors(num):
    return (i for i in xrange(1, num / 2 + 1) if num % i == 0)


def d(n):
    return sum(divisors(n))


def abundant(maxlim):
    return (i + j for i in xrange(12, maxlim / 2 + 1) for j in xrange(12, maxlim / 2 + 1) if
            i < d(i) and j < d(j) and i + j < 28123 and i <= j)


if __name__ == '__main__':
    start = time.time()
    l = [i for i in xrange(1, 28124)]
    for i in abundant(28123):
        print i
        if i in l:
            l.remove(i)
    print l
    end = time.time()
    print end - start