import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
def dfs(now,cnt):
    global n
    k=10**7
    if now==n:
        if a[-1]==b[-1]: k=cnt
        return k
        
    if 1<=now and a[now-1]^1==b[now-1] or now==0:
        if now!=0: a[now-1]^=1
        a[now]^=1
        if now!=n-1: a[now+1]^=1
        k=min(k,dfs(now+1,cnt+1))
        if now!=0: a[now-1]^=1
        a[now]^=1
        if now!=n-1: a[now+1]^=1
    if 1<=now and a[now-1]==b[now-1] or now==0: k=min(k,dfs(now+1,cnt))
    return k

n=int(input())
a,b=[*map(int,input()[:-1])],[*map(int,input()[:-1])]
ans=dfs(0,0)
print(ans if ans!=10**7 else -1)