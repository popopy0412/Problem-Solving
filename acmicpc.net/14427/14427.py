import sys
ip=sys.stdin.readline

def update(i,v):
    k[i]=v
    i+=s-1
    while i:=i//2:
        a,b=k[tree[i*2]],k[tree[i*2+1]]
        tree[i]=tree[i*2+1] if a>b else tree[i*2]

n,k=int(ip()),[1e10]+[*map(int,ip().split())]
s=1<<n.bit_length()
if s%n==0: s//=2
tree=[0]*2*s
for i in range(n): tree[i+s]=i+1
for i in range(s-1,0,-1): tree[i]=tree[i*2+1] if k[tree[i*2]]>k[tree[i*2+1]] else tree[i*2]

for i in range(int(ip())):
    q,*p=map(int,ip().split())
    if q==1: update(*p)
    else: print(tree[1])