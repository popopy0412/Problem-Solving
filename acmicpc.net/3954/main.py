import sys
input=sys.stdin.readline
MOD=2**8

for _ in range(int(input())):
    m,c,n=map(int,input().split())
    l=[0]*m
    p=0
    st=[]
    par=[-1]*c
    ck=[[] for _ in range(c)]
    cnt=0

    t=input()
    inp=input()
    for i in range(len(t)):
        ch=t[i]
        if ch=='[': st.append(i)
        elif ch==']':
            r=st.pop()
            par[r]=i
            par[i]=r

    i=0
    ter=0
    loop=0
    left=10000
    while i<len(t):
        loop+=1
        ch=t[i]
        if ch=='+': l[p]=(l[p]+1)%MOD
        elif ch=='-': l[p]=(l[p]-1)%MOD
        elif ch=='>': p=(p+1)%m
        elif ch=='<': p=(p-1)%m
        elif ch=='[':
            if l[p]==0: i=par[i]
        elif ch==']':
            if l[p]!=0: i=par[i]

        elif ch==',':
            if cnt<n:
                l[p]=ord(inp[cnt])
                cnt+=1
            else: l[p]=255

        if loop>50000000:
            left = min(i,left)
        if loop>100000000:
            ter=1
            break

        i+=1
        
    if ter: print(f'Loops {left} {par[left]}')
    else: print('Terminates')