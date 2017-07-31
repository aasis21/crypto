from Crypto.Cipher import AES
import random
import PKCS7



def get_random_16():
    return bytes(random.getrandbits(8) for i in range(16))

def encryption_oracle(text):
    if random.randrange(2) == 0:
        encrypter = AES.new(get_random_16(),AES.MODE_ECB)
        return encrypter.encrypt(text)
    else:
        cipher = AES.new(get_random_16(), AES.MODE_CBC, IV=get_random_16())
        return cipher.encrypt(text)


def detectMethod(encryption_oracle):
    s = bytes([0] * 100) + 'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc2gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'.encode()
    t = encryption_oracle(PKCS7.encode(s,16))
    if t[16:32] == t[32:48]:
        return 'ECB'
    return 'CBC'

if __name__ == '__main__':
    print(detectMethod(encryption_oracle))