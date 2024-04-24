INF=10**6+1
n=int(input())
p=[1]*INF
p[0]=0
l=[]
for i in range(2,n):
	if p[i]==0: continue
	l.append(i)
	for j in range(i*2,n,i): p[j]=0
a=n//2
b=n-a
while a>=4:
	s=[]
	for j in l:
		if j > a-j: break
		if p[a-j]:
			s.extend([j,a-j])
			break
	for j in l:
		if j > b-j: break
		if p[b-j]:
			s.extend([j,b-j])
			break
	if len(s)==4:
		print(*(sorted(s)))
		exit(0)
	a-=1
	b+=1
print(-1)
