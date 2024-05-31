from heapq import *
from collections import *
def union(x,y):
    x,y=find(x),find(y)
    if x!=y: p[x]=y
def find(x):
    if x==p[x]: return x
    p[x]=find(p[x])
    return p[x]
n,m=map(int,input().split())
l=[[*map(int,input().split())] for _ in range(n)]
X,Y=[0,0,1,-1],[1,-1,0,0]
cnt=0
ck=[[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if l[i][j] and ck[i][j]==0:
            q=deque([[i,j]])
            ck[i][j]=1
            cnt+=1
            l[i][j]=cnt
            while q:
                a,b=q.popleft()
                for t in range(4):
                    x,y=a+X[t],b+Y[t]
                    if 0<=x<n and 0<=y<m and ck[x][y]==0 and l[x][y]:
                        l[x][y]=cnt
                        ck[x][y]=1
                        q.append([x,y])
p=[*range(cnt+1)]
q=[]
for i in range(n):
    for j in range(m):
        if l[i][j]:
            x,y=i+1,j+1
            if i<n-2 and l[i+1][j]==0:
                while x<n and l[x][j]==0: x+=1
                if x<n and l[x][j] and x-i>2: heappush(q,[x-i-1,l[i][j],l[x][j]])
            if j<m-2 and l[i][j+1]==0:
                while y<m and l[i][y]==0: y+=1
                if y<m and l[i][y] and y-j>2: heappush(q,[y-j-1,l[i][j],l[i][y]])
a,k=0,0
while q and k<cnt-1:
    c,x,y=heappop(q)
    if find(x)!=find(y):
        union(x,y)
        a+=c
        k+=1
print(-1 if k!=cnt-1 else a)
    
                