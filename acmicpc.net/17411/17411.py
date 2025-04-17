from collections import *
from bisect import *
MAX=1000001
MOD=10**9+7
n,*k=map(int,open(0).read().split())
s=[]

for v in k:
    if not s: s.append(deque([[v,1]]))
    elif s[-1][0][0]<v:
        x=s[-1][0][1]
        y=bisect_left(s[-1],v,key=lambda x:x[0])
        if y==len(s[-1]): y=0
        else: y=s[-1][y][1]
        s.append(deque([[v,x-y]]))
        s[-1][0][1]%=MOD
    else:
        a=bisect_left(s,v,key=lambda x:x[0][0])
        if a:
            if s[a-1][-1][0]<v: x=0
            else:
                x=bisect_left(s[a-1],v,key=lambda x:x[0])
                x=s[a-1][x][1]
        else: x=0
        if s[a][0][0]==v: s[a][0][1]+=(s[a-1][0][1]-x if a else 1)
        else: s[a].appendleft([v,s[a][0][1]+(s[a-1][0][1]-x if a else 1)])
        s[a][0][1]%=MOD
print(len(s), s[-1][0][1])