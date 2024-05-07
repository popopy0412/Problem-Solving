import sys
ip=sys.stdin.readline
def dfs(v,ck,now):
    s=[[now,0]]
    ck[now]=0
    while s:
        now,c=s.pop()
        for next in v[now]:
            if ck[next]==-1:
                ck[next]=c^1
                s.append([next,c^1])
            elif ck[next]==c: return 1
    return 0
def solve():
    n,m=map(int,ip().split())
    v,ck=[[] for _ in range(n+1)],[-1]*-~n
    for _ in range(m):
        a,b=map(int,ip().split())
        v[a].append(b)
        v[b].append(a)
    for i in range(1,n):
        if ck[i]==-1 and dfs(v,ck,i): return 1
    return 0
for _ in range(int(ip())): print('NO' if solve() else 'YES')