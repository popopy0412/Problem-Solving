from heapq import *
def solve():
    n=int(input())
    heapify(q:=[*map(int,input().split())])
    ans=0
    while len(q)>1:
        a,b=heappop(q),heappop(q)
        ans+=a+b
        heappush(q,a+b)
    print(ans)
for _ in range(int(input())): solve()