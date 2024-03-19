def check(f,s,i):
    for j in range(len(f)):
        if f[j] != s[i+j]: return j
    return len(f)
n,m,s=open(0).read().split()
n,m,c,i=int(n),int(m),0,0
f='IO'*n+'I'
while i < m-2*n:
    if s[i]=='O':
        i+=1
        continue
    if (t:=check(f,s,i)) == 2*n+1:
        c+=1
        i+=t
        while i < m-1 and s[i:i+2]=='OI':
            c+=1
            i+=2
        continue
    i+=t
print(c)