__author__ = 'Matteo'

import gzip, difflib

# Download the GNU zip file from:
# http://www.pythonchallenge.com/pc/return/deltas.gz

h = gzip.open("deltas.gz")
d = difflib.Differ()

part_1, part_2 = [], []
file_1, file_2, file_3 = [], [], []

for line in h:
    part_1.append(line[0:53])
    part_2.append(line[56:-1])

h.close()

for line in list(d.compare(part_1, part_2)):
    if line[0] == "+":
        file_1.append(line[2:])
    elif line[0] == "-":
        file_2.append(line[2:])
    else:
        file_3.append(line[2:])

for n, data in enumerate((file_1, file_2, file_3)):
    temp = []

    for line in data:
        temp.extend([chr(int(o, 16)) for o in line.strip().split(" ") if o])

    h = open("%s.png" % (n + 1), "wb")
    h.writelines(temp)
    h.close()

    # The third file is corrupt and won't be properly displayed by most image
    # viewers. It should work in Gecko-based browsers such as Firefox, though.