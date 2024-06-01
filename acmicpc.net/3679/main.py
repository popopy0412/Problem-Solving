from math import *
import sys
ip=sys.stdin.readline
def cmp(t):
    ax,ay,bx,by,_=x,y,*t
    return atan2(by-ay,bx-ax)
def ccw(a,b,c):
    ax,ay,_,bx,by,_,cx,cy,_=*a,*b,*c
    return (ax-bx)*(ay-cy)-(ax-cx)*(ay-by)
for _ in range(int(ip())):
    n,*t=map(int,ip().split())
    l=[[t[i*2],t[i*2+1],i] for i in range(n)]
    l.sort(key=lambda t:(t[1],t[0]))
    x,y,_=l[0]
    l=[l[0]]+[*sorted(l[1:],key=cmp)]
    t=0
    while ccw(l[-2-t],l[-1-t],l[0])==0:t+=1
    l=l[:n-1-t]+[*reversed(l[n-1-t:])]
    print(*[*zip(*l)][2])