l=[[0]*8 for _ in range(26)]
for i in range(int(input())):
    s=input()
    n=len(s)
    for j in range(n): l[ord(s[j])-65][n-j-1]+=1
l=[*sorted(filter(lambda x:sum(x),l),key=lambda x:sum([10**i*x[i] for i in range(8)]))][::-1]
k,ans=9,0
for x in l:
    for j in range(8): ans+=10**j*x[j]*k
    k-=1
print(ans)