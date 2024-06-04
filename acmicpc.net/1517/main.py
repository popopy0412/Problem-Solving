n,*d=map(int,open(0).read().split())
tree=[[] for _ in range(n*4)]
cnt=[0]*n*4
def init(l,r,i):
    if l==r:
        tree[i]=[d[l]]
        return
    m=l+r>>1
    init(l,m,i*2);init(m+1,r,i*2+1)
    cnt[i]=cnt[i*2]+cnt[i*2+1]
    merge(l,m,r,i)
def merge(l,m,r,i):
    x,y=tree[i*2],tree[i*2+1]
    a,b=0,0
    while a<=m-l or b<=r-m-1:
        while a<=m-l and (b==r-m or x[a]<=y[b]):
            tree[i].append(x[a])
            a+=1
        while b<=r-m-1 and (a==m-l+1 or x[a]>y[b]):
            tree[i].append(y[b])
            b+=1
            cnt[i]+=m-l+1-a
init(0,n-1,1)
print(cnt[1])