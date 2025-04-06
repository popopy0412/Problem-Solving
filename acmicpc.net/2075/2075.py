from heapq import *
n,l=int(input()),[]
for _ in range(n):
    for i in map(int,input().split()):
        if len(l)==n and l[0]<i: heappop(l)
        if len(l)!=n: heappush(l,i)
print(heappop(l))