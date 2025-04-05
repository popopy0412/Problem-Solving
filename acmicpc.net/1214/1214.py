# 정수론 활용 브루트 포스
c,a,b=map(int,input().split())
if a>b: a,b=b,a
ans=1e10
for i in range(min(c//b,a)+1): ans=min(ans,(a-(c-b*i)%a)%a)
ans=min(ans,b-c%b)
print(ans+c)

# 그냥 브루트 포스
c,a,b=map(int,input().split())
d=a+b
if c%a==0 or c%b==0 or c%d==0: print(c);exit(0)
ans=10**10
for i in range(c//d+2):
    if c>d*i:
        t=c-(d*i)
        x=a*(t//a+(1 if t%a else 0))+(d*i)
        y=b*(t//b+(1 if t%b else 0))+(d*i)
        ans=min(ans,x,y)
    if d*i>c: ans=min(ans,d*i)
print(ans)