n,*l=map(int,open(0).read().split())
c,a,s=[0]*8**7,[-1]*n,[]
for i in l:c[i]+=1
for i in range(n):
    while s and c[l[s[-1]]]<c[l[i]]:a[s.pop()]=l[i]
    s+=[i]
print(*a)