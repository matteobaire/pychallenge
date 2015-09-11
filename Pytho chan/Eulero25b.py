__author__ = 'Matteo'

import math as m
import time
start = time.time()
fib0 = 0
fib1 = 1
n = 0
k = 0
count = 1
while k < 1000:
        n = fib0 + fib1
        k = int(m.log10(n))+1
        fib0 = fib1
        fib1 = n
        count += 1
print n
print count
print time.time()-start