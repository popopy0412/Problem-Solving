import sys
from heapq import *
from collections import *
il=lambda:[*map(int,sys.stdin.readline().split())]
def bfs():
    q=deque([y])
    ck=[False]*n
    ck[y]=True
    while q:
        now=q.popleft()
        if now==x: continue
        for prv in path[now]:
            if ck[prv]==0:
                ck[prv]=True
                q.append(prv)
            cke[e[prv][now]]=True

while True:
    n,m=il()
    if (n,m)==(0,0): break
    q=[]
    v=[[] for _ in range(n)]
    e=[[-1 for _ in range(n)] for _ in range(n)]
    cke=[False]*m
    ans=[1e9]*n
    x,y=il()
    path=[[] for _ in range(n)]
    ans[x]=0
    for i in range(m):
        a,b,c=il()
        v[a].append((b,c))
        e[a][b]=i
        if a==x:
            heappush(q,(c,b))
            ans[b]=c
            path[b].append(a)
    while q:
        co,now=heappop(q)
        if ans[now] < co: continue
        for next,cost in v[now]:
            if co+cost <= ans[next]:
                if co+cost < ans[next]:
                    path[next]=[now]
                    ans[next]=co+cost
                    heappush(q,(co+cost,next))
                else: path[next].append(now)
    
    bfs()

    ans=[1e9]*n
    ans[x]=0
    for b,c in v[x]:
        if cke[e[x][b]]: continue
        heappush(q,(c,b))
        ans[b]=c
    while q:
        co,now=heappop(q)
        if ans[now] < co: continue
        for next,cost in v[now]:
            if cke[e[now][next]]: continue
            if co+cost < ans[next]:
                ans[next]=co+cost
                heappush(q,(ans[next],next))
    print(-1 if ans[y]==1e9 else ans[y])