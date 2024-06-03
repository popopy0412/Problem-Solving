def rec(now,k):
    if k==(1<<n)-1: return 0
    if d[now][k]!=1e9: return d[now][k]
    for i in range(n):
        if k&1<<i==0: d[now][k]=min(d[now][k],l[now][i]+rec(now+1,k|1<<i))
    return d[now][k]
n=int(input())
l=[[*map(int,input().split())] for _ in range(n)]
d=[[1e9 for _ in range(1<<n)] for _ in range(n)]
print(rec(0,0))