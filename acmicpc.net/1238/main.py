from collections import *
from heapq import *
import sys
input=sys.stdin.readline
n,m,x=map(int,input().split())
l=[[] for _ in range(n+1)]
dp,ck=[10**10],[0]*-~n
for i in range(m):
    a,b,c=map(int,input().split())
    l[a].append((b,c))

for i in range(1,n+1):
    d=[10**10]*-~n
    q=deque()
    q.append((i,0))
    while q:
        a,b=q.popleft()
        if b > d[a]: continue
        if a==x:
            d[x]=b
            continue
        for i in l[a]:
            if b+i[1] < d[i[0]]:
                d[i[0]] = b+i[1]
                q.append((i[0],b+i[1]))
    dp.append(d[x])

q=[]
dp2=[10**10]*-~n
dp2[x]=0
for i in l[x]:
    heappush(q,(i[1],i[0]))
    dp2[i[0]]=i[1]
ck[x]=1
while q:
    c,a=heappop(q)
    if ck[a]: continue
    ck[a]=1
    for i in l[a]:
        if ck[i[0]]: continue
        if dp2[i[0]] > c+i[1]:
            dp2[i[0]]=c+i[1]
            heappush(q,(c+i[1],i[0]))
ans=0
for i in range(1,n+1):
    if i == x: continue
    ans=max(ans,dp[i]+dp2[i])
print(ans)
