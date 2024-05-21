import sys
sys.setrecursionlimit(10**6)
ip=sys.stdin.readline
def dfs(now):
    global cnt
    ck[now]=cnt
    cnt+=1
    for next in l[now]:
        if ck[next]==0: dfs(next)
n,m,r=map(int,ip().split())
k=[[*map(int,ip().split())] for _ in range(m)]
l=[[] for _ in range(n+1)]
ck=[0]*-~n
cnt=1
for a,b in k:
    l[a].append(b)
    l[b].append(a)
dfs(r)
print(*ck[1:])