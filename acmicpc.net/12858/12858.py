import math
import sys
ip = sys.stdin.readline

class SegTreeNode:
    def __init__(self, first=0, last=0, g=0):
        self.first = first
        self.last = last
        self.g = g

class LazySegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [SegTreeNode() for _ in range(2 * self.size)]
        self.lazy = [0] * (2 * self.size)
        self._build(arr)
    
    def _build(self, arr):
        for i in range(self.n):
            self.tree[self.size + i] = SegTreeNode(arr[i], arr[i], 0)
        for i in range(self.n, self.size):
            self.tree[self.size + i] = SegTreeNode(0, 0, 0)
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self._merge(self.tree[2 * i], self.tree[2 * i + 1])
    
    def _merge(self, left_node, right_node):
        if left_node.first == 0 and left_node.last == 0:
            return right_node
        if right_node.first == 0 and right_node.last == 0:
            return left_node
        new_first = left_node.first
        new_last = right_node.last
        new_g = math.gcd(left_node.g, math.gcd(right_node.g, right_node.first - left_node.last))
        return SegTreeNode(new_first, new_last, new_g)
    
    def _apply(self, idx, val, seg_length):
        self.tree[idx].first += val
        self.tree[idx].last += val
        self.lazy[idx] += val
    
    def _push(self, idx, l, r):
        if self.lazy[idx] != 0 and idx < self.size:
            mid = (l + r) // 2
            self._apply(2 * idx, self.lazy[idx], mid - l + 1)
            self._apply(2 * idx + 1, self.lazy[idx], r - mid)
            self.lazy[idx] = 0
    
    def _update(self, idx, l, r, ql, qr, val):
        if qr < l or ql > r:
            return
        if ql <= l and r <= qr:
            self._apply(idx, val, r - l + 1)
            return
        self._push(idx, l, r)
        mid = (l + r) // 2
        self._update(2 * idx, l, mid, ql, qr, val)
        self._update(2 * idx + 1, mid + 1, r, ql, qr, val)
        self.tree[idx] = self._merge(self.tree[2 * idx], self.tree[2 * idx + 1])
    
    def update_range(self, ql, qr, val):
        self._update(1, 0, self.size - 1, ql, qr, val)
    
    def _query(self, idx, l, r, ql, qr):
        if qr < l or ql > r:
            return None
        if ql <= l and r <= qr:
            return self.tree[idx]
        self._push(idx, l, r)
        mid = (l + r) // 2
        left_res = self._query(2 * idx, l, mid, ql, qr)
        right_res = self._query(2 * idx + 1, mid + 1, r, ql, qr)
        if left_res is None:
            return right_res
        if right_res is None:
            return left_res
        return self._merge(left_res, right_res)
    
    def query_range(self, ql, qr):
        node = self._query(1, 0, self.size - 1, ql, qr)
        return math.gcd(abs(node.first), abs(node.g))

n, k = int(ip()), [*map(int, ip().split())]
seg = LazySegTree([0] + k)
for _ in range(int(ip())):
    q, a, b = map(int, ip().split())
    if q: seg.update_range(a, b, q)
    else: print(seg.query_range(a, b))
