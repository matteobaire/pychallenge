
def nextPermutation(array):
    i = len(array) - 1
    while i > 0 and (array[i - 1] >= array[i]):
        i -= 1
    if i <= 0:
        return False
    j = len(array) - 1
    while array[j] <= array[i - 1]:
        j -= 1
    array[j], array[i-1] = array[i-1], array[j]
    j = len(array) - 1
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in xrange(999999):
        nextPermutation(arr)
    print arr

