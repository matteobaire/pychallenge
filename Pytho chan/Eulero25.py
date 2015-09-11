__author__ = 'Matteo'
from math import *
import time


def fibonaccin(number):
    i = 1
    fib0 = 0
    fib1 = 1
    dig = 0
    while True:
        n = fib0 + fib1
        fib0, fib1 = fib1, n
        dig = int(log10(n)) + 1
        i += 1
        if dig == 1000:
            return i


if __name__ == '__main__':
    start = time.time()
    res = ''
    i = 12
    while i < 1000:
        res = fibonaccin(i)
        i += 1
    print fibonaccin(1000)
    end = time.time()
    print end - start