import sys
input=sys.stdin.readline
inl=lambda: map(int,input().split())

def make(tree, num, l, r, idx):
    if l==r:
        tree[idx]=num[l]
        return num[l]
    m=(l+r)//2
    tree[idx]=make(tree, num, l, m, idx*2)+make(tree, num, m+1, r, idx*2+1)
    return tree[idx]
def check(tree, lazy, l, r, v, idx):
    tree[idx]+=v*(r-l+1)
    if l != r:
        lazy[idx*2]+=v
        lazy[idx*2+1]+=v
def query(tree, lazy, l, r, s, e, idx):
    if lazy[idx]:
        check(tree, lazy, l, r, lazy[idx], idx)
        lazy[idx]=0
    if r < s or e < l: return 0
    if s <= l and r <= e: return tree[idx]
    m=(l+r)//2
    return query(tree, lazy, l, m, s, e, idx*2)+query(tree, lazy, m+1, r, s, e, idx*2+1)
def update(tree, lazy, l, r, s, e, v, idx):
    if lazy[idx]:
        check(tree, lazy, l, r, lazy[idx], idx)
        lazy[idx]=0
    if r < s or e < l: return
    if s <= l and r <= e:
        check(tree, lazy, l, r, v, idx)
        return
    if l <= s <= r <= e: tree[idx]+=v*(r-s+1)
    elif s <= l <= e <= r: tree[idx]+=v*(e-l+1)
    elif l <= s <= e <= r: tree[idx]+=v*(e-s+1)
    m=(l+r)//2
    update(tree, lazy, l, m, s, e, v, idx*2)
    update(tree, lazy, m+1, r, s, e, v, idx*2+1)
    
def solve():
    n,m,k=inl()
    num=[0]+[int(input()) for _ in range(n)]
    q=[[*inl()] for _ in range(m+k)]
    tree=[0]*2500001
    lazy=[0]*2500001
    make(tree, num, 1, n, 1)
    for t in q:
        if t[0] == 1: update(tree, lazy, 1, n, t[1], t[2], t[3], 1)
        else: print(query(tree, lazy, 1, n, t[1], t[2], 1))
solve()