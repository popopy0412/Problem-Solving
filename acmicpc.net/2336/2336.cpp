#include <bits/stdc++.h>
using namespace std;
const int MAX=500010;
const int INF=1e9;
int n, s, tree[MAX*3];
struct stu {
    int a, b, c;
}k[MAX];

bool cmp(stu x, stu y) {
    return x.a < y.a;
}

void update(int i, int v) {
    i+=s-1;
    tree[i]=v;
    while (i/=2) {
        tree[i]=min(tree[i*2],tree[i*2+1]);
    }
}

int query(int l, int r, int s, int e, int i) {
    if (r<s || e<l) return INF;
    else if (s<=l && r<=e) return tree[i];
    int m=l+r>>1;
    return min(query(l,m,s,e,i*2),query(m+1,r,s,e,i*2+1));
}

int main() {
    ios::sync_with_stdio(0), cin.tie(0);
    fill(tree,tree+MAX*3,INF);
    int i, t, cnt=0;
    cin >> n;
    s = 1 << (32 -__builtin_clz(n));
    for (i=1;i<=n;i++){
        cin >> t;
        k[t].a = i;
    }
    for (i=1;i<=n;i++){
        cin >> t;
        k[t].b = i;
    }
    for (i=1;i<=n;i++){
        cin >> t;
        k[t].c = i;
    }
    sort(k+1,k+n+1,cmp);
    for (i=1;i<=n;i++) {
        if (query(1,s,1,k[i].b,1)>k[i].c) cnt++;
        update(k[i].b, k[i].c);
    }
    cout << cnt;
    return 0;
}