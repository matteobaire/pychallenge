__author__ = 'Matteo'

from PIL import Image
from cStringIO import StringIO

'''disproportional. il file evil2.gfx contiene le immagini con la soluzione. Scaricare anche il file evil4.jpg'''

s = open("evil2.gfx", "rb").read()
for i in range(5):
    piece = s[i::5]  # every fifth byte, starting at i
    im = Image.open(StringIO(piece))
    f = open("%d.%s" % (i, im.format.lower()), "wb")
    f.write(piece)
    f.close()