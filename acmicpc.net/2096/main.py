import sys
input=sys.stdin.readline
n=int(input())
l,d,p=[],[],[]
for i in range(n):
    mx,mi=[0]*3,[10**9]*3
    l=list(map(int,input().split()))
    if i==0:
        d=p=l
        continue
    for j in range(3):
        if 0 <= j-1:
            mx[j]=max(mx[j],d[j-1]+l[j])
            mi[j]=min(mi[j],p[j-1]+l[j])
        mx[j]=max(mx[j],d[j]+l[j])
        mi[j]=min(mi[j],p[j]+l[j])
        if j+1 < 3:
            mx[j]=max(mx[j],d[j+1]+l[j])
            mi[j]=min(mi[j],p[j+1]+l[j])
    d,p=mx,mi
print(max(d),min(p))