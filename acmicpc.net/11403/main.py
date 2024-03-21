from collections import *
n=int(input())
l=[]
for i in range(n): l.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        for k in range(n):
            if l[k][i] != 0 and l[i][j] != 0: l[k][j] = 1
for t in l: print(*t)
