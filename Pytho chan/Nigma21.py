import zlib
import bz2

h = open("package.pack", 'rb')  # Hides within the ZIP file we got at the
dataa = h.read()  # end of level 20.
h.close()

# decom = zlib.decompressobj()
# dataa = decom.decompress(dataa)


def unwrap(data):
    history = ""
    while True:
        try:
            data = zlib.decompress(data)
            history += 'z'
            #print 'z'
        except:
            try:
                data = bz2.decompress(data)
                history += 'b'
                #print 'b'
            except:
                history += '\n'
                #print '\n'
                data = data[::-1]
                if history[-3:] == '\n\n\n':
                    break
    return history

print unwrap(dataa).replace('z',' ')