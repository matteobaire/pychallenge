__author__ = 'Matteo'

import time

term = [i for i in range(4, 1001, 2)]

if __name__ == '__main__':
    start = time.time()
    print term
    for num in term:
        for i in range(1, 1000):
            for j in range(1, 1000):
                if num == 2 * i * j:
                    a = abs(i ** 2 - j ** 2)
                    b = 2 * i * j
                    c = i ** 2 + j ** 2
                    if a**2 + b**2 == c**2:
                        if a+b+c == 1000:
                            print a, b, c
                            print a*b*c
                            break
    end = time.time()
    print end - start