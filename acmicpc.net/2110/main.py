import sys
from bisect import *
input=sys.stdin.readline
n,c,*x=map(int,open(0).read().split())
x.sort()
ans,l,r=0,1,(x[-1]-x[0])//~-c
now=0
while l <= r:
    m = (l+r)//2
    temp=10**9
    now,ck=0,0
    for _ in range(c-1):
        next=bisect_left(x,x[now]+m,lo=now)
        if next == n:
            r,ck=m-1,1
            break
        temp=min(temp,x[next]-x[now])
        now = next
    if ck: continue
    ans=max(ans,temp)
    l=m+1
print(ans)