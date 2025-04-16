from bisect import *
INF=-1e15
n=int(input())
k=[[*map(int,input().split())] for _ in range(n)]
k.sort(key=lambda x:x[0])
dx,dy={},{}
for x,y,c in k:
    if x in dx: continue
    dx[x]=len(dx)
k.sort(key=lambda x:x[1])
for x,y,c in k:
    if y in dy: continue
    dy[y]=len(dy)
a,b=len(dx),len(dy)
s=1<<a.bit_length()
if s%a==0: s//=2
for i in range(n):
    x,y,c=k[i]
    k[i]=[dx[x],dy[y],c]

def update(i,v):
    i+=s
    for j in range(4):
        if tree[i][j]==INF: tree[i][j]=v
        else: tree[i][j]+=v
    i//=2
    while i:
        ll,lr,lm,la=tree[i*2]
        rl,rr,rm,ra=tree[i*2+1]
        tree[i]=[max(ll,la+rl),max(rr,ra+lr),max(lr+rl,lm,rm),la+ra]
        i//=2

i,ans=0,0
while i<b:
    tree=[[INF,INF,INF,0] for _ in range(2*s)]
    x,y=bisect_left(k,i,key=lambda x:x[1]),0
    for j in range(i,b):
        y=bisect_right(k,j,key=lambda x:x[1],lo=x)
        for t in range(x,y): update(k[t][0],k[t][2])
        ans=max(ans,tree[1][2])
        if tree[1][2]<=0: i=j;break
        x=y
    i+=1
print(ans)