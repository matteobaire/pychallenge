__author__ = 'Matteo'

import urllib
import re

'''nella stringa dell'url bisogna cercare le lettere minuscole isolate che si trovano tre lettere maiuscole ai due lati
ad es: AAAaAAA'''

if __name__ == '__main__':
    fd = urllib.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
    mess = fd.read()
    resultList = re.findall("[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]", mess)
    outputStr = ""
    for word in resultList:
        outputStr += word[4]
    print outputStr
