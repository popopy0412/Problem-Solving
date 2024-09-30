a,b=input().split()
n,m=len(a),len(b)
x=100
for i in range(m-n+1):
    c=0
    for j in range(n):
        if a[j] != b[i+j]: c+=1
    x=min(x,c)
print(x)