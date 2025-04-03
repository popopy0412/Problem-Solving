from collections import *
INF=10**8
MAX=500000
ans=-1
n,k=map(int,input().split())
ck=[[-1]*2 for _ in range(MAX+1)]
ck[n][0]=0
d=deque([n])
c=0
while d:
    k+=c
    if k>MAX: break
    if ck[k][c%2]>-1: ans=c;break
    for _ in range(len(d)):
        now=d.popleft()
        for nxt in [now-1,now+1,now*2]:
            b=(-~c)%2
            if not 0<=nxt<=MAX: continue
            if ck[nxt][b]!=-1: continue
            ck[nxt][b]=ck[now][c%2]+1
            d.append(nxt)
    c+=1
print(ans)