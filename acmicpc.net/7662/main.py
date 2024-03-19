from heapq import *
import sys
def solve():
    a,l,h,c=int(input()),[],[],0
    ck=[0]*a
    for i in range(a):
        s,n=sys.stdin.readline().split()
        n=int(n)
        if s=='I':
            heappush(l,(n,i))
            heappush(h,(-n,-i))
            c+=1
        elif s=='D' and c:
            if n==1:
                while ck[-(x:=heappop(h))[1]] != 0: pass
                ck[-x[1]]=1
            else:
                while ck[(y:=heappop(l))[1]] != 0: pass
                ck[y[1]]=1
            c-=1
            if not c: l,h=[],[]
    if c:
        while ck[-(x:=heappop(h))[1]] != 0: pass
        while ck[(y:=heappop(l))[1]] != 0: pass
        print(-x[0], y[0])
    else: print('EMPTY')
                
for _ in range(int(input())): solve()

