#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, j, t, n, m, sum[1010]={0};
    ll ans=0;
    vector<ll> v;

    cin >> t >> n;
    for(i=1;i<=n;i++){
        cin >> sum[i];
        sum[i] += sum[i-1];
        for(j=0;j<i;j++) v.push_back(sum[i]-sum[j]);
    }
    sort(v.begin(),v.end());
    cin >> m;
    for(i=1;i<=m;i++){
        cin >> sum[i];
        sum[i] += sum[i-1];
        for(j=0;j<i;j++){
            ll f = t-(sum[i]-sum[j]);
            auto [s, e] = equal_range(v.begin(), v.end(), f);
            ans += e-s;
        }
    }
    cout << ans;
    return 0;
}