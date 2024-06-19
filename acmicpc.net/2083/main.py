while True:
	a,b,c=input().split()
	if a=='#':break
	print(a,'Senior' if int(b)>17 or int(c)>79 else 'Junior')