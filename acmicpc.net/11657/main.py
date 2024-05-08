import sys
ip=sys.stdin.readline
def solve():
    for i in range(n):
        for a,b,c in l:
            if d[a]!=1e9 and d[b]>d[a]+c:
                if i==n-1: return 1
                d[b]=d[a]+c
    return 0
n,m=map(int,ip().split())
l,d=[],[1e9]*-~n
d[1]=0
for _ in range(m):
    a,b,c=map(int,ip().split())
    l.append((a,b,c))
if(solve()): print(-1)
else:
    for i in range(2,n+1): print(-1 if d[i]==1e9 else d[i])