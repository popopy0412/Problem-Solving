import sys
sys.setrecursionlimit(10**6)
ic=lambda:[[0 for _ in range(m)] for _ in range(n)]
def dfs(a,b):
    for i in range(4):
        x,y=a+X[i],b+Y[i]
        if 0<=x<n and 0<=y<m and l[a][b]>l[x][y]:
            if ck[x][y]: d[a][b]+=d[x][y]
            else:
                d[a][b]+=dfs(x,y)
                ck[x][y]=1
    return d[a][b]
n,m=map(int,input().split())
l,d,ck=[],ic(),ic()
d[n-1][m-1]=1
X,Y=[0,0,1,-1],[1,-1,0,0]
for _ in range(n): l.append([*map(int,input().split())])
print(dfs(0,0))