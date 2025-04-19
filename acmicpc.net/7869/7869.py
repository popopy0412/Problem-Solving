from math import *
x1,y1,r1,x2,y2,r2=map(float,input().split())
d=dist([x1,y1],[x2,y2])
if d>=r1+r2: ans=0
elif d<=abs(r1-r2): ans=pi*min(r1,r2)**2
else:
    c1=(r1**2+d**2-r2**2)/(2*r1*d)
    c2=(r2**2+d**2-r1**2)/(2*r2*d)
    t1=2*acos(c1)
    t2=2*acos(c2)
    s1=sin(t1)
    s2=sin(t2)
    h1=r1**2*t1/2
    h2=r2**2*t2/2
    k1=r1**2*s1/2
    k2=r2**2*s2/2
    ans=h1+h2-k1-k2
print(f'{ans:.3f}')