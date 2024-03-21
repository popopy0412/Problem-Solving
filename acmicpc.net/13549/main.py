from collections import *
n,m=map(int,input().split())
s,q,ck=10**9,deque(),[10**9]*200001
ck[n]=0
q.append((n,0))
while q:
    a,b=q.popleft()
    if a==m: s=min(s,b)
    if b>=s: continue
    c=[a-1,a+1,a*2]
    d=[1,1,0]
    for i in range(3):
        co=b+d[i]
        if 0 <= c[i] <= 200000 and ck[c[i]] > co:
            if c[i] > m and co+m-c[i] >= s: continue
            ck[c[i]]=co
            q.append((c[i],co))
print(s)