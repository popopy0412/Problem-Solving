n,m=map(int,input().split())
d=list(map(int,input().split()))
c=list(map(int,input().split()))
s=sum(c)
ans=s
dy=[0]*10001
for i in range(n):
    for j in range(s-c[i],-1,-1):
        if j==0 or dy[j]:dy[j+c[i]]=max(dy[j+c[i]],dy[j]+d[i])
for i in range(s+1):
    if dy[i] >= m:
        print(i)
        break