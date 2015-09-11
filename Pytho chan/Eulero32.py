__author__ = 'Matteo'

from itertools import permutations

digits = range(1, 10)
print digits

results = []

for i in permutations(digits, 9):
    first = 10 * i[0] + i[1]
    second = 100 * i[2] + 10 * i[3] + i[4]
    firstalt = i[0]
    secondalt = 1000 * i[1] + 100 * i[2] + 10 * i[3] + i[4]
    third = 1000 * i[5] + 100 * i[6] + 10 * i[7] + i[8]
    if first * second == third or firstalt * secondalt == third:
        print third
        results.append(third)
print results
print sum(set(results))
