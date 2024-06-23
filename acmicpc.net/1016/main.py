n,m=map(int,input().split())
r=m-n+1
l=[1]*r
for i in range(2,int(m**0.5)+1):
    t=i*i
    a=n//t*t
    for j in range(a-n,r,t):
        if j<0: continue
        l[j]=0
print(sum(l))