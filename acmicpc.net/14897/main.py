import sys
input=sys.stdin.readline

def solve():
    n=int(input())
    rt=int(n**0.5)
    num=list(map(int,input().split()))
    m=int(input())
    d,ans,q,c=[0]*10**6,[0]*m,[],{}
    for i in sorted(set(num)): c[i]=len(c)
    for i in range(n): num[i]=c[num[i]]
    for i in range(m):
        a,b=map(int,input().split())
        q.append([a-1,b-1,i])
    q.sort(key=lambda x:(x[1]//rt,x[0]))

    l,r,temp=0,-1,0
    for s,e,i in q:
        while s < l:
            l-=1
            if d[num[l]]==0: temp+=1
            d[num[l]]+=1
        while l < s:
            d[num[l]]-=1
            if d[num[l]]==0: temp-=1
            l+=1
        while r < e:
            r+=1
            if d[num[r]]==0: temp+=1
            d[num[r]]+=1
        while e < r:
            d[num[r]]-=1
            if d[num[r]]==0: temp-=1
            r-=1
        ans[i]=temp
    for t in ans: sys.stdout.write(f'{t}\n')
solve()