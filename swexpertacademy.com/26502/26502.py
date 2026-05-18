cond=lambda a,b,c: a==b or b==c or a==c
t=int(input())
while t:
    t-=1
    ans=0
    n=int(input())
    l=[[*map(int,input().split())] for _ in range(n)]
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                x1,y1,x2,y2,x3,y3=*l[i],*l[j],*l[k]
                if cond(x1,x2,x3) and cond(y1,y2,y3):
                    a,b,x,y=min(x1,x2,x3),min(y1,y2,y3),max(x1,x2,x3),max(y1,y2,y3)
                    ans=max(ans,(x-a)*(y-b))
    print(ans)