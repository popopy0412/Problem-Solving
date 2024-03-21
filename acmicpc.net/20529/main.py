d={'I':0,'E':1,'N':0,'S':1,'F':0,'T':1,'P':0,'J':1}
def solve():
    n,k=int(input()),8
    s=input().split()
    if n > 32:
        print(0)
        return
    l=[]
    for c in s:
        a,b=1,0
        for i in c:
           if d[i]: b+=a
           a*=2
        l.append(b)
    l.sort()
    for i in range(n-2):
        for j in range(i+1,n-1):
            for t in range(j+1,n):
                a,b,c,m=l[i],l[j],l[t],0
                for _ in range(4):
                    if not a%2==b%2==c%2:m+=2
                    a//=2;b//=2;c//=2
                k=min(k,m)
    print(k)
for _ in range(int(input())):solve()