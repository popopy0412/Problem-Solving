n=int(input())
l=[*map(int,input().split())]
r=[*map(int,input().split())]
l.sort();r.sort()
print(sum([a*b for a,b in zip(l,r[::-1])]))