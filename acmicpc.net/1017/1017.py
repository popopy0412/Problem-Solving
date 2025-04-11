n,*l=map(int,open(0).read().split())
MAX=2001
p=[1]*MAX
v=[[] for _ in range(n)]
p[0]=p[1]=0

def dfs(now):
    ck[now]=1
    for i in v[now]:
        if ck[i]: continue
        ck[i]=1
        if path[i]==-1 or dfs(path[i]):
            path[i]=now
            return 1
    return 0

for i in range(2,MAX//2+1):
    if p[i]==0: continue
    for j in range(i*2,MAX,i): p[j]=0

for i in range(n-1):
    x=l[i]
    for j in range(i+1,n):
        y=l[j]
        if p[x+y]:
             v[i].append(j)
             v[j].append(i)

ans=[]
for i in v[0]:
    path=[-1]*n
    path[i]=0
    cnt=1
    for j in range(1,n):
        ck=[0]*n
        ck[0]=ck[i]=1
        if i!=j and l[0]%2==l[j]%2 and dfs(j): cnt+=1
    if cnt==n//2: ans.append(l[i])
if ans: print(*sorted(ans))
else: print(-1)