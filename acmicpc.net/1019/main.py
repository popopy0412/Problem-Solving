def fac(n):
    for i in range(2,n): n*=i
    return max(n,1)

s=input()
t=n=len(s)-1
l=[0]*10
for k in range(n):
    c=int(s[k])
    m=0; j=0
    for i in range(1,n): j += fac(n-1)//fac(i)//fac(n-1-i)*(9**(n-1-i))*i
    l[0]+=j*9
    for i in range(1,n+1): m += fac(n)//fac(i)//fac(n-i)*(9**(n-i))*i
    if k==0: l[0]-=m
    for i in range(10): l[i]+=m*c
    if c > 0:
        if k != 0: l[0]+=10**n
        for i in range(1,c): l[i]+=10**n
    l[c]+=int(s[k+1:])+1
    n-=1
if(t==0): l[0]-=1
for i in range(int(s[-1])+1): l[i]+=1
print(*l)
