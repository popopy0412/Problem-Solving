n,m=map(int,input().split())
l=[[int(i) for i in input()] for _ in range(n)]
for i in range(1,n):
    for j in range(1,m):
        if l[i][j]: l[i][j]=min(l[i-1][j],l[i][j-1],l[i-1][j-1])+1
print(max(max(i)for i in l)**2)