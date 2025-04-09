from collections import *
import sys
ip=sys.stdin.readline
n,m=map(int,ip().split())
MAX=n*2+3
cap=[[0]*MAX for _ in range(MAX)]
flow=[[0]*MAX for _ in range(MAX)]
v=[[] for _ in range(MAX)]

def max_flow(s, e):
    ans=0
    while 1:
        parent=[-1]*MAX
        q=deque([s])
        while q:
            now=q.popleft()
            for nxt in v[now]:
                if parent[nxt]==-1 and cap[now][nxt] > flow[now][nxt]:
                    parent[nxt]=now
                    if nxt==e: break
                    q.append(nxt)

        if parent[e]==-1: break

        x=e
        while x!=s:
            flow[parent[x]][x] += 1
            flow[x][parent[x]] -= 1
            x=parent[x]
        ans+=1
    return ans
        
for i in range(1,n+1):
    v[i].append(i+n)
    v[i+n].append(i)
    cap[i][i+n]=1 if i>2 else 1e10

for i in range(m):
    a,b=map(int,ip().split())
    v[a].append(b+n)
    v[a+n].append(b)
    v[b].append(a+n)
    v[b+n].append(a)
    cap[a+n][b]=cap[b+n][a]=1
print(max_flow(1,n+2))