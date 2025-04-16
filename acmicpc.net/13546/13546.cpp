#include <bits/stdc++.h>
using namespace std;
const int MAX=110000;
list<int> v[MAX];
int n,m,p,rt,k[MAX],cnt[MAX],buc[400],ans[MAX];

struct temp{
    int x, y, i;
}q[MAX];

bool cmp(temp a, temp b) {
    if (a.x/rt != b.x/rt) return a.x/rt < b.x/rt;
    else return a.y < b.y;
}

void add(int x, int d) {
    int t=k[x];
    if (v[t].size()) {
        int diff = v[t].back() - v[t].front();
        cnt[diff]--; buc[diff/rt]--;
    }
    if (d) v[t].push_front(x);
    else v[t].push_back(x);
    int diff = v[t].back() - v[t].front();
    cnt[diff]++; buc[diff/rt]++;
}

void del(int x, int d) {
    int t=k[x];
    int diff = v[t].back() - v[t].front();
    cnt[diff]--; buc[diff/rt]--;
    if (d) v[t].pop_front();
    else v[t].pop_back();
    if (v[t].size()) {
        int diff = v[t].back() - v[t].front();
        cnt[diff]++; buc[diff/rt]++;
    }
}

int query() {
    for (int i=n/rt+10;i>=0;i--) {
        if (buc[i]==0) continue;
        for (int j=rt-1;j>=0;j--) {
            if (cnt[i*rt+j]) return i*rt+j;
        }
    }
    return 0;
}

int main() {
    ios::sync_with_stdio(0), cin.tie(0);
    int i,j;
    cin >> n >> m;
    rt=(int)sqrt(n)+1;
    for (i=0;i<n;i++) cin >> k[i];
    cin >> p; 
    for (i=0;i<p;i++) {
        cin >> q[i].x >> q[i].y;
        q[i].i = i;
    }
    sort(q,q+p,cmp);

    int l=0, r=-1;
    for (i=0;i<p;i++){
        auto [s,e,idx]=q[i];
        s--;e--;
        while (r<e) add(++r, 0);
        while (s<l) add(--l, 1);
        while (e<r) del(r--, 0);
        while (l<s) del(l++, 1);
        ans[idx]=query();
    }
    for (i=0;i<p;i++) cout << ans[i] << "\n";
    return 0;
}