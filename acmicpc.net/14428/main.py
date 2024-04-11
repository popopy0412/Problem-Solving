import sys
INF=300000
ip=sys.stdin.readline
il=lambda:[*map(int,ip().split())]

def make(tree, index, t, l, r, idx):
    if l==r:
        tree[idx]=l
        index[l]=idx
        return l
    m=(l+r)//2
    a,b=make(tree,index,t,l,m,idx*2),make(tree,index,t,m+1,r,idx*2+1)
    tree[idx]=b if t[a]>t[b] else a
    return tree[idx]
def update(tree,t,index,idx,v):
    t[idx]=v
    now=index[idx]//2
    while now:
        a,b=tree[now*2],tree[now*2+1]
        tree[now]=b if t[a]>t[b] else a
        now//=2
def query(tree,l,r,s,e,idx):
    if r<s or e<l: return 0
    if s<=l and r<=e: return tree[idx]
    m=(l+r)//2
    a,b=query(tree,l,m,s,e,idx*2),query(tree,m+1,r,s,e,idx*2+1)
    return b if t[a]>t[b] else a

n,t,m=int(ip()),[10**10]+il(),int(ip())
q=[[*map(int,ip().split())]for _ in range(m)]
tree,index=[0]*INF,[0]*INF
make(tree,index,t,1,n,1)
for a,b,c in q:
    if a==1: update(tree,t,index,b,c)
    else: print(query(tree,1,n,b,c,1))