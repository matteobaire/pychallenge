__author__ = 'Matteo'

'''somma dei numeri divisibili per 3 o per 5 inferiori a 1000'''
import time

if __name__ == '__main__':
    start = time.time()
    a = [i for i in xrange(1, 1000) if (i % 3 == 0 or i % 5 == 0)]
    print sum(a)
    end = time.time()
    print end - start