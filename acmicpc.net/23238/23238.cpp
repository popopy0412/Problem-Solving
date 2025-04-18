#include <bits/stdc++.h>
using namespace std;
const int MAX=110000;
int n,rt,buc[350][MAX],cnt[MAX],ans[MAX],d[MAX],mx;
vector<int> k(MAX);
struct Q{
    int x, y, i;
}q[MAX];

bool cmp(Q x, Q y) {
    return x.x/rt != y.x/rt ? x.x/rt < y.x/rt : x.y < y.y;
}

int query() {
    for (int i=n/rt+1;i>=0;i--) {
        if (!buc[i][mx]) continue;
        for (int j=rt-1;j>=0;j--) {
            if (cnt[i*rt+j]==mx) return i*rt+j;
        }
    }
}

void add(int i) {
    int t=k[i];
    if (cnt[t]) {
        d[cnt[t]]--;
        buc[t/rt][cnt[t]]--;
    }
    cnt[t]++;
    d[cnt[t]]++;
    buc[t/rt][cnt[t]]++;
    if (mx<cnt[t]) {
        mx=cnt[t];
    }
}

void del(int i) {
    int t=k[i];
    d[cnt[t]]--;
    buc[t/rt][cnt[t]]--;
    cnt[t]--;
    if (cnt[t]) {
        d[cnt[t]]++;
        buc[t/rt][cnt[t]]++;
    }
    if (mx!=0 && d[mx]==0) {
        mx=cnt[t];
    }
}

int main() {
    ios::sync_with_stdio(0), cin.tie(0);
    int i,u;
    cin >> n >> u;
    rt=sqrt(n);
    for (i=0;i<n;i++) cin >> k[i];
    vector<int> tmp(k);
    sort(tmp.begin(),tmp.end());
    tmp.erase(unique(tmp.begin(),tmp.end()),tmp.end());
    for (i=0;i<n;i++) {
        auto it = lower_bound(tmp.begin(),tmp.end(),k[i]);
        k[i]=it-tmp.begin();
    }
    for (i=0;i<u;i++) cin >> q[i].x >> q[i].y, q[i].i=i;
    sort(q,q+u,cmp);
    int l=0,r=-1;
    for (i=0;i<u;i++) {
        auto [s,e,idx] = q[i];
        s--;e--;
        while (r<e) add(++r);
        while (s<l) add(--l);
        while (e<r) del(r--);
        while (l<s) del(l++);
        ans[idx]=tmp[query()];
    }
    for (i=0;i<u;i++) cout << ans[i] << "\n";
    return 0;
}