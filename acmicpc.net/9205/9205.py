import sys
input=sys.stdin.readline
il=lambda:map(int,input().split())
dt=lambda a,b,x,y:abs(a-x)+abs(b-y)
ans=['sad','happy']
d=1000

for _ in range(int(input())):
    n=int(input())
    sx,sy=il()
    l=[[*il()] for _ in range(n)]
    ex,ey=il()
    check=[0]*n
    ck=0
    s=[[sx,sy]]
    while len(s):    
        x,y=s.pop()
        if dt(x,y,ex,ey)<=d: ck=1;break
        for i in range(n):
            if check[i] or dt(x,y,*l[i])>d: continue
            check[i]=1
            s.append(l[i])
    print(ans[ck])