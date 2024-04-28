def bt(s,now):
    global l
    if now==n:
        print(s)
        return 1
    ret=0
    for i in range(65,65+a):
        c=chr(i)
        temp=s+c
        next=now+1
        ck=0
        t=[0]*(n//k+1)
        for r in range(1,n//k+1):
            if next-r<0: break
            if temp[next-r:]==temp[next-2*r:next-r]:
                if l[now-r][r]+1<k: t[r]=l[now-r][r]+1
                else:
                    ck=1
                    break
            else: t[r]=1
        if ck: continue
        l[now]=t.copy()
        if ret:=bt(temp,next): return 1
    return ret
            
k,n,a=map(int,input().split())
l=[[1 for _ in range(n//k+1)] for _ in range(n+1)]
if bt('A',1)==0: print(-1)