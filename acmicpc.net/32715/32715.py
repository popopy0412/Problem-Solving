import sys
ip=sys.stdin.readline
n,m=map(int,ip().split())
k=int(ip())
l=[[*map(int,ip().split())] for _ in range(n)]
d=[[[0,0] for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if l[i][j]==0: continue
        if i and l[i-1][j]: d[i][j][0]=d[i-1][j][0]+1
        if j and l[i][j-1]: d[i][j][1]=d[i][j-1][1]+1
ans=0
for i in range(k,n):
    for j in range(k,m):
        if l[i][j] and i+k<n and j+k<m and d[i][j][0]>=k and d[i+k][j][0]>=k and d[i][j][1]>=k and d[i][j+k][1]>=k: ans+=1

print(ans)