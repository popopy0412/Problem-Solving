n=int(input())
l=[[0]*-~n]
d=[[[0,0,0] for _ in range(n+1)] for _ in range(n+1)]
d[1][2][0]=1
for _ in range(n): l.append([0]+list(map(int,input().split())))
for i in range(1,n+1):
    for j in range(1,n+1):
        if l[i][j]: continue
        d[i][j][0] += d[i][j-1][0] + d[i][j-1][2]
        d[i][j][1] += d[i-1][j][1] + d[i-1][j][2]
        if not(l[i-1][j] or l[i][j-1]): d[i][j][2] += sum(d[i-1][j-1])
print(sum(d[n][n]))