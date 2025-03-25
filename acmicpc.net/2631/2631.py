from bisect import *
n,*l=map(int,open(0).read().split())
d=[]
for i in l:
    if d and d[-1]>i: d[bisect_left(d,i)]=i
    else: d+=[i]
print(n-len(d))