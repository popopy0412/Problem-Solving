import sys
sys.setrecursionlimit(10**6)
ip=sys.stdin.readline
def dfs(i):
    global ans
    if ck[i]:
        temp=0
        while s:
            t=s.pop()
            temp+=1
            if t==i:
                ans+=temp
                break
        return
    ck[i]=1
    s.append(i)
    dfs(l[i])
for _ in range(int(ip())):
    n,l=int(ip()),[0]+[*map(int,ip().split())]
    ck=[0]*-~n
    ans=0
    for i in range(1,n+1):
        if ck[i]==0: s=[];dfs(i)
    print(n-ans)