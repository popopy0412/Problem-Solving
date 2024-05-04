import sys
ip=sys.stdin.readline
s=lambda n:set([int(ip())for _ in range(n)])
while 1:
	a,b=map(int,ip().split())
	if a==b==0:break
	x,y=s(a),s(b)
	print(len(x&y))