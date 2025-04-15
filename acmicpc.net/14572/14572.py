import sys
ip=sys.stdin.readline
n,k,d=map(int,ip().split())
l=[]
v=[[] for _ in range(n)]
S=set(range(1,31))
ck=[0]*31
for i in range(n):
    M,D=map(int,ip().split())
    v[i]=[*map(int,ip().split())]
    l.append([D,M,i])

l.sort(key=lambda x:[x[0],-x[1]])

s,e=0,0
cnt,all=0,0
ans=0
while s<=e and e<n:
    ld,lm,li=l[s]
    rd,rm,ri=l[e]
    if rd-ld<=d:
        e+=1
        for i in v[ri]:
            ck[i]+=1
            if ck[i]==1: cnt+=1
        S &= set(v[ri])
        all=len(S)
        ans=max(ans,(cnt-all)*(e-s))
    else:
        while s<e and rd-ld>d:
            s+=1
            for i in v[li]:
                ck[i]-=1
                if ck[i]==0:
                    cnt-=1
            S.clear()
            for i in range(1,31):
                if ck[i]==(e-s): S.add(i)
            all=len(S)
            ans=max(ans,(cnt-all)*(e-s))
            if s<n: ld,lm,li=l[s]
while s<e:
    s+=1
    for i in v[li]:
        ck[i]-=1
        if ck[i]==0:
            cnt-=1
    S.clear()
    for i in range(1,31):
        if ck[i]==(e-s): S.add(i)
    all=len(S)
    ans=max(ans,(cnt-all)*(e-s))
    if s<n: ld,lm,li=l[s]
print(ans)