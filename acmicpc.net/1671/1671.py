from collections import *
n=int(input())
spec=[[]]+[[*map(int,input().split())] for _ in range(n)]
MAX=n*2+3
cap=[[0]*MAX for _ in range(MAX)]
flow=[[0]*MAX for _ in range(MAX)]
v=[[] for _ in range(MAX)]

def comp(i, j):
    if spec[i][0]>=spec[j][0] and spec[i][1]>=spec[j][1] and spec[i][2]>=spec[j][2]:
        v[i].append(n+j)
        v[n+j].append(i)
        cap[i][n+j]=1
        return 0
    return 1

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

v[MAX-2].append(0)
v[0].append(MAX-2)
cap[MAX-2][0]=n-1
for i in range(1,n+1):
    v[0].append(i)
    v[i].append(0)
    v[n+i].append(MAX-1)
    v[MAX-1].append(n+i)
    cap[0][i]=2
    cap[n+i][MAX-1]=1
    for j in range(i+1,n+1):
        if comp(i,j): comp(j,i)
        

print(n-max_flow(MAX-2,MAX-1))