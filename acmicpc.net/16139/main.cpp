#include <bits/stdc++.h>
using namespace std;
int sum[26][200010];
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    string str;
    int i, j, n, m, l, r;
    char c;
    cin >> str; n = str.length();
    for(i=0;i<n;i++){
        sum[str[i]-97][i]++;
        for(j=0;j<26;j++) sum[j][i+1] = sum[j][i];
    }
    cin >> m;
    for(i=0;i<m;i++){
        cin >> c >> l >> r;
        cout << sum[c-97][r] - (l ? sum[c-97][l-1] : 0) << "\n";
    }
    return 0;
}