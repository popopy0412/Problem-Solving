from bisect import *
n,l,d,ck,a,b,tmp,ans=0,[],[],[0]*300,[],[],0,[]
def hapa(l,t,cnt):
    global d,n,a
    if cnt==n:
        a.append(t)
        return
    for i in d[l[cnt]]:
        hapa(l,t+i,cnt+1)
def hapb(l,t,cnt):
    global d,n,b
    if cnt==n:
        b.append(t)
        return
    for i in d[l[cnt]]:
        hapb(l,t+i,cnt+1)
def solve(l):
    global d,n,a,b
    t=[]
    for i in range(n*2):
        if i not in l: t.append(i)
    a,b=[],[]
    hapa(l,0,0),hapb(t,0,0)
    a.sort()
    b.sort()
    k=0
    for i in a:
        x=max(0,bisect_right(b,i-1)-1)
        k+=x
    return k
    
def rec(now, cnt):
    global tmp,ans,l
    if cnt==n:
        t=solve(l)
        if tmp < t:
            tmp = t
            ans = l.copy()
        return
    for i in range(now,n*2):
        l.append(i)
        rec(i+1, cnt+1)
        l.pop()
def solution(dice):
    global d,n
    n=len(dice)//2
    d=dice
    rec(0,0)
    for i in range(n): ans[i]+=1
    return ans