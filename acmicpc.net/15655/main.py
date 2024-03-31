from itertools import *
n,m,*l=map(int,open(0).read().split())
for a in combinations(sorted(list(set(l))),m):print(*a)