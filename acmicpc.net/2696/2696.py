from heapq import *
import sys
ip=sys.stdin.readline
def solve():
    a,b=[],[]
    n,l=int(ip()),[]
    for i in range(n//10+(1 if n%10 else 0)): l+=[*map(int,ip().split())]
    t=1e10
    print(-~n//2)
    for j in range(n):
        i=l[j]
        if t==1e10: t=i
        else:
            if i>t:
                heappush(b,t);heappush(b,i)
                t=heappop(b)
            else:
                heappush(a,-t);heappush(a,-i)
                t=-heappop(a)
            x,y=len(a),len(b)
            if x-y==2:
                heappush(b,t)
                t=-heappop(a)
            elif y-x==2:
                heappush(a,-t)
                t=heappop(b)
        if -~j%2: print(t,end=' ')
        if -~j%20==0 and 0<j<n-1: print()
    print()
for _ in range(int(ip())): solve()