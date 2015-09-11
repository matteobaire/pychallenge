__author__ = 'Matteo'

import time

letternum = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
             9: 'nine',
             10: 'ten', 11: 'eleven', 12: 'twelve'}
decs = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

decone = {3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: "nineteen"}


def write(num):
    if len(str(num)) == 4:
        return 'onethousand'
    return cent(num)


def cent(num):
    if num < 100:
        return dec(num)
    n = map(int, list(str(num)))
    s = letternum[n[0]] + 'hundred'
    if n[1] == 0 and n[2] == 0:
        return s
    s += 'and' + dec(n[1] * 10 + n[2])
    return s


def dec(num):
    n = map(int, list(str(num)))
    if num in letternum.keys():
        return letternum[num]
    if num < 20:
        return decone[n[1]]
    if n[1] == 0:
        return decs[n[0]]
    return decs[n[0]] + letternum[n[1]]


if __name__ == '__main__':
    start = time.time()
    print sum([len(write(i))for i in range(1, 1001)])
    end = time.time()
    print end -start

