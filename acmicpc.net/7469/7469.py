from bisect import *
import sys
ip=sys.stdin.readline
mp=lambda:[*map(int,ip().split())]
n,q=mp()
k=mp()
s=1<<n.bit_length()
if s%n==0: s//=2
tree=[[] for _ in range(2*s)]

def merge(a,b):
    x,y=len(a),len(b)
    l,r=0,0
    t=[]
    while l<x or r<y:
        while l<x and (r==y or a[l]<b[r]):
            t.append(a[l])
            l+=1
        while r<y and (l==x or b[r]<a[l]):
            t.append(b[r])
            r+=1
    return t

def query(l,r,s,e,i,v):
    if r<s or e<l: return 0
    elif s<=l and r<=e: return bisect_right(tree[i],v)
    m=l+r>>1
    return query(l,m,s,e,i*2,v)+query(m+1,r,s,e,i*2+1,v)

for i in range(n): tree[i+s].append(k[i])
for i in range(s-1,0,-1): tree[i]=merge(tree[i*2],tree[i*2+1])
for _ in range(q):
    l,r=int(-1e9),int(1e9)
    x,y,c=mp()
    while l<=r:
        m=l+r>>1
        if l==r: break
        t=query(1,s,x,y,1,m)
        if t<c: l=m+1
        elif c<=t: r=m
    print(m)