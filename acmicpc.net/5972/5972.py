import sys
from heapq import *
ip=sys.stdin.readline
n,m=map(int,ip().split())
d,ck=[1e9]*-~n,[0]*-~n
l,q=[[] for _ in range(n+1)],[]
for _ in range(m):
    a,b,c=map(int,ip().split())
    l[a].append([b,c])
    l[b].append([a,c])

for b,c in l[1]:
    heappush(q,[c,b])
    d[b]=c

ck[1]=1
d[1]=0

while q:
    c,now=heappop(q)
    ck[now]=1
    for nxt,nc in l[now]:
        if ck[nxt]: continue
        if d[nxt] > c+nc:
            d[nxt]=c+nc
            heappush(q,[d[nxt],nxt])
print(d[n])