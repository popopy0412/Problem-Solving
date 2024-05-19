import sys
ip=sys.stdin.readline
n,m=map(int,ip().split())
l=[[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,ip().split())
    l[a][b]=l[b][a]=1
ans=n*(n-1)*(n-2)//6
for i in range(1,n-1):
    for j in range(i+1,n):
        for k in range(j+1,n+1):
            ans-=l[i][j]|l[j][k]|l[i][k]
print(ans)