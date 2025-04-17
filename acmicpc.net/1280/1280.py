MOD=10**9+7
n,*k=map(int,open(0).read().split())
mx=max(k)+1
if min(k)==max(k): print(0);exit(0)
s=1<<mx.bit_length()
if s%mx==0: s//=2
tree=[[0,0] for _ in range(2*s+1)]

def update(v):
    i=s+v
    tree[i]=[tree[i][0]+v,tree[i][1]+1]
    while i:=i//2:
        x,y=tree[i*2],tree[i*2+1]
        tree[i]=[(x[0]+y[0])%MOD,x[1]+y[1]]

def query(l,r,s,e,i):
    if r<s or e<l: return [0,0]
    elif s<=l and r<=e: return tree[i]
    m=l+r>>1
    x,y=query(l,m,s,e,i*2),query(m+1,r,s,e,i*2+1)
    return [(x[0]+y[0])%MOD,x[1]+y[1]]

ans=1
for v in k:
    a=0
    update(v)
    x,y=query(0,s-1,0,v-1,1),query(0,s-1,v+1,mx-1,1)
    a=(v*x[1]-x[0]+y[0]-v*y[1])%MOD
    if a: ans*=a
    ans%=MOD
print(ans)
