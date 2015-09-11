# coding=utf-8
__author__ = 'Matteo'

'''la sequenza è [1, 11, 21, 1211, 111221,...] occorre trovare il 30° numero e determinare la lunghezza'''

run = 0
loop = 0
total = 0
count = 1
numbers = [1]
final = []


while run < 30:
    length = len(numbers)
    while loop < length - 1:
        if numbers[loop] == numbers[loop + 1]:
            count += 1
        else:
            final.append(count)
            final.append(numbers[loop])
            count = 1
        loop += 1

    final.append(count)
    final.append(numbers[loop])
    numbers = final
    final = []
    count = 1
    loop = 0
    run += 1    
print len(numbers)