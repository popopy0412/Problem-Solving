n,*l=map(int,open(0).read().split())
l.sort()
print(max(l[i]*(n-i) for i in range(n)))