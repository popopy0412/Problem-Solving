n=int(input())
l=[0,*map(int,input().split())]
v=[[0]*-~n for _ in range(n+1)]
ck=[0]*-~n
red,blue=[],[]
root=[*range(n+1)]
s=sum(l)
ans=1e9
for i in range(1,n+1):
    for j in [*map(int,input().split())][1:]: v[i][j]=1

sumv=lambda x: sum([l[i] for i in range(1,n+1) if ck[i]==x])
def union(x, y):
    global root
    x,y=find(x),find(y)
    if x!=y:
        if x>y: root[x]=y
        else: root[y]=x
        find(x);find(y)
    
def find(x):
    global root
    if x!=root[x]: root[x]=find(root[x])
    return root[x]

def check(li):
    global root,n
    root=[*range(n+1)]
    for i in range(len(li)):
        for j in range(len(li)):
            x,y=li[i],li[j]
            if v[x][y]: union(x,y)

    t=find(root[li[0]])
    for i in li[1:]:
        if t!=find(root[i]): return 0
    return 1

def rec(now):
    global n,ans
    if now==n+1:
        if check(red) and check(blue):
            ans=min(ans,abs(sumv(0)-sumv(1)))
        return
    if len(red)<n//2:
        ck[now]=1
        red.append(now)
        rec(now+1)
        red.pop()
        ck[now]=0
    if len(blue)<n-1:
        blue.append(now)
        rec(now+1)
        blue.pop()

rec(1)
print(-1 if ans==1e9 else ans)