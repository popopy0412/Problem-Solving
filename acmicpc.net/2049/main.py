from math import *
import sys
ip=sys.stdin.readline
def cmp(t):
    ax,ay,bx,by=x,y,*t
    return atan2(by-ay,bx-ax)
def ccw(a,b,c):
    ax,ay,bx,by,cx,cy=*a,*b,*c
    return (ax-bx)*(ay-cy)-(ax-cx)*(ay-by)
def dis(a,b):
    ax,ay,bx,by=*a,*b
    return ((ax-bx)**2+(ay-by)**2)
n=int(ip())
l=[[*map(int,ip().split())] for _ in range(n)]
l.sort(key=lambda t:(t[1],t[0]))
x,y=l[0]
l=[l[0]]+[*sorted(l[1:],key=cmp)]
s=[*l[:2]]
cnt=2
while cnt<n:
    while len(s)>=2:
        a,b,c=s[-2],s.pop(),l[cnt]
        if ccw(a,b,c)>0:
            s.append(b)
            break
    s.append(c)
    cnt+=1
a,b=0,1
n=len(s)
ans=dis(s[a],s[b])
x1,y1,x2,y2=*s[a],*s[b]
if n>2:
    while True:
        ax,ay,bx,by=*s[a],*s[b%n]
        atx,aty,btx,bty=*s[(a+1)%n],*s[(b+1)%n]
        ta,tb=[atx-ax,aty-ay],[btx-bx,bty-by]
        ans=max(ans,dis([ax,ay],[bx,by]))
        tb=[ta[0]+tb[0],ta[1]+tb[1]]
        if ccw([0,0],ta,tb)>0: b+=1
        else: a+=1
        if b==n: break
print(ans)
