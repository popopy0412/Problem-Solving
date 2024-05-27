z=lambda x:[[x for _ in range(m+1)] for _ in range(m+1)]
n=int(input())
m=int(input())
l=[[[1,1],[n,n]]]
for _ in range(m):
    t=[*map(int,input().split())]
    l.append([t,t])
d,p=z(1e9),z([0,0,0])
d[0][0]=0
for i in range(m):
    x1,y1=l[i][0]
    x2,y2=l[i+1][0]
    x3,y3=l[i+1][1]
    dt1=abs(x1-x2)+abs(y1-y2)
    for j in range(0,i+1):
        x4,y4=l[j][1]
        dt2=abs(x3-x4)+abs(y3-y4)
        if d[i+1][j]>d[i][j]+dt1:
            d[i+1][j]=d[i][j]+dt1
            p[i+1][j]=[1,i,j]
        if d[i][i+1]>d[i][j]+dt2:
            d[i][i+1]=d[i][j]+dt2
            p[i][i+1]=[2,i,j]
    x1,y1=l[i][1]
    x2,y2=l[i+1][1]
    x3,y3=l[i+1][0]
    dt1=abs(x1-x2)+abs(y1-y2)
    for j in range(0,i+1):
        x4,y4=l[j][0]
        dt2=abs(x3-x4)+abs(y3-y4)
        if d[j][i+1]>d[j][i]+dt1:
            d[j][i+1]=d[j][i]+dt1
            p[j][i+1]=[2,j,i]
        if d[i+1][i]>d[j][i]+dt2:
            d[i+1][i]=d[j][i]+dt2
            p[i+1][i]=[1,j,i]
ans=1e9
for i in range(m):
    if d[m][i]<ans:
        ans=d[m][i]
        x,y=m,i
    if d[i][m]<ans:
        ans=d[i][m]
        x,y=i,m
t=p[x][y]
v=[]
while t[0]!=0:
    v.append(t[0])
    t=p[t[1]][t[2]]
print(ans,*v[::-1])