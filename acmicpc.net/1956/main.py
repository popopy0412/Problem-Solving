import sys
ip=sys.stdin.readline
n,m=map(int,ip().split())
v=[[1e9 for _ in range(n+1)] for _ in range(n+1)]
ans=1e9
for _ in range(m):
    a,b,c=map(int,ip().split())
    v[a][b]=c
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            v[i][j]=min(v[i][j],v[i][k]+v[k][j])
for i in range(1,n+1): ans=min(ans,v[i][i])
print(-1 if ans==1e9 else ans)