# coding=utf-8
__author__ = 'Matteo'


import urllib
import re

'''l'url è una lista concatenata di pagine. È impossibile arrivare all'ultimo a mano. Si sceglie un nodo a caso e si
fa scorrere in automatico tutta la lista fino alla fine, dove nel sorgente è scritta la soluzione'''

ending = "27709"
i = 0
if __name__ == '__main__':
    while i == 0:
        pagesource = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + ending)
        text = pagesource.read()
        print text
        number = re.findall(r'\d+', text)
        ending = "".join(number)
        if ending == "":
            print text
            i = 1
    print ending