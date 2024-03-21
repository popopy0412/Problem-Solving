n=int(input())
d=[4]*-~n
l=[i*i for i in range(int(n**0.5)+1) if i*i<=n]
for i in l:
    d[i]=1
    for j in range(i+1,n+1):
        if d[j-i] and d[j]>d[j-i]+1:d[j]=d[j-i]+1
print(d[n])