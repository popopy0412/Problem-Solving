import sys
ip=sys.stdin.readline
MAX=100001
tree=[0]*MAX
n,m=[*map(int,ip().split())]
k=[*map(int,ip().split())]
rt=int(n**.5)
ans=[0]*m
mx=0
q=[[*map(int,ip().split())]+[i] for i in range(m)]
q.sort(key=lambda x:[x[0]//rt, x[1]])
l,r=0,-1

def update(i,v,q):
    global mx
    i=k[i]
    cnt=0
    if q: mx+=v*(query(MAX-1)-query(i))
    else: mx+=v*(query(i-1))
    while i<=MAX and cnt<20:
        tree[i]+=v
        i+=i&-i

def query(i):
    z=0
    while i:
        z+=tree[i]
        i-=i&-i
    return z

z={}
for i in sorted(k):
    if i in z: continue
    z[i]=len(z)+1
for i in range(n): k[i]=z[k[i]]

for s,e,i in q:
    s,e=s-1,e-1
    while r<e: r+=1;update(r,1,1)
    while s<l: l-=1;update(l,1,0)
    while e<r: update(r,-1,1);r-=1
    while l<s: update(l,-1,0);l+=1
    ans[i]=mx
for i in ans: print(i)