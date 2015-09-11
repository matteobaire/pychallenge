__author__ = 'Matteo'
import time


def divisors(num):
    return (i for i in xrange(1, num/2+1) if num % i == 0)


def d(n):
    return sum(divisors(n))


def amicablelist(n):
    L = sorted(list(set((d(i) for i in xrange(2, n+1)))))
    A = (i for i in L if i != d(i) and i == d(d(i)))
    return sum((a for a in A))


if __name__ == '__main__':
    start = time.time()
    print amicablelist(10000)
    end = time.time()
    print end - start