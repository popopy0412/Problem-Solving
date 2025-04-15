import sys
ip=sys.stdin.readline
MOD=10**9+7
n,k=int(ip()),[*map(int,ip().split())]
s=1<<n.bit_length()
if s%n==0: s//=2
tree=[0]*2*s
lazy1=[1]*2*s
lazy2=[0]*2*s
for i in range(n): tree[s+i]=k[i]
for i in range(s-1,0,-1): tree[i]=tree[2*i]+tree[2*i+1]%MOD

def save(q,i,l,r,v):
    if q==1:
        lazy2[i]+=v
        tree[i]+=(r-l+1)*v
    elif q==2:
        lazy1[i]*=v
        lazy2[i]*=v
        tree[i]*=v
    elif q==3:
        lazy1[i]=0
        lazy2[i]=v
        tree[i]=(r-l+1)*v
    tree[i]%=MOD
    lazy1[i]%=MOD
    lazy2[i]%=MOD

def apply(l,r,i):
    m=l+r>>1
    p=[l,m,m+1,r]
    for t in range(i*2,2*-~i):
        if t<n+s:
            c=t-2*i
            save(2,t,p[2*c],p[2*c+1],lazy1[i])
            save(1,t,p[2*c],p[2*c+1],lazy2[i])
    lazy1[i]=1
    lazy2[i]=0

def update(l,r,s,e,i,v,q):
    if r<s or e<l: return
    elif s<=l and r<=e: save(q,i,l,r,v);return
    apply(l,r,i)
    m=l+r>>1
    update(l,m,s,e,i*2,v,q);update(m+1,r,s,e,i*2+1,v,q)
    tree[i]=(tree[i*2]+tree[i*2+1])%MOD

def query(l,r,s,e,i):
    if r<s or e<l: return 0
    elif s<=l and r<=e: return tree[i]%MOD
    apply(l,r,i)
    m=l+r>>1
    return (query(l,m,s,e,i*2)+query(m+1,r,s,e,i*2+1))%MOD

for _ in range(int(ip())):
    q,*a=map(int,ip().split())
    if q!=4: update(1,s,a[0],a[1],1,a[2],q)
    else: print(query(1,s,a[0],a[1],1))