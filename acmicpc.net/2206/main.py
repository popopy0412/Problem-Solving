from collections import *
n,m=map(int,input().split())
l,ck=[],[[0 for _ in range(m)] for _ in range(n)]
X,Y=[0,0,1,-1],[1,-1,0,0]
for i in range(n):l.append([int(i) for i in input()])
q=deque()
q.append((0,0,1,1))
ck[0][0]=2
while q:
    x,y,c,d=q.popleft()
    if (x,y)==(n-1,m-1):
        print(d)
        exit(0)
    for i in range(4):
        a,b=x+X[i],y+Y[i]
        if 0<=a<n and 0<=b<m and ck[a][b]<c+1 and c-l[a][b]>=0:
            ck[a][b]=c+1
            q.append((a,b,c-l[a][b],d+1))
print(-1)