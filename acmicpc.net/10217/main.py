from heapq import *
import sys
ip=sys.stdin.readline
il=lambda x:[[x for _ in range(10001)] for _ in range(n+1)]
def dijk():
    q=[[0,0,1]]
    while q:
        d,c,now=heappop(q)
        if dis[now][c]!=d: continue
        for next,cost,dist in l[now]:
            nc,nd=c+cost,d+dist
            if nc>m: continue
            if dis[next][nc]>nd:
                for i in range(nc,m+1):
                    if dis[next][i]<=nd: break
                    dis[next][i]=nd
                heappush(q,[nd,nc,next])
ip()
n,m,k=map(int,ip().split())
dis,ck=il(1e9),il(0)
dis[1]=[0]*10001
l=[[] for _ in range(n+1)]
for i in range(k):
    u,v,c,d=map(int,ip().split())
    l[u].append([v,c,d])
for i in range(1,n+1): l[i].sort()
dijk()
print(min(dis[n]) if min(dis[n])!=1e9 else 'Poor KCM')