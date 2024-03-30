n=int(input())
l=[]
for _ in range(n):
	l.append(input())

for i in range(n):
	for j in range(n-i-1):
		if len(l[j]) > len(l[j+1]):
			l[j],l[j+1]=l[j+1],l[j]
			continue
		elif len(l[j]) == len(l[j+1]):
			a,b=0,0
			for c in l[j]:
				if c.isdigit(): a+=int(c)
			for c in l[j+1]:
				if c.isdigit(): b+=int(c)
			if a > b:
				l[j],l[j+1]=l[j+1],l[j]
				continue
			elif a == b:
				if l[j] > l[j+1]: l[j],l[j+1]=l[j+1],l[j]
print(*l)