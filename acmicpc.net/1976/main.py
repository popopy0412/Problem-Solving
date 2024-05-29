def union(x,y):
    x,y=find(x),find(y)
    if x!=y: p[y]=x
def find(x):
    if x==p[x]: return x
    p[x]=find(p[x])
    return p[x]
n,m=int(input()),int(input())
p=[*range(n+1)]
for i in range(1,n+1):
    t=[0,*map(int,input().split())]
    for j in range(i+1,n+1):
        if t[j]: union(i,j)
print('YES' if len(set([find(i) for i in map(int,input().split())]))==1 else 'NO')