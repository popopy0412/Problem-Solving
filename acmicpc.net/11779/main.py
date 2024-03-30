from heapq import *
import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
v=[[] for _ in range(n+1)]
ck=[0]*-~n
d=[10**10]*-~n
prev=[0]*-~n
q=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    if a==b: continue
    v[a].append((b,c))
x,y=map(int,input().split())
d[x]=0
ck[x]=1
for e in v[x]:
    heappush(q,(e[1],e[0]))
    d[e[0]]=min(d[e[0]],e[1])
    prev[e[0]]=x
while q:
    cost,now=heappop(q)
    if ck[now]: continue
    ck[now] = 1
    for e in v[now]:
        next,cost=e
        if not ck[next] and d[next] > d[now]+cost:
            d[next] = d[now]+cost
            prev[next] = now
            heappush(q,(d[next],next))
path=[]
now=y
while now:
    path.append(now)
    now=prev[now]
print(d[y])
print(len(path))
print(*path[::-1])