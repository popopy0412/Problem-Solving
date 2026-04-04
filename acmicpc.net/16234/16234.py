n,l,r=map(int,input().split())
d=[[*map(int,input().split())] for _ in range(n)]

def union(a, b):
    a=find(a)
    b=find(b)
    if root[a]<root[b]: root[b]=root[a]
    else: root[a]=root[b]

def find(x):
    if x!=root[x]: root[x]=find(root[x])
    return root[x]

ck=1
ans=-1
while ck:
    s=[[0,0] for _ in range(n**2)]
    root=[i for i in range(n*n)]
    ck=0
    ans+=1
    for i in range(n):
        for j in range(n):
            if i+1<n and l<=abs(d[i][j]-d[i+1][j])<=r:
                ck=1
                union(i*n+j,-~i*n+j)
            if j+1<n and l<=abs(d[i][j]-d[i][j+1])<=r:
                ck=1
                union(i*n+j,i*n+j+1)

    for i in range(n):
        for j in range(n):
            k=find(i*n+j)
            s[k][0]+=d[i][j]
            s[k][1]+=1
    
    for i in range(n):
        for j in range(n):
            k=find(i*n+j)
            d[i][j]=s[k][0]//s[k][1]
    
print(ans)