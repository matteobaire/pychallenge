# coding=utf-8
__author__ = 'Matteo'
import time
maxpal = 0
'''trovare il più grande palindromo ottenibile moltiplicando 2 numeri di 3 cifre)'''

if __name__ == '__main__':
    start = time.time()
    for n in xrange(800, 999):
        for s in xrange(800, 999):
            p = n * s
            if str(p) == str(p)[::-1]:
                maxpal = p
    print maxpal
    end = time.time()
    print end-start
