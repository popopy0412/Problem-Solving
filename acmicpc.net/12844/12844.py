import sys
ip=sys.stdin.readline
n=int(ip())
k=[*map(int,ip().split())]
m=int(ip())
s=1<<n.bit_length()
if s%n==0: s//=2
tree=[0]*s*2
lazy=[0]*s*2
for i in range(s): tree[s+i]=k[i] if i<n else 0
for i in range(s-1,0,-1): tree[i]=tree[i*2]^tree[i*2+1]
def save(i,v):
    if i>=s: tree[i]^=v
    lazy[i]^=v
def apply(i):
    if lazy[i]:
        if i*2<s+n: save(i*2,lazy[i])
        if i*2+1<s+n: save(i*2+1,lazy[i])
        lazy[i]=0
def update(l,r,s,e,i,v):
    if r<s or e<l: return
    elif s<=l and r<=e:
        save(i,v)
        return
    apply(i)
    M=l+r>>1
    update(l,M,s,e,i*2,v);update(M+1,r,s,e,i*2+1,v)
    tree[i]=tree[i*2]^tree[i*2+1]

def query(l,r,s,e,i):
    if r<s or e<l: return 0
    elif s<=l and r<=e: return tree[i]
    apply(i)
    M=l+r>>1
    return query(l,M,s,e,i*2)^query(M+1,r,s,e,i*2+1)

for _ in range(m):
    q,a,*b=map(int,ip().split())
    if q==1: update(0,s-1,a,b[0],1,b[1])
    else: print(query(0,s-1,a,b[0],1))
