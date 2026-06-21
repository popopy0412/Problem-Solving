n=0
k=0
l=[]
d=[[] for _ in range(4)]
now=[]
check=[0]*101
def bfs(p):
    global now,check
    for i in now:
        for x,y in l[i]:
            if check[x] or y!=p: continue
            check[x]=1
            now.append(x)
def dfs(cnt):
    global now,check
    ans=0
    if cnt==k: return len(now)
    temp=now.copy()
    ck=check.copy()
    for i in range(1,4):
        bfs(i)
        ans=max(ans,dfs(cnt+1))
        now=temp.copy()
        check=ck.copy()
    return ans
        
def solution(N, infection, edges, K):
    global n,l,d,k
    n,k=N,K
    l=[[] for _ in range(n+1)]
    for a,b,c in edges:
        l[a].append((b,c))
        l[b].append((a,c))
        d[c].append((a,b))
    
    check[infection]=1
    now.append(infection)
    return dfs(0)