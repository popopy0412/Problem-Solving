for _ in range(int(input())):
    d={}
    input()
    for i in map(int,input().split()): d[i]=d[i]+1 if i in d else 1
    input()
    for i in map(int,input().split()): print(1 if i in d else 0)