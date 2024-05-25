import sys
ip=sys.stdin.readline
k=lambda x:[[x for _ in range(n+1)] for _ in range(n+1)]
n,m=int(ip()),int(ip())
d,l=k([]),k(1e9)
for _ in range(m):
	a,b,c=map(int,ip().split())
	l[a][b]=min(l[a][b],c)
	d[a][b]=[a]
for k in range(1,n+1):
	for i in range(1,n+1):
		for j in range(1,n+1):
			if i!=j and l[i][k]+l[k][j]<l[i][j]:
				l[i][j]=l[i][k]+l[k][j]
				d[i][j]=d[i][k]+d[k][j]
for i in range(1,n+1):
	for j in range(1,n+1):
		if l[i][j]==1e9: l[i][j]=0
for i in l[1:]:print(*i[1:])
for i in range(1,n+1):
	for j in range(1,n+1):
		if l[i][j]:print(len(d[i][j])+1,*d[i][j],j if l[i][j] else 0)
		else:print(0)