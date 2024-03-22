from collections import *
e=input()
def rec(i):
    s1,s2=deque(),deque()
    s,k=e[i],i
    if e[i] == '(':
        s,k=rec(i+1)
    s1.append(s)
    i=k+1
    while i < len(e):
        o=e[i]
        if o == ')': break
        if e[i+1] == '(': s,k=rec(i+2)
        else: s,k=e[i+1],i+1
        if o in '*/':
            s=s1.pop()+s+o
            s1.append(s)
        elif o in '+-':
            s1.append(s)
            s2.append(o)
        i=k+1
            
    r=s1.popleft()
    while s2:
        r += s1.popleft()+s2.popleft()
    return r, i
print(rec(0)[0])