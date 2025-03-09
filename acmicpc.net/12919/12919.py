from collections import *
s,t=open(0).read().split()
ck,q={t},deque([t])
ans=0
while len(q):
    n=q.popleft()
    if n==s: ans=1;break
    if len(n) <= len(s): continue
    if n[-1]=='A' and n[:-1] not in ck:
        ck.add(n[:-1])
        q.append(n[:-1])
    if n[0]=='B' and n[1:][::-1] not in ck:
        ck.add(n[1:][::-1])
        q.append(n[1:][::-1])
print(ans)
