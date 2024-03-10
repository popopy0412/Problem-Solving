a=" "+input(); b=" "+input()
n=len(a); m=len(b)
dy=[[0 for _ in range(m)] for _ in range(n)]
path=[[0 for _ in range(m)] for _ in range(n)]
for i in range(1,n):
    for j in range(1,m):
        if a[i] == b[j]:
            dy[i][j] = dy[i-1][j-1]+1
            path[i][j] = 3
        else:
            dy[i][j] = max(dy[i-1][j], dy[i][j-1])
            if dy[i-1][j] > dy[i][j-1]: path[i][j] = 1
            else: path[i][j] = 2
i=n-1; j=m-1
ans=""
while path[i][j] != 0:
    if path[i][j] == 3:
        ans=a[i]+ans
        i-=1; j-=1
    elif path[i][j] == 1: i-=1
    else: j-=1
print(f'{dy[n-1][m-1]}\n'+ans)