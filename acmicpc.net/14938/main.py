n,m,r=map(int,input().split())
l=[0]+list(map(int,input().split()))
ans,INF=0,10**9
p=[[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(r):
    a,b,c=map(int,input().split())
    p[a][b]=p[b][a]=c
for k in range(1,n+1):
    p[k][k]=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i != j != k != i and p[i][k] != INF and p[k][j] != INF:
                p[i][j] = min(p[i][j],p[i][k]+p[k][j])
for d in p[1:]:
    t=0
    for i in range(1,n+1):
        if d[i] <= m: t+=l[i]
    ans=max(ans,t)
print(ans)
