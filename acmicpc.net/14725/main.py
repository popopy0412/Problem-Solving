from collections import *
def solve(s, t):
    if s == t: return 0
    check=set([s])
    q=deque(); q.append((s,''))

    while q:
        n,p = q.popleft()
        l=[(n**2,'*'),(n*2,'+'),(1,'/')]
        for i, j in l:
            if i == t: return p+j
            if i not in check and i <= t:
                check.add(i)
                q.append((i,p+j))
    return -1
print(solve(*map(int,input().split())))