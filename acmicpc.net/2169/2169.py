import sys
ip=sys.stdin.readline
n,m=map(int,ip().split())
l=[[*map(int,ip().split())] for _ in range(n)]
d=[[-1e8]*m for _ in range(n)]
d2=[[-1e8]*m for _ in range(n)]
def solve():
    for i in range(n):
        if i==0:
            for j in range(m):
                d[i][j]=d2[i][j]=l[i][j]+(d[i][j-1] if j else 0)
            continue
        for j in range(m):
            if 0<=i-1: d[i][j]=max(d[i][j], max(d[i-1][j],d2[i-1][j])+l[i][j])
            if 0<=j-1: d[i][j]=max(d[i][j], d[i][j-1]+l[i][j])
        for j in range(m-1,-1,-1):
            if 0<=i-1: d2[i][j]=max(d2[i][j], max(d[i-1][j],d2[i-1][j])+l[i][j])
            if j+1<m: d2[i][j]=max(d2[i][j], d2[i][j+1]+l[i][j])
    print(max(d[n-1][m-1], d2[n-1][m-1]))
solve()