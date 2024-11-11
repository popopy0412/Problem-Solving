n,k,*l=map(int,open(0).read().split())
d=[0]+[1e9]*k
for i in l:
    for j in range(i,k+1): d[j]=min(d[j],d[j-i]+1)
print(d[k] if d[k]!=1e9 else -1)