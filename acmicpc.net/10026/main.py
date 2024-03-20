from collections import *
n=int(input())
l=[]
ck=[[0 for _ in range(n)] for _ in range(n)]
X=[0,0,-1,1]
Y=[1,-1,0,0]
ans1,ans2=0,0
for i in range(n): l.append(input())
for i in range(n):
    for j in range(n):
        if ck[i][j]: continue
        ck[i][j] = 1
        ans1+=1
        c=l[i][j]
        q=deque()
        q.append((i,j))
        while q:
            x,y=q.popleft()
            for k in range(4):
                a,b=x+X[k],y+Y[k]
                if 0<=a<n and 0<=b<n and not ck[a][b] and l[a][b]==c:
                    ck[a][b]=1
                    q.append((a,b))

ck=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if ck[i][j]: continue
        ck[i][j] = 1
        ans2+=1
        c = 'B' if l[i][j]=='B' else 'RG'
        q=deque()
        q.append((i,j))
        while q:
            x,y=q.popleft()
            for k in range(4):
                a,b=x+X[k],y+Y[k]
                if 0<=a<n and 0<=b<n and not ck[a][b] and l[a][b] in c:
                    ck[a][b]=1
                    q.append((a,b))
print(ans1,ans2)