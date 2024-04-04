ans=1000
def init(l,now,cnt,on,off):
    if now==10:
        rec(l,1,0,cnt,on,off)
        return
    X=[1,0,0,0]
    Y=[0,-1,0,1]
    init(l,now+1,cnt,on,off)
    for i in range(4):
        a,b=X[i],now+Y[i]
        if 0 <= b < 10:
            l[a][b]^=1
            if l[a][b]: on,off=on+1,off-1
            else: on,off=on-1,off+1
    init(l,now+1,cnt+1,on,off)
    for i in range(4):
        a,b=X[i],now+Y[i]
        if 0 <= b < 10: l[a][b]^=1
    
def rec(l, x, y, cnt, on, off):
    global ans,m
    if not on:
        ans=min(ans,cnt)
        return
    if cnt>ans or x==10: return
    X=[0,0,-1,1,0]
    Y=[1,-1,0,0,0]
    a,b=x-1,y
    if 0 <= a < 10 and 0 <= b and 10 and l[a][b]:
        for i in range(5):
            a,b=x+X[i],y+Y[i]
            if 0 <= a < 10 and 0 <= b < 10:
                l[a][b]^=1
                if l[a][b]: on,off=on+1,off-1
                else: on,off=on-1,off+1
        if ans > cnt+1: rec(l, x+(y+1)//10, (y+1)%10, cnt+1, on, off)
        for i in range(5):
            a,b=x+X[i],y+Y[i]
            if 0 <= a < 10 and 0 <= b < 10: l[a][b]^=1
    else: rec(l, x+(y+1)//10, (y+1)%10, cnt, on, off)
on,off=0,0
b=[]
for i in range(10):
    b.append([*map(lambda x:(0 if x=='#' else 1),input())])
    on+=b[-1].count(1)
    off+=b[-1].count(0)
init(b,0,0,on,off)
print(-1 if ans==1000 else ans)