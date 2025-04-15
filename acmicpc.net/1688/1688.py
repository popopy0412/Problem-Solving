import sys
ip=sys.stdin.readline
n=int(ip())
l=[[*map(int,ip().split())] for _ in range(n)]

def ccw(x1, y1, x2, y2):
    s=x1*y2-x2*y1
    if s<0: return -1
    elif s==0: return 0
    else: return 1

def solve(a, b):
    x,y=a+1e10,b
    cnt=0
    for i in range(n):
        x1,y1,x2,y2=*l[i],*l[(i+1)%n]
        s1=ccw(x-a,y-b,x1-a,y1-b)
        s2=ccw(x-a,y-b,x2-a,y2-b)
        s3=ccw(x-x1,y-y1,x2-x1,y2-y1)
        s4=ccw(a-x1,b-y1,x2-x1,y2-y1)
        if s1*s2>0 or s3*s4>0: continue
        if y1==y2==b:
            if min(x1,x2) <= a <= max(x1,x2): cnt=1;break
            continue
        if x1==x2==a:
            if min(y1,y2) <= b <= max(y1,y2): cnt=1;break
            continue
        elif s4==0 and min(x1,x2) <= a <= max(x1,x2): cnt=1;break
        elif s1*s2==0 and s3*s4==0 and (a<min(x1,x2) or max(x1,x2)<a): continue
    
        elif s1*s2==0:
            if min(y1,y2)<b: cnt+=1
            continue
        elif s1*s2<=0 and s3*s4<=0: cnt+=1
    print(cnt%2)


for _ in range(3):
    a,b=map(int,ip().split())
    solve(a, b)