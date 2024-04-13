from collections import *
import sys
sys.setrecursionlimit(10**6)
ip=sys.stdin.readline
il=lambda:[*map(int,ip().split())]
ic=lambda:[0]*-~n
it=lambda:[[] for _ in range(n+1)]
id,cnt=0,0
def dfs(now):
    global id,cnt
    id+=1
    parent=ck[now]=id
    st.append(now)
    for next in v[now]:
        if not ck[next]:
            parent = min(parent, dfs(next))
        elif not fin[next]:
            parent = min(parent, ck[next])
    
    if parent == ck[now]:
        cnt+=1
        while True:
            t=st.pop()
            co[cnt]+=c[t]
            scc[t]=cnt
            fin[t]=1
            if t == now: break
    return parent
def bfs(now):
    q=deque()
    q.append(now)
    ck=ic()
    ck[now]=1
    while q:
        now=q.popleft()
        for next in np[now]:
            prv[next]+=1
            if ck[next]==0:
                ck[next]=1
                q.append(next)
def topo(now):
    q=deque()
    q.append(now)
    ck=[[0,0] for _ in range(n+1)]
    ans=ck[now][go[now]]=co[now]
    while q:
        now=q.popleft()
        for next in np[now]:
            if go[next]: ck[next][1]=max(max(ck[now])+co[next], ck[next][1])
            else: ck[next][0]=max(max(ck[now])+co[next], ck[next][0])
            if ck[next][1]: ans=max(ans,ck[next][1])
            prv[next]-=1
            if prv[next]==0: q.append(next)
    return ans
n,m=il()
scc,ck,fin,co,go=ic(),ic(),ic(),ic(),ic() 
c,st=[0],[]
v=it()
for _ in range(m):
    a,b=il()
    v[a].append(b)
for _ in range(n): c.append(int(ip()))
for i in range(1,n+1):
    if not fin[i]: dfs(i)
s,p=il()
x,np,prv=il(),it(),ic()
for i in x: go[scc[i]]=1
for i in range(1,n+1):
    for j in v[i]:
        if scc[i] != scc[j]: np[scc[i]].append(scc[j])
for i in range(1,cnt+1): np[i]=list(set(np[i]))
bfs(scc[s])
print(topo(scc[s]))