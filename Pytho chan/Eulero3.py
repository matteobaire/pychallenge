__author__ = 'Matteo'
import time

i = 2
n = 600851475143

'''trova il massimo fattore primo di n'''

if __name__ == '__main__':
    start = time.time()
    while i * i < n:
        while n % i == 0:
            n = n / i
        i += 1
    print (n)
    end = time.time()
    print end-start