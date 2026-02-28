n,k=map(int,input().split())
l=[[*map(int,input().split())] for _ in range(n)]
d=[[1e9]*2**n for _ in range(n)]

def dfs(now, bit):
    if bit==2**n-1: return 0
    if d[now][bit] != 1e9: return d[now][bit]
    temp=1e9
    for i in range(n):
        if i==now or 1<<i&bit: continue
        temp = min(temp, dfs(i, 1<<i|bit)+l[now][i])
    d[now][bit]=temp
    return temp

for t in range(n):
    for i in range(n):
        for j in range(n):
            if l[i][t]+l[t][j]<l[i][j]: l[i][j]=l[i][t]+l[t][j]

print(dfs(k,1<<k))