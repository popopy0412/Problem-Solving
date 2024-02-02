from collections import *
import sys
n,m,h=map(int,input().split());c=0
x=[1, -1, 0, 0, 0, 0]
y=[0, 0, 1, -1, 0, 0]
z=[0, 0, 0, 0, 1, -1]
q=deque(); l=[[[0 for _ in range(n)] for _ in range(m)] for _ in range(h)]
for i in range(h):
    for j in range(m):
        for t, c in enumerate(map(int,sys.stdin.readline().split())):
            l[i][j][t]=c
            if c==1: q.append((i,j,t,1))

while len(q):
    i,j,t,c=q.popleft()
    for k in range(6):
        tx=t+x[k]; ty=j+y[k]; tz=i+z[k]
        if 0 <= tx < n and 0 <= ty < m and 0 <= tz < h and l[tz][ty][tx] == 0:
            l[tz][ty][tx]=c+1
            q.append((tz,ty,tx,c+1))
for i in range(h):
    for j in range(m):
        for t in range(n):
            if l[i][j][t]==0:
                print(-1); exit(0)
print(c-1)