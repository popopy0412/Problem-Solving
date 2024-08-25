b='aeiou'
for s in open(0).read().split()[:-1]:
    n,x=len(s),1
    for i in s:
        if i in b: x=0
    for i in range(n-2):
        if s[i] in b and s[i+1] in b and s[i+2] in b: x=1
        elif s[i] not in b and s[i+1] not in b and s[i+2] not in b: x=1
    for i in range(n-1):
        if s[i] == s[i+1] and s[i] not in 'eo': x=1
    print(f'<{s}> is {"not " if x else ""}acceptable.')