import sys
ip=sys.stdin.readline
il=lambda:[*map(int,ip().split())]
n,l,m=int(ip()),il(),int(ip())
d=[[0 for _ in range(n)] for _ in range(n)]
def check(i,c=0):
    for j in range(n//2+1):
        x,y=i-j,i+c+j
        if x<0 or y>=n or l[x]!=l[y]: break
        d[x][y]=1
for i in range(n):
    check(i)
    if i<n-1 and l[i]==l[i+1]: check(i,1)
for _ in range(m):
    a,b=il()
    print(d[a-1][b-1])
