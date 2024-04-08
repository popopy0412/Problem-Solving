n,m=map(int,input().split())
a,b,MOD=1,1,10**9+7
def f(n):
    x=1
    for i in range(1,n+1): x=x*i%MOD
    return x
a,b=f(n),f(m)*f(n-m)%MOD
x,k,t=1,b,MOD-2
while t:
    if t%2: x=x*k%MOD
    k=k*k%MOD
    t//=2
print(a*x%MOD)