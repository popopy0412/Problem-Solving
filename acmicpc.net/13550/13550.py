from collections import *
import sys
ip=sys.stdin.readline
MAX=110000
v=[deque() for _ in range(MAX)]
d=[0]*MAX
cnt=[0]*MAX
n,m=map(int,ip().split())
k=[0]+[*map(int,ip().split())]
rt=int(n**.5)+1
buc=[0]*400
a=int(ip())
ans=[0]*a
q=[[*map(int,ip().split())]+[i] for i in range(a)]
q.sort(key=lambda x:[x[0]//rt, x[1]])
l,r=0,-1

def get_max():
    for i in range(n//rt,-1,-1):
        if buc[i]==0: continue
        for j in range(rt-1,-1,-1):
            if cnt[i*rt+j]: return i*rt+j
    return 0

def add(x,q):
    t=k[x]
    if d[t]:
        diff=v[t][-1]-v[t][0]
        cnt[diff]-=1; buc[diff//rt]-=1
    d[t]+=1
    if q: v[t].appendleft(x)
    else: v[t].append(x)
    diff=v[t][-1]-v[t][0]
    cnt[diff]+=1; buc[diff//rt]+=1

def delete(x,q):
    t=k[x]
    diff=v[t][-1]-v[t][0]
    cnt[diff]-=1; buc[diff//rt]-=1
    d[t]-=1
    if q: v[t].popleft()
    else: v[t].pop()
    if d[t]:
        diff=v[t][-1]-v[t][0]
        cnt[diff]+=1; buc[diff//rt]+=1

for i in range(1,n+1): k[i]=(k[i]+k[i-1])%m
z={}
for i in sorted(k):
    if i in z: continue
    z[i]=len(z)
for i in range(1,n+1): k[i]=z[k[i]]

for s,e,i in q:
    s=s-1
    while r<e: r+=1;add(r,0)
    while s<l: l-=1;add(l,1)
    while e<r: delete(r,0);r-=1
    while l<s: delete(l,1);l+=1
    ans[i]=get_max()
for i in ans: print(i)