MOD=10**9+7
for i in range(int(input())):
    n,m=map(int,input().split())
    if i: x,y=(x*n+y*m)%MOD,y*n%MOD
    else: x,y=m,n
a,b=1,MOD-2
while b:
    if b%2: a*=y
    y*=y
    b//=2
    a%=MOD
    y%=MOD
print(x*a%MOD)
