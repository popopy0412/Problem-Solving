n,k=map(int,input().split())
ck=[0]*-~n
for i in range(2,n+1):
    if ck[i]: continue
    for j in range(i,n+1,i):
        if ck[j]: continue
        ck[j]=1
        if (k:=k-1)==0:
            print(j)
            exit(0)