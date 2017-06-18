#----hamming distance------http://classroom.synonym.com/calculate-hamming-distance-2656.html
import base64
from freq import score
from s1c5 import encode_xor_key
def hamming_no(str1,str2):
    ham=0
    if len(str1)==len(str2):
        for i in range(len(str1)):
            ham_bin=bin(str1[i]^str2[i])
            for each in ham_bin[2:]:
                ham=ham + int(each)
        return ham/len(str1)
    else:
        return("different length string")


def open_file(file):
    x = base64.b64decode(open('s1c6.txt', 'r').read())
    return x

def find_keylength(s):
    hams=[]
    for keylength in range(2,40):
        hams.append((keylength,hamming_no(s[:keylength],s[keylength:(2*keylength)])))

    def sc(a):
        return a[1]

    key=min(hams,key=sc)
    print(key[0])
    return key[0]

def give_key(s):
    decoded_list=[]
    for key in range(255):
        decoded = []
        for i in s:
            decoded.append(chr(ord(i) ^ key))

        decoded_str = ''.join(e for e in decoded)
        decoded_list.append(decoded_str)
    return decoded_list.index(max(decoded_list, key=score))

def find_key(s,keylen):
    breaked_strings = [''] * keylen
    for i in range(len(s)):
        breaked_strings[i%keylen]=breaked_strings[i%keylen] + chr(s[i])
    key=''
    for i in range(keylen):
        key=key + chr(give_key(breaked_strings[i]))

    print(key)





file='s1c6.txt'
key=find_key(open_file(file),29)
print(encode_xor_key(open_file(file),key))





