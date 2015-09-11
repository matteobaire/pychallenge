# coding=utf-8
__author__ = 'Matteo'

import xmlrpclib

'''nel file evil4.jpg (Nigma12) aperto con notepad c'è scritto Bert is Evil, go back!
occorre chiamare Bert con XML-RPC'''

conn = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

print conn.phone("Bert")