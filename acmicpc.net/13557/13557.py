import sys
ip=sys.stdin.readline
INF=1e15
def update(x,y):
    ll,lr,la,lm=x
    rl,rr,ra,rm=y
    return [max(ll,la+rl),max(rr,ra+lr),la+ra,max(lr+rl,lm,rm)]

def query(l,r,s,e,i,q):
    if r<s or e<l: return (-1)**q*INF
    if s<=l and r<=e: return tree[q][i]
    m=l+r>>1
    return qry[q](query(l,m,s,e,i*2,q),query(m+1,r,s,e,i*2+1,q))

def range_query(l,r,s,e,i):
    if r<s or e<l: return [-INF,-INF,0,-INF]
    if s<=l and r<=e: return rtree[i]
    m=l+r>>1
    return update(range_query(l,m,s,e,i*2),range_query(m+1,r,s,e,i*2+1))

n,k=int(ip())+1,[0]+[*map(int,ip().split())]
s=1<<n.bit_length()
if s%n==0: s//=2
mi,mx=[INF]*2*s,[-INF]*2*s
tree=[mi,mx]
rtree=[[-INF,-INF,0,-INF] for _ in range(2*s)]
qry=[min, max]
for i in range(n):
    rtree[s+i]=[k[i]]*4
    k[i]+=(k[i-1] if i else 0)
    mx[s+i]=mi[s+i]=k[i]

for i in range(s-1,0,-1):
    mx[i]=max(mx[i*2],mx[i*2+1])
    mi[i]=min(mi[i*2],mi[i*2+1])
    rtree[i]=update(rtree[i*2],rtree[i*2+1])

for i in range(int(ip())):
    x1,y1,x2,y2=map(int,ip().split())
    if x1<=y1<=x2<=y2: ans=query(0,s-1,x2,y2,1,1)-query(0,s-1,x1-1,y1-1,1,0)
    elif x1<=x2<=y1:
        ans=range_query(0,s-1,x2,min(y1,y2),1)[3]
        ans=max(ans,query(0,s-1,x2,y2,1,1)-query(0,s-1,x1-1,x2-1,1,0))
        if y1<y2: ans=max(ans,query(0,s-1,y1,y2,1,1)-query(0,s-1,x1-1,y1-1,1,0))
    elif x2<=x1<=y2:
        ans=range_query(0,s-1,x1,min(y1,y2),1)[3]
        if y1<y2: ans=max(ans,query(0,s-1,y1,y2,1,1)-query(0,s-1,x1-1,y1-1,1,0))
    else: ans=0
    print(ans)
