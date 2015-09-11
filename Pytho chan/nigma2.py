# coding=utf-8
__author__ = 'Matteo'

import urllib
import collections

'''la stringa da decifrare è nascosta nella sorgente della pagina. Dentro vi sono alcune lettere e per trovarle occorre
cercare i caratteri con la frequenza più bassa (1) le lettere anagrammate compongono la parola "equality"'''

if __name__ == '__main__':
    fd = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
    mess = fd.read()
    messarr = mess.split("--")
    histogram = collections.defaultdict(lambda: 0)
    for char in messarr[3]:
        histogram[char] += 1
    a = dict(histogram)
    for i in a:
        if a[i] == 1:
            print i,