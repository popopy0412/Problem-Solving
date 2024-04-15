from collections import *
n,m=map(int,input().split())
k=[1e6]*200001
k[n]=0
q,d=deque([(n,0)]),{n:-1}
while q:
	n,c=q.popleft()
	if c>k[n] or n==m:continue
	l=[n-1,n+1,n*2]
	for x in l:
		if 0<=x<2*1e5 and k[x]>c+1:
			q.append((x,c+1))
			k[x],d[x]=c+1,n
print(k[m])
while m!=-1:q.appendleft(m);m=d[m]
print(*q)