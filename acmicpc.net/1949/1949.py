import sys
sys.setrecursionlimit(10**5)
ip=sys.stdin.readline
n,*l=int(ip()),*map(int,ip().split())
v=[[] for _ in range(n)]
dp=[[0,0] for _ in range(n)]
def rec(now,prv):
    a,b=0,0
    for i in v[now]:
        if i==prv: continue
        t=rec(i,now)
        a+=max(t)
        b+=t[0]
    dp[now]=[a,b+l[now]]
    return dp[now]

for _ in range(n-1):
    a,b=map(int,ip().split())
    a,b=a-1,b-1
    v[a].append(b)
    v[b].append(a)
print(max(rec(0,-1)))