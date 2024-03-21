from collections import *
n,m=map(int,input().split())
l=[0]*101
for i in range(n+m):
    a,b=map(int,input().split())
    l[a]=b
ck=[0]*101
ck[1]=1
q=deque()
q.append((1,0))
while q:
    now,c=q.popleft()
    if now==100:
        print(c)
        break
    for i in range(1,7):
        next=now+i
        if next > 100 or ck[next]: continue
        if l[next] and not ck[l[next]]:
            ck[next],ck[l[next]]=1,1
            q.append((l[next],c+1))
        elif not l[next]:
            ck[next]=1
            q.append((next,c+1))