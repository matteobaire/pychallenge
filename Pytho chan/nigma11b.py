# coding=utf-8
__author__ = 'Matteo'

'''ODD Even è l'indizio (nome della pagina). Bisogna separare i pixel dell'immagine cave.jpg'''

from PIL import Image
import urllib
from cStringIO import StringIO


def splitOE(source):
    width, height = source.size
    results = [Image.new(source.mode, (width // 2, height // 2))
               for dummy in xrange(4)]
    for x in xrange(width):
        for y in xrange(height):
            target = results[x % 2 + (y % 2 << 1)]
            target.putpixel((x // 2, y // 2), source.getpixel((x, y)))
    return results

if __name__ == '__main__':
    url = 'http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg'
    odd_even = splitOE(Image.open(StringIO(urllib.urlopen(url).read())))
    for i, result in enumerate(odd_even):
        result.save('cave%s.bmp'% str(i))