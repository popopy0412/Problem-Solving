from collections import *
n,k,*l=map(int,open(0).read().split())
q=deque()
t,s=1,0
cnt=0
while 1:
    s=(s-1)%(2*n)
    for i in range(len(q)): q[i]+=1
    if q and q[0]==n-1: q.popleft()
    for i in range(len(q)):
        nxt=(s+q[i]+1)%(2*n)
        if l[nxt] and (i==0 or i and q[i]+1 != q[i-1]):
            q[i]+=1
            l[nxt]-=1
            if l[nxt]==0: cnt+=1
    if q and q[0]==n-1: q.popleft()
    if l[s]:
        q.append(0)
        l[s]-=1
        if l[s]==0: cnt+=1
    if cnt>=k: break
    t+=1
print(t)