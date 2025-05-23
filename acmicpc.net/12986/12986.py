from collections import *
import sys
ip=sys.stdin.readline
MAX=100001
cnt=[0]*MAX
d=[0]*MAX
n,m=[*map(int,ip().split())]
k=[*map(int,ip().split())]
rt=int(n**.5)
ans=[0]*m
mx=0
q=[[*map(int,ip().split())]+[i] for i in range(m)]
q.sort(key=lambda x:[x[0]//rt, x[1]])
l,r=0,-1

def update(x,v):
    global mx
    t=k[x]
    b=cnt[t]
    if b: d[b]-=1
    if d[b]==0 and v<0 and mx==b: mx=b-1
    b+=v;cnt[t]=b
    if b: d[b]+=1
    if d[b]==1: mx=max(mx,b)

z={}
for i in sorted(k):
    if i in z: continue
    z[i]=len(z)
for i in range(n): k[i]=z[k[i]]

for s,e,i in q:
    s,e=s-1,e-1
    while r<e: r+=1;update(r,1)
    while s<l: l-=1;update(l,1)
    while e<r: update(r,-1);r-=1
    while l<s: update(l,-1);l+=1
    ans[i]=mx
for i in ans: print(i)