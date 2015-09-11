__author__ = 'Matteo'
import time
"""
Longest Collatz sequence
------------------------

The following iterative sequence is defined for the set of positive integers:
n  n/2 (n is even)
n  3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.

Approach:

A function `collatz` which returns the number of terms in the chain, given it's starting position.
It goes trough the sequence, but It also remembers previous ones using a global dictionary.
Get the maximum one.
"""

collatz_counts = {}


def collatz(n):
    count = 1
    start = n
    while n != 1:
        if n in collatz_counts:
            count += collatz_counts[n]
            break
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        count += 1

    collatz_counts[start] = count
    return count

if __name__ == '__main__':
    inizio = time.time()
    answer = max(((collatz(i), i) for i in range(1, 1000000)))
    print("The starting position generating the longest sequence is {0}".format(answer[1]))
    end = time.time()
    print end - inizio