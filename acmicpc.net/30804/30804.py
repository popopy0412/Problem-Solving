n,*l=map(int,open(0).read().split())
a,b,c=0,0,0
ck=[0]*10
ans=0
while a<=b and b<n:
    while b<n:
        if ck[l[b]]==0 and c==2: break
        ck[l[b]]+=1
        if ck[l[b]]==1: c+=1
        b+=1
        ans=max(ans,b-a)
    while a<b and c==2:
        ck[l[a]]-=1
        if ck[l[a]]==0: c-=1
        a+=1
print(ans)