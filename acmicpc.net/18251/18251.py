n,*k=map(int,open(0).read().split())
a=n.bit_length()
d=[]
dp=[0]*a

def dfs(l,r,i):
    m=l+r>>1
    if l!=r: dfs(l,m-1,i*2)
    d.append([k[i-1],(r-l+1).bit_length()-1])
    if l!=r: dfs(m+1,r,i*2+1)
dfs(0,n-1,1)

ans=-1e20
for lo in range(a):
    for hi in range(lo+1,a+1):
        su=0
        for i in range(n):
            v,h=d[i]
            if h<lo or hi<=h: continue
            if su<0: su=0
            su+=v
            ans=max(ans,su)
print(ans) 