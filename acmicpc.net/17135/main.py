from itertools import *
o=[]
n,m,d=map(int,input().split())
h=n-1
for i in range(n):
    t=[*map(int,input().split())]
    if h==n-1 and t.count(1): h=i
    o.append(t)

comb = combinations(range(m),r=3)
ans=0

def attack(x,a,d,n,m):
    for t in range(1,d+1):
        for i in range(-t+1,t):
            X,Y=a-(t-abs(i)),x+i
            if 0<=X<n and 0<=Y<m:
                if l[X][Y]:
                    if l[X][Y]==1: temp.append([X,Y])
                    l[X][Y]+=1
                    return

for x,y,z in comb:
    l=[]
    for j in o: l.append(j.copy())
    t=0
    for a in range(n,h,-1):
        temp=[]
        attack(x,a,d,n,m)
        attack(y,a,d,n,m)
        attack(z,a,d,n,m)
        t+=len(temp)
        for i,j in temp: l[i][j]=0
    ans=max(ans,t)
print(ans)
