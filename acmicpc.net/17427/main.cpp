#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(0);
    int i, n;
    long long ans=0;
    cin >> n;
    for(i=1;i<=n;i++) ans += (n/i)*i;
    cout << ans;
    return 0;
}