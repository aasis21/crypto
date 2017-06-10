

def xor(str1,str2):
    int1=int(str1,16)
    int2=int(str2,16)
    int_out=int1^int2
    hex_out=hex(int_out)[2:]
    return hex_out

a='1c0111001f010100061a024b53535009181c'
b='686974207468652062756c6c277320657965'

c=xor(a,b)
print(c)

