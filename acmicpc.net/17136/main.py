n,num,ans=10,0,1e9
l=[]
p=[5]*5

def check(x,y,k):
    for i in range(x,x+k+1):
        for j in range(y,y+k+1):
            if l[i][j]==0: return 1
    return 0
def change(x,y,k,v):
    for i in range(x,x+k+1):
        for j in range(y,y+k+1):
            l[i][j]=v
def rec(cnt,x,y):
    global n,ans
    if x==n:
        ans=min(ans,cnt)
        return
    if l[x][y]:
        for i in range(4,-1,-1):
            if x+i < n and y+i < n and p[i]:
                if check(x,y,i): continue
                change(x,y,i,0)
                p[i]-=1
                rec(cnt+1,x+(y+1)//10,(y+1)%10)
                p[i]+=1
                change(x,y,i,1)
    else: rec(cnt,x+(y+1)//10,(y+1)%10)

for _ in range(n): l.append([*map(int,input().split())])

rec(0,0,0)
print(ans if ans!=1e9 else -1)
