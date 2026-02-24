import sys
ip=sys.stdin.readline
l=sorted([[*map(int,ip().split())] for _ in range(int(ip()))], key=lambda x:x[0])
s=[]
a=0
for i in l:
    i=i[1]
    while s and s[-1]>=i:
        if s.pop()==i: a-=1
    if i:
        s.append(i)
        a+=1
print(a)