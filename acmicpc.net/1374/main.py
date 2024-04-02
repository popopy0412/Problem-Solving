from heapq import *
from bisect import *
import sys
input=sys.stdin.readline
ans,n=0,int(input())
i1,x1,y1=[],[],[]
i2,x2,y2=[],[],[]
l,ck=[],[0]*-~n
for _ in range(n):
    i,x,y=map(int,input().split())
    l.append([x,y,i])
l.sort()
x1,y1,i1=zip(*l)
l.sort(key=lambda x:(x[1],x[0]))
x2,y2,i2=zip(*l)
for i in range(n):
    a,b,c=x2[i],y2[i],i2[i]
    if ck[c]: continue
    ck[c]=1
    ans+=1
    t=0
    while True:
        t=bisect_left(x1,b,lo=t)
        while t < n and ck[i1[t]]: t+=1
        if t==n: break
        ck[i1[t]]=1
        b=y1[t]
print(ans)