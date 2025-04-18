s=[]
for c in input():
    if c in'+-*/':s[-1]=eval('int(s[-2]'+c+'s.pop())')
    else:s+=[int(c)]
print(*s)