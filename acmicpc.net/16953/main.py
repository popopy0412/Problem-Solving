from collections import *
n,m=map(int,input().split())
d={n:1}
q=deque()
q.append((n,1))
while q:
    now,c=q.popleft()
    if now == m:
        print(c)
        exit(0)
    l=[now*2,now*10+1]
    for k in l:
        if k <= 10**9 and k not in d:
            d[k]=c+1
            q.append((k,c+1))
print(-1)