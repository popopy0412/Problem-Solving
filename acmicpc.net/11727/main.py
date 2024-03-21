d=[1,1]
for i in range(int(input())-1): d.append(d[-1]+d[-2]*2)
print(d[-1]%10007)