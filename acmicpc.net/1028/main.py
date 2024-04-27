n,m=map(int,input().split())
ans=0
l=[]
d=[[[0,0] for _ in range(m)] for _ in range(n)]
h=[[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    l.append([*map(int,input())])
    for j in range(m):
        if l[i][j]:
            d[i][j]=[1,1]
            h[i][j]=1
X=[-1,-1]
Y=[-1,1]
for i in range(n):
    for j in range(m):
        if l[i][j]:
            for t in range(2):
                x,y=i+X[t],j+Y[t]
                if 0<=x<n and 0<=y<m and l[x][y]: d[i][j][t]=d[x][y][t]+1
            if d[i][j][0]>1 and d[i][j][1]>1:
                a,b=d[i][j]
                k=min(a,b)
                for t in range(k,0,-1):
                    if d[i-t+1][j-t+1][1]>=t and d[i-t+1][j+t-1][0]>=t:
                        h[i][j]=t
                        break
            ans=max(ans,h[i][j])
print(ans)
