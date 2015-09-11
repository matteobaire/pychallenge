# coding=utf-8
__author__ = 'Matteo'

import string
import time

scoring = {letter: score + 1 for score, letter in enumerate(list(string.ascii_uppercase))}


def sortnames(namefile):
    fin = open(namefile, 'r')
    names = sorted(fin.read().replace('"', '').split(','))
    fin.close()
    return names


def worthname(name):
    return sum((scoring[i] for i in name))


def score(namelist):
    return sum(((i+1) * worthname(j) for i, j in enumerate(namelist)))


if __name__ == '__main__':
    start = time.time()
    A = sortnames('names.txt')
    print score(A)
    end = time.time()
    print end - start