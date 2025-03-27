from collections import *
n,k,*l=map(int,open(0).read().split())
l=[0]+l
s,dp=l.copy(),[0]*-~n
d=deque()
for i in range(1,n+1):
    s[i]+=s[i-1]
    now=dp[i-1]-s[i]
    while d and i-d[0][0]>k: d.popleft()
    while d and d[-1][1]<now: d.pop()
    d.append((i,now))
    if i<=k: dp[i]=s[i]
    else: dp[i]=d[0][1]+s[i]
print(dp[n])