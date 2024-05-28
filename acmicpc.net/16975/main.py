import sys
ip=sys.stdin.readline
def init(l,r,i):
    if l==r:
        tree[i]=d[l]
        return
    m=(l+r)//2
    init(l,m,i*2);init(m+1,r,i*2+1)
    tree[i]=tree[i*2]+tree[i*2+1]
def lazy(l,r,i):
    t=temp[i]
    if t:
        tree[i]+=t*(r-l+1)
        if l!=r:
            m=(l+r)//2
            temp[i*2]+=t
            temp[i*2+1]+=t
    temp[i]=0
def update(l,r,s,e,i,v):
    lazy(l,r,i)
    if e<l or r<s: return
    elif s<=l and r<=e: temp[i]=v
    else:
        m=(l+r)//2
        update(l,m,s,e,i*2,v)
        update(m+1,r,s,e,i*2+1,v)
def query(l,r,s,e,i):
    lazy(l,r,i)
    if e<l or r<s: return 0
    elif s<=l and r<=e: return tree[i]
    m=(l+r)//2
    return query(l,m,s,e,i*2)+query(m+1,r,s,e,i*2+1)
n=int(ip())
d=[0]+[*map(int,ip().split())]
tree,temp=[0]*(n*4),[0]*(n*4)
init(1,n,1)
for _ in range(int(ip())):
    q,*t=map(int,ip().split())
    if q==1: update(1,n,t[0],t[1],1,t[2])
    else: print(query(1,n,t[0],t[0],1))