__author__ = 'Matteo'

import math
import time

term = [i for i in range(1, 2000, 2)]

if __name__ == '__main__':
    start = time.time()
    for i, num in enumerate(term):
        if math.sqrt(num) - int(math.sqrt(num)) == 0.0:
            n = (num + 1)/2
            a = int(math.sqrt(num))
            b = int(math.sqrt(sum(term[:i])))
            c = int(math.sqrt(sum(term[:i+1])))
            print a, b, c, a + b + c
            if a + b + c == 1000:
                print a, b, c
                break
    print a*b*c
    end = time.time()
    print end - start

