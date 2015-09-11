__author__ = 'Matteo'
import time


def fat(num):
    if num < 2:
        return 1
    return reduce(lambda x, y: x * y, xrange(1, num + 1))


if __name__ == '__main__':
    start = time.time()
    a = map(int, list(str(fat(100))))
    print sum(a)
    end = time.time()
    print end - start