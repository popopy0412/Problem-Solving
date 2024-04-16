import sys
s,m=[],0
for _ in range(int(input())):
    n,t=int(sys.stdin.readline()),1
    while s and s[-1][0]<=n:
        a,b=s[-1]
        if a==n:t+=b
        m+=b
        s.pop()
    m+=1 if s else 0
    s.append((n,t))
print(m)