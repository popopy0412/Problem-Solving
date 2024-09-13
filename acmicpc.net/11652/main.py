n,*l=map(int,open(0).read().split())
m,a,d=0,2**63,{}
for i in l:
	d[i]=d.get(i,0)+1
	if m<=d[i]:
		if m<d[i]: m,a=d[i],i
		else: a,m=min(a,i),max(m,d[i])
print(a)
