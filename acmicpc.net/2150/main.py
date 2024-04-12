import sys
sys.setrecursionlimit(10**6)
ip=lambda:map(int,sys.stdin.readline().split())
n,m=ip()
l=[[] for _ in range(n+1)]
ck=[0]*-~n
fin=[0]*-~n
s,ans=[],[]
id=0

def dfs(now):
    global id
    id+=1
    parent=ck[now]=id
    s.append(now)
    for next in l[now]:
        if not ck[next]:
            parent = min(parent, dfs(next))
        elif not fin[next]:
            parent = min(parent, ck[next])
    
    if parent == ck[now]:
        temp=[]
        while True:
            t=s.pop()
            temp.append(t)
            fin[t]=1
            if now==t: break
        temp.sort()
        temp.append(-1)
        ans.append(temp)
    return parent
          
for _ in range(m):
    a,b=ip()
    l[a].append(b)
for i in range(1,n+1): l[i].sort()
for i in range(1,n+1):
    if not fin[i]: dfs(i)
ans.sort()
print(len(ans))
for i in ans: print(*i)