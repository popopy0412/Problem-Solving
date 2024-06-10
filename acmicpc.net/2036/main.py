n,*l=map(int,open(0).read().split())
ans=0
l.sort()
i=0
while i<n-1:
    a,b=l[i],l[i+1]
    i+=1
    if a<=0:
        if b<=0:
            ans+=a*b
            i+=1
        else: ans+=a            
    else:
        if (n-i-1)%2 or a+b>a*b: ans+=a
        else:
            ans+=a*b
            i+=1
if i==n-1: ans+=l[i]
print(ans)
