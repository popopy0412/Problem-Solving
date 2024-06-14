x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())
ccw=lambda ax,ay,bx,by,cx,cy:(ax-bx)*(ay-cy)-(ax-cx)*(ay-by)
mima=lambda x1,x2,x3,x4:min(max(x1,x2),max(x3,x4))
mami=lambda x1,x2,x3,x4:max(min(x1,x2),min(x3,x4))
lap=lambda x1,x2,x3,x4:mima(x1,x2,x3,x4)<mami(x1,x2,x3,x4)
c1,c2,c3,c4=ccw(x1,y1,x2,y2,x3,y3),ccw(x1,y1,x2,y2,x4,y4),ccw(x3,y3,x4,y4,x1,y1),ccw(x3,y3,x4,y4,x2,y2)
a,b,c=c1*c2,c3*c4,lap(x1,x2,x3,x4)|lap(y1,y2,y3,y4)
if (a>0 or b>0) or a==0 and b==0 and c: print(0)
else:
	print(1)
	xia,xai,yia,yai=mima(x1,x2,x3,x4),mami(x1,x2,x3,x4),mima(y1,y2,y3,y4),mami(y1,y2,y3,y4)
	t=(y1-y2)/(x1-x2) if x1!=x2 else 1e9
	k=(y3-y4)/(x3-x4) if x3!=x4 else 1e9
	if a==0 or b==0:
		if t!=k:
			if c1==0: print(x3,y3)
			elif c2==0: print(x4,y4)
			elif c3==0: print(x1,y1)
			elif c4==0: print(x2,y2)
		elif xia==xai and yia==yai: print(xai,yai)
	else:
		if t==1e9: x=x1
		elif k==1e9: x=x3
		else: x=(t*x1-k*x3-y1+y3)/(t-k)
		if t==0: y=y1
		elif k==0: y=y3
		else:
			if t!=1e9: y=t*(x-x1)+y1
			else: y=k*(x-x3)+y3
		print(x, y)