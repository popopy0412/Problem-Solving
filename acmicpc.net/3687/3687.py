# 최적화 필요
s=[[],[],[1],[7],[4],[2,5],[0,9],[8]]
d=[[0,0] for _ in range(101)]
for i in range(2,101):
    for j in range(2,min(i,7)+1):
        if i-j==0 or d[i-j][0]:
            m,M=d[i-j]
            sm,sM=s[j][0],s[j][-1]

            if j!=6:
                k=0
                while k<len(str(m)):
                    if m//(10**k)%10<=sm: break
                    k+=1
                d1=m%(10**k)+m//(10**k)*(10**-~k)+sm*(10**k)

                k=len(str(M))-1
                while k>=0:
                    if M//(10**k)%10<=sM: break
                    k-=1
                d2=M%(10**-~k)+M//(10**-~k)*(10**(k+2))+sM*(10**-~k)
            else:
                t=len(str(m))
                d1=m%(10**~-t)+m//(10**~-t)*(10**t)
                d2=M*10

            d[i]=[min(d[i][0],d1) if d[i][0] else d1,max(d[i][1],d2)]
    if i==6: d[6][0]=6
for I,i in enumerate(d): print(I,i)
n=int(input())
while n:
    n-=1
    i=int(input())
    print(d[i][0],d[i][1]//10)
