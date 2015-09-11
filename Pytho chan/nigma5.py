# coding=utf-8
__author__ = 'Matteo'

#!/usr/bin/env python2

import urllib
import pickle

'''nel sorgente viene menzionato un file banner.p, e l'indizio è riferito alla libreria pickle.'''

if __name__ == '__main__':
    myFile = pickle.load(urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
    for line in myFile:
        print "".join(map(lambda pair: pair[0]*pair[1], line))
