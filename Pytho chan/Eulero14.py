__author__ = 'Matteo'
import time


def collatz(number):
    if number % 2 == 0:
        return number / 2
    return 3 * number + 1


def cseries(start):
    chain = 0
    while start != 1:
        start = collatz(start)
        chain += 1
    return chain


if __name__ == '__main__':
    inizio = time.time()
    greater = 0
    starter = 1
    for i in xrange(1, 1000000):
        num = cseries(i)
        if greater < num:
            greater = num
            starter = i
    print starter
    end = time.time()
    print end - inizio




