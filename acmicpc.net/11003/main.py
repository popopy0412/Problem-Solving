from heapq import *
n,l,*a=map(int,open(0).read().split())
q=[]
for i in range(n):
    while q and q[0][1]<=i-l:heappop(q)
    heappush(q,(a[i],i))
    print(q[0][0],end=' ')