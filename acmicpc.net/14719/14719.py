n,m,*l=map(int,open(0).read().split())
s,t=[],0
for i,h in enumerate(l):
    while s and l[s[-1]]<=h:
        b=s.pop()
        if s: t+=(min(h,l[s[-1]])-l[b])*(i-s[-1]-1)
    s.append(i)
print(t)