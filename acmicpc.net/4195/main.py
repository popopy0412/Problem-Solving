import sys
ip=sys.stdin.readline
def union(x,y):
    x,y=find(x),find(y)
    if x!=y:
        if s[x]>s[y]:
            s[x],s[y]=s[x]+s[y],0
            p[y]=x
        else:
            s[x],s[y]=0,s[x]+s[y]
            p[x]=y
def find(x):
    if x==p[x]: return x
    p[x]=find(p[x])
    return p[x]

for _ in range(int(ip())):
    n=int(ip())
    d={}
    s=[1]*2*n
    p=[*range(n*2)]
    for _ in range(n):
        a,b=ip().split()
        if a not in d: d[a]=len(d)
        if b not in d: d[b]=len(d)
        x,y=d[a],d[b]
        union(x,y)
        print(s[find(x)])