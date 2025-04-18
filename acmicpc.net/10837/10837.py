import sys
ip=sys.stdin.readline
n,m=int(ip()),int(ip())
for _ in range(m):
    a,b=map(int,ip().split())
    if a<b: a,b,k=0,b-a,n-a
    else: a,b,k=a-b,0,n-b
    if b and b>(k+1)//2: print(0)
    elif a and a>k//2+1: print(0)
    else: print(1)