l=input
n,k=int(l()),int(l())
l,r=1,k
while l<=r:
    m,c=(l+r)//2,0
    for i in range(1,n+1):c+=min(m//i,n)
    if c>=k:a,r=m,m-1
    else:l=m+1
print(a)