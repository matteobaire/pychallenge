__author__ = 'Matteo'

import re
import urllib
import urllib2
import bz2
import xmlrpclib

# First of all, get the data that is hidden within the "Set-Cookie" headers:

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s"
nn_rep = re.compile("the next busynothing is (\d+)")
cookie_val = re.compile("info=([^;]+);")
result = []
n = "12345"

while True:
    h = urllib.urlopen(uri % n)
    next = h.read()
    cookie = h.info().getheader("Set-Cookie")
    h.close()

    cval = cookie_val.search(cookie)

    if cookie and cval:
        result.append(urllib.unquote_plus(cval.group(1)))

    try:
        n = nn_rep.search(next).group(1)
    except:
        break

print bz2.decompress("".join(result))

# Get Leopold's phone numer using the code for level 13:

conn = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

print conn.phone("Leopold")

# Now phone Mozart's father and tell him that "the flowers are on their way":

uri = "http://www.pythonchallenge.com/pc/stuff/violin.php"
msg = "the flowers are on their way"
req = urllib2.Request(
    uri, headers={"Cookie": "info=" + urllib.quote_plus(msg)}
)

print urllib2.urlopen(req).read()