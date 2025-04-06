import sys
ip=sys.stdin.readline
n,t,q=map(int,ip().split())
s=1<<n.bit_length()
if s%n==0: s//=2
tree=[0 for _ in range(2*s)]
lazy=[0 for _ in range(2*s)]
for i in range(n): tree[s+i]=1
for i in range(s-1,0,-1): tree[i]=tree[i*2]|tree[i*2+1]

def save(i,v):
    tree[i]=v
    lazy[i]=v

def apply(i):
    if lazy[i]:
        if i*2<s+n: save(i*2,lazy[i])
        if i*2+1<s+n: save(i*2+1,lazy[i])
        lazy[i]=0

def update(l,r,s,e,i,v):
    if r<s or e<l: return
    elif s<=l and r<=e: save(i,v);return
    apply(i)
    m=l+r>>1
    update(l,m,s,e,i*2,v);update(m+1,r,s,e,i*2+1,v)
    tree[i]=tree[i*2]|tree[i*2+1]

def query(l,r,s,e,i):
    if r<s or e<l: return 0
    elif s<=l and r<=e: return tree[i]
    apply(i)
    m=l+r>>1
    return query(l,m,s,e,i*2)|query(m+1,r,s,e,i*2+1)

for _ in range(q):
    m,*v=ip().split()
    v=[*map(int,v)]
    if v[0]>v[1]: v[0],v[1]=v[1],v[0]
    if m=='C': update(1,s,v[0],v[1],1,1<<~-v[2])
    else: print(query(1,s,v[0],v[1],1).bit_count())