__author__ = 'Matteo'

import smtplib
import email
import md5
import array


'''apology = email.Message.Message()
apology.add_header('To', 'leopold.moz@pythonchallenge.com')
apology.add_header('From', "mbdigital@virgilio.it")
apology.add_header('Subject', 'Apology')
apology.set_payload('Sorry!')
print apology.as_string()
server = smtplib.SMTP('localhost')
server.sendmail(apology['from'], apology['to'], apology.as_string())
server.quit()'''


def sub(data, good_md5):
    allchars = map(chr, range(256))
    for i, oldch in enumerate(data):
        for newch in allchars:
            data[i] = newch
            if md5.new(data).hexdigest() == good_md5:
                return True
        data[i] = oldch
    return False


data = array.array("c", open("mybroken.zip", "rb").read())
sub(data, "bbb8b499a0eef99b52c7f13f4e78c24b")
f = open("repaired.zip", "wb")
f.write(data)
f.close()