import sys
sys.setrecursionlimit(10**6)
ip=sys.stdin.readline
def dfs(now):
    global id,num
    ck[now]=parent=id
    s.append(now)
    id+=1
    for next in l[now]:
        if not ck[next]: parent=min(parent,dfs(next))
        elif not f[next]: parent=min(parent,ck[next])
    
    if parent==ck[now]:
        while s:
            t=s.pop()
            w[t]=num
            f[t]=1
            if t==now: break
        num+=1
    return parent

for _ in range(int(ip())):
    n,m=map(int,ip().split())
    id,num=1,0
    l,s=[[] for _ in range(n+1)],[]
    ck,f,p,w=[0]*-~n,[0]*-~n,[0]*-~n,[0]*-~n
    for _ in range(m):
        a,b=map(int,ip().split())
        l[a].append(b)
    for i in range(1,n+1):
        if ck[i]==0: dfs(i)
    t=set()
    for i in range(1,n+1):
        for j in l[i]:
            if w[i]!=w[j] and w[j] not in t: t.add(w[j])
    print(num-len(t))