import sys
sys.setrecursionlimit(10**6)
n,m,k=map(int,input().split())
v=[[] for _ in range(n+1)]
ck=[0]*(n+m+1)
path=[0]*(n+m+1)
ans=0
mx=0

def dfs(now):
    global mx
    for i in v[now]:
        if ck[i]: continue
        ck[i]=1
        if (path[i]==0 or dfs(path[i])):
            path[i]=now
            return 1
    return 0


for i in range(1,n+1):
    a,*b=map(int,input().split())
    for j in b: v[i].append(j+n)

for j in range(2):
    for i in range(1,n+1):
        ck=[0]*(n+m+1)
        if dfs(i):
            if j:
                if mx==k: break
                mx+=1
            ans+=1
            
print(min(ans,n+k))