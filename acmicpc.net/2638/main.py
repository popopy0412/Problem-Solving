from collections import *
n,m=map(int,input().split())
ck=[[0 for _ in range(m)] for _ in range(n)]
X,Y=[0,0,1,-1],[1,-1,0,0]
l=[]
ans=-1
q=deque()
q.append((0,0))
for _ in range(n): l.append(list(map(int,input().split())))
l[0][0]=2

while q:
    x,y=q.popleft()
    for k in range(4):
        nx,ny=x+X[k],y+Y[k]
        if 0 <= nx < n and 0 <= ny < m and not l[nx][ny]:
            l[nx][ny]=2
            q.append((nx,ny))
check=1
while check:
    ans+=1
    check=0
    ck=[[0 for _ in range(m)] for _ in range(n)]
    temp=[]
    for i in range(n):
        for j in range(m):
            if l[i][j] == 1:
                check=1
                cnt=0
                if 0 <= i-1 and l[i-1][j] == 2: cnt+=1
                if i+1 < n and l[i+1][j] == 2: cnt+=1
                if 0 <= j-1 and l[i][j-1] == 2: cnt+=1
                if j+1 < m and l[i][j+1] == 2: cnt+=1
                if cnt >= 2:
                    temp.append((i,j))
                    q=deque()
                    q.append((i,j))
                    ck[i][j]=1
                    while q:
                        x,y=q.popleft()
                        for k in range(4):
                            nx,ny=x+X[k],y+Y[k]
                            if 0 <= nx < n and 0 <= ny < m and not ck[nx][ny] and l[nx][ny] == 0:
                                ck[nx][ny]=1
                                q.append((nx,ny))
    for i in range(n):
        for j in range(m):
            if ck[i][j]: l[i][j] = 2
    for x,y in temp: l[x][y]=2
print(ans)