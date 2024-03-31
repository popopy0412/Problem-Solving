from itertools import *
n,m,*l=map(int,open(0).read().split())
for a in sorted(list(set(combinations(sorted(l),m)))):print(*a)