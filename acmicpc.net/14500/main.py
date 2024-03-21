# 시간 줄일 방법을 생각해보자
n,m=map(int,input().split())
ans,l,k=0,[],[[[1,1],[1,1]]]
t=[[[1,1,1],[0,1,0]],[[1,1,1,1]],[[1,1,1],[1,0,0]],[[1,1,1],[0,0,1]],[[1,1,0],[0,1,1]],[[0,1,1],[1,1,0]]]
for _ in range(n):l.append(list(map(int,input().split())))

def getSum(x,y):
    global n,m,l,k
    a=0
    for r in k:
        s=0
        h,w=len(r),len(r[0])
        if x > n-h or y > m-w: continue
        for i in range(h):
            for j in range(w):
                s+=l[x+i][y+j]*r[i][j]
        a=max(a,s)
    return a

for r in t:
    q=r.copy()
    for _ in range(2 if len(r)==1 else 4):
        q=list(zip(*q))[::-1]
        k.append(q)
    
for i in range(n):
    for j in range(m):
        ans=max(ans,getSum(i,j))
print(ans)