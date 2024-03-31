from itertools import *
n,m,*l=map(int,open(0).read().split())
l=list(set(l))
l.sort()
for a in product(l,repeat=m): print(*a)