__author__ = 'Matteo'


def sequence(num):
    for t in xrange(1, num):
        print 10**t % num, t


if __name__ == '__main__':
    sequence(11)