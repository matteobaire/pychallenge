__author__ = 'Matteo'


def finddiag(n):
    first = (2 * n + 1) ** 2
    second = first - 2 * n
    third = second - 2 * n
    fourth = third - 2 * n
    return sum({first, second, third, fourth})

def getring(n):
    return (n - 1)/2

if __name__ == '__main__':
    tot = 0
    rings = getring(1001)
    for r in xrange(rings+1):
        tot += finddiag(r)
    print tot