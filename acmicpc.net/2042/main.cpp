#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int where[1000010];
ll tree[3000010], num[1000010];
void seg(int i, int s, int e){
    if(s == e){
        tree[i] = num[s];
        where[s] = i;
        return;
    }
    seg(i*2, s, (s+e)/2);
    seg(i*2+1, (s+e)/2+1, e);
    tree[i] = tree[i*2] + tree[i*2+1];
}
void update(int i, ll v){
    while(i){
        tree[i] += v;
        i /= 2;
    }
}
ll query(int i, int s, int e, int l, int r){
    if(l <= s && e <= r) return tree[i];
    else if(e < l || s > r) return 0;
    return query(i*2, s, (s+e)/2, l, r) + query(i*2+1, (s+e)/2+1, e, l, r);
}
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, n, m, k, s=1, e;
    cin >> n >> m >> k;
    for(i=1;i<=n;i++) cin >> num[i];
    seg(1, 1, n);
    for(i=0;i<m+k;i++){
        ll q, a, b;
        cin >> q >> a >> b;
        if(q == 1) update(where[a], b - tree[where[a]]);
        else cout << query(1, 1, n, a, b) << "\n";
    }
    return 0;
}