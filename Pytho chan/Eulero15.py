__author__ = 'Matteo'
import time


def fat(num):
    if num < 2:
        return 1
    return reduce(lambda x, y: x * y, xrange(1, num + 1))


def binomial(sup, inf):
    num = fat(sup)
    den = fat(sup - inf) * fat(inf)
    return num / den


if __name__ == '__main__':
    start = time.time()
    print binomial(40, 20)
    end = time.time()
    print end - start
