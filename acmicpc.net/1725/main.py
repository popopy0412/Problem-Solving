import sys
input=sys.stdin.readline
ans,l=0,[]
for _ in range(int(input())):
    n,a,b=int(input()),0,0
    while l and l[-1][0] >= n:
        t,k=l.pop()
        a=t
        b+=k
        ans = max(ans,a*b)
    l.append((n,b+1))
    ans = max(ans,n*(b+1))
m=0
while l:
    t,k=l.pop()
    n=t
    m+=k
    ans = max(ans,n*m)
print(ans)