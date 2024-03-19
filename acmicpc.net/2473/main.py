from bisect import *
def hap(l,a,b,c): return abs(l[a]+l[b]+l[c])
n,*l=map(int,open(0).read().split())
l.sort()
a,b,c=0,1,2
min=hap(l,a,b,c)
for i in range(n-2):
    for j in range(i+1,n-1):
        if min==0:
            print(l[a],l[b],l[c])
            exit(0)
        e=bisect_right(l,-l[i]-l[j],lo=j+1,hi=n)
        s=e-1
        if e<n:
            t=hap(l,i,j,e)
            if min > t: a,b,c,min=i,j,e,t
        if s<=j: continue
        t=hap(l,i,j,s)
        if min > t: a,b,c,min=i,j,s,t
print(l[a],l[b],l[c])
