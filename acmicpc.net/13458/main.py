import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
b,c=map(int,input().split())
ans=0
for m in l:
    ans+=1
    if m>b: ans+=(m-b)//c+(1 if (m-b)%c else 0)
print(ans)
