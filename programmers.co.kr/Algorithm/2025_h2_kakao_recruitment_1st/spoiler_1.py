def solution(message, spoiler_ranges):
    n=len(message)
    d={}
    ck=['']*n
    idx=[0]*n
    check=[0]*n
    s=set()
    m=message.split()
    cnt={}
    for w in m:
        if w not in cnt: cnt[w]=0
        cnt[w]+=1

    a=0 if message[0]!=' ' else -1
    for i in range(n):
        if message[i]==' ':
            a+=1
        else:
            ck[i]=m[a]
            idx[i]=a
    for l,r in spoiler_ranges:
        for i in range(l,r+1):
            if ck[i]!='' and check[idx[i]]==0:
                if ck[i] not in d: d[ck[i]]=0
                d[ck[i]]+=1
                check[idx[i]]=1

    ans=0
    for i in d:
        if cnt[i]==d[i] and i not in s:
            ans+=1
            s.add(i)
    return ans