from bisect import *
import sys
ip=sys.stdin.readline
n=int(ip())
l,s,k,p=[],[],[],[0]*n
for i in range(n): l.append([*map(int,ip().split())])
l.sort()
for i in range(n):
    t=l[i][1]
    if (not s) or l[s[-1]][1] < t:
        p[i]=(s[-1] if s else -1)
        s.append(i)
    else:
        x=bisect_left(s,t,key=lambda x:l[x][1])
        s[x]=i
        p[i]=(s[x-1] if x else -1)
now=s[-1]
while now!=-1:
    k.append(l[now][0])
    now=p[now]
k.sort()
b=0
print(n-len(k))
for i in range(n):
    t=l[i][0]
    if b<len(k) and t==k[b]: b+=1
    else: print(t)