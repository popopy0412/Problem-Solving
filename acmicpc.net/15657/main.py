from itertools import *
n,m,*l=map(int,open(0).read().split())
l.sort()
for i in combinations_with_replacement(l,m):print(*i)
