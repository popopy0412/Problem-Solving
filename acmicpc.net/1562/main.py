n,m=int(input()),1<<10
d=[[[0 for _ in range(10)] for _ in range(m)] for _ in range(n+1)]
for i in range(1,10): d[1][1<<i][i]=1
for i in range(2,n+1):
    for j in range(10):
        for k in range(j,11):
            now=2**k-1
            for t in range(j):
                d[i][now|1<<j][j]+=d[i-1][now][j-1]
                now^=(1<<t)
        for k in range(j+2):
            now=~(2**k-1)&m-1
            for t in range(9-j):
                d[i][now|1<<j][j]+=d[i-1][now][j+1]
                now^=(1<<9-t)
print(sum(d[n][m-1])%10**9)