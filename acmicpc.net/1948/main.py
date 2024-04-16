from collections import *
import sys
ip=sys.stdin.readline
il=lambda:[*map(int,ip().split())]
iz=lambda:[0]*-~n
iv=lambda:[[] for _ in range(n+1)]
n=int(ip());m=int(ip())
ck,h,prv,v,path=iz(),iz(),iz(),iv(),iv()
for _ in range(m):
    a,b,c=il()
    v[a].append((b,c))
    prv[b]+=1
x,y=il()
q=deque([x])
while q:
    now=q.popleft()
    for next,cost in v[now]:
        n_cost=h[now]+cost
        if h[next] <= n_cost:
            if h[next] == n_cost: path[next].append(now)
            else: path[next]=[now]
            h[next]=n_cost
        prv[next]-=1
        if prv[next]: continue
        q.append(next)

print(h[y])
q.append(y)
ck[y]=1
ans=0
while q:
    now=q.popleft()
    ans+=len(path[now])
    for prev in path[now]:
        if ck[prev]: continue
        ck[prev]=1
        q.append(prev)
print(ans)