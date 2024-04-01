from collections import *
n,m=map(int,input().split())
q=deque()
ans=INF=200000
ck=[INF]*-~INF
cnt=[0]*-~INF
ck[n],cnt[n]=0,1
q.append((n,0))
while q:
    now,c=q.popleft()
    if c > ans: continue
    if now == m:
        ans=min(c,ans)
        continue
    t=[now-1,now+1,now*2]
    for next in t:
        if 0 <= next <= INF and c+1 <= ans and c+1 <= ck[next]:
            if c+1 == ans and next != m: continue
            q.append((next,c+1))
            ck[next]=c+1
            cnt[next]+=1
print(ans)
print(cnt[m])