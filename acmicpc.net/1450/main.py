n,m,*l=map(int,open(0).read().split())
x,y=[0],[0]
ans=0
for i in l[:n//2]:
    for j in range(len(x)): x.append(x[j]+i)
for i in l[n//2:]:
    for j in range(len(y)): y.append(y[j]+i)
x.sort()
y.sort()
a,b=len(x)-1,len(y)-1
while b and x[a]+y[b]>m: b-=1
while a>=0:
    while b<len(y) and x[a]+y[b]<=m: b+=1
    ans+=b
    a-=1
print(ans)