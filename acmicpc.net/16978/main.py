import sys
ip=sys.stdin.readline
def update(i,v):
    while i<=n:
        tree[i]+=v
        i+=i&-i
def query(i):
    v=0
    while i:
        v+=tree[i]
        i-=i&-i
    return v
n=int(ip())
l=[0]+[*map(int,ip().split())]
tree=[0]*-~n
for i in range(1,n+1): update(i,l[i])
m=int(ip())
x,y=0,0
q1,q2=[[]],[[] for _ in range(m+1)]
for _ in range(m):
    a,*b=map(int,ip().split())
    if a==1:
        x+=1
        q1.append(b)
    elif a==2:
        q2[b[0]].append([b[1],b[2],y])
        y+=1
ans=[0]*y
for now in range(x+1):
    if now:
        i,v=q1[now]
        update(i,v-l[i])
        l[i]=v
    for s,e,i in q2[now]:
        v=query(e)-query(s-1)
        ans[i]=v
print(*ans)