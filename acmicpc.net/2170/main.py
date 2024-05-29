import sys
ip=sys.stdin.readline
a,b=-1e9,-1e9
ans=0
l=[[*map(int,ip().split())] for _ in range(int(ip()))]
l.sort()
for x,y in l:
    if b<x:
        ans+=b-a
        a,b=x,y
    else: b=max(b,y)
print(int(ans+b-a))
