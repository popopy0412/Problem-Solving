# 1번 방법 - Two Pointer + Sliding Window
for _ in range(int(input())):
    s,n=input(),int(input())
    d=[[] for _ in range(26)]
    for i, c in enumerate(s): d[ord(c)-97].append(i)
    ck=[0]*26
    a,b,l,r=10**6,0,0,0
    while r<len(s):
        now=ord(s[r])-97
        ck[now]+=1
        r+=1
        if ck[now]==n:
            while l<=r:
                now=ord(s[l])-97
                ck[now]-=1
                l+=1
                if ck[now]==n-1: break
            a=min(a,r-l+1)
    for t in d:
        for j in range(len(t)-n+1): b=max(b,t[j+n-1]-t[j]+1)
    if a!=10**6 and b!=0: print(a, b)
    else: print(-1)
#==================================================================
# 2번 방법 - Sliding Window
for _ in range(int(input())):
    s,n=input(),int(input())
    d=[[] for _ in range(26)]
    for i, c in enumerate(s): d[ord(c)-97].append(i)
    ck=[0]*26
    a,b=10**6,0
    for t in d:
        for j in range(len(t)-n+1):
            a,b=min(a,t[j+n-1]-t[j]+1),max(b,t[j+n-1]-t[j]+1)
    if a!=10**6 and b!=0: print(a, b)
    else: print(-1)