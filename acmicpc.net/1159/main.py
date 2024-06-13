n,*l=open(0).read().split()
a,c=1,1
l.sort()
for i in range(int(n)-1):
	x,y=l[i][0],l[i+1][0]
	c=c+1 if x==y else 1
	if c==5:
		a=0
		print(x,end='')
if a:print('PREDAJA')