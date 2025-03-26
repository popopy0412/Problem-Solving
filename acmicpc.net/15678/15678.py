from collections import *
n,m,*l=map(int,open(0).read().split())
d=deque()
for i in range(n):
    while d and i-d[0]>m: d.popleft()
    if d: l[i]+=max(0,l[d[0]])
    while d and l[d[-1]]<=l[i]: d.pop()
    d.append(i)
print(max(l))