n=0
for i in range(8):
	s=input()
	for j in range(8):
		if (i+j+1)%2 and s[j]=='F': n+=1
print(n)