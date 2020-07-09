from base64 import *

# we have 'a' as multiple line string
a = '''

hello

'''  # string ended here

a = str.encode(a)  # string to byte-like object
a = b64encode(a)  # b64 encoded

print('encoded: ',a)

a = b64decode(a)  # b64 decoded
a = a.decode()  # byte-like object to string

print('decoded: ',a)


