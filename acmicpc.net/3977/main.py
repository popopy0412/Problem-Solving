from collections import *
import sys
sys.setrecursionlimit(10**6)
ip=sys.stdin.readline
z=lambda:[0]*-~n
il=lambda:[[] for _ in range(n)]
def dfs(now):
    global num,cnt
    s.append(now)
    ck[now]=p=num
    num+=1
    for next in v[now]:
        if ck[next]==0: p=min(p,dfs(next))
        elif fin[next]==0: p=min(p,ck[next])
    if ck[now]==p:
        while True:
            t=s.pop()
            scc[cnt].append(t)
            idx[t]=cnt
            if t==now: break
        cnt+=1
    fin[now]=1
    return p
for I in range(T:=int(ip())):
    n,m=map(int,ip().split())
    num,cnt=1,0
    s,nv=[],[]
    v,scc=il(),il()
    ck,fin,idx,ind=z(),z(),z(),z()
    scc=[[] for _ in range(n)]
    for _ in range(m):
        a,b=map(int,ip().split())
        v[a].append(b)
    ip()
    for i in range(n):
        if ck[i]==0: dfs(i)
    for i in range(n):
        for now in v[i]:
            if idx[now]!=idx[i]:ind[idx[now]]+=1
    t=[]
    for i in range(cnt):
        if ind[i]==0: t.append(i)
    if len(t)-1: print('Confused')
    else:
        for i in sorted(scc[t[-1]]): print(i)
    if I!=T-1: print()