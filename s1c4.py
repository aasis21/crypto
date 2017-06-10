from s1c3 import decode
from freq import score
def find(a):
    file=open(a,'r')
    d=[]
    ans=open('s1a4.txt','w')
    for i,line in enumerate(list(file)):
        print(type(line[:-1]))
        print(decode(line[:-1]),i)
        d.append(decode(line[:-1]))
        ans.write(decode(line[:-1]))
        ans.write(str(i))
        ans.write('\n')

    return max(d,key=score)

a='s1c4.txt'
print(find(a))


# ans----Now that the party is jumping-----line 170





