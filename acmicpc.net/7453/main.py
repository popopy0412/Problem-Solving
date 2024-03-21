from bisect import *
n,d,l,r,s,ans=int(input()),[],[],[],0,0
def hap(m):
    t=[]
    for i in d[m]:
        for j in d[m+1]:
            t.append(i+j)
    return t    
for i in range(n): d.append(list(map(int,input().split())))
d=list(zip(*d))
l,r=hap(0),hap(2)
l.sort(reverse=True)
r.sort()
for i in l:
    if s==n*n: break
    br,bl=bisect_right(r,-i,lo=s),bisect_left(r,-i,lo=s)
    s=bl
    ans+=br-bl
print(ans)