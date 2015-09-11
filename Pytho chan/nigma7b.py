# coding=utf-8
__author__ = 'Matteo'

import urllib
import re
from PIL import Image

'''Nell'immagine oxygen.png ci sono dei pixel grigi situati a metà altezza.'''

if __name__ == '__main__':
    num = 0
    myList = []
    myList2 = []
    myList3 = []
    myString = ""
    myNumbers = []

    file_URL = "http://www.pythonchallenge.com/pc/def/oxygen.png"
    download = urllib.urlopen(file_URL)
    myPic = download.read()
    savedFile = open("oxygen.png", 'wb')
    savedFile.write(myPic)
    savedFile.close()

    im = Image.open('oxygen.png')
    width = im.size[0]
    height = im.size[1]
    pixels = im.load()
    bar_y = height / 2  # bar is half way down the image
    # look at every 7th pixel
    answer = ''
    for i in range(0, width, 7):
        p = pixels[i, bar_y]  # get a pixel object[x, y] - (r, g, b, a)
        if p[0] == p[1] == p[2]:  # only look at greyscale pixels (r = g = b)
            answer += chr(p[0])
    print '\n', answer, '\n'
    lista = re.findall('(\d+)', answer)  # find all numbers and put into a list
    print ''.join(map(chr, map(int, lista)))  # int() each, then chr() each