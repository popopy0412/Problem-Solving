#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MAX = 1e18;

struct Node {
    int first, second;
    ll sum;
    int count;
    Node() : first(-1), second(-1), sum(0), count(0) {}
    Node(int f, int s, ll su, int c) : first(f), second(s), sum(su), count(c) {}
};

class SegmentTree {
private:
    int n, size;
    vector<Node> tree;
    vector<ll> lazy;

    Node merge(Node a, Node b) {
        if (a.first == b.first) {
            return Node(a.first, max(a.second, b.second), a.sum + b.sum, a.count + b.count);
        } else if (a.first > b.first) {
            return Node(a.first, max(a.second, b.first), a.sum + b.sum, a.count);
        } else {
            return Node(b.first, max(a.first, b.second), a.sum + b.sum, b.count);
        }
    }

    void apply(int i) {
        if (lazy[i] != MAX) {
            for (int c = i*2; c <= i*2+1; c++) {
                if (c < n+size) save(c, lazy[i]);
            }
            lazy[i] = MAX;
        }
    }

    void save(int i, ll v) {
        if (tree[i].second < v && v < tree[i].first) {
            tree[i].sum -= (tree[i].first - v) * tree[i].count;
            tree[i].first = v;
            lazy[i] = min(lazy[i], v);
        }
    }

    void update(int l, int r, int s, int e, int i, ll v) {
        if (r < s || e < l || tree[i].first < v) return;
        if (s <= l && r <= e && tree[i].second < v) {
            save(i, v);
            return;
        }
        apply(i);
        int m = (l + r) / 2;
        update(l, m, s, e, 2*i, v);
        update(m+1, r, s, e, 2*i+1, v);
        tree[i] = merge(tree[2*i], tree[2*i+1]);
    }

    int max_query(int l, int r, int s, int e, int i) {
		if (r < s || e < l) return 0;
        if (s <= l && r <= e) return tree[i].first;
        apply(i);
        int m = (l + r) / 2;
        return max(max_query(l, m, s, e, 2*i), max_query(m+1, r, s, e, 2*i+1));
    }

    ll sum_query(int l, int r, int s, int e, int i) {
        if (r < s || e < l) return 0;
        if (s <= l && r <= e) return tree[i].sum;
        apply(i);
        int m = (l + r) / 2;
        return sum_query(l, m, s, e, 2*i) + sum_query(m+1, r, s, e, 2*i+1);
    }

public:
    SegmentTree(int _n, vector<int>& arr) : n(_n) {
        int bit_len = 32 - __builtin_clz(n);
        size = 1 << bit_len;
        if (size % n == 0) size >>= 1;

        tree.resize(2*size);
        lazy.assign(2*size, MAX);

        for (int i=0; i<n; i++)
            tree[size+i] = Node(arr[i], -1, arr[i], 1);
        for (int i=size-1; i>0; i--)
            tree[i] = merge(tree[2*i], tree[2*i+1]);
    }

    void range_update(int l, int r, ll v) {
        update(1, size, l, r, 1, v);
    }

    int get_max(int l, int r) {
        return max_query(1, size, l, r, 1);
    }

    ll get_sum(int l, int r) {
        return sum_query(1, size, l, r, 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n; cin >> n;
    vector<int> k(n);
    for (int i=0; i<n; i++) cin >> k[i];
    
    SegmentTree st(n, k);
    
    int q; cin >> q;
    while (q--) {
        int cmd; cin >> cmd;
        if (cmd == 1) {
            int a, b, v;
            cin >> a >> b >> v;
            st.range_update(a, b, v);
        } else if (cmd == 2) {
            int a, b;
            cin >> a >> b;
            cout << st.get_max(a, b) << '\n';
        } else {
            int a, b;
            cin >> a >> b;
            cout << st.get_sum(a, b) << '\n';
        }
    }
}
