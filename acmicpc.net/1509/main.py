s=input()
n=len(s)
ck,k=[1e9]*n,range(n)
def dp(i,c):
    for j in k:
        x,y=i-j,i+j+c
        if x<0 or y>=n or s[x]!=s[y]: break
        ck[y]=min(ck[y],ck[x-1]+1 if x else 1)
for i in k:dp(i,0);dp(i,1)
print(ck[-1])