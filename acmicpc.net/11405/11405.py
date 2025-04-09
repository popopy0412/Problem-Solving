from collections import *
n,m=map(int,input().split())
need=[0]+[*map(int,input().split())]
book=[0]+[*map(int,input().split())]
MAX=n+m+2
v=[[] for _ in range(MAX)]
idx=[[0]*MAX for _ in range(MAX)]
cap=[[0]*MAX for _ in range(MAX)]
flow=[[0]*MAX for _ in range(MAX)]
parent=[-1]*MAX

def spfa():
    global parent
    s=0
    parent=[-1]*MAX
    inQ=[0]*MAX
    count=[0]*MAX
    dist=[1e10]*MAX
    q=deque([0])

    inQ[s]=1
    dist[s]=0
    count[s]+=1
    while q:
        now=q.popleft()
        inQ[now]=0

        for nxt,c in v[now]:
            if cap[now][nxt] > flow[now][nxt] and dist[now] + c < dist[nxt]:
                parent[nxt]=now
                dist[nxt] = dist[now] + c
                if inQ[nxt]==0:
                    count[nxt]+=1
                    if count[nxt] >= MAX: return 0
                    q.append(nxt)
                    inQ[nxt]=1
    return parent[MAX-1] != -1

for i in range(1,n+1):
    idx[0][i]=len(v[0]); v[0].append([i,0]);
    idx[i][0]=len(v[i]); v[i].append([0,0])
    cap[0][i]=need[i]

for i in range(1,m+1):
    b=[0]+[*map(int,input().split())]
    for j in range(1,n+1):
        idx[j][n+i]=len(v[j]); v[j].append([n+i,b[j]])
        idx[n+i][j]=len(v[n+i]); v[n+i].append([j,-b[j]])
        cap[j][n+i]=need[j]
        
for i in range(1,m+1):
    idx[n+i][MAX-1]=len(v[n+i]); v[n+i].append([MAX-1,0])
    idx[MAX-1][n+i]=len(v[MAX-1]); v[MAX-1].append([n+i,0])
    cap[n+i][MAX-1]=book[i]

ans=0
while spfa():
    s,mFlow=MAX-1,1e10
    while s!=0:
        diff = cap[parent[s]][s] - flow[parent[s]][s]
        mFlow = min(mFlow, diff)
        s=parent[s]

    s=MAX-1
    while s!=0:
        flow[parent[s]][s] += mFlow
        flow[s][parent[s]] -= mFlow
        ans+=v[parent[s]][idx[parent[s]][s]][1]*mFlow
        s=parent[s]
    
print(ans)