__author__ = 'Matteo'

import string

'''la stringa va convertita spostando le lettere di due posizioni avanti come per k -> m e a->c'''
''' ocr '''

if __name__ == '__main__':
    letters = string.ascii_lowercase
    uletters = string.ascii_uppercase
    text = (
        "g fmnc wms bgbl'r rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb"
        " rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. ")
    text2 = "map"
    for x in range(0, 26):
        text = text.replace(letters[x - 2], uletters[x])
        text2 = text2.replace(letters[x - 2], uletters[x])
    print(text.lower())
    print(text2.lower())