#implementing cbc mode in aes....
from Crypto.Cipher import AES


vector = b'0000000000000000'
key = b'YELLOW SUBMARINE'
text=open('s2c10.txt', 'r').read()
cipher = AES.new(key,AES.MODE_CBC,IV=vector)
ciphertext=cipher.encrypt(text)
print(ciphertext)