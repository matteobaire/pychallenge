__author__ = 'Matteo'

import calendar
import time

if __name__ == '__main__':
    start = time.time()
    print len([i for i in range(1901, 2001) for j in range(1, 13) if calendar.weekday(i, j, 1) == 5])
    end = time.time()
    print end - start