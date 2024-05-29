import sys
sys.setrecursionlimit(10**6)
ip=sys.stdin.readline
def union(x,y):
    x,y=find(x),find(y)
    if x!=y:
        p[x]=y
        return 0
    return 1
def find(x):
    if x==p[x]: return x
    p[x]=find(p[x])
    return p[x]

n,m=map(int,ip().split())
p=[*range(n)]
for i in range(m):
    a,b=map(int,ip().split())
    if union(a,b):
        print(i+1)
        exit(0)
print(0)