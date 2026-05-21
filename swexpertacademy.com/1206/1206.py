for t in range(10):
    n,l=int(input()),[*map(int,input().split())]
    k=[0]*n
    ans=0
    for i in range(2,n-2): ans+=min(max(0,l[i]-max(l[i-2:i])),max(0,l[i]-max(l[i+1:i+3])))
    print(f'#{t+1} {ans}')