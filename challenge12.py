import base64
from Crypto.Cipher import AES
import PKCS7

encodedSuffix = b'''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK'''
key = None

def encryption_oracle(s):
    key = b'YELLOW SUBMARINE'
    cipher = AES.new(key, AES.MODE_ECB)
    s = PKCS7.encode(s + base64.b64decode(encodedSuffix), 16)
    return cipher.encrypt(s)

def findBlockSize(encryption_oracle):
    l = len(encryption_oracle(b''))
    i = 1
    while True:
        s = bytes([0] * i)
        t = encryption_oracle(s)
        if len(t) != l:
            return len(t) - l
        i += 1

def findNextByte(encryption_oracle, blocksize, knownBytes):
    s = bytes([0] * (blocksize - (len(knownBytes) % blocksize) - 1))
    d = {}
    for i in range(256):
        t = encryption_oracle(s + knownBytes + bytes([i]))
        d[t[0:len(s) + len(knownBytes) + 1]] = i
    t = encryption_oracle(s)
    u = t[0:len(s) + len(knownBytes) + 1]
    if u in d:
        return d[u]
    return None

if __name__ == '__main__':
    blocksize = findBlockSize(encryption_oracle)
    s = b''
    while True:
        b = findNextByte(encryption_oracle, blocksize, s)
        if b is None:
            break
        s += bytes([b])
    print(s)

