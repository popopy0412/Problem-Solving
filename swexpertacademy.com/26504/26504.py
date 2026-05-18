t=int(input())
while t:
    t-=1
    n=int(input())
    l=[*map(int,input().split())]
    l.sort()
    print(sum(l[:n-1]),sum(l[i*-~i//2] for i in range(n-1)))