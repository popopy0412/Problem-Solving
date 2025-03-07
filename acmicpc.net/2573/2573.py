import sys
from collections import *
input=sys.stdin.readline
def solve():
    n,m=map(int,input().split())
    l=[[*map(int,input().split())] for _ in range(n)]
    X=[1,-1,0,0]
    Y=[0,0,1,-1]
    t=1

    while 1:
        d=[]
        for i in range(n):
            for j in range(m):
                if l[i][j]:
                    temp=0
                    for k in range(4):
                        a,b=i+X[k],j+Y[k]
                        if 0<=a<n and 0<=b<m and l[a][b]==0: temp+=1
                    if temp: d.append((i,j,temp))
        for a,b,c in d: l[a][b]=max(l[a][b]-c,0)

        q=deque()
        check=[[0]*m for _ in range(n)]
        tmp=[]
        cnt=0
        for i in range(n):
            for j in range(m):
                if l[i][j]:
                    if cnt==0:
                        q.append((i,j))
                        check[i][j]=1
                    cnt+=1
        if cnt==0:
            print(0)
            break
        c=1
        while len(q):
            x,y=q.popleft()
            for i in range(4):
                a,b=x+X[i],y+Y[i]
                if 0<=a<n and 0<=b<m and l[a][b] and check[a][b]==0:
                    check[a][b]=1
                    c+=1
                    q.append((a,b))
        if cnt!=c:
            print(t)
            break
        t+=1
solve()