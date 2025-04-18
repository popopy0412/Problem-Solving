s=[]
for c in input():
    if c.isdigit(): s+=[int(c)]
    else: a,b=s.pop(),s.pop();eval('s.append(int(b'+c+'a))')
print(*s)