__author__ = 'Matteo'
import time

prev, cur = 0, 1
total = 0

'''trova la somma dei fibonacci di 4000000'''

if __name__ == '__main__':
    start = time.time()
    while True:
        prev, cur = cur, prev + cur
        if cur >= 4000000:
            break
        if cur % 2 == 0:
            total += cur
    print(total)
    end = time.time()
    print end-start