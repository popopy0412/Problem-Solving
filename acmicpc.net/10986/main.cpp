#include <bits/stdc++.h>
using namespace std;
long long ans, sum, cnt[1001];
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    int i, n, m, a;
    cin >> n >> m;
    while(n--){
        cin >> a;
        sum += a;
        cnt[sum % m]++;
    }
    ans += cnt[0];
    for(i=0;i<m;i++) ans += (cnt[i] ? cnt[i]*(cnt[i]-1)/2 : 0);
    cout << ans;
    return 0;
}