#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MAX=100010;
int n,p,rt,a[MAX],b[MAX],atree[MAX],btree[MAX];
ll sum,ans[MAX];

struct temp{
    int x, y, k, i;
}q[MAX];

bool cmp(temp a, temp b) {
    if (a.x/rt != b.x/rt) return a.x/rt < b.x/rt;
    else return a.y < b.y;
}

void update(int* tree, int i, int v) {
    while (i<=MAX) {
        tree[i]+=v;
        i+=i&-i;
    }
}

ll query(int* tree, int i) {
    ll z=0;
    while (i) {
        z+=tree[i];
        i-=i&-i;
    }
    return z;
}

void get_sum(int k) {
    sum=0;
    int krt=sqrt(k);
    ll aq=query(atree, krt);
    for (int i=1;i<=krt;i++) {
        ll ax=query(atree, i)-query(atree, i-1);
        ll bx=query(btree, k/i);
        sum+=ax*bx;

        ll ay=query(atree, k/i)-aq;
        ll by=query(btree, i)-query(btree,i-1);
        sum+=ay*by;
    }
}

void mod(int i, int v) {
    int A=a[i], B=b[i];
    update(atree, A, v); update(btree, B, v);
}

int main() {
    ios::sync_with_stdio(0), cin.tie(0);
    int i;
    cin >> n;
    rt=(int)sqrt(n)+1;
    for (i=0;i<n;i++) cin >> a[i];
    for (i=0;i<n;i++) cin >> b[i];
    cin >> p; 
    for (i=0;i<p;i++) {
        cin >> q[i].x >> q[i].y >> q[i].k;
        q[i].i = i;
    }
    sort(q,q+p,cmp);

    int l=0, r=-1;
    for (i=0;i<p;i++){
        auto [s,e,k,idx]=q[i];
        s--; e--;
        while (r<e) mod(++r,1);
        while (s<l) mod(--l,1);
        while (e<r) mod(r--,-1);
        while (l<s) mod(l++,-1);
        get_sum(k);
        ans[idx]=sum;
    }
    for (i=0;i<p;i++) cout << ans[i] << "\n";
    return 0;
}