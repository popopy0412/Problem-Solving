p=[0]*6
n,m,x,y,k=map(int,input().split())
l=[[*map(int,input().split())] for _ in range(n)]

def change(d):
    global x,y
    q,w,e,r=0,0,0,0
    if d==1:
        if y!=m-1:
            y+=1
            q,w,e,r=4,1,5,3
    elif d==2:
        if y!=0:
            y-=1
            q,w,e,r=3,5,1,4
    elif d==3:
        if x!=0: 
            x-=1
            q,w,e,r=3,2,1,0
    else:
        if x!=n-1: 
            x+=1
            q,w,e,r=0,1,2,3
    if (q,w,e,r)==(0,0,0,0): return
    p[q],p[w],p[e],p[r]=p[r],p[q],p[w],p[e]
    if l[x][y]!=0:
        p[3]=l[x][y]
        l[x][y]=0
    else: l[x][y]=p[3]
    print(p[1])
for i in map(int,input().split()): change(i)