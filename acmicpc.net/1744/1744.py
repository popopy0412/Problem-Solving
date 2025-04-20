n,*l=map(int,open(0).read().split())
ans=0
l=[*sorted(filter(lambda x:x>0,l))][::-1]+[*sorted(filter(lambda x:x<=0,l))]
i=0
while i<n:
    a=l[i]
    if i==n-1: ans+=a;break
    b=l[i+1]
    if a*b>a+b: ans+=a*b;i+=1
    else: ans+=a
    i+=1
print(ans)