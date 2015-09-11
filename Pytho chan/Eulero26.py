__author__ = 'Matteo'
import time

start = time.time()


def recurring_cycle(d):
    # solve 10^s % d == 10^(s+t) % d
    # where t is length and s is start
    for t in xrange(1, d):
        if 1 == 10 ** t % d:
            return t
    return 0


if __name__ == '__main__':
    longest = max(recurring_cycle(i) for i in xrange(2, 1001))
    print (i for i in xrange(2, 1001) if recurring_cycle(i) == longest).next()
    end = time.time()
    print end - start

