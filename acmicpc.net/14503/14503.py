il=lambda:map(int,input().split())
n,m=il()
x,y,d=il()
l=[[*il()] for _ in range(n)]
X=[-1,0,1,0]
Y=[0,1,0,-1]
ans=0
while 1:
    if l[x][y]==0:l[x][y]=2;ans+=1;continue
    ck=0
    for i in range(4):
        a,b=x+X[i],y+Y[i]
        if 0<a<n-1 and 0<b<m-1 and l[a][b]==0:
            ck=1
            break
    if ck:
        d=(d-1)%4
        a,b=x+X[d],y+Y[d]
        if 0<a<n-1 and 0<b<m-1 and l[a][b]==0: x,y=a,b
    else:
        a,b=x+X[(d+2)%4],y+Y[(d+2)%4]
        if 0<a<n-1 and 0<b<m-1 and l[a][b]!=1: x,y=a,b
        else: break
print(ans)