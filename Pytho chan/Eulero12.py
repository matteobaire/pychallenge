__author__ = 'Matteo'
import time


def triangle_number(num):
    return num * (num + 1) / 2


def divisors(num):
    result = 0
    for i in xrange(2, num + 1):
        if num % i == 0:
            result += 1
    return result


if __name__ == '__main__':
    start = time.time()
    print triangle_number(7)
    print divisors(21)
    count = 1
    l = 0
    while l < 500:
        n = triangle_number(count)
        l = divisors(n)
        print l
        count += 1
    print n
    end = time.time()
    print end-start
