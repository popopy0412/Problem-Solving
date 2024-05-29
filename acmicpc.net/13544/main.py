import sys
from bisect import *
ip=sys.stdin.readline
n,d,m=int(ip()),[0]+[*map(int,ip().split())],int(ip())
tree=[[] for _ in range(n*4)]
def init(l,r,i):
    if l==r:
        tree[i].append(d[l])
        return
    m=(l+r)//2
    init(l,m,i*2);init(m+1,r,i*2+1)
    merge(l,m,r,i)
def merge(l,m,r,i):
    x,y=tree[i*2],tree[i*2+1]
    a,b=0,0
    while a<=m-l or b<=r-m-1:
        while a<=m-l and (b==r-m or x[a]<=y[b]):
            tree[i].append(x[a])
            a+=1
        while b<=r-m-1 and (a==m-l+1 or y[b]<=x[a]):
            tree[i].append(y[b])
            b+=1
def query(l,r,s,e,v,i):
    if r<s or e<l: return 0
    if s<=l and r<=e: return r-l-bisect_right(tree[i],v)+1
    m=(l+r)//2
    return query(l,m,s,e,v,i*2)+query(m+1,r,s,e,v,i*2+1)

init(1,n,1)
t=0
for _ in range(m):
    a,b,c=map(int,ip().split())
    a,b,c=a^t,b^t,c^t
    print(t:=query(1,n,a,b,c,1))