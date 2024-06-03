def init(l,r,i):
    if l==r:
        tree[i]=1
        return
    m=l+r>>1
    init(l,m,i*2);init(m+1,r,i*2+1)
    tree[i]=tree[i*2]+tree[i*2+1]
def update(x):
    l,r,i=1,n,1
    while l!=r:
        m=l+r>>1
        tree[i]-=1
        if x>m: l,i=m+1,i*2+1
        else: r,i=m,i*2
    tree[i]-=1
    return x
def query(l,r,i,v):
    if l==r: return l
    t=tree[i*2]
    m=l+r>>1
    if t<v: return query(m+1,r,i*2+1,v-t)
    else: return query(l,m,i*2,v)
n,k=map(int,input().split())
tree=[0]*n*4
a,c,t,p,q=0,n,-1,[],1
init(1,n,1)
for i in range(n):
    if t+k>=c:
        t=(t+k-c)%(c-a)
        c-=a
        a=0
    else: t+=k
    p.append(str(update(query(1,n,1,t+1-a))))
    a+=1
print(f'<{", ".join(p)}>')