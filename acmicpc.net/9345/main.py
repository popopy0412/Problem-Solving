import sys
ip=sys.stdin.readline
sum=lambda n:n*(n+1)//2
def init(l,r,i):
    if l==r:
        min_tree[i],max_tree[i]=l,l
        return
    m=l+r>>1
    init(l,m,i*2);init(m+1,r,i*2+1)
    min_tree[i],max_tree[i]=l,r
def update(x,s,e,v,i):
    if s==e:
        min_tree[i],max_tree[i]=v,v
        return
    m=s+e>>1
    if x>m: update(x,m+1,e,v,i*2+1)
    else: update(x,s,m,v,i*2)
    a,b,c,d=min_tree[i*2],min_tree[i*2+1],max_tree[i*2],max_tree[i*2+1]
    min_tree[i],max_tree[i]=min(a,b),max(c,d)
def query(l,r,s,e,i):
    if e<l or r<s: return [1e9,0]
    elif s<=l and r<=e: return [min_tree[i],max_tree[i]]
    m=l+r>>1
    x,y=query(l,m,s,e,i*2),query(m+1,r,s,e,i*2+1)
    return [min(x[0],y[0]),max(x[1],y[1])]
for _ in range(int(ip())):
    n,k=map(int,ip().split())
    l=[*range(n)]
    min_tree,max_tree=[1e9]*n*4,[0]*n*4
    init(0,n-1,1)
    for _ in range(k):
        q,a,b=map(int,ip().split())
        if q: print('YES' if query(0,n-1,a,b,1)==[a,b] else 'NO')
        else:
            x,y=l[a],l[b]
            update(a,0,n-1,y,1);update(b,0,n-1,x,1)
            l[a],l[b]=y,x