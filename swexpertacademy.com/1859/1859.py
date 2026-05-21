ip=input
for i in range(int(ip())):
    ip()
    l=[*map(int,ip().split())]
    a,m=0,0
    while l:
        x=l.pop()
        m=max(m,x)
        a+=m-x
    print(f'#{i+1} {a}')