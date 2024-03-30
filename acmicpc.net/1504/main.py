import sys
from heapq import *
input=sys.stdin.readline

def solve(ck,q,d,t):
    while q:
        cost,now=heappop(q)
        if ck[now]: continue
        ck[now]=1
        for edge in t[now]:
            cost,next=edge
            if d[now]+cost < d[next]:
                d[next] = d[now]+cost
                heappush(q,(d[next],next))

n,e=map(int,input().split())
l,t=[],[[] for _ in range(n+1)]
INF=10**10
d1,d2,d3=[INF]*-~n,[INF]*-~n,[INF]*-~n
ck1,ck2,ck3=[0]*-~n,[0]*-~n,[0]*-~n

for _ in range(e):
    a,b,c=map(int,input().split())
    t[a].append((c,b))
    t[b].append((c,a))
u,v=map(int,input().split())

d1[1],d2[u],d3[v]=0,0,0
q1,q2,q3=[(0,1)],[(0,u)],[(0,v)]
solve(ck1,q1,d1,t)
solve(ck2,q2,d2,t)
solve(ck3,q3,d3,t)

ans=min(d1[u]+d2[v]+d3[n], d1[v]+d2[n]+d3[u])
if ans >= INF: print(-1)
else: print(ans)