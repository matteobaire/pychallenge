__author__ = 'Matteo'
import time
sumsq = 0
sumqq = 0

if __name__ == '__main__':
    start = time.time()
    for i in xrange(1, 101):
        sumsq += i ** 2
        sumqq += i
    sumqq **= 2
    print sumqq - sumsq
    end = time.time()
    print start - end