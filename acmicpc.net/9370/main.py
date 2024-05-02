from heapq import *
import sys
ip=sys.stdin.readline
il=lambda:[*map(int,ip().split())]
def dijk(n,s,l):
    d=[10**10]*-~n
    d[s]=0
    q=[(0,s)]
    while q:
        c,now=heappop(q)
        for next,cost in l[now]:
            if d[next]>cost+c:
                d[next]=cost+c
                heappush(q,(cost+c,next))
    return d
def solve():
    n,m,t=il()
    s,g,h=il()
    l,k=[[] for _ in range(n+1)],[]
    for _ in range(m):
        a,b,c=il()
        l[a].append((b,c))
        l[b].append((a,c))
    S,G,H=dijk(n,s,l),dijk(n,g,l),dijk(n,h,l)
    for _ in range(t):
        i=int(ip())
        if S[g]+G[h]+H[i]==S[i] or S[h]+H[g]+G[i]==S[i]: k.append(i)
    print(*sorted(k))

for _ in range(int(ip())): solve()