import binascii
from freq import score

def decode(encoded_hex):
    decoded_list=[]
    if len(encoded_hex)%2==0:
        str_in_ascii_chr=binascii.unhexlify(encoded_hex)
        for key in range(255):
            decoded = []
            for ascii_dec in str_in_ascii_chr:
                decoded.append(chr(ascii_dec^key))

            decoded_str=''.join(e for e in decoded)
            decoded_list.append(decoded_str)
        return max(decoded_list,key=score)
    else:
        return('////////////////////')





