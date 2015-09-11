__author__ = 'Matteo'

import string

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
lettere = string.ascii_lowercase
letterem = string.ascii_uppercase
url = 'map'

if __name__ == '__main__':
    for i in range(0, len(lettere)):
        s = s.replace(lettere[i - 2], letterem[i])
        url = url.replace(lettere[i - 2], letterem[i])

    print s.lower()
    print url



