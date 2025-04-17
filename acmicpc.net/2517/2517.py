def update(i):
    tree[i]+=1
    while i:=i//2: tree[i]=tree[i*2]+tree[i*2+1]

def query(l,r,s,e,i):
    if r<s or e<l: return 0
    elif s<=l and r<=e: return tree[i]
    m=l+r>>1
    return query(l,m,s,e,i*2)+query(m+1,r,s,e,i*2+1)

n,*k=map(int,open(0).read().split())
for i in range(n): k[i]=[i,k[i]]
k.sort(key=lambda x:x[1])
for i in range(n): k[i][1]=i
s=1<<n.bit_length()
if s%n==0: s//=2
tree=[0]*2*s
ans=[0]*n

for i in range(n-1,-1,-1):
    x=k[i][0]
    update(x+s)
    ans[x]=query(0,s-1,0,x,1)
for i in ans: print(i)