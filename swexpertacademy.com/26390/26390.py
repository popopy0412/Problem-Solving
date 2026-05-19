ip=input
t=int(ip())
while t:
    t-=1
    n=int(ip())
    ans=0
    l,ck=[0]*-~n,[0]*-~n
    d=[[] for _ in range(n+1)]
    k=[[*map(int,ip().split())] for _ in range(n-1)]
    for a,b in k:
        l[a]+=1
        l[b]+=1
    for i in l[1:]:
        if i==1: ans+=1
    print(max(0,ans-2))