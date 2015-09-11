__author__ = 'Matteo'

import itertools
import time

if __name__ == '__main__':
    start = time.time()
    for i, j in enumerate(itertools.permutations((i for i in xrange(10)), 10)):
        if i == 1000000-1:
            print ''.join(map(str, j))
    end = time.time()
    print end - start