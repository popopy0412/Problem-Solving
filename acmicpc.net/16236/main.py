from collections import *
from heapq import *
def move(n,m,x,y,size):
    pq=[]
    q=deque()
    q.append((x,y,0))
    ck=[[0 for _ in range(n+1)] for _ in range(n+1)]
    m[x][y]=0
    ck[x][y]=1
    while q:
        a,b,c=q.popleft()
        if 0 < m[a][b] < size:
            if pq and c > pq[0][0]: break
            heappush(pq,(c,a,b))
            continue
        X=[a-1,a,a,a+1]
        Y=[b,b-1,b+1,b]
        for i in range(4):
            x,y=X[i],Y[i]
            if 0 <= x < n and 0 <= y < n and m[x][y] <= size and ck[x][y]==0:
                ck[x][y]=1
                q.append((x,y,c+1))
    return pq[0] if pq else (-1,0,0)
def solve(n,m,x,y,cnt):
    ans=0
    for size in range(2,30):
        for _ in range(size):
            if cnt==0: return ans
            c,a,b=move(n,m,x,y,size)
            if c==-1: return ans
            else: x,y,ans=a,b,ans+c
            cnt-=1
n=int(input())
m=[[*map(int,input().split())] for _ in range(n)]
cnt=0
for l in m:
    if 9 in l: x,y=m.index(l),l.index(9)
    cnt+=n-l.count(0)
print(solve(n,m,x,y,cnt-1))
