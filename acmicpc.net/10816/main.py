import sys
p=sys.stdin.readline
l=lambda:[*map(int,p().split())]
n,x,m,y,d=p(),l(),p(),l(),{}
for i in x:d[i]=(d[i]+1if i in d else 1)
for i in y:print(d[i]if i in d else 0,end=' ')