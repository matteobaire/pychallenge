__author__ = 'Matteo'

#!/usr/bin/env python2
import urllib
import zipfile
import re
import os

'''l'indizio consiglia di scaricare il file channel.zip che contiene la directory zipped_stuff.
Il file readme indica di partire dal file 90052.txt.'''

if __name__ == '__main__':
    file_number = "90052"
    comments = []
    file_URL = "http://www.pythonchallenge.com/pc/def/channel.zip"
    download = urllib.urlopen(file_URL)
    myZipped = download.read()
    savedFile = open("file.zip", 'wb')
    savedFile.write(myZipped)
    savedFile.close()

    myUnZipped = zipfile.ZipFile("file.zip")
    new_path = "zipped_stuff"
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    for name in myUnZipped.namelist():
        uncompressed = myUnZipped.read(name)
        savedFile = open(new_path + "/" + name, 'wb')
        savedFile.write(uncompressed)
        savedFile.close()
    while file_number is not "":
        file_content = open(new_path + "/" + file_number + ".txt", 'r')
        file_text = file_content.read()
        file_number = "".join(re.findall(r'\d+', file_text))
        if file_number is not "":
            comments.append(myUnZipped.getinfo(file_number + ".txt").comment)
    print file_text, "".join(comments)