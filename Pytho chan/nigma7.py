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

    myImage = Image.open("oxygen.png")
    picW, picH = myImage.size
    picMiddleH = picH // 2
    for length in range(0, picW, 7):
        myList.append(myImage.getpixel((length, picMiddleH)))

    for one, two, three, four in myList:
        if re.search(r'[ ,.a-z]', chr(one)):
            myList2.append(chr(one))
        if re.search(r'\d+', chr(one)):
            myList3.append(chr(one))
    del myList2[-18:]

    for loop in range(len(myList3)):
        myNumbers.append(myList3[loop])
        num += 1
        if num == 3:
            myList2.append(chr(int("".join(myNumbers))))
            myNumbers = []
            num = 0
    myString = "".join(myList2)
    print myString