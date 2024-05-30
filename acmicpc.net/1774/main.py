from heapq import *
dis=lambda x1,y1,x2,y2:((x1-x2)**2+(y1-y2)**2)**0.5
def union(x,y):
    x,y=find(x),find(y)
    if x!=y: p[x]=y
def find(x):
    if x==p[x]: return x
    p[x]=find(p[x])
    return p[x]
n,m=map(int,input().split())
k=[[]]+[[*map(int,input().split())] for _ in range(n)]
q,p=[],[*range(n+1)]
for i in range(1,n):
    for j in range(i+1,n+1): heappush(q,[dis(*k[i],*k[j]),i,j])
ans=0
for _ in range(m):
    a,b=map(int,input().split())
    if find(a)==find(b): m-=1
    else: union(a,b)
while m<n-1:
    d,x,y=heappop(q)
    x,y=find(x),find(y)
    if x!=y:
        union(x,y)
        ans+=d
        m+=1
ans=ans*1000
if ans%10>=5: ans+=10
ans=(ans-ans%10)/1000
print(f'{ans:.2f}')