n=int(input())
l=[input() for _ in range(n)]
now=0
chan=['KBS1','KBS2']
c=0
while l[0]!='KBS1' or l[1]!='KBS2':
    if l[now]!=chan[c]:
        now+=1
        print(1,end='')
    else:
        if now==c: c+=1;continue
        l[now],l[now-1]=l[now-1],l[now]
        now-=1
        print(4,end='')