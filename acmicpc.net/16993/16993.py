import sys
sys.setrecursionlimit(10**6)
ip=sys.stdin.readline
n,k=int(ip()),[0]+[*map(int,ip().split())]
s=1<<n.bit_length()
MAX=int(-1e10)
if s%n==0: s//=2
tree=[[] for _ in range(2*s)]

def init(l,r,i):
    if l==r: tree[i]=[k[l]]*4;return
    m=l+r>>1
    init(l,m,i*2);init(m+1,r,i*2+1)
    tree[i]=merge(tree[i*2],tree[i*2+1])
    return

def merge(x,y):
    if y[0]<=MAX: return [x[0],x[0],x[2],max(x)]
    if x[0]<=MAX: return [y[1],y[1],y[2],max(y)]
    t=[max(x[0],x[2]+y[0]),max(y[1],y[2]+x[1]),x[2]+y[2]]
    t.append(max(max(t),max(x),max(y),max(x[1],x[2])+max(y[0],y[2])))
    return t

def query(l,r,s,e,i):
    if r<s or e<l: return [MAX]*4
    if s<=l and r<=e: return tree[i]
    m=l+r>>1
    return merge(query(l,m,s,e,i*2),query(m+1,r,s,e,i*2+1))

init(1,n,1)

for _ in range(int(ip())):
    a,b=map(int,ip().split())
    print(max(query(1,n,a,b,1)))