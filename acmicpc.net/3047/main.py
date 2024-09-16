l=sorted(map(int,input().split()))
print(*[l[ord(c)-65]for c in input()])