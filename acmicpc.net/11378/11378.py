from collections import *
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
MAX=n+m+3
v=[[] for _ in range(MAX)]
cap=[[0]*MAX for _ in range(MAX)]
flow=[[0]*MAX for _ in range(MAX)]

def max_flow(s,e):
    ans=0
    while 1:
        parent=[-1]*MAX
        q=deque([s])
        end=0
        while q:
            now=q.popleft()
            for nxt in v[now]:
                if parent[nxt] == -1 and cap[now][nxt] > flow[now][nxt]:
                    parent[nxt]=now
                    q.append(nxt)
                    if nxt==e:
                        end=1
                        break
                    
            if end: break

        if parent[e]==-1: break
        x,minF=e,1e10
        while x!=s:
            diff = cap[parent[x]][x] - flow[parent[x]][x]
            minF=min(minF, diff)
            x=parent[x]

        x=e
        while x!=s:
            flow[parent[x]][x] += minF
            flow[x][parent[x]] -= minF
            x=parent[x]
        ans += minF
    return ans

v[MAX-1]=[0]
v[0]=[MAX-1]
cap[MAX-1][0]=min(m,n)
for i in range(1,n+1):
    v[0].append(i)
    v[i].append(0)
    cap[0][i]=1
    _,*b=map(int,input().split())
    for j in b:
        v[i].append(n+j)
        v[n+j].append(i)
        cap[i][n+j]=1
for i in range(m):
    v[n+i+1].append(MAX-2)
    v[MAX-2].append(n+i+1)
    cap[n+i+1][MAX-2]=1
ans=max_flow(MAX-1, MAX-2)
cap[MAX-1][0]=k
flow[MAX-1][0]=flow[0][MAX-1]=0
for i in range(1,n+1): cap[0][i]+=k
print(ans+max_flow(MAX-1, MAX-2))