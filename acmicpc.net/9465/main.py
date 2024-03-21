import sys
input=sys.stdin.readline
def solve():
    n=int(input())
    l,d=[],[[0 for _ in range(n+1)] for _ in range(2)]
    for _ in range(2):l.append([0]+list(map(int,input().split())))
    d[0][1],d[1][1]=l[0][1],l[1][1]
    for i in range(2,n+1):d[0][i],d[1][i]=max(d[1][i-1],d[0][i-2],d[1][i-2])+l[0][i],max(d[0][i-1],d[1][i-2],d[0][i-2])+l[1][i]
    print(max(d[0][n],d[1][n]))
for _ in range(int(input())):solve()