ck=[]
def bellFord(s,n,e):
    global ck
    ck[s]=1
    dis=[INF:=10**10]*-~n
    dis[s]=0
    for _ in range(n):
        ref=False
        for i in e:
            a,b,c=i
            if dis[a] != INF and dis[b] > dis[a]+c:
                dis[b] = dis[a]+c
                ck[b]=1
                ref=True
    return ref

def solve():
    global ck
    n,m,w=map(int,input().split())
    ck,e=[0]*-~n,[]
    for _ in range(m):
        a,b,c=list(map(int,input().split()))
        e.extend([[a,b,c],[b,a,c]])
    for _ in range(w):
        a,b,c=map(int,input().split())
        e.append([a,b,-c])
    
    for i in range(1,n+1):
        if not ck[i] and bellFord(i,n,e):
            print('YES')
            return
    print('NO')

for _ in range(int(input())):solve()