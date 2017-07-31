import binascii
import itertools

def score(x):
    k = 16
    blocks = [x[i:i+k] for i in range(0, len(x), k)]
    pairs = itertools.combinations(blocks, 2)
    same = 0
    count = 0
    for p in pairs:
        if p[0] == p[1]:
            same += 1
    return same



def check(filename):
    f = open(filename, 'r')
    ans=['',0]
    for line in f:
        s = binascii.unhexlify(line[:-1])
        sc=score(s)
        if sc > ans[1]:
            ans=[s,sc]


    print(ans)


