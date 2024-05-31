from heapq import *
import sys
sys.setrecursionlimit(10**6)
ip=sys.stdin.readline
def union(x,y):
    x,y=find(x),find(y)
    if x!=y: p[x]=y
def find(x):
    if x==p[x]: return x
    p[x]=find(p[x])
    return p[x]
while True:
    n,m=map(int,ip().split())
    if (n,m)==(0,0): break
    p,q=[*range(n)],[]
    t,k=0,0
    for _ in range(m):
        a,b,c=map(int,ip().split())
        k+=c
        heappush(q,[c,a,b])
    while t<n-1:
        c,a,b=heappop(q)
        if find(a)==find(b): continue
        union(a,b)
        t+=1
        k-=c
    print(k)