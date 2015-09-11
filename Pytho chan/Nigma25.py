__author__ = 'Matteo'

import wave
from PIL import Image


pieces = []
for i in range(1, 26):
    f = wave.open("lake%d.wav" % i, "rb")
    pieces.append(f.readframes(f.getnframes()))
    f.close()

combined = []
for i in range(0, 25, 5): # row i//5 comes from pieces i:i+5
    for j in range(60):   # 60 pixels tall
        for k in range(5): # take a row of 60 pixels from each piece
            combined.append(pieces[i+k][180*j:180*(j+1)])
im = Image.frombuffer("RGB", (300, 300), "".join(combined), "raw", "RGB", 0, 1)
im.save("decent.jpg")

