import sys
ip=sys.stdin.readline
n=int(ip())
l=[*map(int,ip().split())]
t=[[] for _ in range(n)]
d=[[0,0] for _ in range(n)]
dt=[[[],[i]] for i in range(n)]
def dfs(now,par):
    a,b,z=0,0,[]
    for i in t[now]:
        if i==par: continue
        dfs(i,now)
        a+=max(d[i])
        b+=d[i][0]
        z+=dt[i][0] if d[i][0]>d[i][1] else dt[i][1]
        dt[now][1]+=dt[i][0]
    
    d[now]=[a,b+l[now]]
    dt[now][0]+=z

for _ in range(n-1):
    a,b=map(int,ip().split())
    a,b=a-1,b-1
    t[a].append(b)
    t[b].append(a)

dfs(0,-1)
i=d[0].index(max(d[0]))
print(d[0][i])
print(*sorted(map(lambda x:int(x)+1, dt[0][i])))
