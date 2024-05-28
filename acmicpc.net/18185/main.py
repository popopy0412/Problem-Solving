n,*l=map(int,open(0).read().split())
p=[3,5,7]
ans=0
for i in range(n):
	j=0
	while l[i]:
		while i+j+1<n and j<2 and l[i+j]<=l[i+j+1]: j+=1
		t=l[i]
		if i+j+1<n and j!=2 and l[i+j+1]!=0: t=min(t,l[i+j]-l[i+j+1])
		ans+=p[j]*t
		for k in range(j+1): l[i+k]-=t
print(ans)