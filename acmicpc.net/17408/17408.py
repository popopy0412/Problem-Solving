import sys
ip=sys.stdin.readline
merge=lambda x,y:[*sorted(x+y)][:-3:-1]
n=int(ip())
k=[*map(int,ip().split())]
s=1<<n.bit_length()
if s%n==0: s//=2
tree=[[0,0] for _ in range(2*s)]
for i in range(n): tree[s+i]=[k[i],0]
for i in range(s-1,0,-1): tree[i]=merge(tree[i*2],tree[i*2+1])
def update(i,v):
    tree[i]=[v,0]
    i//=2
    while i:
        tree[i]=merge(tree[i*2],tree[i*2+1])
        i//=2
def query(l,r,s,e,i):
    if r<s or e<l: return [0,0]
    elif s<=l and r<=e: return tree[i]
    m=l+r>>1
    return merge(query(l,m,s,e,i*2),query(m+1,r,s,e,i*2+1))

for _ in range(int(ip())):
    q,a,b=map(int,ip().split())
    if q==1: update(s+a-1,b)
    else: print(sum(query(1,s,a,b,1)))