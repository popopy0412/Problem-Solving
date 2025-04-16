import sys
ip=sys.stdin.readline
MAX=100001
n,m=[*map(int,ip().split())]
S=1<<MAX.bit_length()
tree=[0]*-~S
k=[*map(int,ip().split())]
rt=int(n**.5)
su=0
a=int(ip())
ans=[0]*a
q=[[*map(int,ip().split())]+[i] for i in range(a)]
q.sort(key=lambda x:[x[0]//rt, -x[1]])
l,r=0,-1

def update(i,v):
    global su
    i,z=k[i],k[i]
    while i<=S:
        tree[i]+=v
        i+=i&-i
    su+=v*max(0,(query(min(MAX-1,z+m))-query(max(0,z-m-1))-1*max(0,v)))

def query(i):
    z=0
    while i:
        z+=tree[i]
        i-=i&-i
    return z
for s,e,i in q:
    s,e=s-1,e-1
    while r<e: r+=1;update(r,1)
    while s<l: l-=1;update(l,1)
    while e<r: update(r,-1);r-=1
    while l<s: update(l,-1);l+=1
    ans[i]=su

for i in ans: print(i)