import sys
sys.setrecursionlimit(10**6)
ip=sys.stdin.readline
def dfs(now):
    c[now]=1
    for next in v[now]:
        if ck[next]==0:
            ck[next]=1
            dfs(next)
            c[now]+=c[next]
n,r,q=map(int,ip().split())
v=[[] for _ in range(n+1)]
c,ck=[0]*-~n,[0]*-~n
for _ in range(n-1):
    a,b=map(int,ip().split())
    v[a].append(b)
    v[b].append(a)
ck[r]=1
dfs(r)
for _ in range(q): print(c[int(ip())])