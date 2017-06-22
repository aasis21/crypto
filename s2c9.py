import PKCS7
text = "YELLOW SUBMARINE"
print(PKCS7.encode(text,20))
print(PKCS7.decode(PKCS7.encode(text,20)))