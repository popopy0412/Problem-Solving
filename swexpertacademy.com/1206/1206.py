for t in range(10):
    n,l=int(input()),[*map(int,input().split())]
    print(f'#{t+1} {sum([max(0,l[i]-max(*l[i-2:i],*l[i+1:i+3])) for i in range(2,n-2)])}')