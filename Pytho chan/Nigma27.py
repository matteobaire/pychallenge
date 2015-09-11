__author__ = 'Matteo'

from PIL import Image
import bz2
import keyword


img = Image.open('zigzag.gif')
data = list(img.getdata())
pal = img.getpalette()[::3]
for i in range(10):
    p = data[i]
    print "%3d %3d" % (p, pal[p])

exceptions = []
expected = None
indices = []
for i, p in enumerate(data):
    if expected is not None and p != expected:
        exceptions.append(p)
        indices.append(i)
    expected = pal[p]

bzdata = "".join(map(chr, exceptions))
bzexpanded = bz2.decompress(bzdata)
im2 = Image.new("RGB", img.size)
colors = [(255, 255, 255)] * len(data)
blue = 0, 0, 255
for i in indices:
    colors[i] = blue
im2.putdata(colors)
im2.show()
allwords = bzexpanded.split()
oddballs = set(allwords) - set(keyword.kwlist)
for word in allwords:
    if word in oddballs:
        print word
        oddballs.remove(word)
        if not oddballs:
            break