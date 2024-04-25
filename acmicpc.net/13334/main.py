from heapq import *
import sys
ip=sys.stdin.readline
l,q=[],[]
n=int(ip())
for _ in range(n): l.append([*sorted(map(int,ip().split()))])
d=int(ip())
l.sort(key=lambda x:x[1])
a=0
for s,e in l:
    heappush(q,s)
    while q and q[0]<e-d: heappop(q)
    a=max(a,len(q))
print(a)