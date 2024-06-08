from heapq import *
n,*l=map(int,open(0).read().split())
q=[*sorted(l)]
ans=0
while len(q)>1:
    a,b=heappop(q),heappop(q)
    ans+=a+b
    heappush(q,a+b)
print(ans)