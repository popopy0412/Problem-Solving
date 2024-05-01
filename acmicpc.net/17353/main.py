import sys
ip=sys.stdin.readline
def init(l,r,i):
    if l==r:
        tree[i]=d[l]
        return
    m=(l+r)//2
    init(l,m,i*2)
    init(m+1,r,i*2+1)
def lazy(l,r,i):
    x,y=temp[i]
    if l!=r:
        m=(l+r)//2
        temp[i*2][0]+=x
        temp[i*2][1]+=y
        temp[i*2+1][0]+=x+(y*(m-l+1))
        temp[i*2+1][1]+=y
    else: tree[i]+=x
    temp[i][0],temp[i][1]=0,0
def update(l,r,s,e,i,c):
    m=(l+r)//2
    if r<s or e<l: return
    if s<=l and r<=e:
        temp[i][0]+=l-c
        temp[i][1]+=1
        return
    update(l,m,s,e,i*2,c)
    update(m+1,r,s,e,i*2+1,c)
def query(l,r,k,i):
    lazy(l,r,i)
    if r<k or k<l: return 0
    if l==k==r: return tree[i]
    m=(l+r)//2
    return query(l,m,k,i*2)+query(m+1,r,k,i*2+1)
n,d=int(ip()),[0]+[*map(int,ip().split())]
tree=[0]*1700000
temp=[[0,0] for _ in range(1700000)]
init(1,n,1)
for _ in range(int(ip())):
    q,*l=map(int,ip().split())
    if q==1: update(1,n,l[0],l[1],1,l[0]-1)
    else: print(query(1,n,l[0],1))