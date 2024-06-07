from itertools import *
p=lambda i:[j*l[i]*m[i%2] for j in k[i]]
k=[(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]
m=(1,2**-0.5)
ans=0
for l in permutations(map(int,input().split()),8):
    ck=1
    for i in range(8):
        a,b,c,d,e,f=*p(i),*p((i+1)%8),*p((i+2)%8)
        if (a-c)*(b-f)-(a-e)*(b-d)<=0:
            ck=0
            break
    if ck: ans+=1
print(ans)