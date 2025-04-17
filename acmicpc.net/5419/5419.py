import sys
ip=sys.stdin.readline
def solve():
    def update(i):
        tree[i]+=1
        while i:=i//2: tree[i]=tree[i*2]+tree[i*2+1]
    
    def query(l,r,s,e,i):
        if r<s or e<l: return 0
        elif s<=l and r<=e: return tree[i]
        m=l+r>>1
        return query(l,m,s,e,i*2)+query(m+1,r,s,e,i*2+1)
    
    n=int(ip())
    k=[[*map(int,ip().split())] for _ in range(n)]

    d={}
    k.sort(key=lambda x:x[0])
    for x,_ in k:
        if x in d: continue
        d[x]=len(d)
    for i in range(n): k[i][0]=d[k[i][0]]
    k.sort(key=lambda x:-x[1])
    a=len(d)
    s=1<<a.bit_length()
    if s%a==0: s//=2
    tree=[0]*2*s
    ans=0

    for x,_ in k:
        ans+=query(0,s-1,0,x,1)
        update(x+s)
    print(ans)

for _ in range(int(ip())): solve()