__author__ = 'Matteo'

from PIL import Image, ImageSequence

img = Image.open("white.gif")  # http://www.pythonchallenge.com/pc/hex/white.gif
out = Image.new("P", (125, 125))
pix = out.load()
pos = [25, 25]

for x in [list(f.getdata()).index(8) for f in ImageSequence.Iterator(img)]:
    if x == 19698:
        pos[0] -= 1
        pos[1] -= 1
    elif x == 19700:
        pos[1] -= 1
    elif x == 19702:
        pos[0] += 1
        pos[1] -= 1
    elif x == 20098:
        pos[0] -= 1
    elif x == 20100:
        pos = [pos[0] + 10, pos[1] + 10]
    elif x == 20102:
        pos[0] += 1
    elif x == 20498:
        pos[0] -= 1
        pos[1] += 1
    elif x == 20500:
        pos[1] += 1
    elif x == 20502:
        pos[0] += 1
        pos[1] += 1

    pix[pos[0], pos[1]] = 200

out.save("solution.png")