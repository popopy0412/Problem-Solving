import sys
sys.setrecursionlimit(10**6)
ip=sys.stdin.readline
def dfs(prev,now):
    ck[now]=1
    t=1
    for next in v[now]:
        if next==prev: continue
        if ck[next]: t=0
        else: t=min(t,dfs(now,next))
    return t
T=1
while True:
    n,m=map(int,ip().split())
    if (n,m)==(0,0): break
    print(f'Case {T}: ',end='')
    r,v,ck=[*range(n+1)],[[] for _ in range(n+1)],[0]*-~n
    for _ in range(m):
        a,b=map(int,ip().split())
        v[a].append(b)
        v[b].append(a)
    t=0
    t=sum([dfs(0,i) for i in range(1,n+1) if ck[i]==0])
    print(['No trees.','There is one tree.',f'A forest of {t} trees.'][min(2,t)])
    T+=1