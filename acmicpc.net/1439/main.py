s=input()
print(len([1]+[i for i in range(len(s)-1) if s[i]!=s[i+1]])//2)