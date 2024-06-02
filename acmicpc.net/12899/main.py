import sys
ip=sys.stdin.readline
def update(x,i,v):
	l,r=1,n
	while l!=r:
		tree[i]+=v
		m=l+r>>1
		if x>m:l,i=m+1,i*2+1
		else:r,i=m,i*2
	tree[i]+=v
def query(l,r,i,v):
	if l==r: return l
	m=l+r>>1
	t=tree[i*2]
	if t<v: return query(m+1,r,i*2+1,v-t)
	else: return query(l,m,i*2,v)
n=2000000
tree=[0]*n*3
for i in range(int(ip())):
	t,x=map(int,ip().split())
	if t==1: update(x,1,1)
	else:
		t=query(1,n,1,x)
		print(t)
		update(t,1,-1)