import sys
input=sys.stdin.readline
a,b,MOD,INF=1,1,10**9+7,4000001
N=[1]*INF
for i in range(1,INF): N[i]=N[i-1]*i%MOD
q=int(input())
while q:
    q-=1
    n,m=map(int,input().split())
    a,b=N[n],N[m]*N[n-m]%MOD
    x,k,t=1,b,MOD-2
    while t:
        if t%2: x=x*k%MOD
        k=k*k%MOD
        t//=2
    print(a*x%MOD)