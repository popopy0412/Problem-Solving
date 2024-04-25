import sys
ip=sys.stdin.readline
s,a=[],0
for _ in range(int(ip())):
    n=int(ip())
    while s and s[-1]<=n:s.pop()
    a+=len(s)
    s.append(n)
print(a)