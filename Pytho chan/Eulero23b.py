__author__ = 'Matteo'

from math import sqrt
from bisect import bisect_left
import time

def abundant_numbers(limit):
    lii = []
    for num in xrange(1, limit+1):
        tot = 1
        last_num = int(sqrt(num)+1)
        for i in xrange(2, last_num):
            if num % i == 0:
                tot += i
                if i != num / i:
                    tot += num / i
        if tot > num:
            lii.append(num)
    return lii


def index(ly, x):
    """Locate the leftmost value exactly equal to x"""
    i = bisect_left(ly, x)
    if i != len(ly) and ly[i] == x:
        return True
    else:
        return False

if __name__ == '__main__':
    start = time.time()
    li = abundant_numbers(28123)
    total = 0
    for i in xrange(1, 28123):
        total += i
        for j in li:
            rem = i - j
            if rem < 12:
                break
            if index(li, rem):
                total -= i
                break
    print total
    end = time.time()
    print end - start