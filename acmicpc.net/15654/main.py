import sys
input=sys.stdin.readline
n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()

def rec(cnt,d,c):
    if cnt==m:
        print(*d)
        return
    for i in range(n):
        if c[i]: continue
        c[i]=1
        rec(cnt+1,d+[l[i]],c)
        c[i]=0

rec(0,[],[0]*n)