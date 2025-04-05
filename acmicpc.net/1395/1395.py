import sys
ip=sys.stdin.readline
n,m=map(int,ip().split())
s=1<<n.bit_length()
if s%n==0: s//=2
tree=[0]*s*2
lazy=[0]*s*2
def save(l,r,i):
    tree[i]=(r-l+1)-tree[i]
    lazy[i]^=1
def apply(l,r,i):
    if lazy[i]:
        M=l+r>>1
        if i*2<s+n: save(l,M,i*2)
        if i*2+1<s+n: save(M+1,r,i*2+1)
        lazy[i]=0
def update(l,r,s,e,i):
    if r<s or e<l: return
    elif s<=l and r<=e:
        save(l,r,i)
        return
    apply(l,r,i)
    M=l+r>>1
    update(l,M,s,e,i*2);update(M+1,r,s,e,i*2+1)
    tree[i]=tree[i*2]+tree[i*2+1]

def query(l,r,s,e,i):
    if r<s or e<l: return 0
    elif s<=l and r<=e: return tree[i]
    apply(l,r,i)
    M=l+r>>1
    return query(l,M,s,e,i*2)+query(M+1,r,s,e,i*2+1)
 
for _ in range(m):
    q,a,b=map(int,ip().split())
    if q: print(query(1,s,a,b,1))
    else: update(1,s,a,b,1)