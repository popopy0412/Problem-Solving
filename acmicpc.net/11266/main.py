import sys
sys.setrecursionlimit(10**6)
il=lambda:[*map(int,sys.stdin.readline().split())]
n,m=il()
id=0
v=[[] for _ in range(n+1)]
ans=[]
pre=[0]*-~n

def dfs(prev,now):
    global id
    id+=1
    parent=pre[now]=id
    check=0
    for next in v[now]:
        if next==prev: continue
        if pre[next]: parent=min(parent,pre[next])
        else:
            temp=dfs(now,next)
            if prev==0: check+=1
            elif pre[now] <= temp: check=1
            parent=min(parent,temp)
            
    if prev==0 and check > 1 or prev and check and len(v[now]) > 1: ans.append(now)
    return parent

for _ in range(m):
    a,b=il()
    v[a].append(b)
    v[b].append(a)
for i in range(1,n+1):
    if pre[i]==0: dfs(0,i)
print(len(ans))
print(*sorted(ans))

