from collections import *
n,m=map(int,input().split())
l=[]
ck=[[0 for _ in range(m)] for _ in range(n)]
X=[0,0,1,-1]
Y=[1,-1,0,0]
q=deque()
for i in range(n):
    l.append(input())
    if 'I' in l[i]: x,y=i,l[i].index('I')
c,ck[x][y]=0,1
q.append((x,y))
while q:
    x,y=q.popleft()
    for i in range(4):
        a,b=x+X[i],y+Y[i]
        if 0<=a<n and 0<=b<m and l[a][b]!='X' and not ck[a][b]:
            ck[a][b]=1
            if l[a][b]=='P': c+=1
            q.append((a,b))
print(c if c else 'TT')