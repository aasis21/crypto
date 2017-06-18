import binascii

#convert a string in ascii to ahex string
def ascii_hex(ascii):
    out=''
    for i in ascii:
        hex_i=hex(ord(i))[2:]
        if len(hex_i)!=2:
            hex_i='0'+hex_i
        out=out+hex_i
    return out


def encode_xor_key(message,key):
    encoded=[]
    for i in message:
        encoded.append(chr(i ^ ord(key[i%len(key)])))

    encoded_str=''.join(e for e in encoded)
    return ascii_hex(encoded_str)





message="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

key='ICE'
print(encode_xor_key(message,key))

