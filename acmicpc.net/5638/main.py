import sys
input=sys.stdin.readline
sys.setrecursionlimit(2*10**5)
n=10**6
r,tree=int(input()),[[0,0] for _ in range(n)]
def trav(now):
    if tree[now][0]: trav(tree[now][0])
    if tree[now][1]: trav(tree[now][1])
    print(now)
while True:
    try: v=int(input())
    except: break
    now=r
    while True:
        if v < now:
            if tree[now][0]: now=tree[now][0]
            else:
                tree[now][0] = v
                break
        else:
            if tree[now][1]: now=tree[now][1]
            else:
                tree[now][1] = v
                break
trav(r)
