from collections import *
import sys
ip=sys.stdin.readline
for _ in range(int(ip())):
	n,l=int(ip()),[*map(int,ip().split())]
	ind,outd=[0]*-~n,[[0 for _ in range(n+1)] for _ in range(n+1)]
	for i in range(n-1):
		for j in l[i+1:]:
			ind[j]+=1
			outd[l[i]][j]=1

	for _ in range(int(ip())):
		a,b=map(int,ip().split())
		if outd[a][b]:
			ind[a]+=1
			ind[b]-=1
			outd[a][b]=0
			outd[b][a]=1
		else: 
			ind[b]+=1
			ind[a]-=1
			outd[a][b]=1
			outd[b][a]=0

	q=deque()
	for i in range(1,n+1):
		if ind[i]==0: q.append(i)

	a=[]
	while q:
		now=q.popleft()
		a.append(now)
		for i in range(1,n+1):
			if outd[now][i]:
				ind[i]-=1
				if ind[i]==0:
					q.append(i)
	if len(a)!=n: print('IMPOSSIBLE')
	else: print(*a)
