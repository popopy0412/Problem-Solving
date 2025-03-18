import sys
from collections import *
input=sys.stdin.readline
def ch(s):
    t=[]
    for c in s: t.append('.*C'.index(c))
    return t
def start(l):
    for i in range(n):
        for j in range(m):
            if l[i][j]==2: return i,j
    return -1,-1
ans=10**7
m,n=map(int,input().split())
l=[ch(*input().split()) for _ in range(n)]
ck=[[0]*m for _ in range(n)]
dy=[[[ans,-1] for _ in range(m)] for _ in range(n)]
X=[0,0,1,-1]
Y=[1,-1,0,0]
h,w=start(l)
ck[h][w]=1
q=deque([[h,w,4,-1]])
while q:
    a,b,d,c=q.popleft()
    if (a,b)!=(h,w) and l[a][b]==2:
        ans=c
        continue
    for i in range(d,d+4):
        i%=4
        x,y=a+X[i],b+Y[i]
        t=c+(0 if i==d else 1)
        if 0<=x<n and 0<=y<m and l[x][y]!=1:
            if t<ans and (dy[x][y][1]!=i and dy[x][y][0]>=t or dy[x][y][1]==i and dy[x][y][0]>t):
                dy[x][y]=[t,i]
                q.append([x,y,i,t])
print(ans)