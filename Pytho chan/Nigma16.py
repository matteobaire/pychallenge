__author__ = 'Matteo'

from PIL import Image, ImageChops

image = Image.open("mozart.gif")
magic = chr(195)

for y in xrange(image.size[1]):
    box = 0, y, image.size[0], y + 1
    row = image.crop(box)
    bites = row.tostring()
    i = bites.index(magic)
    row = ImageChops.offset(row, -i)
    image.paste(row, box)

image.save("new2.gif")
