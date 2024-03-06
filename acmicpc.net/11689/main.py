# Euler Phi Function
n=m=int(input()); c=1;s=2
f=[];g=[]
while m>1:
    ck=0
    for i in range(s,int(m**(1/2)+1)):
        if m==1: break
        if m%i==0:
            s=i+1;ck=1
            f.append(i); g.append(0)
            while m%i==0:
                m//=i
                g[-1]+=1
    if ck==0:
        f.append(m); g.append(1)
        break
for i in range(len(f)): c*=(f[i]**g[i]-f[i]**(g[i]-1))
print(c)