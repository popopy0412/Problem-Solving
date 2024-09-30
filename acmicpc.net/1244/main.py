ip=input
n,l=int(ip()),[*map(int,ip().split())]
for _ in range(int(ip())):
    a,b=map(int,ip().split())
    if a==1:
        for i in range(b-1,n,b): l[i]^=1
    else:
        for i in range(min(b,n-b+1)):
            if l[b-1+i]!=l[b-1-i]: break
            l[b-1+i]=l[b-1-i]=l[b-1+i]^1
for i in range(n//20+(1 if n%20 else 0)): print(*l[i*20:i*20+20])