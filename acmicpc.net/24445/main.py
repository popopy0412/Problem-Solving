from collections import *
import sys
ip=sys.stdin.readline
n,m,r=map(int,ip().split())
k=[[*map(int,ip().split())] for _ in range(m)]
l=[[] for _ in range(n+1)]
ck=[0]*-~n
q=deque([r])
cnt=1
k.sort(reverse=True)
for a,b in k:
    l[a].append(b)
    l[b].append(a)
while q:
    now=q.popleft()
    ck[now]=cnt
    cnt+=1
    for next in l[now]:
        if ck[next]==0:
            ck[next]=-1
            q.append(next)
print(*ck[1:])