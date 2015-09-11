__author__ = 'Matteo'

if __name__ == '__main__':
    res = []
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            num = a**b
            if num not in res:
                res.append(num)
    print len(res)