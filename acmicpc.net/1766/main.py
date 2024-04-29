from heapq import *
import sys
n,m=map(int,input().split())
l,p,q=[[] for _ in range(n+1)],[0]*-~n,[]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    l[a].append(b)
    p[b]+=1
for i in range(1,n+1):
    if p[i]==0: heappush(q,i)
while q:
    t=heappop(q)
    print(t,end=' ')
    for i in l[t]:
        p[i]-=1
        if p[i]==0: heappush(q,i)