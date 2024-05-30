from heapq import *
dis=lambda x1,y1,x2,y2:((x1-x2)**2+(y1-y2)**2)**0.5
def union(x,y):
    x,y=find(x),find(y)
    if x!=y: p[x]=y
def find(x):
    if x==p[x]: return x
    p[x]=find(p[x])
    return p[x]
n=int(input())
l=[[] for _ in range(n)]
k=[[*map(float,input().split())] for _ in range(n)]
q,p=[],[*range(n)]
for i in range(n-1):
    x1,y1=k[i]
    for j in range(i+1,n):
        x2,y2=k[j]
        heappush(q,[dis(x1,y1,x2,y2),i,j])
ans,c=0,0
while c<n-1:
    d,x,y=heappop(q)
    x,y=find(x),find(y)
    if x!=y:
        union(x,y)
        ans+=d
        c+=1
print(f'{ans:.2f}')