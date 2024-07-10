n=len(s:=input())
t='z'*n
for i in range(n-2):
    for j in range(i+1,n-1): t=min(t,s[:i+1][::-1]+s[i+1:j+1][::-1]+s[j+1:][::-1])
print(t)
