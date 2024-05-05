l=[500,100,50,10,5,1]
n,ans,i=1000-int(input()),0,0
while n and i<6:
	ans+=n//l[i]
	n%=l[i]
	i+=1
print(ans)