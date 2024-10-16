n=10000
l=[0]*-~n
l[0]=1
for i in range(2,4):
    for j in range(i,n+1): l[j]+=l[j-i]
for i in range(1,n+1): l[i]+=l[i-1]
for _ in range(int(input())): print(l[int(input())])