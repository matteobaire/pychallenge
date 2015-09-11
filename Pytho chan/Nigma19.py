__author__ = 'Matteo'

import email
import wave
import array

message = open('pc19_mail.txt')
emsg = email.message_from_file(message)

for index, part in enumerate(emsg.walk()):
    if part.get_content_maintype() == 'multipart':
        continue
    filename = 'indians.wav'
    print 'Writing file: ', filename
    try:
        fp = open(filename, 'wb')
        fp.write(part.get_payload(decode=True))
        fp.close()
        break
    except Exception, e:
        print 'Excepted: ', e

w_in = wave.open(filename, 'rb')
w_out = wave.open('pc19_' + filename, 'wb')

w_out.setnchannels(w_in.getnchannels())
w_out.setsampwidth(w_in.getsampwidth())
w_out.setframerate(w_in.getframerate())
w_out.setnframes(w_in.getnframes())

arr = array.array('i')
arr.fromstring(w_in.readframes(w_in.getnframes()))
arr.byteswap()

print 'Writing file: pc19_' + filename
w_out.writeframes(arr.tostring())

w_in.close()
w_out.close()