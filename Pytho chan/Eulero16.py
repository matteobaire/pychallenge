__author__ = 'Matteo'
import time

if __name__ == '__main__':
    start = time.time()
    print sum(map(int, list(str(2**1000))))
    end = time.time()
    print end - start



